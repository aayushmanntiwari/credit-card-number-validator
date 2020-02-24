from functools import reduce
def card_type(number,n):
    print(number)
    print(n)
    if n==1 and number.startswith('4'):
       validate(number)
    elif n ==2 and number.startswith('5'):
         validate(number)
    elif n == 3 and number.startswith('37'):
         validate(number)
    elif n == 4 and number.startswith('6'):
         validate(number)
    elif n==5:
         validate(number)
    else:
       print('Wrong input')
      


def validate(number):
    if len(number) >13 or len(number)<16:
        values = list(number)
        values.pop() #1.Drop the last digit.
        values.reverse() #2.Reverse the digits.
        #3.Multiple odd digits by 2.
        f1=lambda n:int(n)*2 if int(n)%2!=0 else         int(n)           
        result1=list(map(f1,values))
        #4.Subtract 9 to numbers over 9:
        f2=lambda n:n-9 if n>9 else n
        result2 = list(map(f2,result1))
        #5.Add all numbers:
        f3=lambda x,y:x+y
        result3 = reduce(f3,result2)
        #4.Mod 10:
        if result3%10== int(number[-1]):
           print('Card is valid')
        else:
           print('Card is not valid')
    else:
        print('card number must have between 13 and 16 digits')
     
#The Luhn Formula
print('''
Please select card type:
1.Visa card
2.Master card
3.American card 
4.Discover
5.Other
    ''')
value =  input('Please enter card number and the card type: ').split(' ')
number = value[0]
n = int(value[1])
card_type(number,n)
