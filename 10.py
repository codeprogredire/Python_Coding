'''
(Make Chocolate problem - Coding Bat)
We want make a package of goal kilos of chocolate. 
We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, 
assuming we always use big bars before small bars. 
Return -1 if it can't be done.
'''

def make_chocolate(small, big, goal):
  if goal%5<=small and goal-5*big<=small:
    if goal%5==0 and goal<=5*big:
      return 0
    if (goal-5*big)>0:
      return goal-5*big
    else:
      return (goal-((goal/5)*5))
  else:
    return -1

print(make_chocolate(4,1,9))