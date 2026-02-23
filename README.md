Author: Chloe Robinson & Camila Fienco

## Problem Selection
Investors evaluate how profitable an investment is over multiple years. The return on investment measures how much profit or loss is made compared to the initial investment. In this project, we implemented a recursive investment calculator that will calculate:
1.	Total future value of an investment after n years
2.	Total profit earned
3.	ROI percentage

## Recursive Design
### Base Case
Base Case: If n = 0, then V(0) = P
If no years have passed, the investment is the initial principal
### Recursive Case
Recursive Case: If n > 0, then T(n) = (T(n-1) + C) (1+r)
Each year adds the annual contribution and applying the growth rate

### Why Recursion is Appropriate
Recursion in this scenario is appropriate because it is the traversal of a tree. A person’s investment depends on their previous investment’s value. Each problem is decomposed into a smaller, similar, set of subproblems. Thus, recursion is an appropriate approach to find total investment after n years. 

## Implementation
Pseudocode
```
Func investment (P, r, C, n)
	If n< 0 raise error

#Base Case: Take O(1) time
	If n == 0 return p

#Recursive Case: Take O(n) time
	Previous_value = investment (P, r, C, n-1)

	#O(1) time
	Current_value = (previous_value+C)(1xr)
	Return current_value
```

## Analysis
### Time complexity (Big-Oh notation)
 The worst case occurs when the number of years is very large. Each call takes O(1) time. Therefore, n calls take O(n) time.

### Space complexity (recursion stack)
It should also be noted that each call stores the previous value, take O(1) space each call; O(n) space total. 
Time: O(n)
Space: O(n)

## Deployment
Windows CMD
```
python investment_calc.py
```

To test a sample
Windows CMD
```
python investment_calc.py < n_input.txt
```
Output will be output.txt
Cases 5-10 are edge cases

