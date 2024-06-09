#weekly code challenge week3

def large_power(base,exponent):
    if base**exponent>5000:
        print(True)
    else:
        print(False)    
base=3
exponent=10
large_power(base,exponent)


def divisible_by_ten(num):
    if num%10==0:
        print(True)
    else:
        print(False)
num=15
divisible_by_ten(num)   

# weeK3 Assignment

def calculate_discount(price,discount_percent):
    if discount_percent>=0.2:
        discount_price=price*(1-discount_percent)
        print(discount_price)
    else:
        print(price)
price=500
discount_percent=0.15
calculate_discount(price,discount_percent)            

    
    
    
        


    