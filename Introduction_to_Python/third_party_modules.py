
#^ Install third party libraries 
    # ~ From command line use 
        # * pip install packageName
        # * pip install ntplib

import ntplib  #* Import the ntplib library to interact with NTP servers
from time import ctime  #* Import the ctime function from time module to convert time to a readable format

c = ntplib.NTPClient()  #* Create a new NTPClient object to communicate with NTP servers

response = c.request('europe.pool.ntp.org', version=3)  #* Send a request to the NTP server for the time, using version 3 of the protocol

print(ctime(response.tx_time))  #* Print the time received from the server after converting it to a readable format using ctime
