---
type: raw-source
title: Advanced Tool Development and Integration 1.7 Harden and Test the Logistics Toolkit
tags:
- raw-source
status: preserved
created: '2026-06-21'
vault_area: raw sources
canonical_path: raw sources/Advanced Tool Development and Integration 1.7 Harden and Test the Logistics Toolkit.md
---

## **Overview**

You've successfully refactored Innovate Logistics' naive functions into reliable, agent-callable tools. However, your functions (get_tracking_status, check_inventory, etc.) all contain identical, repetitive try/except blocks for error handling.

You’ve learned about the **Production Wrapper Pattern** (@production_agent_function). Now, it's time to apply it. Your first task is to "harden" your functions by applying this decorator, which will allow you to remove all that repetitive error-handling code.

Your second task is to build a comprehensive pytest suite from scratch (using a provided stub file) to prove that your new, hardened functions are 100% production-ready for Innovate Logistics.

## **Activity Goals**

By completing this activity, you will:

- Apply a production-grade decorator (@production_agent_function) to an existing set of functions.
    
- Refactor code to remove repetitive try/except blocks, delegating error handling to the decorator.
    
- Build a comprehensive pytest suite by filling in a provided stub file (1_7_START_test_logistics.py).
    
- Write tests that validate the "Happy Path," "Input Validation," and the critical "Error Response Format".
    

## **Getting Started**

Ready to get started? Select **Launch VSCode** to access your Lab.

You are welcome to use your local environment to develop if you’d like. To do so, launch the lab, navigate to the middle icon on one side of the header corner that says 'Lab Files'. Once there, there will be a link that says “Download all files” near the header of the pane. Select that and you will get a zip of the lab contents. Within the extracted folder, you’ll find the code at home/coder/coursera/vscode.

Required Files You will need the following files for this activity:

.env file

module_01/activities/logistics_tools.py: The file you created in the previous Activity. This is what you will be modifying.

module_01/activities/1_7_START_production_wrapper.py: This file contains the @production_agent_function decorator for you to import.

module_01/activities/1_7_START_test_logistics.py: This is a stub pytest file with empty test functions and TODO comments for you to complete.

Part A: Harden Functions (Refactor with Decorator)

1. Open module_01/activities/logistics_tools.py: Open the file you created in Activity 1.3( Refactor the Legacy Logistics Functions ), which contains your get_tracking_status, check_inventory, and calculate_delivery_days functions.
    
2. Import the Decorator: At the start of your logistics_tools.py file, add the following import statement:
    

1

3. Apply the Decorator: Add the line @production_agent_function directly before the def line for all three of your functions.
    
4. Refactor Your Functions: This is the most important step. The decorator now handles all try/except logic. You must delete the try/except ValueError and except Exception blocks from all three of your functions.
    

Your functions should now be "clean" — they should only contain validation logic (that raise ValueError) and the "happy path" return {"success": True, ...}.

Analyze the example in 1_7_START_production_wrapper.py ( the end of the file ) for what your refactored functions should look like.

Part B: Build the Test Suite

1. Open 1_7_START_test_logistics.py: This file contains all the test function names you need, but the logic is missing.
    
2. Import Your Functions: At the top of 1_7_START_test_logistics.py, uncomment the import line to import the three (now hardened) functions from your logistics_tools.py file.
    
3. Complete the TODOs: Your task is to fill in the body of every test_ function. Read the TODO comments in 1_7_START_test_logistics.py—they explain exactly what you need to call and what you need to assert.
    

Happy Path Tests (e.g., test_tracking_success): Call the function with valid data and assert result["success"] is True and check the result value.

Error Response Tests (e.g., test_tracking_invalid_length): Call the function with invalid data and assert result["success"] is False, assert result["result"] is None, and assert result["error_type"] == "validation".

Part C: Validate Your Work

1. Install pytest: If you haven't already, install pytest in your environment:

1

2. Run Tests: In your terminal, run the test suite you just built:

1

3. Debug and Iterate: Your goal is to make all tests pass. If tests fail, read the pytest output, fix the corresponding function in logistics_tools.py or the test in 1_7_START_test_logistics.py, and run the tests again.
You are finished when:

- Your module_01/activities/logistics_tools.py file is updated: all three functions have the @production_agent_function decorator, and the old try/except blocks have been removed.
    
- Your 1_7_START_test_logistics.py file is complete, with all TODO comments replaced by working pytest code.
    
- Running pytest 1_7_START_test_logistics.py -v results in all tests passing (e.g., == 15 passed ==).
A comparable solution is available for download if you encounter challenges or wish to validate your approach.

After completing your lab, take a moment to review the exemplar solution. This sample solution can offer insights into different coding techniques and approaches. You can view the exemplar solution project in the solution folder located here: **/home/coder/coursera/vscode/projects/module_01/solutions/**

- Open the project in VSCode in a new window to view your project and the exemplar solution at the same time.
    
- Reflect on what you can learn from the exemplar solution to improve your coding skills.
    
- Remember, multiple solutions can exist for a problem; the goal is to learn and grow as a programmer by exploring various approaches.
    

Use the exemplar solution as a learning tool to enhance your understanding and refine your approach to coding challenges.