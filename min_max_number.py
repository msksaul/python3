largest = None
smallest = None

def larger (number):
    global largest
    if largest is None:
        largest = number
    elif number > largest:
        largest = number
    return largest

def smaller (number):
    global smallest
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
    return smallest
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    else:
        try:
            intnum = int(num)
        except:
            print('Invalid input')
        else:
            smaller(intnum)
            larger(intnum)

print('Maximum is',largest)
print('Minimum is',smallest)
