
num = ""
isaNum  = False

while isaNum == False:
    
    num = input("Enter a number")
    if num.isnumeric():
        print("Thank you")
    else:
        print("That was not a number")

confNum = int(num)

print(f"Number doubled is {confNum*2}")