if __name__ == '__main__':
    NO_HOURS = 10
    temperatures = []
    for loop in range(NO_HOURS):
         temp = input(f"enter temp{loop+1} : ")
         temp = temp[:-1]
         temp = int(temp)
         temperatures.append(temp)
print(f"Highest temp :{max(temperatures)}C")
print(f"Lowest temp :{min(temperatures)}C")
print(f"Average temp :{sum(temperatures)/len(temperatures)}C")
