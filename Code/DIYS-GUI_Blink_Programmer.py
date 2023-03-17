from tkinter import *
import serial.tools.list_ports

def connect_init():
    global root, connect_btn
    root = Tk()
    root.title("DIYS - Blink Programmer")
    root.geometry("500x500") #px
    root.config(background="white")

    #Show Available Port(s)
    port_label=Label(root, text="Available Port(s):", bg="white")
    port_label.grid(column=1, row=1, pady=10, padx=10)

    # Show Baud Rate
    port_bd= Label(root, text="Baud Rate:", bg="white")
    port_bd.grid(column=1, row=2, pady=10, padx=10)

    #show button "Refresh"
    refresh_btn=Button(root, text="Refresh", height=1, width=4, command=update_com) #?
    refresh_btn.grid(column=3, row=1, pady=10, padx=10)

    #show "connect" button
    connect_btn= Button(root, text="connect", height=1, width=7, state="disable") #?
    connect_btn.grid(column=3, row=2, pady=10, padx=10)

    update_com()
    baud_select()

def connect_ceck(args):
    if "-" in clicked_com.get() or "-" in clicked_bd.get():
        connect_btn["state"]="disable"

    else :
        connect_btn["state"]="active"

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
    drob_bd=OptionMenu(root, clicked_bd, *bds) #?
    drob_bd.config(width=20)
    drob_bd.grid(column=2, row=2, padx=50)

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
    drob_COM.config(width=20)
    drob_COM.grid(column=2, row=1, padx=50)
    connect_ceck(0)

#def connexion():
#    if connect_btn=


    

connect_init()
root.mainloop()