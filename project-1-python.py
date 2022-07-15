#Program by William Lemay. Allows user to input temperature and inputs it into a list to be averaged.
tempTrack = 1
tempList = []

while tempTrack == 1:
    temp = int(input("Enter a temperature between: "))
    
#if temp is unbelievable, temp is invalid. temp data based on natural hottest and coldest recorded temps on earth
    if -126 < temp < 136:
        tempList.append(temp)
        def average(tempList):
            return sum(tempList) / len(tempList)
        averageTemp = average(tempList)
        print("Average temperature: " + str(round(averageTemp, 2)))
#if list has 2 or more entries, tell user if entry is above or below average
        if len(tempList) >=2:
            if temp > averageTemp:
                print(str(temp) + " is above the current average temperature.")
            else:
                print(str(temp) + " is below the current average temperature.")
    else:
        print("Invalid Temperature!")

    control = str(input("Do you want to continue? (Y for yes, any key for no): "))
    if control == 'Y':
        tempTrack = 1
    else:
        tempTrack = 0
        
