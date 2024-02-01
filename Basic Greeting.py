import time
time_check=time.strftime('%H:%M:%S')
hour=int(time.strftime("%H"))
if(hour < 12 and hour >=0):
    print("goodmorning")
elif(hour >=12 and hour <=17):
    print("goodafternoon")
elif(hour > 17 ):
    print("goodnight")
