import serial
import time

class Bluetooth:
    """Class Bluetooth in order to send data to Arduino"""
    def __init__(self, port, baud):
        self.port = port
        self.baud = baud
        print("Start")
        self.bluetooth = serial.Serial(self.port, self.baud)  # Start communications with the bluetooth unit
        print("Connected")
        self.bluetooth.flushInput()  # This gives the bluetooth a little kick

    #def initialise_communication(self):
     #  """Initialise the Bluetooth communication"""
      #  print("Start")
       # self.bluetooth=serial.Serial(self.port, self.baud)#Start communications with the bluetooth unit
        #print("Connected")
        #self.bluetooth.flushInput() #This gives the bluetooth a little kick

    def send_data(self, data):
        """Send data to Arduino"""
        self.bluetooth.write(str.encode(str(data)))
        time.sleep(0.4)  # A pause between bursts

    def receive_data(self):
        """Receive data from Arduino"""
        input_data = self.bluetooth.readline()  # This reads the incoming data. In this particular example it will be the "Hello from Blue" line
        time.sleep(0.1)  # A pause between bursts
        return input_data.decode()  # These are bytes coming in so a decode is needed

    def close_communication(self):
        """Close the Bluetooth communication"""
        self.bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
        print("Done")

    def kick(self):
        self.bluetooth.flush()
