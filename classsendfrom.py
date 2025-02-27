from testclasssend import sentohere

fart = sentohere(5,1)
shit = sentohere(10,2)
fart.getinstance(fart)
shit.getinstance(shit)


fart.moveit()
shit.moveit()
print("now from sent to class")
fart.runfromout()
shit.runfromout()
print("now add ten")
sentohere.Avalues +=1000
fart.runfromout()
shit.runfromout()