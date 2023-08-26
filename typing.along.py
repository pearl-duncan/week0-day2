#DATA TYPES
    #TEXT TYPE: str
    #NUMERIC TYPES: int(whole number), float(number with decimal), complex
        #when combining (*,-,+,/) an int & float, it will come out as a float unless we make it come out as an int in which case it will round down to the nearest whole number
     #SEQUENCE TYPES: list, tuple, range
    #SET TYPE: set
    #BOOLEAN TYPE: bool
    #NONE TYPE: NoneType
num1 = 987
num2 = 4.0
intex = int(num2)
print(int(num1 / num2)) #this demo was showing int conversion of a float
print(num1/num2)

#comments!!!
#comments are great for notating code, reminding us to do things, or even saving stuff we dont want to delete- make them by putting a # before what you want to right

print('\n', "MATH OPERATORS" , '\n')
#MATH operators!!

# + add

add1 = 5+6
print("add", add1)

# - subtract
sub1 =10-5
print("sub", sub1)

# * multiply
mult1 = 9*9
print("mult", mult1)

# / divide
div =81/9
print('div', div) #div defaults to floats

# // floor divide- is going to give us the lowest divisor without any remainder. will show us how many times a number will go into another number without having anything left over
floor_div = 7//2 #so 2 goes into 7 3 times evenly and then theres a remainder of 1 so the answer to this equation is going to be 3
print('floor divide', floor_div)

# % modulo operator- gives us the remainder^^
mod =7%2
print('mod', mod)

#SPOILER ALERT!!! modulo is commonly used for determining even or odd
odd=7
even=6
print(odd %2==0) #the == is asking a question while a single = is asigning a value 

print(7%2) #odd ex
print(6%2) #even ex

#STRINGS!!! strings are immuteable- they can't be changed
print('\n'"Stings")
string1='abc'
string2='1234 + 234234'
string3= 'another string we\'ve come up with' #can use a \ to override a special character like ' otherwise we would have more than 1 string when we just wanted 1

string4 =string3 + 'this is my literal string'  + string2 #this is an example of concatenation
print(string4)

f_string= f"this is numb1 ---->{num1} !!!" #this is an f string or formatted string example
print(f_string)

#LISTS!!!!
print('\nLISTS!')

some_list =[1234, 'string', True, False, 5.099,]
print(some_list)

#lists are ordered, 0-indexed, dynamic
    #0-indexed means we can start at the first step (0)- the positions of a list always starts at 0

print(some_list[0]) #the index of a list gives us the value!
print(some_list[1].upper())

order_list = [0,1,2,3,4]
print(len(order_list)) #len= length of list- how many placements in the list (for this example, its 5)
print(order_list[3]) #the number in the bracket is the placement of the value we want printed

#python list methods
    #.append() adds element at the end of list
    #.remove() removes the FIRST OCCURENCE of a value from a list
    #.insert( inserts a value into the list at a specified position)
    #.pop() defaults to removing the last element from the list, but you can specify position optional

#FUNC VS METHOD EXAMPLE: FUNC---> functioncall(input) vs item.method(input)

print('\nLIST methods:')
    #.append() adds element at the end of list
print(order_list)
order_list.append(5)
print (order_list)

    #.remove() removes the FIRST OCCURENCE of a value from a list
order_list.remove(5)
print(order_list)

    #.insert( inserts a value into the list at a specified position)
order_list.insert(0,10)
print(order_list)

    #.pop() defaults to removing the last element from the list, but you can specify position optional
popped_value = order_list.pop(0)
print(popped_value)
print(order_list)

#CONDITIONALS!!!
print("\nConditionals")
# if / elif /else
age=78

if age == 16:
    print('sweet')


if age <18:
    print('just a baby')
elif age >64: #you can have as many elif's as you need
    print("senior")
else:
    print('adult')


#Truth - Tree!    (and&     or|)
#T&T= True
#T&F= False
#F&F= False

#T|T= True
#T|F= True
#F|F= False


if age <18 :
    print('just a baby')
elif age >=18 and age <65: #have to put age on both sides of "and" because python doesnt keep track of the fact that were talking about that
    print('adult')
else:
    print("senior")

if age > 846516549:
    print('really really old')

#print('15' == 15) -- this will come out false because they are equal value but not type
#print('15'=='15')  --this will come out true b/c they are equal value and type

names= ['hassan', 'david', 'tucker']

if "tucker" in names:
    print('tucker made it to class today!')

#to put multiple cursors, hold down alt key and click where you want a cursor

#LOOPS!!
print('\n Loops!!!')

#range fuction: start will default to 0, start will be noninclusive, and step will show the values in your choice of pattern
#for x in range(5,10,2):
 #   print(x)

# For loop
# syntax--> for item in items:
for name in names:
    print(name)
    if name == 'tucker' : 
        print('tucker made it to class today!--- LOOP VERSION')

# index loop
for i in (range(len(names))):
    print(names[i], i)

# while loop 
print('\nWHILE LOOP')
pointer =0 
while True:
    print(names[pointer])
    pointer+=1 
    if pointer > 1:
        break

print('\nincrementing / decrementing')
#incrementing / decrementing
counter=0
for x in range(5):
    counter = counter+1
    counter+= 1 #+= is shorthand for increment
print(counter)


num_ex = 456
num_ex1 = 45234
num_ex2 = 45547

if num_ex % 2 == 0:
    print(f'Number is even!!!--->{num_ex}')
else:
    print(f'Number is odd-->{num_ex}')


def odds(num):
    if num % 2 ==0:
        print(f'number is even--> {num}')
    else:
        return 'odd'
odds(num_ex1)
odds(num_ex2)
odds(num_ex)




