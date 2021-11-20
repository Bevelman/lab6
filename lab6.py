import random
import time
from led8x8 import led8x8
import multiprocessing

dataPin, latchPin, clockPin = 23, 24, 25
led = led8x8(dataPin,latchPin,clockPin)
for i in range(8):
  led.pattern[i]=0b00000000
  if i==4:
    led.pattern[i]=0b00010000

try:
  for i in range(0,8):
    if led.pattern[i]>0:
      x=random.randint(0,3)
      if x==0 and led.pattern[i]!=0b10000000: 
        led.pattern[i]=led.pattern[i]<<1
      elif x==1 and led.pattern[i]!=0b00000001: 
        led.pattern[i]=led.pattern[i]>>1
      elif x==2 and i!=0:
        led.pattern[i-1]=led.pattern[i]
        led.pattern[i]=0b00000000
      elif x==3 and i!=7:
        led.pattern[i+1]=led.pattern[i]
        led.pattern[i]=0b00000000
      break
  time.sleep(0.1)
        


except KeyboardInterrupt:   # catch everything, just in case
  led.p.terminate()      # terminate the process
  led.p.join(2)          # wait up to 2 sec for process termination
                         # before ending code