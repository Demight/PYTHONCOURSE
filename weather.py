temperature = 55
raining = True 

if temperature > 80:
    print("It's too hot")
    print("stay inside!")
elif temperature < 27:
    print("It's too cold")
    print("stay inside!")
elif raining and temperature < 60:
    print("It's raining")
    print("stay inside!")
else:
    print("Enjoy the outdoors!")
    print("Have a good day!")
