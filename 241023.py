# a loop model
num = input("enter a number")
num = int(num)
print(num)
if num > 10:
    print("your number is too big! INVALID")
else:
    print("your number is valid")
    print("Let's continue")

# a continuous loop for when the end-user has responded incorrectly
response = ""
while response != 'y' and response != 'n':
    response = input("y or n")
print("you responded with", response)

# printing the message you want backwards
message = "Hello, World"
length = len(message)
myRange = range(length-1, 0, -1)
for count in myRange:
    print(message[count], end="")

# iteration
knights = ["bill", "jack", "ben", "henry"]
for knight in knights:
    print(knight)

    if temp > 13.5:
        print("Stay put and tell us the temp throughout the day")
    else:
        print("Weather is below average. Better wrap up!")
        print("Cheerio")
