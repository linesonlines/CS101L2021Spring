# Week 13
# Captain Daryani
# cpd6g3@umsystem.edu
#A
import time

class Clock:
  def __init__(self, hour, minute, second, military):
    self.hour = hour
    self.minute = minute
    self.second = second
    self.military = military

  def __str__ (self):
    if self.military == 1:
      return "{:02}:{:02}:{:02}".format(self.hour, self.minute, self.second)
    elif self.military == 0:
      am = True
      if self.hour > 12:
        am = False
        hour = self.hour - 12
        if hour == 0:
          am = True
      elif self.hour == 12:
        am = False
        hour = self.hour
      elif self.hour == 0:
        am = True
        hour = 12
      else:
        hour = self.hour
      text = "{:02}:{:02}:{:02}".format(hour, self.minute, self.second)
      if am:
        text += " am"
      else:
        text += " pm"
      return text
      
  def tick(self):
    time.sleep(1)
    self.second += 1
    if self.second == 60:
      self.second = 0
      self.minute += 1
    if self.minute == 60:
      self.minute = 0
      self.hour += 1
    if self.hour == 24:
      self.hour = 0

h = int(input("What is the current hour? "))
m = int(input("What is the current minute? "))
s = int(input("What is the current second? "))
clock = Clock(h, m, s, 0)
while True:
 print(str(clock))
 clock.tick()
