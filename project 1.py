#Traffic stimulator
print("Traffic signal")
signal=str(input("Enter the signal colour: "))
if signal=="green":
    print("the vehicle can GO")
elif signal=="yellow":
    print("the vehicle can be started")
elif signal=="red":
    print("should stop")
else:
    print("please enter the correct color code")