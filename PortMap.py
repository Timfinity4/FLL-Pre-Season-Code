#!/usr/bin/env pybricks-micropython
try:# all imports here
    from pybricks.hubs import *
    from pybricks.parameters import *
    try: from pybricks.pupdevices import *
    except: from pybricks.ev3devices import *
    from pybricks.robotics import *
    from pybricks.tools import *
except ImportError: print("Import error") #ModuleNotFoundError doesn't seem to work everywhere

try: from PortMapPlus import *
except ImportError: print("PortMapPlus Needed")

hubName = hubType()
if hubName == 'prime':
    #if you are using the spike this is all you need to mess with
    motorRight=Motor(Port.A, Direction.CLOCKWISE)
    motorLeft=Motor(Port.E, Direction.COUNTERCLOCKWISE)
    try:
        colorSensorLeft=ColorSensor(Port.F)
        colorSensorLight=ColorSensor(Port.B)
        driveBase=DriveBase(motorLeft, motorRight, 56, 114)
        hubName += 'snow'
    except:
        driveBase=DriveBase(motorLeft, motorRight, 50, 50)
        hubName += 'bug'

# don't mess with the below unless you are not using the spike
if hubName == 'city':
    pass
if hubName == 'move':
    try:
        motorLeft=Motor(Port.B, Direction.COUNTERCLOCKWISE)
        motorRight=Motor(Port.A, Direction.CLOCKWISE)
        driveBase=DriveBase(motorLeft, motorRight, 50, 50)
    except: print("Check Motors")
if hubName == 'EV3':
    try:
        motorLeft=Motor(Port.A)
        motorGear=Motor(Port.B)
        motorRight=Motor(Port.C)
        motorCross=Motor(Port.D)
        gyroSensor=GyroSensor(Port.S1)
        colorSensor=ColorSensor(Port.S4)
        colorSensorLeft=colorSensor #alias official names
        colorSensorRight=colorSensor
        driveBase=DriveBase(motorLeft, motorRight, 100, 130)
    except: print('Check Ports')
if hubName == 'technic':
    pass
if hubName == 'essential':
    pass

hub = hubDef()
device = Device()

#demo remove later
if __name__=='__main__':
    print(device.has_motorLeft)
    print(device.has_motorRight)
    print(device.has_colorSensorLeft)
    print(device.has_colorSensorRight)
    print(device.has_driveBase)