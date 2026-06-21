Overview

As a Praxis AI Associate Consultant working on the Innovate Logistics engagement, you need to create a systematic architecture analysis that demonstrates your mastery of agent design principles. This activity focuses on their specific logistics challenges, allowing you to practice architectural decision-making using professional frameworks and templates.

You'll work with Innovate Logistics' customer service scenarios, apply the ACTOR framework to make architectural decisions, and create a complete architecture diagram using industry-standard templates.

## Activity Goals

By completing this activity, you will:

- Create a complete agent architecture diagram for a business scenario by identifying required components and documenting decision flows
    
- Apply the ACTOR framework to determine whether an agent or chatbot approach is appropriate
    
- Select appropriate architectural components and document decision rationale
    

## Scenario

**Innovate Logistics Customer Service Agent Use Case:**

Innovate Logistics processes over 10,000 monthly customer service inquiries, with 60% involving complex multi-step problems like shipment delays, routing changes, and exception handling. Their current chatbot handles only 20% of inquiries successfully, requiring expensive human escalation for most complex cases.

During peak shipping seasons, inquiry volume increases to 25,000 monthly interactions. Common scenarios include weather-related delays requiring alternative routing, inventory shortages needing substitute products, delivery exceptions requiring customer communication, and cost optimization requests for complex shipping arrangements.

The company wants to implement an AI system that can autonomously handle complex logistics scenarios while maintaining integration with their warehouse management, customer relationship, and shipping carrier systems.

## Setup Requirements

ACTOR framework worksheet

ACTOR Framework Worksheet  
Praxis AI - Agent vs. Chatbot Decision Analysis  
Instructions  
Use this worksheet to systematically analyze whether your client scenario requires an AI agent  
or chatbot solution. Complete each section thoroughly, providing specific examples from your  
client's business context.  
Client: Innovate Logistics  
Use Case: Customer Service System  
Analyst: _________________________  
Date: _________________________  
A - Autonomy Requirements  
Question: Does the system need to operate independently without constant human oversight?  
Analysis Prompts:  
- Can the system handle inquiries during after-hours and peak seasons without human  
intervention?  
- Are there scenarios where immediate action is required without waiting for human  
approval?  
- How often do current customer inquiries require real-time decision-making?  
Your Analysis:  
_________________________________________________________________  
_________________________________________________________________  
_________________________________________________________________  
_________________________________________________________________  
None  
Autonomy Score: ☐ Low (Human oversight required) ☐ Medium (Some independence) ☐  
High (Full autonomy needed)

## Steps:

### Part A: Scenario Analysis (5 minutes)

**Apply ACTOR framework to Innovate Logistics scenario:**

Using the ACTOR framework worksheet, analyze the logistics customer service use case:

- **Autonomy:** Does the system need to operate independently during peak seasons and after-hours?
    
- **Complexity:** How many steps are involved in resolving shipment delays and routing issues?
    
- **Tool Usage:** What external systems (warehouse, carriers, CRM) require integration?
    
- **Outcome Variability:** Are there multiple solutions for typical logistics problems?
    
- **Reasoning Depth:** How much analysis is needed for route optimization and exception handling?
    

**Determine: agent or chatbot?**

Based on your ACTOR analysis, decide whether Innovate Logistics' scenario requires an agent or would be suitable for a chatbot approach.

**List 3 specific tasks** the system should handle (e.g., "Resolve shipment delays with alternative routing options," "Handle delivery exceptions with automated customer communication," "Provide cost optimization for multi-modal shipping").

### Part B: Architecture Design (10 minutes)

**Select components from the template library:**

Using a simple diagramming tool such as [app.diagrams.net](http://app.diagrams.net/), select the five core components needed for your Innovate Logistics solution:

- Reasoning Model
    
- Tools/Functions
    
- Memory
    
- Task Manager
    
- Interface
    

**Draw basic data flow connections:**

Show how information flows between components during a typical complex logistics inquiry (e.g., shipment delay resolution).

**Add minimum 2 tools/functions:**

Specify at least two tools the agent will need for Innovate Logistics (e.g., warehouse management API, shipping carrier integration, route optimization calculator).

### Part C: Documentation (5 minutes)

**Complete architecture decision record:**

Document your key architectural decisions using the provided template.

**Justify component selections:**

Explain why you selected specific components and tools based on Innovate Logistics' requirements identified in Part A.

## Deliverables

- **Single architecture diagram (image file):** Visual representation of your complete agent architecture with all five components and data flows for Innovate Logistics
    
- **Completed ACTOR framework worksheet:** Your analysis determining agent vs. chatbot suitability with supporting rationale specific to logistics operations
    

## Success Checklist

- ACTOR framework analysis addresses all five criteria for Innovate Logistics' specific challenges
    
- Architecture diagram clearly shows all five core components with logical connections
    
- At least two logistics-specific tools/functions are identified and integrated into the design
    
- Component selections are justified based on Innovate Logistics' operational requirements
    
- Final recommendation (agent vs. chatbot) aligns with ACTOR framework analysis and logistics complexity
    

## Key Points

- Use the ACTOR framework systematically to make objective architectural decisions for logistics scenarios
    
- Focus on the five core components that every agent system requires
    
- Consider how components work together to solve complex logistics problems
    
- Base tool selection on actual requirements from Innovate Logistics' use case analysis
    

## Exemplar Solution

A comparable solution is available for download if you encounter challenges or wish to validate your approach.

**Completed ACTOR framework worksheet**

ACTOR Framework Worksheet  
Praxis AI - Agent vs. Chatbot Decision Analysis  
Instructions  
Use this worksheet to systematically analyze whether your client scenario requires an AI agent  
or chatbot solution. Complete each section thoroughly, providing specific examples from your  
client's business context.  
Client: SkillSprint EdTech  
Use Case: Student & Corporate Support System  
Analyst: _Ben (Praxis AI)_  
Date: _October 3, 2025_  
A - Autonomy Requirements  
Question: Does the system need to operate independently without constant human oversight?  
Analysis Prompts:  
- Can the system handle inquiries during after-hours and peak seasons without human  
intervention?  
- Are there scenarios where immediate action is required without waiting for human  
approval?  
- How often do current customer inquiries require real-time decision-making?  
Your Analysis:  
None  
Yes, the system must be highly autonomous. SkillSprint has a global user base,  
requiring 24/7 support for tasks like enrollment changes and progress  
inquiries. A corporate client in a different time zone needs to be able to  
manage their team's seats immediately, without waiting for a support agent to  
be online. The goal is instant resolution, not ticket creation.

**Architecture Diagram**

![Diagram showing SkillSprint UI at top, Praxis AI Task Manager in center, and tools connected to LMS, CRM and Knowledge Base](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/_b3ee5c89495e41f0af138671dec1b76c_ArchitectureDiagram.jpg?expiry=1778771239967&hmac=zzlzDig32Zp_ZfeJVTn8BsG5z69VtSU1MFa5TWZx2is)

## Related

- [[Governance and PHAROS MOC]]
- [[Sales Objection Handling — Diagnosing Fog Without Coercion]]
