# Basic-Artificial-Intelligence-Part-2

Task

Complete the function nextMove which takes in 4 parameters - an integer N, integers r and c indicating the row & column position of the bot and the character array grid - and outputs the next move the bot makes to rescue the princess.

Input Format:

The first line of the input is N (<100), the size of the board (NxN). The second line of the input contains two space separated integers, which is the position of the bot.
The position of the princess is indicated by the character 'p' and the position of the bot is indicated by the character 'm' and each cell is denoted by '-' (ascii value: 45).

Output Format:
Output only the next move you take to rescue the princess. Valid moves are LEFT, RIGHT, UP or DOWN

Sample Input:
5
2 3
-----
-----
p--m-
-----
-----
Sample Output:
LEFT

Resultant State:
-----
-----
p-m--
-----
-----
Explanation:
As you can see, bot is one step closer to the princess.
