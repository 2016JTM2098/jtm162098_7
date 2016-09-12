#------------------------------ Problem Statement 1 --------------------------------

import sys

#-------------------------------String Input ---------------------------------------

mystring=raw_input("Enter a string :")
result = mystring.split()
print result

z=result[0]
y=result[1]
y2=result[2]
y3=result[3]
y4=result[4]


print "The total number of words is: "  + str(len(result))

l=str(len(result))

#------------------------------------- Frequency Print --------------------------------------------------

print z + " Occurs ===> " + str(result.count(z)) + " times "

print y + " Occurs ===> " + str(result.count(y)) + " times "

print y2 + " Occurs ===> " + str(result.count(y2)) + " times "

print y3 + " Occurs ===> " + str(result.count(y3)) + " times "

print y4 + " Occurs ===> " + str(result.count(y4)) + " times "

x=max(str(result.count(z)), str(result.count(y)), str(result.count(y2)), str(result.count(y3)), str(result.count(y4)))

#--------------------------------- MOST FREQUENT WORD PRINT -------------------------------

m=int(x)

mf=result[m]
if m>1:
	print "Most frequently word is = " +result[m]
else:
	print "All words different" 

#---------------------------------- PART 2-----------------------------------

#-------------------------------------- PERMUTATIONS-------------------------------------

k=result[m]

perm=[]

perm = k[1:] + k[:1]

if m>1:
	print "Permutation of most frequently occured word is : " +perm

else: 
	print ''

#--------------------------------------------------------------------------------------------------

def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l
 
 
# Driver program to test above function

string=result[m]
if m>1:
	data = list(string)
	for p in permutation(data):
    		print p
else: 
    	print ''
#---------------------------------------- END OF SCRIPT---------------------------------------------




