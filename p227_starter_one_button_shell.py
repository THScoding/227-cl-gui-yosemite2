import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import threading

def do_command(ip, option_selected):
    if ip != "":
        if option_selected == "nslookup":
            command = ["nslookup", ip]
        elif option_selected == "ping":
            command = ["ping", ip]
            if infiniteping.get() == 1 and pingcount.get() != 1:
                command.append("-t")
            else:
                if infiniteping.get() ==1:{
                    messagebox.showerror(
                    message="Infinite ping selected while specifying amount of pings.",
                    parent=frame
                )
                
            }
            if pingcount.get() == 1 and infiniteping.get() != 1:
                global pingcountoption
                count = pingcountoption.get()
                command.append("-n")
                command.append(count)
            else:
                if pingcount.get() ==1:{
                    messagebox.showerror(
                    message="Infinite ping selected while specifying amount of pings.",
                    parent=frame
                )
                
                }
            if pingsize.get() == 1:
                global pingsizeoption
                size = pingsizeoption.get()
                command.append("-l")
                command.append(size)
            if pingtimeout.get() == 1:
                global pingtimeoutoption
                timeout = pingtimeoutoption.get()
                command.append("-w")
                command.append(timeout)
            if pinghops.get() == 1:
                global pinghopsoption
                hops = pinghopsoption.get()
                command.append("-i")
                command.append(hops)
            if pingversion.get() == 1:
                global pingversionoptionactual
                selected_pingversionoption = pingversionoptionactual.get()
                if selected_pingversionoption == 0:
                    command.append("-4")
                else:
                    command.append("-6")
        elif option_selected == "nmap":
            command = ["nmap", ip]
        elif option_selected == "tracert":
            command = ["tracert", ip]
        else:
            messagebox.showerror(
                title="An Error Occured", #the title doesnt work still ugh
                message="Please Enter A Valid Command",
                parent=frame
            )
                    
    else:
        messagebox.showerror(
                title="An Error Occured", #this isnt working and is showing the pyton logo instrad
                message="Please Enter An IP Adress", 
                parent=frame
            )
        
    # Mac version to limit to 4 requests:     command = ["ping", "localhost", "-n", "4"]
    try:
        global command_textbox
    
        command_textbox.delete(1.0, tk.END)
        command_textbox.update()

        with subprocess.Popen(command,stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                command_textbox.insert(tk.END,line)
                command_textbox.update()
    except BaseException as e:
            messagebox.showerror(
                title="An Error Occured", #this isnt working and is showing the pyton logo instrad
                message="Please Double-Check Your Selected Options./nError Caught: " + str(e), 
                parent=frame
            )
            
def get_text():
    try:
        ip = ip_entry.get()
        option_selected = options_listbox.curselection()
        option_selected = options_listbox.get(option_selected)
        do_command(ip, option_selected)
    except BaseException as e:
        messagebox.showerror(
                title="An Error Occured", #this isnt working and is showing the pyton logo instrad
                message="Please Double-Check Your Selected Options./nError Caught: " + str(e), 
                parent=frame
            )
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  file.write(text_to_save)
  file.close()

root = tk.Tk()
frame = tk.Frame(root, background="#343434")
frame.pack(fill="both", expand=True)
extra_options = False
#owen here, got the (event) from chatgpt
def on_focus_in(event):
    if ip_entry.get() == "Enter IP Adress":
        ip_entry.delete(0, "end")
        ip_entry.config(foreground="white")
    
def on_focus_out(event):
    if ip_entry.get() == "":
        ip_entry.insert(0, "Enter IP Adress")
        ip_entry.config(foreground="grey")
def pingcountfunction():
    global pingcountoption
    if pingcount.get() == 1:
        pingcountoption.pack()
    else:
        pingcountoption.pack_forget()
def pingsizefunction():
    global pingsizeoption
    if pingsize.get() == 1:
        pingsizeoption.pack()
    else:
        pingsizeoption.pack_forget()
def pingtimeoutfunction():
    global pingtimeoutoption
    if pingtimeout.get() == 1:
        pingtimeoutoption.pack()
    else:
        pingtimeoutoption.pack_forget()

def pinghopsfunction():
    global pinghopsoption
    if pinghops.get() == 1:
        pinghopsoption.pack()
    else:
        pinghopsoption.pack_forget()

def pingversionfunction():
    global pingversionoption
    if pingversion.get() == 1:
        pingversionoption.pack()
        pingversionoption2.pack()
    else:
        pingversionoption2.pack_forget()
        pingversionoption.pack_forget()
            

# set up button to run the do_command function
execute_btn = tk.Button(frame, text="Execute Operation", command=get_text, foreground="#1e1e1e", background="white")
ip = ""
options = ['ping', 'nslookup', 'tracert', 'nmap']
ip_entry = tk.Entry(frame, width=16, textvariable=ip, foreground="grey", background="#1e1e1e")
ip_entry.insert(0, "Enter IP Adress")
command_textbox = tksc.ScrolledText(frame, height=10, width=50, background="#1e1e1e", foreground="white") 
options_listbox = tk.Listbox(frame, height=4, background="#1e1e1e", foreground="white")
save_output_btn = tk.Button(frame, text="Save Output", command=mSave, background="white", foreground="#1e1e1e")
# info_label = tk.Label(frame, text="")
# info_label.pack()

for option in options:
    options_listbox.insert(tk.END, option)

#Variable Barf
pingcountoption = tk.Entry(frame, width = 10)
pingsizeoption = tk.Entry(frame, width=10)
pingtimeoutoption = tk.Entry(frame, width=10)
pinghopsoption = tk.Entry(frame, width=10)
pingversionoptionactual = tk.IntVar()

infiniteping = tk.IntVar()
pingcount = tk.IntVar()
pingsize = tk.IntVar()
pingtimeout = tk.IntVar()
pinghops = tk.IntVar()
pingversion = tk.IntVar()

pingversionoption = tk.Radiobutton(frame, text="IPv4", variable=pingversionoptionactual, value=0)
pingversionoption2 = tk.Radiobutton(frame, text="IPv6", variable=pingversionoptionactual, value=1)
check_ping_infinite = tk.Checkbutton(frame, variable=infiniteping, text="-t")
check_ping_count = tk.Checkbutton(frame, variable=pingcount, command=pingcountfunction, text= "-n")
check_ping_size = tk.Checkbutton(frame, variable=pingsize, command=pingsizefunction, text="-l")
check_ping_timeout = tk.Checkbutton(frame, variable=pingtimeout, command=pingtimeoutfunction, text="-w (ms)")
check_ping_hops = tk.Checkbutton(frame, variable=pinghops, command=pinghopsfunction, text="-i")
check_ping_version = tk.Checkbutton(frame, variable=pingversion, command=pingversionfunction, text="-4 or -6")


#Function Barf
ip_entry.pack()
execute_btn.pack()
save_output_btn.pack()
options_listbox.pack()
command_textbox.pack()

check_ping_infinite.pack()
check_ping_count.pack()
check_ping_size.pack()
check_ping_timeout.pack()
check_ping_hops.pack()
check_ping_version.pack()

#owen talking: i got the bind command from chatgpt 
ip_entry.bind("<FocusIn>", on_focus_in)
ip_entry.bind("<FocusOut>", on_focus_out)
root.mainloop()