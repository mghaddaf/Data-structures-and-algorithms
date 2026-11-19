def display_name(number):
    if number == 0: # base case
        return
    else:  # recursive case
        print("Ryan")
        display_name(number - 1)

display_name(50)
count = int(input("Choose a number: "))

def countdown(count):
    if count == 0:
        return
    else:
        print(count)
        countdown(count - 1)
        

countdown(count)

def countup(count):
    if count == 0:
        return
    else:
        countup(count - 1)
        print(count)
        

countup(count)