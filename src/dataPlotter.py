import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import time
import glob
import argparse
import sys

# Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--savelog", type=str, required=True,
	help="Want to save the data? True or False")
ap.add_argument("-r", "--refreshrate", type=int, required=True,
	help="Every x milliseconds the data will be acquired")
args = vars(ap.parse_args())

# Works on linux change it to use in Windows | BAUDRATE = 9600
port1 = "/dev/ttyACM0"
port2 = "/dev/ttyUSB0"

if (glob.glob(port1)==[port1]): 
	comport = serial.Serial(port1, 9600)
else: 
	comport = serial.Serial(port2, 9600)

print ('Using port: {!r}'.format(comport.name))

# Set this from 1.5 to 2.0s
time.sleep(1.8) 

# Setup for plotting in Matplotlib
style.use('fivethirtyeight')

# Define a vector to graphic data
xs = []
ys = []

# Variable to count the samples that are being received
count = 0

# Reference voltage
Vref = 5

# Create figure, add a plot 1x1 and use plot 1
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
fig.subplots_adjust(0.16, 0.12, 0.95, 0.9, 0.2, 0.2)
dataFromSerial = 0

# Store what the user gave to us
saveLog = args["savelog"]
refreshRate = args["refreshrate"]

def readFromSerial():
    """ Callback that is called everytime we want to plot a new point, the rate
    that this callback is called is defined by the user. This basically hears the
    serial port. """
	# try send 't' serially, read data from serial, convert to int and fits from 0 to 5V 
    try:
        PARAM_CARACTER='t'
        comport.write(PARAM_CARACTER.encode())
        print("TETSTE1")
        print(comport.read())
        dataFromSerial = int.from_bytes(comport.read(), "big")
        print("TESTE2")
        print(dataFromSerial)
        # TODO: Colocar tratamento se vier None
        #dataFromSerial = int.from_bytes(b'\x00\x01', "big")
        return dataFromSerial*Vref/255
    except(KeyboardInterrupt, ):
        comport.close()


def plotData(i):
    """ Plot the retrieved data from Arduino via serial communication using Matplotlib. """
    global count, ys  
    count += 1
    data = readFromSerial()
    # The data must me plotted as float not as a string!
    xs.append(float(count))
    ys.append(float(data))

    # Clean everything before we plot
    ax1.clear()
    ax1.plot(xs,ys)

	# Adding labels and title
    ax1.set_xlabel('milliseconds (ms)')
    ax1.set_ylabel('Volts (V)')
    ax1.set_title('Sensor Acquistion')


def saveData():
    """ Store the retrieved data into a txt file to the local where the script is running. """
    outputFile = "logFromATMega328.txt"  
    global xs,ys
    # save data to 2d column, set the decimal precision to 3 floating-point values and ',' as delimiter
    np.savetxt(outputFile, np.column_stack((xs, ys)), fmt='%0.3f', delimiter=',') 


def main():
    """ Calls the plotData() constantly """
	# Create the fig, calls plotData every refreshRate milliseconds
    animt = animation.FuncAnimation(fig, plotData, interval=refreshRate)
    plt.show()
    if saveLog=='True':
        saveData()

if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt):
        comport.close()
