
# -*- coding: utf-8 -*-
import Tkinter;
from Tkinter import *
import tkMessageBox;
from serial.tools import list_ports
import time
import serial
import re


# Serial port defines
default_baud_rate = 9600;
serial_port = None;
SerPortList = StringVar;
ControllerIsConnected = False;


Btn_FindPorts = Button;
Opt_SerPortSelect = OptionMenu;
SerPortList = StringVar;
PortList = list;

SerialPorts = [0];


# Device defines

StateDevice1 = False;
StateDevice2 = False;
StateDevice3 = False;
StateDevice4 = False;

firstdevice = "First Device";
seconddevice = "Second Device";
thirddevice = "Third Device";
forthdevice = "Fourth Device";

def ToggleDevice1(event):
	global StateDevice1;
	global ControllerIsConnected;
	if(False == ControllerIsConnected):
		return;
	if(StateDevice1 ==  True):
		Device1Btn.config(image = btnOff);
		print "Switching off " + firstdevice;
		StateDevice1 = False;
	else:
		Device1Btn.config(image = btnOn);
		print "Switching on " + firstdevice;
		StateDevice1 = True;

def ToggleDevice2(event):
	global StateDevice2;
	global ControllerIsConnected;
	if(False == ControllerIsConnected):
		return;
	if(StateDevice2 ==  True):
		Device2Btn.config(image = btnOff);
		print "Switching off " +  seconddevice;
		StateDevice2 = False;
	else:
		Device2Btn.config(image = btnOn);
		print "Switching on " +  seconddevice;
		StateDevice2 = True;


def ToggleDevice3(event):
	global StateDevice3;
	global ControllerIsConnected;
	if(False == ControllerIsConnected):
		return;

	if(StateDevice3 ==  True):
		Device3Btn.config(image = btnOff);
		print "Switching off " +  thirddevice;
		StateDevice3 = False;
	else:
		Device3Btn.config(image = btnOn);
		print "Switching on " +  thirddevice;
		StateDevice3 = True;


def ToggleDevice4(event):
	global StateDevice4;
	global ControllerIsConnected;
	if(False == ControllerIsConnected):
		return;

	if(StateDevice4 ==  True):
		Device4Btn.config(image = btnOff);
		print "Switching off " +  forthdevice;
		StateDevice4 = False;
	else:
		Device4Btn.config(image = btnOn);
		print "Switching on " +  forthdevice;
		StateDevice4 = True;


def Cleanup():
	global root;
	global serial_port;

	if(None != serial_port and serial_port.isOpen()):
		serial_port.close();

	root.destroy();
	pass;
	return;

def Set_SerialPort(dummy1,dummy2,dummy3):
	global serial_port;
	global SerPortList;
	global ControllerIsConnected;
	print "Setting serail port: " + SerPortList.get();
	
	# close existing open port getting exception
	# if(serial_port.isOpen()):
		# serial_port.close();
	try:
		serial_port = serial.Serial(SerPortList.get(), timeout=None,\
		baudrate=default_baud_rate,\
		xonxoff=False,\
		rtscts=False,\
		dsrdtr=False,\
		parity=serial.PARITY_NONE,\
		stopbits=serial.STOPBITS_ONE,\
		bytesize=serial.EIGHTBITS);
		serial_port.flush();
		# Serial port is set.., 
		ControllerIsConnected = True;
		
		# Send ready string to check if controller is ready..,
		# TODO

	except:
		print "Could not connect to serial port => " + SerPortList.get();
		tkMessageBox.showinfo("Control Panel", "Could not connect to serial port > " + SerPortList.get());
		raise SystemExit();

	return;

def SendCommand(data):
	global serial_port;
	if(None == serial_port):
		return;
		
	# print "lcd: " + data;
	if(None != data and len(data) > 0):
		# data = data + "\n";
		serial_port.write(data.encode("utf-8"));
		serial_port.flush();
	time.sleep(0.5);
	# print "write done";
	return;


def FindSerPorts():
	global Opt_SerPortSelect;
	global SerPortList;
	global PortList;
	global SerialPorts;

	OptMenu = Opt_SerPortSelect['menu'];
	OptMenu.delete(0, 'end');
	
	PortList = list(list_ports.comports());
	for val in PortList:
		OptMenu.add_command(label=val[0], command=Tkinter._setit(SerPortList, val[0]))

	pass;
	return;

root = Tk();
root.title("Control Panel");
root.configure(background='black');
root.geometry('320x240+700+200');
root.resizable(0,0);

try:
	root.wm_iconbitmap('ctrlbox.ico');
except TclError:
	pass; # Ignore exception, display "Tk" icon and continue.
try:
	btnOff = PhotoImage(file = 'OFF.gif');
	btnOn = PhotoImage(file = 'ON.gif');
except TclError:
	print "Can not find ON/OFF icons";


SerPortList = StringVar(root)

Opt_SerPortSelect	= OptionMenu(root, SerPortList, *SerialPorts);
Btn_FindPorts		= Button(root, text = "Find Ports",		command = FindSerPorts		,bd=3	);
SerPortList.trace('w',Set_SerialPort);
Opt_SerPortSelect.place(x=80,y=10);
Btn_FindPorts.place(x=190,y=12);

Device1Btn = Label (root, image = btnOff,borderwidth=0);
Device1Btn.bind('<Button-1>',ToggleDevice1);
Device1Btn.place(x=250,y=50);
Device1Name = Label(root,text=firstdevice,borderwidth = 0,background='black',fg="white");
Device1Name.place(x=20,y = 50);

Device2Btn = Label (root, image = btnOff,borderwidth=0);
Device2Btn.bind('<Button-1>',ToggleDevice2);
Device2Btn.place(x=250,y=100);
Device2Name = Label(root,text=seconddevice,borderwidth = 0,background='black',fg="white");
Device2Name.place(x=20,y = 100);

Device3Btn = Label (root, image = btnOff,borderwidth=0);
Device3Btn.bind('<Button-1>',ToggleDevice3);
Device3Btn.place(x=250,y=150);
Device3Name = Label(root,text=thirddevice,borderwidth = 0,background='black',fg="white");
Device3Name.place(x=20,y = 150);


Device4Btn = Label (root, image = btnOff,borderwidth=0);
Device4Btn.bind('<Button-1>',ToggleDevice4);
Device4Btn.place(x=250,y=200);
Device4Name = Label(root,text=forthdevice,borderwidth = 0,background='black',fg="white");
Device4Name.place(x=20,y = 200);


root.mainloop();



