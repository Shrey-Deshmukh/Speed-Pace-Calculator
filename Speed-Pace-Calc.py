from tkinter import*
from tkinter.ttk import*
master = Tk()
master.geometry('800x400')

master.title("Speed and Pace Calculator")

entDIST = Entry(master, width = 10)
entHOUR = Entry(master, width = 10)
entMIN = Entry(master, width = 10)
entSEC = Entry(master, width = 10)
entSPEEDMPS = Entry(master, state = DISABLED, width = 10)
entSPEEDKPH = Entry(master, state = DISABLED, width = 10)
entSPEEDMPH = Entry(master, state = DISABLED, width = 10)
entSPEEDPLAP = Entry(master, state = DISABLED, width = 10)
entPACEKMMIN = Entry(master, state = DISABLED, width = 10)
entPACEKMSEC = Entry(master, state = DISABLED, width = 10)
entPACEMIMIN = Entry(master, state = DISABLED, width = 10)
entPACEMISEC = Entry(master, state = DISABLED, width = 10)


labelCOLON1 = Label(master, text = " : ")
labelCOLON2 = Label(master, text = " : ")
labelCOLON3 = Label(master, text = " : ")
labelCOLON4 = Label(master, text = " : ")
labelTOP = Label(master, text = "Calculate Your Running Speed and Pace  ")
labelDISK = Label(master, text = "Enter distance run in km")
labelTIME = Label(master, text = "Time (in hh:mm:ss)")
labelSPEEDMPS = Label(master, text = "Average speed in m/s")
labelSPEEDKPH = Label(master, text = "Average speed in kmph")
labelSPEEDMPH = Label(master, text = "Average speed in mph")
labelSPEEDPLAP = Label(master, text = "Average seconds per lap")
labelPACEKM = Label(master, text = "Pace per km")
labelPACEMI = Label(master, text = "Pace per mile")


labelTOP.place(x = 60,y = 10)

labelDISK.place(x = 60,y = 40)
entDIST.place(x = 250, y = 40)

labelTIME.place(x = 60, y = 70)
entHOUR.place(x = 250,y = 70)
labelCOLON1.place(x = 320,y = 70)
entMIN.place(x = 335,y = 70)
labelCOLON2.place(x = 405,y = 70)
entSEC.place(x = 420,y = 70)

labelSPEEDMPS.place(x = 60,y = 100)
entSPEEDMPS.place(x = 250, y = 100)

labelSPEEDKPH.place(x = 60,y = 130)
entSPEEDKPH.place(x = 250, y = 130)

labelSPEEDMPH.place(x = 60,y = 160)
entSPEEDMPH.place(x = 250, y = 160)

labelSPEEDPLAP.place(x = 60,y = 190)
entSPEEDPLAP.place(x = 250, y = 190)

labelPACEKM.place(x = 60,y = 220)
entPACEKMMIN.place(x = 250, y = 220)
labelCOLON3.place(x = 320, y = 220)
entPACEKMSEC.place(x = 335, y = 220)

labelPACEMI.place(x = 60,y = 250)
entPACEMIMIN.place(x = 250, y = 250)
labelCOLON4.place(x =320, y = 250)
entPACEMISEC.place(x = 335, y = 250)


def calc():

    disk = float(entDIST.get())
    hour = int(entHOUR.get())
    min = int(entMIN.get())
    sec = int(entSEC.get())

    dism = disk*1000
    laps = dism/400
    time = (hour*60)+(min*60)+sec
    speedms = round(dism/time, 3)
    speedkph = round((18/5)*speedms, 3)
    speedmph = round(0.62137*speedkph, 3)

    pkm = (time*1000)/dism
    minpkm = int(pkm//60)
    secpkm = int(pkm%60)

    secplap = time/laps

    dismile = round(0.62137*disk, 3)
    pmile = time/dismile
    minpmile = int(pmile//60)
    secpmile = int(pmile%60)

    entSPEEDMPS['state'] = NORMAL
    entSPEEDMPS.delete(0, END)
    entSPEEDMPS.insert(0, speedms)
    entSPEEDMPS['state'] = DISABLED

    entSPEEDKPH['state'] = NORMAL
    entSPEEDKPH.delete(0, END)
    entSPEEDKPH.insert(0, speedkph)
    entSPEEDKPH['state'] = DISABLED

    entSPEEDMPH['state'] = NORMAL
    entSPEEDMPH.delete(0, END)
    entSPEEDMPH.insert(0, speedmph)
    entSPEEDMPH['state'] = DISABLED

    entSPEEDPLAP['state'] = NORMAL
    entSPEEDPLAP.delete(0, END)
    entSPEEDPLAP.insert(0, secplap)
    entSPEEDPLAP['state'] = DISABLED

    entPACEKMMIN['state'] = NORMAL
    entPACEKMMIN.delete(0, END)
    entPACEKMMIN.insert(0, minpkm)
    entPACEKMMIN['state'] = DISABLED

    entPACEKMSEC['state'] = NORMAL
    entPACEKMSEC.delete(0, END)
    entPACEKMSEC.insert(0, secpkm)
    entPACEKMSEC['state'] = DISABLED

    entPACEMIMIN['state'] = NORMAL
    entPACEMIMIN.delete(0, END)
    entPACEMIMIN.insert(0, minpmile)
    entPACEMIMIN['state'] = DISABLED

    entPACEMISEC['state'] = NORMAL
    entPACEMISEC.delete(0, END)
    entPACEMISEC.insert(0, secpmile)
    entPACEMISEC['state'] = DISABLED

    f = open("SpeedDetails.txt","a") #a, append mode
    #we are storing only the speed details not pace
    f.write(entSPEEDMPS.get()+";"+entSPEEDKPH.get()+";"+entSPEEDMPH.get()+"\n")
    f.close()


b = Button(master, text = "Calculate", width = 10, command=calc)
b.place(x = 60, y = 280)

mainloop()
