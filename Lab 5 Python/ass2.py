def isValid(num):
    total = sumOfDoubleEvenPlace(num) + sumOfOddPlace(num)
    if total % 10 != 0:
        return 0
    else:
        return 1
    
def sumOfOddPlace(num):
    total = 0
    start = (len(num)-1)  
    for i in range(start, -1, -2):
         total+= int(num[i])
    return total

def sumOfDoubleEvenPlace(num):
     total = 0
     start = (len(num)-2)
     for i in range(start, -1, -2):
         digit =  int(num[i])
         doubled = digit * 2
         total+=getDigit(doubled)
     return total
 
def getDigit(num):
    if num < 10:
        return num
    else:
        return (num // 10) + (num % 10)
        
def getSize(d):
    return len(d)

def prefixMatched(num, d):
    num_str = str(num)
    prefix_str = str(d)
    match = 1
    for i in range(len(prefix_str)):
        if i >= len(num_str) or num_str[i] != prefix_str[i]:
            match = 0
            break
    return match

def getCardType(num):
    if prefixMatched(num, 4):
        return "Visa"
    elif prefixMatched(num, 5):
        return "MasterCard"
    elif prefixMatched(num, 37):
        return "American Express"
    elif prefixMatched(num, 6):
        return "Discover"
    else:
        return "Unknown"

num= (input("Enter credit_card number "))

valid_input = True
for ch in num:
    if ch < '0' or ch > '9':
        valid_input = False
        break

if not valid_input:
    print("Please enter only digits.")
else:
    card_type = getCardType(num)
    if isValid(num):
        print(f"{card_type} card is valid")
    else:
        print(f"{card_type} card is invalid")
