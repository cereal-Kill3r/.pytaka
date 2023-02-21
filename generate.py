import string
import random
from random import randint

tips = { 
1 : "Budget your money for payment of bills", 
2 : "Plan for long-term goals",
3 : "Cut down unnecessary expenses",
4 : "Have some emergency funds",
5 : "Look for a cheaper alternatives",
6 : "Set clear financial goals ",
7 : "Do not easily give in to your cravings",
8 : "Give yourself a treat sometime!",
9 : "Review your budget regularly",
10: "Allocate specific budget for everything"
}

# Generates random tips from the dictionary
tip = tips[randint(1,10)]

# Generates random code used for PK id
def code():
    run = True
    if run is True:
        create_id = str(''.join(random.choices(string.ascii_uppercase + string.digits, k=6)))
        run = False
    return create_id

print(code())