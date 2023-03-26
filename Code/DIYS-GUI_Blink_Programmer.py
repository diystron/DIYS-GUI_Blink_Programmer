from tkinter import *
import serial.tools.list_ports
import time


def connect_init():
    global root, connect_btn, refresh_btn, ser
    root = Tk()
    root.title("DIYS - Blink Programmer")
    root.geometry("500x500") #px
    root.config(background="white")

    #Show Available Port(s)
    port_label=Label(root, text="Available Port(s):", bg="white")
    port_label.grid(column=1, row=1)

    # Show Baud Rate
    port_bd= Label(root, text="Baud Rate:", bg="white")
    port_bd.grid(column=1, row=2)

    #show button "Refresh"
    refresh_btn=Button(root, text="Refresh", height=1, width=3, command=update_com) #?
    refresh_btn.grid(column=3, row=1, padx=8)

    #show "connect" button
    connect_btn= Button(root, text="connect", height=1, width=7, state="disable", command=connexion) #?
    connect_btn.grid(column=3, row=2, padx=8)

    update_com()
    baud_select()
    content()
    
    

def connect_ceck(args):
    if "-" in clicked_com.get() or "-" in clicked_bd.get():
        connect_btn["state"] = "disable"

    else :
        connect_btn["state"] = "active"

def baud_select():
    global clicked_bd, drob_bd
    clicked_bd=StringVar()
    bds=[
        "-",
        "110",
        "300",
        "600",
        "1200",
        "2400",
        "4800",
        "9600",
        "14400",
        "19200",
        "38400",
        "57600",
        "115200",
        "128000",
        "256000",
    ]

    clicked_bd.set(bds[0])
    drob_bd=OptionMenu(root, clicked_bd, *bds, command=connect_ceck) #?
    drob_bd.config(width=15)
    drob_bd.grid(column=2, row=2, pady=5)

def update_com():
    global clicked_com, drob_COM
    ports=serial.tools.list_ports.comports()
    coms=[com[0] for com in ports]
    coms.insert(0, "-")

    #for Refresh COM ports
    try:
        drob_COM.destroy()
    except:
        pass

    clicked_com=StringVar()
    clicked_com.set(coms[0])
    drob_COM=OptionMenu(root, clicked_com, *coms, command=connect_ceck) #?
    drob_COM.config(width=15)
    drob_COM.grid(column=2, row=1, pady=5)
    connect_ceck(0)

def connexion():
    global connect_btn, serialData, ser
    if connect_btn["text"] in "Disconnect":
        serialData = False
        connect_btn["text"] = "Connect"
        refresh_btn["state"] = "active"
        drob_bd["state"] = "active"
        drob_COM["state"] = "active"
        serialData = False

    else:
        serialData = True
        connect_btn["text"] = "Disconnect"
        refresh_btn["state"] = "disable"
        drob_bd["state"] = "disable"
        drob_COM["state"] = "disable"
        port = clicked_com.get()
        baud = clicked_bd.get()

        try:
            ser = serial.Serial(port, baud, timeout=0)

        except:
            pass

def dataSend():
    global entryTimeHigh, ser
    #ser.write(b'o')
    time.sleep(1)
    timeHigh = entryTimeHigh.get()
    timeLow = entryTimeLow.get()
    dataToSend = timeHigh + "-" + timeLow
    ser.write(dataToSend.encode())
    #data send testing
    print(dataToSend)
    
    

def content():
    global entryTimeHigh, entryTimeLow
    #display "BLINK SETTING"
    label_BlinkSetting = Label(root, text="BLINK SETTING", background="white")
    label_BlinkSetting.grid(column=2, row=5, pady=5)

    #display label "TIME HIGH"
    label_TimeHigh = Label(root, text="TIME HIGH", background="white")
    label_TimeHigh.grid(column=1, row=7, pady=5)

    #display entry "TIME HIGH"
    entryTimeHigh = Entry(root, width=5)
    entryTimeHigh.insert(0, "500")
    entryTimeHigh.grid(column=2, row=7)

    #display label "TIME LOW"
    label_TimeLow = Label(root, text="TIME LOW", background="white")
    label_TimeLow.grid(column=1, row=8, pady=5)

    #display entry "TIME LOW"
    entryTimeLow = Entry(root, width=5)
    entryTimeLow.insert(0, "500")
    entryTimeLow.grid(column=2, row=8)

    #tombol Button SAVE
    save_btn = Button(root, text="SAVE", height=1, width=4, command=dataSend)
    save_btn.grid(column=3, row=7)




    

connect_init()
root.mainloop()