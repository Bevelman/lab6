import time
import multiprocessing
from shifter import Shifter



class led8x8():

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
    self.pattern = multiprocessing.Array('i',8)
    self.p = multiprocessing.Process(target=self.display,args=(self.pattern,))
    self.p.daemon = True
    self.p.start

  def display(self):
    while True:
      for i in range(len(self.pattern)):
        self.shifter.shiftByte(self.pattern[i]) # load the row values
        self.shifter.shiftByte(1 << (i)) # select the given row
        self.shifter.latch()
      time.sleep(0.001)