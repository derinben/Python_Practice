# Python_Practice

# Question 1
Write a program:
Programming Challenge Description:
The goal of this challenge is to design a cash register program.
You will be given two decimal numbers. The first is the purchase price (PP) of the item.
The second is the cash (CH) given by the customer.
Your register currently has the following bills/coins within it:
'PENNY': .01,
'NICKEL': .05,
'DIME': .10,
'QUARTER': .25,
'HALF DOLLAR': .50,
'ONE': 1.00,
'TWO': 2.00,
'FIVE': 5.00,
'TEN': 10.00,
'TWENTY': 20.00,
'FIFTY': 50.00,
'ONE HUNDRED': 100.00

The aim of the program is to calculate the change that has to be returned to the customer.

Input:
The first input is the Purchase price (PP) and the second input is the cash(CH) given by the customer.

Output:
For each line of input print a single line to standard output which is the change to be returned to the customer.
In case the CH < PP, print out ERROR. If CH == PP, print out ZERO.
For all other cases print the amount that needs to be returned, in terms of the currency values provided.
The output should be alphabetically sorted. <br>

```python
Test 1
Test Input : 15.94 , 16.00
Expected Output : NICKEL,PENNY


Test 2
Test Input : Input17 , 16
Expected Output : ERROR  

Test 3
Test Input : 35 , 35
Expected Output : ZERO  


Test 4
Test Input : 45 , 50
Expected Output : FIVE
```

# Question 2
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, a<sub>i</sub>). n vertical lines are drawn such that the two endpoints of the line i is at (i, a<sub>i</sub>) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.Notice that you may not slant the container.

<img src = 'https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg' width="500" height="300">

```python
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1

Input: height = [4,3,2,1,4]
Output: 16  
```

# Question 3
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
```python
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
```
# Question 4 
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
```python
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```
