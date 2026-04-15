#string can be closed in both single and double quotes 
friend = "alisha tarika"
roll_no ='cgc2236679!!' 
print(friend+roll_no) #two strings can be add


#if you want to write string in multiple line
Introduction="""my 
name 
is alisha """
print(Introduction)
print(friend[-2]) #indexing can be negative in python
print(len(Introduction)) 
#looping with strings
for a in friend:
 print(a,end=" ") 
 #string slicing
print(roll_no[0:3])
print(roll_no[-4:-1])

print(roll_no.upper()) #upper method
print(roll_no.lower()) #lower method
print(roll_no.rstrip("!!"))
print(roll_no.replace("79","80"))

#to make list from string
clas="btech cse cec cgc 4tha"
print(clas.split(" "))  

#to write in correct order
print(clas.capitalize())

#to count letters #to find letter #to check index
print(clas.count("c"),clas.find("c"))

print(clas.isalpha(),clas.isalnum(),clas.islower())
print(clas.isprintable()) #if all the characters are printable /n is not printable
print(clas.isspace()) #is string contain all the space 
print(clas.istitle()) #to check first letter is capital or not in all words
print(clas.title())   #to change into title
print(clas.swapcase()) #to change the lower to upper and upper to lower
print("{}{}".format(roll_no,friend))
a=56.788
print(f"{a:.2f}")
