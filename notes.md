# day 1

This is a fairly straight-forward question with an easy solution. It requires taking an input and parsing that file for new line items separated into sections by empty lines. These sections should be 
summed, and the top three values of those summations should be returned. 

To do this, I looked at the file input functions in python, and chose to parse the file by line. If the line was blank, I added all the values in the previous section to a list and summed the values, 
creating a list of totals for each section. I then simply sorted and returned the top three values from the list. 

# day 2

This was a slightly more complicated problem, and took a little more effort. I also am certain there is a better way to solve this problem, I just don't know it yet. 

The input in this case is a file of two columns of values, one indicating the selection of an opponent in a RPS (rock paper scissors) match, the other being initially unknown but suspected to be the 
planned selection for my "strategic" (read: cheating) value. It is later discovered that this column is for the plan to either lose, tie, or win the match. 

The goal is to find my final score, given the following values for scoring. 

|Loss|Tie|Win|
|----|----|----|
| 0 | 3 | 6 |

with the additional score criteria being from the choice I made:

|Rock|Paper|Scissors|
|----|----|----|
| 1 | 2 | 3 |

Which results in a set of values that are definable by a matrix of values for the final scores based on the choices presented. 

Part one has a matrix that looks like this:

| | Rock | Paper | Scissors |
|--:|:--:|:--:|:--:|
|Rock|4|7|3|
|Paper|1|5|9|
|Scissors|7|2|6|

However, given that the assumed meaning of the second column is incorrect, we need to adjust the matrix to look like this

| | Lose | Tie | Win |
|--:|:--:|:--:|:--:|
|Rock|3|4|8|
|Paper|1|5|9|
|Scissors|2|6|7|

The most simple and brute force way is to create this matrix, and as there are only 9 possible combinations, create a dictionary which can take the parsed line and determine which combination value is 
present, and sum all of those values. 

### Possible alternate solutions to investigate

Noting that there are matricies of values, it is quite likely that some matrix algebra could help solve this faster, and with extensibility to larger possible sets of choices, therefore games more complex 
than RPS. 

Things to look into:

 - dot product
 - cross product
 - true false tables

# day 3

Initially, I thought a dictionary would be the best for scoring each letter, but then considered if I could generate the dictionary each time so I wouldn't have to hard code it in. Then, I realizeed that `find()` is a feature of python that returns the index of the search in the string. This could be added to 1 to get the score if the letters were simply arranged in order. 


