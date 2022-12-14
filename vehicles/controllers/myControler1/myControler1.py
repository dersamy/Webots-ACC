from vehicle import Driver
from controller import Keyboard

keyboard = Keyboard(10)
driver = Driver()
speed= 10
keyboard.enable(10)
#driver.setSteeringAngle(0)
#driver.setCruisingSpeed(-10)



while driver.step() != -1:
    key=keyboard.get_key()
    print(key)
    
    #SPEED SELECTION
    match key:
        case '1':
            speed = 10
            print("SPEED 10")
        case '2':
            speed = 20
            print("SPEED 20")
        case '3':
            speed = 30
            print("SPEED 30")    
        case '4':
            speed = 40
            print("SPEED 40")
        case '5':
            speed = 50
            print("SPEED 50")
        case '6':
            speed = 60
            print("SPEED 60") 
    
    #FORWARD/BACKWARD
    match key:
        case 'up':
            driver.setCruisingSpeed(speed)
            print("FORWARD SPEED")
        case 'down':
            driver.setCruisingSpeed(-speed)
            print("BACKWARD SPEED")
        case _:
            driver.setCruisingSpeed(0)
    #LEFT/RIGHT
    match key:
        case 'right':
            driver.setSteeringAngle(1)
            print("TURN LEFT")
        case 'left':
            driver.setSteeringAngle(-1)
            print("TURN RIGHT")    
        case _:
            driver.setSteeringAngle(0)     
           
    pass

# Enter here exit cleanup code.
