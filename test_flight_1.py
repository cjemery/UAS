from UAS_Functions import Arm_it, connect_it,Get_Parameters, takeoff,land_it
from dronekit import connect, VehicleMode #, LocationGlobalRelative
import time
import atexit
#import RPi.GPIO as GPIO
from ctypes import *
import sys
import argparse

parser=argparse.ArgumentParser(description='parameters')
parser.add_argument('--desiredAlt',help='set desired altitude')
parser.add_argument('--connect',help='set connection string i.e. 127.0.0.1:14550')

args=parser.parse_args()
desiredAlt=float(args.desiredAlt)
connection_string=args.connect



print'***************'

print'DesiredAlt: ',desiredAlt


vehicle=connect_it(connection_string)    #Connect to Pixhawk via Pi
Get_Parameters(vehicle)        #Get start up parameters of UAS
Arm_it(vehicle)        #arm the motors
time.sleep(3)


takeoff(vehicle,desiredAlt)

time.sleep(1)

land_it(vehicle)


