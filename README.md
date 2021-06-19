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
