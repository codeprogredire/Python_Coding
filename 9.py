'''
(CodingBat)
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks.
'''

# Brute Force
def make_bricks(small, big, goal):
  for i in range(small+1):
    for j in range(big+1):
      if (i+j*5)==goal:
        return True
  return False

# Improved Version
def make_bricks(small,big,goal):
    return (goal%5<=small) and (goal-5*big)<=small