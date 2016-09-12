#----------------------------------- PROBLEM STATEMENT 2 -------------------------------------------

import random

ic=0
oc=0

#----------------------------------- RANDOM NUMBER GENERATOR -----------------------------------------

for i in range(10):
	(x,y)=(random.random()*2-1, random.random()*2- 1)
	print x,y
	if (x*x + y*y) < 1:
		print "Inside circle"
		ic+=1
	else:
		print "Outside Circle"
		oc+=1

#------------------------------------- CALCULATING INSIDE/OUTSIDE POINTS --------------------------------

print "*********************************"
print "Number of points inside circle",ic

print "Number of points outside circle",oc

print "**********************************"

#-------------------------------------- END OF SCRIPT ----------------------------------------------------
