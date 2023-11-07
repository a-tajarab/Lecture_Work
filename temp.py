def fahrenheit_to_celcius(f):
    return (f - 32) / 2

if __name__=="__main__":
    temperatures = []
    loop = 0
    while True:
        temp = input(f"enter temp {loop} followed by f or c (e.g. 10c) {loop + 1} :")
        loop += 1
        if temp == '':
            break
        unit = temp[-1]

        temp = temp[:-1]
        temp = int(temp)
        if unit == 'f':
            print(f'{temp} fahrenheit')
            temp = fahrenheit_to_celcius(temp)
            print(f'is {temp} to celcius')
        temperatures.append(temp)
        #print(unit)
        #print(temp)
        max_temp = max (temperatures)
        sum_temp = sum(temperatures)
        lengths_temp = len(temperatures)

    print(temperatures)
    print()
    print('finished')