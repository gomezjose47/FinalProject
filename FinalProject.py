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


def main():
  getinput()

def getinput():
  h = int(input("Enter the initial height of the ball: "))
  v = int(input("Enter the inital velocity of the ball: "))
  isvalid(h,v)

def isvalid(h,v):
  if ((h <= 0) or (v <= 0)):
    print("Please enter positive values")
    getinput()

  else:
      maxheight(h,v)

def maxheight(h,v):
  t = (v/32)
  maxH = (h + (v*h) - (16*t*t))
  print("The maximum heigh of the ball is ", maxH, "feet.")
  balltime (h,v)

def balltime (h,v):
  t = 0 
  ballHeight = (h + (v*t) - (16*t*t))
  while expression: (ballHeight >= 0)
  t += 0.1
  ballHeight = (h + (v*t) - (16*t*t))
  print("The ball will hit the ground aprroximately after", ballHeight, "seconds.")

main()
