"""
This program will tell a user how high a ball will go in the air, and the amount
of time it will take to hit the ground. The program will first obtain the initial heigh from where
the ball is thrown and the initial velocity that the ball is thrown from. This information will come from
the user as an input function. 

First the program will request the initial height and velocity from the user. With this information,
we will use the formula (h + vt - 16t^2) to calculate the max height of the ball. After calculating the
height, the program will loop and calculate the height every .1 seconds until the height is no longer positive. 

After the program is done doing it's calculations, it should output the maximum height of the ball
and when the ball will hit the ground as well as the two input functions for the user to change the numbers
however they would like. 
"""

"""
defmain():

getinput() 
H = user inputs initial height of ball
V = user inputs initial velocity of ball

isvalid()
determines if (h,V) are valid and positive
if not positive 
print to user "enter positive values"
else

Maxheight()
t = v / 32 to find time it take to reach max height
plug answer into (h + (v*h) - (16*t*t)) 
print to user height of ball is " _" feet

Balltime()
set time = 0
do equation (h + (v*t)-(16*t*t))
while loop: while ball height is greater than or equal to 0
set time to atke height every .1 sec
use equation to determine ball height after every .1 sec (h + (v*t)-(16*t*t))
print to user The ball will hit the ground in about _ seconds"

main():
"""