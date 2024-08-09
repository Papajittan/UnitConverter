from tkinter import *
import scipy as ipy
class UnitConverter:
    root = None
    root2 = None
    e1  = ""
    def __init__(self, speed, pressure, time, force, binary):
        self.speed = speed
        self.pressure = pressure
        self.time = time
        self.force = force
        self.binary = binary
    def clear(self):
        self.value_inside.set("Select a unit")
        self.value_inside2.set("Select a unit")
        self.e1.delete(0, 'end')
        self.textvar.set("")
        self.textvar1.set("")
    def checkfloat(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    def returni(self):
        self.root2.destroy()
        self.root2 = None
        self.textvar.set("")
        self.textvar1.set("")
        self.mainloop()
    def exit(self):
        self.root2.destroy()
        self.root2 = None
        self.textvar.set("")
        self.textvar1.set("")
    def calculate(self):
            v1 = self.e1.get()
            v2 = self.value_inside.get()
            v3 = self.value_inside2.get()
            v4 = self.y
            v5 = v4[v2]
            v6 = v4[v3]
            if(self.checkfloat(v1)):
                v1 = float(v1)
                v7 = v1*v5
                v8 = v7/v6
                self.textvar.set(v8)
                self.textvar1.set("The result is:")
            else:
                self.e1.delete(0, 'end')
    def changew(self, unit):
        if(self.root is not None):
            self.root.destroy()
            self.root = None
        if(self.root2 is None):
            self.root2 = Tk()
        self.root2.configure(bg="gray25")
        self.root2.title("Converting " + unit)
        if(unit == "Speed"):
            self.y = self.speed
            self.x = list(speed.keys())
        elif(unit == "Pressure"):
            self.y = self.pressure
            self.x = list(pressure.keys())
        elif(unit == "Time"):
            self.y = self.time
            self.x = list(time.keys())
        elif(unit == "Binary"):
            self.y = self.binary
            self.x = list(binary.keys())
        elif(unit == "Force"):
            self.y = self.force
            self.x = list(force.keys())
        x2 = self.x
        text9 = Label(text = "Converting "+ unit,fg='ghost white',font='Helvetica 12',bg='MediumOrchid4')
        text9.grid(row=0,column=0,columnspan=4,ipadx=70,ipady=2,pady=1) 
        label1 = Label(text = "Insert a number here:",fg='light cyan',font='Helvetica 10',bg="dark slate grey")
        label1.grid(row=1,column = 0,columnspan=2,ipadx=10,ipady=0,pady=1)
        self.e1 = Entry(bg="thistle2")
        self.e1.grid(row=1,column=2)
        label2 = Label(text = "Convert From:",fg='light cyan',font='Helvetica 10',bg="dark slate grey")
        label2.grid(row = 2,column = 0,columnspan=2,ipadx=30,ipady=0,pady=1)
        self.value_inside = StringVar()
        self.value_inside2 = StringVar()
        self.value_inside.set("Select a unit") 
        self.option_menu = OptionMenu(self.root2, self.value_inside, *self.x)
        self.option_menu.grid(column=2, row=2, sticky=W)
        label3 = Label(text = "Convert To:",fg='light cyan',font='Helvetica 10',bg="dark slate grey")
        label3.grid(row = 3,column = 0,columnspan=2,ipadx=40,ipady=0,pady=1)
        self.value_inside2.set("Select a unit")
        self.option_menu1 = OptionMenu(self.root2, self.value_inside2, *x2)
        self.option_menu1.grid(column=2, row=3, sticky=W)
        self.textvar = StringVar()
        self.textvar1 = StringVar()
        label4 = Label(textvariable=self.textvar1 ,fg='light cyan',font='Helvetica 10',bg="dark slate grey")
        label4.grid(row = 4,column = 0,ipadx=10,ipady=0,pady=1)
        label5 = Label(textvariable= self.textvar,fg='light cyan',font='Helvetica 10',bg="dark slate grey")
        label5.grid(row = 4,column = 1,columnspan=2,ipadx=10,ipady=0,pady=1)
        button6=Button(text='Return',compound=TOP,fg='grey9',bg='MediumPurple1',command=self.returni)
        button6.grid(row=5,column=0)
        button7=Button(text='Convert',compound=TOP,fg='grey9',bg='MediumPurple1',command = self.calculate)
        button7.grid(row=5,column=1)
        button7=Button(text='Clear',compound=TOP,fg='grey9',bg='MediumPurple1',command = self.clear)
        button7.grid(row=5,column=2)
        button8=Button(text='Exit',compound=TOP,fg='grey9',bg='MediumPurple1',command = self.exit)
        button8.grid(row=6,column=1)
        self.root2.mainloop()
    def mainloop(self):
        if(self.root is None):
            self.root = Tk()
        self.root.title("Unit Converter")
        self.root.configure(bg="black")
        text = Label(text = "Unit Converter",fg='black',font='Helvetica 12',bg='azure')
        text.grid(row=0,column=0,columnspan=4,ipadx=135,ipady=2,pady=1) 
        text2 = Label(text = "Select the unit category!",fg='gray84',font='Arail 10',bg='purple')
        text2.grid(row=1,column=0,columnspan=4,ipadx=50,ipady=1,pady=0)
        photo1 = PhotoImage(file='Screenshot_2024-08-09_101946-removebg-preview(1).png')
        photo2 = PhotoImage(file='Screenshot_2024-08-09_102317-removebg-preview.png')
        photo3 = PhotoImage(file='Screenshot_2024-08-09_102600-removebg-preview(1).png')
        photo4 = PhotoImage(file='Screenshot_2024-08-09_224427-removebg-preview(1).png')
        photo5 = PhotoImage(file='Screenshot_2024-08-09_103125-removebg-preview.png')
        button1  =Button(text='Speed',image=photo1,compound=TOP,fg='grey9',bg='MediumPurple1',command=lambda: self.changew("Speed"))
        button1.grid(row=2,column=0,)
        button2  =Button(text='Pressure',image=photo2,compound=TOP,fg='grey9',bg='MediumPurple1',command=lambda: self.changew("Pressure"))
        button2.grid(row=2,column=1)
        button3  =Button(text='Time',image=photo3,compound=TOP,fg='grey9',bg='MediumPurple1',command=lambda: self.changew("Time"))
        button3.grid(row=2,column=2)
        button4  =Button(text='Binary Prefixes',image=photo4,compound=TOP,fg='grey9',bg='MediumPurple1',command=lambda: self.changew("Binary"))
        button4.grid(row=3,column=0,columnspan=2)
        button5  =Button(text='Force',image=photo5,compound=TOP,fg='grey9',bg='MediumPurple1',command=lambda: self.changew("Force"))
        button5.grid(row=3,column=1,columnspan=2)
        self.root.mainloop()
speed = {"kmh": ipy.constants.kmh, "mph": ipy.constants.mph, "mach": ipy.constants.mach, "speed of sound": ipy.constants.speed_of_sound , "knot": ipy.constants.knot, "ms": 1.0}
pressure = {"atm": ipy.constants.atm, "atmosphere": ipy.constants.atmosphere, "bar": ipy.constants.bar, "torr": ipy.constants.torr, "mmHg": ipy.constants.mmHg, "psi": ipy.constants.psi, "pascals": 1.0}
time = {"minute": ipy.constants.minute, "hour": ipy.constants.hour, "day": ipy.constants.day, "week": ipy.constants.week, "year": ipy.constants.year, "Juliian_year": ipy.constants.Julian_year, "second": 1.0}
force = {"dyn":ipy.constants.dyn,"dyne":ipy.constants.dyne,"lbf":ipy.constants.lbf,"pound force":ipy.constants.pound_force,"kgf":ipy.constants.kgf,"kilogram force": ipy.constants.kilogram_force, "newtons": 1.0 }
binary = {"kibi":ipy.constants.kibi, "mebi":ipy.constants.mebi, "gibi":ipy.constants.gibi, "tebi":ipy.constants.tebi, "pebi":ipy.constants.pebi, "exbi":ipy.constants.exbi, "zebi":ipy.constants.zebi, "yobi":ipy.constants.yobi}
converter = UnitConverter(speed, pressure, time, force, binary)
converter.mainloop()
