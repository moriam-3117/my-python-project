'''
a = "hello moriam"
#string slicing
print(a[:11])
#sting length 
print(len(a))
#string methods
print("hello" in a)
if "yay" not in a:
    print ("yay is not in not in main string")
'''
'''
b = "anhyeongasseyo everyone is a cool"
print(b[-7:-4])
print(b.capitalize())
print(b.upper())
print(b.lower())

#f string formating
price = 3000
sentence = "the price for the manual is "+ str(price) + " today "
print (sentence)
sentences= f"the price of the manual is {price * 1.2:.2f} today"
print (sentences)
#escape character
sentence="The philosophy text is \" good\"

#boolean
x=200
print(isinstance(x,int))
x=20>30
print(isinstance(x,bool))
#assignment operators
x=5
x+=3 #x=x+3
'''

#list they accept diffrent data types and also duplicates
thislist=["banana","apple","grape","watermelon","orange"]
#thislist.reverse()
'''
print(len(thislist))
blist=["abc", 3 , True,40,"sale"]
print(type(blist))
print(thislist[0:3])
#array
if "apple" in thislist:
    print("i love apple")
else :
    print("no mangoes")
'''
thislist[2]= "mango"
print(thislist)
thislist[0:1]=["straberry","qiwi","melon"]
print(thislist)
thislist.pop()
thislist.clear()
#use all the 62 function in the list class and use it 