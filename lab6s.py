from led8x8 import led8x8

dataPin, latchPin, clockPin = 23, 24, 25
pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001,
0b10100101, 0b10011001, 0b01000010, 0b00111100]
theLed8x8 = led8x8(dataPin,latchPin,clockPin)
theLed8x8.display(pattern)