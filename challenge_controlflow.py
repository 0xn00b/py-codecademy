

def in_range(num,lower,upper):
    if num >= lower and num <= upper :
        return True
    else:
        return False
print(in_range(12,6,27))




def movie_review(rating):
    if rating == 5 :
        return "Avoid at all costs!"
    if rating > 5 and rating < 9:
        return "This one was fun."
    if rating >= 9 :
        return "Outstanding!"



def twice_as_large(num1,num2):
    if num1 > 2*num2 :
        return True
    else:
        return False

def large_power(base,exponent):
    if base**exponent > 5000:
        return True
    else:
        return False

def divisible_by_ten(numb):
    if numb % 10 == 0:
        return True
    else:
        return False

def max_num(num1,num2,num3):
    if num1 > num2  and num1 > num3 :
        return num1

    elif num2 > num1  and num2 > num3 :
        return num2

    elif num3 > num2  and num3 > num1 :
        return num3

    else:
        return "It's a tie!"

def over_budget(budget,food_bill, electricity_bill, internet_bill, rent):
    if budget < food_bill+electricity_bill+internet_bill+rent:
        return True
    else:
        return False

def always_false(num):
    if num == num:
        return False

def not_sum_to_ten(num1,num2):
    if num1 + num2 == 10:
        return False
    else :
        return True

def same_name(your_name,my_name):
    if your_name == my_name :
        return True
    else:
        return False

