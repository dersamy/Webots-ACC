from controller import DistanceSensor
from vehicle import Driver

driver = Driver()
dist = DistanceSensor('ds', 10)

setpoint = 2
sampleTime = 0.2
kp,kd,ki = 10,0.1,0.1
lastTime, errSum, lastError = 0.0, 0.0, 0.0
Input, output = 0.0, 0.0


def computePID():
    global lastTime,sampleTime,output,errSum,lastError
    now = driver.getTime()
    
    if (now - lastTime >= sampleTime ):
        error = setpoint - Input
        errSum += error
        dErr = error - lastError
        
        output = kp * error + ki * errSum + kd * dErr
        
        output = -output
        lastTime = now
        lastError = error
 
 
def constrain(value, min, max):
    if(value >= max):
        value = max
    elif(value <= min):
        value = min
    return value

while driver.step() != -1:
    Input = dist.getValue()
    computePID()
    val = constrain(output, 0, 20)
    print(output)
    print(val)
    driver.setCruisingSpeed(output)

    pass

