import pyspeedtest
from datetime import datetime

st = pyspeedtest.SpeedTest()


def get_speeds():
  speeds = { 
    "up": str(st.upload() / 1000000),
    "down": str(st.download() / 1000000),
  }  
  return speeds

def log_speeds(speeds):
  with open("logs.txt", "a+") as f:
    f.write("At " + str(datetime.now()) + " I got  " + speeds['down'] + " mbs down and " + speeds['up'] + " mbs up.")





speeds = get_speeds()
log_speeds(speeds)


