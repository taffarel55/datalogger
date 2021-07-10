# Datalogger for ATMega328
Work for the lecture Microprocessor Systems ENGC50 from Federal University of Bahia.

Implementation of a Data Logger using C and Python to retrieve the data from sensors (ADC) from ATMega328. 

![dataplotter](https://user-images.githubusercontent.com/24254286/70197806-bfd8bf00-16eb-11ea-86ee-78e6bfe7d23b.gif)

## Installation

The program was mainly designed for Linux, an adaptation is welcome for Windows. We used Python3.5 and the needed packages to work are:

``` $ pip3.5 install pyserial ```

``` $ pip3.5 install matplotlib ```

``` $ sudo apt-get install python3.5-tk ```

## Tested setup
We used the following setup:

![setup](https://user-images.githubusercontent.com/24254286/69362707-cdaf2e80-0c6d-11ea-9f6f-5ea44a958eea.jpg)

Upload the code from ``` /src/uCInterface.ino ``` to your Arduino using Arduino IDE, command line or any other IDE as you wish.

After uploading run the Python program:

```$ python3.5 graphicalInterface.py ```

## Authors

* **Mauricio Taffarel** - [taffarel55](https://github.com/taffarel55)
* **Henrique Poleselo** - [hpoleselo](https://github.com/hpoleselo)
* **Matheus Carvalho Handley**
* **César Soeiro**
* **Miguel Damásio**
* **Pedro Argolo**

## Professor

**Paulo Cesar Farias** - [pcmaf](https://github.com/pcmaf)

