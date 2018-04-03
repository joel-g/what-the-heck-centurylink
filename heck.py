import pyspeedtest, time
from datetime import datetime

st = pyspeedtest.SpeedTest()

def get_speeds():
  speeds = { 
    "up": str(round(st.upload() / 1000000, 2)),
    "down": str(round(st.download() / 1000000, 2)),
  }  
  return speeds

def log_speeds(speeds):
  with open("logs.txt", "a+") as f:
    f.write(str(datetime.now()) + ", " + speeds['down'] + ", " + speeds['up'] + "\n")

while True:
  print("Testing...")
  speeds = get_speeds()
  print("Logging...")
  log_speeds(speeds)
  print("Sleeping...")
  time.sleep(3600)