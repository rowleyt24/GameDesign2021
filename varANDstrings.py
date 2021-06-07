#Thomas Rowley
#6/7/2021
#Learning how to work with strings
#While loop
#Different types of var

num1 = 19
num2 = 3.5
num3 = 0x2336537653863576357
#How to know what type of date is a variable
print(type(num1))
print(type(num2))
print(type(num3))
phrase = "Hello there!"
print(type(phrase))
#String functions

num=len(phrase)
print(num)   #shows the lengths of the phrase

print(phrase[3:7]) #print from 3 to 6
print(phrase[6:])  #print from index to the end
print(phrase *2)   #print it twice
#concadenation --> joining strings
phrase = phrase + " Goodbye"
print(phrase[2:num -2])  #Subtracts the letters that come "2" before the num

while "there" in phrase:
    print("there" in phrase)
    phrase = "changed"
    print(phrase)

    

# make 3 string variables print them individually 
#"print s1 + s2"
#print st2 + st3
#print st1 + st2 + st3