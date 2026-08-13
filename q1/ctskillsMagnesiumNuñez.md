# Computational Thinking Exercise
## Smart School Canteen Queue
**Name:** Denver Angel O. Nuñez
**Section:** 9 - Magnesium
**Last Name:** Nuñez
**Date:** August 12, 2026
---

## Step 1: Identify the Big Problem
### Main Problem
The line in the canteen is so long, it would starve some students short on time.
---
## Step 2: Identify the Sub-Problems
1. Students' Wake-Up Time
2. 5:30 Opening
3. Few Employees
4. Having only 3 Lines for Hundreds of Students
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem            | CT Skill | Proposed Solution       |
|---                     |---       |---                      |
| Students' Wake-Up Time | CT skill | Brief proposed solution |
| 5:30 Opening           | CT skill | Brief proposed solution |
| Few Employees          | CT skill | Brief proposed solution |
| Having only 3 Lines    | CT skill | Brief proposed solution |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Having only 3 Lines for placing and getting orders is a sub-problem. Some students don't get their meal, I will identify the varibales which will be the number of potential customers(every single scholar in the campus), the time they take to order and take, the time the canteen is opened.
### Pseudocode
START
DECLARE number_of_scholars
ASSIGN number_of_scholars as INT
DECLARE opening
ASSIGN opening as INT
INPUT order_time
DECLARE number_of_lines
ASSIGN number_of_lines as (opening / order_time) // number_of_scholars IF number_of_lines < 5 ELSE 5 
PRINT number of lines should be number_of_lines
END
---