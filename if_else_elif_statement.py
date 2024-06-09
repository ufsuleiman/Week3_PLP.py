# here is an example of an if statement
a=25
if a>35:
    print('a is greater than 30')
print('a is less than 30')    

# here is if else statement
a=5
b=2
if b%a==0:
    print('statement is an even number')
else:
    print('statement is an odd number')    

# if, elif, else statement

var='i'
if var=='a':
    print('var is a vowel')
elif var=='e':
    print('var is a vowel')
elif var=='i':
    print('var is  vowel')
elif var=='a':
    print('var is a vowel')
elif var=='a':
    print('var is a vowel')
else:
    print('var is a consonant')       
# find the greatest of the three numbers
a=15
b=4
c=30
if a>b and a>c:
    print('a is the greatest')
elif b>a and b>c:
    print('b is the greatest')
else:
    print('c is the greatest')      

# find if a number is divisible by 2,3,5
a=17
count=0
if a%2==0:
    print('a is divisible by 2')
    count+=1
if a%3==0:
    print('a is divisble by 3')
    count+=1
if a%5==0:
    print('a is divisible by 5')
    count+=1    
if count==0:
    print('a is not divisible by 2,3,5')    

# for loop
x=['toyota', 'camry', 'benz']
for i in x:
    print(i, end='')

# while loop

x=int(input('enter a multiple of 7'))
while x%7==0:
    print('%d this satisfied the statement')
else:
     x=(input('enter a multiple of 7'))

# a for loop with a break

for i in range(0,21):
    if i==10:
        break
    print(i, end=',')
        
    
        

