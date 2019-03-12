

permship = 125

def gship(weight):
    if weight <= 2:
        return   weight * 1.50 + 20
    elif weight > 2 and weight <= 6:
        return weight * 3.00 + 20
    elif weight > 6 and weight <= 10:
        return weight * 4.00 + 20
    else:
        return weight * 4.75 + 20

def dship(weight):
    if weight <= 2:
        return   weight * 4.5
    elif weight > 2 and weight <= 6:
        return weight * 9
    elif weight > 6 and weight <= 10:
        return weight * 12
    else:
        return weight * 14.25
def cheapest(weight):
    if dship(weight) < gship(weight) and dship(weight) < permship:
        return "the cheapest method is drone shipping and the cost is "+ str(dship(weight))
    elif gship(weight) < dship(weight) and gship(weight) < permship:
        return "the cheapest method is ground shipping and the cost is "+ str(gship(weight))
    else:
        return "the cheapest methode is premuim shipping and the cost is 125."
real_weight =  int(input('how much does the shipping weigh : '))
print(cheapest(real_weight))
