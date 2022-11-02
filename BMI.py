def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
#Add code here to calculate BMI
    numHeight=float(height)
    numWeight=float(weight)
    bmi =numWeight/(numHeight*numHeight)
    if (bmi<18.5):
        print("under weight")
    elif(18.5<=bmi<=25):
        print("normal weight")
    else:
        print("over weight")

    print("BMI = "+str(bmi))
#Add code here to display calculate BMI
calculate_bmi(57, 1.73)