import time
from shifter import Shifter



class led8x8():
  

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)

  def display(self, pat):
    while True:
      for i in range(len(pat)):
        self.shifter.shiftByte(pat[i]) # load the row values
        self.shifter.shiftByte(1 << (i-1)) # select the given row
        self.shifter.latch()
      time.sleep(0.001)