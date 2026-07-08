# Findings Detail — MEDIUM and above

Only one finding meets the MEDIUM+ threshold. Per the skill's format, this section
adapts "exact HTTP request(s) to trigger" to "exact call sequence to trigger," since
this target is an in-process Python library with no HTTP surface (confirmed in
`architecture.md`, Phase 1).

---

## MEDIUM — Unbounded infinite loop via unvalidated circular task dependencies

### Complete data flow

1. **Entry point (input):** `WorkflowExecutor.add_task(workflow_id, task_id, agent, description, dependencies)` — `scripts/workflow_management.py`, lines 74-90. This is the *only* place a `Task`'s `dependencies` list is set. No validation of any kind is performed here:

   ```python
   def add_task(
       self,
       workflow_id: str,
       task_id: str,
       agent: str,
       description: str,
       dependencies: Optional[List[str]] = None,
   ) -> Task:
       """Add task to workflow."""
       task = Task(
           task_id=task_id,
           agent=agent,
           description=description,
           dependencies=dependencies or [],
       )
       self.workflows[workflow_id].tasks[task_id] = task
       return task
   ```

   Nothing checks that `dependencies` doesn't contain `task_id` itself, or that the
   dependency graph across all tasks in the workflow is acyclic.

2. **Propagation:** `Task.dependencies` (a plain `List[str]`, `dataclasses.field(default_factory=list)`, `scripts/workflow_management.py` line 45) is stored unchanged and later read by `_get_ready_tasks`.

3. **Sink — where the defect actually manifests:** `_get_ready_tasks`, `scripts/workflow_management.py` lines 156-168:

   ```python
   def _get_ready_tasks(
       self, workflow: Workflow, executed: set
   ) -> List[str]:
       """Get tasks ready to execute."""
       ready = []
       for task_id, task in workflow.tasks.items():
           if task_id not in executed and task.status == TaskStatus.PENDING:
               deps_met = all(dep in executed for dep in task.dependencies)
               if deps_met:
                   ready.append(task_id)
       return ready
   ```

   For a self-referential or cyclic dependency set, `deps_met` is `False` for every
   affected task on every call — `ready` is always `[]`.

4. **Failure point:** `execute_workflow`, `scripts/workflow_management.py` lines 92-154, specifically the loop at lines 112-137:

   ```python
   while len(executed_tasks) < len(workflow.tasks):
       ready_tasks = self._get_ready_tasks(workflow, executed_tasks)
       if not ready_tasks:
           if len(executed_tasks) > 0:
               break
       for task_id in ready_tasks:
           ...
           executed_tasks.add(task_id)
   ```

   `ready_tasks` is `[]` every iteration (step 3), so the `for` loop body never runs,
   `executed_tasks` never grows past its starting size of `0`, `len(executed_tasks) > 0`
   is always `False`, the `break` never fires, and `len(executed_tasks) < len(workflow.tasks)`
   never becomes false. The `while` loop spins indefinitely with no I/O, no sleep, and no
   counter — a pure CPU-bound busy loop.

### Exact call sequence to trigger

```python
from scripts.workflow_management import WorkflowExecutor

executor = WorkflowExecutor()
executor.create_workflow("w1", "test")
executor.add_task("w1", "t1", "agent", "task", dependencies=["t1"])  # self-reference
executor.execute_workflow("w1", lambda task: "done")  # hangs forever
```

Equivalent two-task variant (no independent starting task):

```python
executor.create_workflow("w1", "test")
executor.add_task("w1", "t1", "agent", "task A", dependencies=["t2"])
executor.add_task("w1", "t2", "agent", "task B", dependencies=["t1"])
executor.execute_workflow("w1", lambda task: "done")  # hangs forever
```

Both variants were independently executed live (Phase 3 validation) with a 3-second
external `timeout` wrapper; both were killed (exit code 124), never reaching any
statement after the `execute_workflow` call.

### What the attacker gets

Denial of service against the process that embeds this library — the calling thread
hangs indefinitely, consuming CPU, with no exception to catch and no way to recover
without killing the process externally. No data is exposed, no other process or
resource is affected, and there is no privilege or trust boundary crossed (the package
has none, per `architecture.md`). The realistic path to harm is a caller — plausibly an
LLM agent using this library to construct a workflow from task descriptions it doesn't
fully control — accidentally or adversarially producing a cyclic dependency and hanging
its own process.

### How the baseline comparable handles the same scenario

Production workflow engines (Airflow, Prefect, Temporal) validate DAG structure at
definition time and raise an explicit error on a detected cycle, before any execution
begins — this is treated as a baseline correctness requirement, not an advanced feature.
`README.md` (line 124) lists "Production Ready" as a Key Feature of this package and
documents `WorkflowExecutor` as the primary usage pattern (lines 55-72), which is why
this finding is rated Medium rather than Low: the package holds itself to the standard
its comparable meets, and fails a check that comparable treats as basic hygiene, with a
one-line fix available (`if task_id in dependencies: raise ValueError(...)`, or a full
topological-sort validation pass in `add_task` / before `execute_workflow` begins).
