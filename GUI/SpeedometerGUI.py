#!/usr/bin/env python

from Tkinter import *
from math import *

class SpeedometerGUI(Frame):

   def __init__(self, width, max_number, number_of_labels):
      Frame.__init__(self)

      self.orange_color = '#F38A1D'
      self.blue_color = '#36CCFB'
      self.grey_color = "white"
      self.speed = 0
      self.meanSpeed = 0
      self.numberOfDataPoints = 0
      self.totalSpeed = 0
      self.max_number = max_number+5
      number_of_labels = number_of_labels

      self.speed_start_angle = -8*pi/10
      self.speed_angle_range = -self.speed_start_angle
      self.bgColor = "black"
      self.fgColor = "white"
      self.width = width
      self.height = self.width
      self.canvas = Canvas(self, width=self.width, height=self.height, highlightthickness=0, bg=self.bgColor)
      self.canvas.pack(fill=X)

      self.x0 = self.width/2; lx = 9*self.width/20              # center and half-width of clock face
      self.y0 = self.height/2; ly = 9*self.height/20
      self.r0 = 0.77 * min(lx,ly)         # distance of labels from center     
      self.r1 = 0.65 * min(lx,ly)                     
      self.r2 = min(lx,ly)                        # length of speedArrow
      r3 = 0.95 * min(lx,ly)
      r4 = 0.90 * min(lx,ly)   
      self.r6 = self.r2+4
      self.r7 =self.r2-2

      #self.canvas.create_oval(self.x0-lx-11, self.y0-ly-11, self.x0+lx+11, self.y0+ly+11, outline=self.grey_color, width=4)
      #self.canvas.create_oval(self.x0-self.r1, self.y0-self.r1, self.x0+self.r1, self.y0+self.r1, outline='#7E7E7E', width=3)

      for i in range(0,self.max_number+1):
         phi = self.speed_start_angle + self.speed_angle_range/self.max_number * i
         if i%10 == 0 and i != 0:   
            x = self.x0 + self.r0 * sin(phi)
            y = self.y0 - self.r0 * cos(phi)
            self.canvas.create_text(x, y, fill=self.fgColor, font=('gotham', 36), text=str(i))

         if i%5 != 0:
            x1 = self.x0 + r3 * sin(phi)
            y1 = self.y0 - r3 * cos(phi)
         else:
            x1 = self.x0 + r4 * sin(phi)
            y1 = self.y0 - r4 * cos(phi)


         if i == 0:
            x2 = self.x0 + (self.r2+9) * sin(phi)
            y2 = self.y0 - (self.r2+9) * cos(phi)
            self.canvas.create_line(x1, y1, x2, y2, fill=self.orange_color, width=3)
         elif i == self.max_number:
            break
         else:
            x2 = self.x0 + self.r2 * sin(phi)
            y2 = self.y0 - self.r2 * cos(phi)
            self.canvas.create_line(x1, y1, x2, y2, fill=self.orange_color, width=3)

      for j in range(0,56):
         phi = self.speed_angle_range/55 * (55-j)
         if j%10 == 0 and j != 0:   
            x = self.x0 + self.r0 * sin(phi)
            y = self.y0 - self.r0 * cos(phi)
            self.canvas.create_text(x, y, fill=self.fgColor, font=('gotham', 36), text=str(j/10))

         if j%5 != 0:
            x1 = self.x0 + r3 * sin(phi)
            y1 = self.y0 - r3 * cos(phi)
         else:
            x1 = self.x0 + r4 * sin(phi)
            y1 = self.y0 - r4 * cos(phi)


         if j == 0:
            x2 = self.x0 + (self.r2+9) * sin(phi)
            y2 = self.y0 - (self.r2+9) * cos(phi)
            self.canvas.create_line(x1, y1, x2, y2, fill=self.blue_color, width=3)
         elif j == 55:
            break
         else:
            x2 = self.x0 + self.r2 * sin(phi)
            y2 = self.y0 - self.r2 * cos(phi)
            self.canvas.create_line(x1, y1, x2, y2, fill=self.blue_color, width=3)



      y = self.y0-(self.height/8)
      x_1 = self.x0 + self.r1 * sin(self.speed_start_angle-2*pi/180)
      y_1 = self.y0 - self.r1 * cos(self.speed_start_angle-2*pi/180)
      x_2 = self.x0 + (self.r6+4) * sin(self.speed_start_angle-2*pi/180)
      y_2 = self.y0 - (self.r6+4) * cos(self.speed_start_angle-2*pi/180)
      #self.canvas.create_line(x_1, y_1, x_2, y_2, fill='#7E7E7E', width=4)
      #self.canvas.create_line(self.x0+(self.x0-x_1), y_1, self.x0+(self.x0-x_2), y_2, fill='#7E7E7E', width=4)
      self.canvas.create_line(self.x0, self.y0-r4+5, self.x0, self.y0-ly-9, fill=self.grey_color, width=4)

      #self.canvas.create_rectangle(self.x0-30, y-16, self.x0+30, y+16, outline=self.fgColor, width=3)
      self.canvas.create_text(self.x0, self.y0-(4*self.r1/10), fill=self.fgColor, font=('gotham', 20), text="km/h")
      self.canvas.create_text(self.x0, self.y0, fill=self.fgColor, font=('gotham', 70), text="00:00")
      self.canvas.create_text(self.x0, self.y0+(1*self.r1/2)+6, fill=self.fgColor, font=('gotham', 55), text="00:00")
      
      #GPS and ECU label
      self.canvas.create_text(self.x0-self.width/12, self.height*8.5/10, fill="#EE2B2E", font=('gotham', 40), text="GPS")
      self.canvas.create_text(self.x0+self.width/12, self.width*8.5/10, fill="#138C03", font=('gotham', 40), text="ECU")
     

      self.speedLabel = self.canvas.create_text(self.x0, self.y0-(4*self.r1/5), font=('gotham', 70, 'bold'), text="0")
      
      self.meanSpeedArrow = self.canvas.create_line(self.x0, self.y0, x, y, dash=(4,4), fill="yellow", width=4)  
      self.speedArrow = self.canvas.create_line(self.x0, self.y0, x, y, fill=self.orange_color, width=5)  
      
      self.speedArc = self.canvas.create_arc(self.x0-self.r2-4, self.y0-self.r2-4, self.x0+self.r2+4, self.y0+self.r2+4, outline=self.orange_color, extent=20, style=ARC, width=10, start=180)
      
      self.rpmArrow = self.canvas.create_line(self.x0, self.y0, x, y, fill=self.orange_color, width=5)  
      self.rpmArc = self.canvas.create_arc(self.x0-self.r2-4, self.y0-self.r2-4, self.x0+self.r2+4, self.y0+self.r2+4, outline=self.orange_color, extent=-20, style=ARC, width=10, start=180)

      self.setSpeed(0)
      self.setRPM(0)

   def setMeanSpeed(self,speed):
      self.numberOfDataPoints += 1
      self.totalSpeed += speed
      self.meanSpeed = self.totalSpeed / self.numberOfDataPoints

      self.canvas.delete(self.meanSpeedArrow) 

      meanAngle = self.speed_start_angle + self.speed_angle_range/self.max_number*self.meanSpeed
      x1 = self.x0 + (self.r1+1) * sin(meanAngle)
      y1 = self.y0 - (self.r1+1) * cos(meanAngle)
      x2 = self.x0 + (self.r6+3) * sin(meanAngle)
      y2 = self.y0 - (self.r6+3) * cos(meanAngle)
      self.meanSpeedArrow = self.canvas.create_line(x1, y1, x2, y2, dash=(4,4), fill="yellow", width=4)  
      

   def setSpeed(self, value):
      self.speed = float(value)
      self.setMeanSpeed(self.speed)
      self.canvas.delete(self.speedArrow) 
      self.canvas.delete(self.speedLabel)   
      self.canvas.delete(self.speedArc) 

      phi = self.speed_start_angle + self.speed_angle_range/self.max_number*value
      if phi>self.speed_start_angle + self.speed_angle_range-1.5*pi/180:
         phi = self.speed_start_angle + self.speed_angle_range-1.5*pi/180
      elif phi < self.speed_start_angle:
         phi = self.speed_start_angle
      x1 = self.x0 + (self.r1+1) * sin(phi)
      y1 = self.y0 - (self.r1+1) * cos(phi)
      x2 = self.x0 + (self.r6+5) * sin(phi)
      y2 = self.y0 - (self.r6+5) * cos(phi)                             
      self.speedLabel = self.canvas.create_text(self.x0, self.y0-(7*self.r1/10), font=('gotham', 70, 'bold'), fill=self.fgColor, text=str('%.0f' % self.speed))
      self.speedArrow = self.canvas.create_line(x1, y1, x2, y2, fill=self.orange_color, width=5)
      self.speedArc = self.canvas.create_arc(self.x0-self.r2-4, self.y0-self.r2-4, self.x0+self.r2+4, self.y0+self.r2+4, outline=self.orange_color, extent=(-self.speed_start_angle+phi)*(180/pi), style=ARC, width=10, start=90-(phi*180/pi))
      
      

   def setRPM(self, rpm):

      phi = self.speed_angle_range - self.speed_angle_range/5500*rpm
      if phi<0:
         phi = 1.5*pi/180
      elif phi > self.speed_angle_range:
         phi = self.speed_angle_range
      x1 = self.x0 + (self.r1+1) * sin(phi)
      y1 = self.y0 - (self.r1+1) * cos(phi)
      x2 = self.x0 + (self.r6+5) * sin(phi)
      y2 = self.y0 - (self.r6+5) * cos(phi)
      self.canvas.delete(self.rpmArrow)   
      self.canvas.delete(self.rpmArc)                              
      self.rpmArrow = self.canvas.create_line(x1, y1, x2, y2, fill=self.blue_color, width=5)
      self.rpmArc = self.canvas.create_arc(self.x0-self.r2-4, self.y0-self.r2-4, self.x0+self.r2+4, self.y0+self.r2+4, outline=self.blue_color, extent=-(self.speed_start_angle+phi)*(180/pi), style=ARC, width=10, start=90-self.speed_angle_range*180/pi)




   def reset(self):
      self.meanSpeed = 0
      self.numberOfDataPoints = 0
      self.totalSpeed = 0
      self.setMeanSpeed(0)



# main
if __name__ =='__main__':

   def checkSerial(speed):
      var = raw_input("Command: " )
      if var == "s":
         value = raw_input("Speed: " )
         speed.setSpeed(float(value))
      elif var == "r":
         value = raw_input("RPM: " )
         speed.setRPM(float(value))
      elif var == "reset":
         speed.reset()

      root.after(1, checkSerial(speed))


   root = Tk() 
   c = SpeedometerGUI(350, 40, 4) 
   root.bind('<Escape>', lambda x: root.attributes("-fullscreen", False))
   root.bind('<space>', lambda x: root.attributes("-fullscreen", True))
   #root.config(cursor="none")
   c.pack(fill=X) 
   root.after(1, checkSerial(c))
   root.mainloop()