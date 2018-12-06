import RPi.GPIO as GPIO
import datetime
import time

mhe=18
phy=17
ws=27
math=23
pwp=22
eee=21
pc=26
free=20

Timetable=[[phy,math,pwp,mhe,phy,ws,ws],[math,math,pwp,pwp,eee,phy,math],[mhe,pc,eee,free,free,free,free],[pwp,pwp,pc,phy,eee,free,free],[phy,phy,ws,ws,free,math],[free,free,free,free]]
subjects={mhe:"mhe",phy:"phy",math:"math",pwp:"pwp",eee:"eee",pc:"pc",free:"free"}

wd={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(mhe,GPIO.OUT)
GPIO.setup(phy,GPIO.OUT)
GPIO.setup(ws,GPIO.OUT)
GPIO.setup(math,GPIO.OUT)
GPIO.setup(pwp,GPIO.OUT)
GPIO.setup(eee,GPIO.OUT)
GPIO.setup(pc,GPIO.OUT)
GPIO.setup(free,GPIO.OUT)


print("welcome to timetable")
GPIO.output(mhe,GPIO.HIGH)
GPIO.output(phy,GPIO.HIGH)
GPIO.output(ws,GPIO.HIGH)
GPIO.output(math,GPIO.HIGH)
GPIO.output(pwp,GPIO.HIGH)
GPIO.output(eee,GPIO.HIGH)
GPIO.output(pc,GPIO.HIGH)
GPIO.output(free,GPIO.HIGH)
time.sleep(2)
print ("Get Ready")
GPIO.output(mhe,GPIO.LOW)
GPIO.output(phy,GPIO.LOW)
GPIO.output(ws,GPIO.LOW)
GPIO.output(math,GPIO.LOW)
GPIO.output(pwp,GPIO.LOW)
GPIO.output(eee,GPIO.LOW)
GPIO.output(pc,GPIO.LOW)
GPIO.output(free,GPIO.LOW)

wk=datetime.datetime.today().weekday()

print("Today is : ",wd[wk])
print("Today we have :")

for i in Timetable[wk]:
    GPIO.output(i,GPIO.HIGH)
    print(subjects[i])

time.sleep(10)

for i in Timetable[wk]:
    GPIO.output(i,GPIO.LOW)

