import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox

def do_command(ip, option_selected):
    if ip != "":
        if option_selected == "nslookup":
            command = ["nslookup", ip]
        elif option_selected == "ping":
            command = ["ping", ip]
            if infiniteping.get() == 1 and pingcount.get() != 1:
                command.append("-t")
            else:
                if infiniteping.get() ==1:
                    messagebox.showerror(
                        message="Infinite ping selected while specifying amount of pings.",
                        parent=frame
                    )
                    
            if pingcount.get() == 1 and infiniteping.get() != 1:
                global pingcountoption
                count = pingcountoption.get()
                command.append("-n")
                command.append(count)
                
            else:
                if pingcount.get() ==1:
                    messagebox.showerror(
                    message="Infinite ping selected while specifying amount of pings.",
                    parent=frame
                    )
                
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
            command = ["tracert"]
            if traceversion.get() == 1:
                global traceversionoptionactual
                selected_traceversionoption = traceversionoptionactual.get()

                if selected_traceversionoption == 0:
                    command.append("-4")
                else:
                    command.append("-6")
            if tracetimeout.get() == 1:
                global tracetimeoutoption
                timeout = tracetimeoutoption.get()
                command.append("-w")
                command.append(timeout)
            if tracemaxhops.get() == 1:
                global tracemaxhopsoption
                hops = tracemaxhopsoption.get()
                command.append("-h")
                command.append(hops)
            if tracenoresolve.get() == 1:
                command.append("-d")
            command.append(ip)
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
        
# File saving function      
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

#owen here again, a lot of this is gemini but i made sure to spend time learning what it all did, 
# to whom it may concern: im more than happy explaining it in class.
def on_select(event):
    selection = event.widget.curselection()
    if not selection:
        return

    value = event.widget.get(selection[0])

    if value == "ping":
        show_ping_options()
        hide_tracert_options()
        
        tracemaxhopsoption.pack_forget()
        tracetimeoutoption.pack_forget()
        
        check_trace_no_hostnames.deselect()
        check_trace_max_hops.deselect()
        check_trace_timeout.deselect()
        check_trace_version.deselect()
        
    elif value == "tracert":
        show_tracert_options()
        hide_ping_options()
        
        pingcountoption.pack_forget()
        pingsizeoption.pack_forget()
        pingtimeoutoption.pack_forget()
        pinghopsoption.pack_forget()
        
        check_ping_infinite.deselect()
        check_ping_count.deselect()
        check_ping_size.deselect()
        check_ping_timeout.deselect()
        check_ping_hops.deselect()
        check_ping_version.deselect()
        
    else:
        hide_ping_options()      
        hide_tracert_options()
        
        pingcountoption.pack_forget()
        pingsizeoption.pack_forget()
        pingtimeoutoption.pack_forget()
        pinghopsoption.pack_forget()
        
        check_ping_infinite.deselect()
        check_ping_count.deselect()
        check_ping_size.deselect()
        check_ping_timeout.deselect()
        check_ping_hops.deselect()
        check_ping_version.deselect()
        
        tracemaxhopsoption.pack_forget()
        tracetimeoutoption.pack_forget()
        
        check_trace_no_hostnames.deselect()
        check_trace_max_hops.deselect()
        check_trace_timeout.deselect()
        check_trace_version.deselect()
        
# -------------------------------------
def show_ping_options():
    ping_options_frame.pack()
    
def hide_ping_options():
    ping_options_frame.pack_forget()
# -------------------------------------
def show_tracert_options():
    tracert_options_frame.pack()
    
def hide_tracert_options():
    tracert_options_frame.pack_forget()
# -------------------------------------

#owen here, got the (event) from chatgpt
#placeholder text for entry
def on_focus_in_ip_entry(event):
    if ip_entry.get() == "Enter IP Adress":
        ip_entry.delete(0, "end")
        ip_entry.config(foreground="white")
    
def on_focus_out_ip_entry(event):
    if ip_entry.get() == "":
        ip_entry.insert(0, "Enter IP Adress")
        ip_entry.config(foreground="grey")
        
def on_focus_in_ping_count(event):
    if pingcountoption.get() == "# of Pings":
        pingcountoption.delete(0, "end")
        pingcountoption.config(foreground="white")
    
def on_focus_out_ping_count(event):
    if pingcountoption.get() == "":
        pingcountoption.insert(0, "# of Pings")
        pingcountoption.config(foreground="grey")
        
def on_focus_in_ping_size(event):
    if pingsizeoption.get() == "Size of Packets":
        pingsizeoption.delete(0, "end")
        pingsizeoption.config(foreground="white")
        
def on_focus_out_ping_size(event):
    if pingsizeoption.get() == "":
        pingsizeoption.insert(0, "Size of Packets")  
        pingsizeoption.config(fg="gray") 
        
def on_focus_in_ping_timeout(event):
    if pingtimeoutoption.get() == "Ms to Timeout":
        pingtimeoutoption.delete(0, "end")
        pingtimeoutoption.config(foreground="white")
    
def on_focus_out_ping_timeout(event):
    if pingtimeoutoption.get() == "":
        pingtimeoutoption.insert(0, "Ms to Timeout")  
        pingtimeoutoption.config(fg="gray")
        
def on_focus_in_ping_hops(event):
    if pinghopsoption.get() == "Max # of Hops":
        pinghopsoption.delete(0, "end")
        pinghopsoption.config(foreground="white")
    
def on_focus_out_ping_hops(event):
    if pinghopsoption.get() == "":
        pinghopsoption.insert(0, "Max # of Hops")  
        pinghopsoption.config(fg="gray")
        
#tracert entry placeholder text -------------------------------------------
def on_focus_in_tracert_hops(event):
    if tracemaxhopsoption.get() == "Max # of Hops":
        tracemaxhopsoption.delete(0, "end")
        tracemaxhopsoption.config(foreground="white")
        
def on_focus_out_tracert_hops(event):
    if tracemaxhopsoption.get() == "":
        tracemaxhopsoption.insert(0, "Max # of Hops")  
        tracemaxhopsoption.config(fg="gray")
        
def on_focus_in_tracert_timeout(event):
    if tracetimeoutoption.get() == "Ms to Timeout":
        tracetimeoutoption.delete(0, "end")
        tracetimeoutoption.config(foreground="white")
        
def on_focus_out_tracert_timeout(event):
    if tracetimeoutoption.get() == "":
        tracetimeoutoption.insert(0, "Ms to Timeout")  
        tracetimeoutoption.config(fg="gray")        

#ping functions  ----------------------------------------------------------
def pingcountfunction():
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
    global pingversionoption2
    if pingversion.get() == 1:
        pingversionoption.pack()
        pingversionoption2.pack()
    else:
        pingversionoption2.pack_forget()
        pingversionoption.pack_forget()
        
#trace functions ----------------------------------------------------------
def tracemaxhopsfunction():
    global tracemaxhopsoption
    if tracemaxhops.get() == 1:
        tracemaxhopsoption.pack()
    else:
        tracemaxhopsoption.pack_forget()
        
def tracetimeoutfunction():
    global tracetimeoutoption
    if tracetimeout.get() == 1:
        tracetimeoutoption.pack()
    else:
        tracetimeoutoption.pack_forget()
        
def traceversionfunction():
    global traceversionoption
    global traceversionoption2
    if traceversion.get() == 1:
        traceversionoption.pack()
        traceversionoption2.pack()
    else:
        traceversionoption.pack_forget()
        traceversionoption2.pack_forget()

# set up button to run the do_command function
execute_btn = tk.Button(frame, text="Execute Operation", command=get_text, foreground="#1e1e1e", background="white")
ip = tk.StringVar()
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
ping_options_frame = tk.Frame(frame, bg="#343434")
tracert_options_frame = tk.Frame(frame, bg="#343434")

#ping stuff ---------------------------------------------------------------
#entries with placeholder text
pingcountoption = tk.Entry(frame, width = 15, bg="#1e1e1e", fg="white")
pingcountoption.insert(0, "# of Pings")  
pingcountoption.config(fg="gray")

pingsizeoption = tk.Entry(frame, width=15, bg="#1e1e1e", fg="white")
pingsizeoption.insert(0, "Size of Packets")  
pingsizeoption.config(fg="gray")

pingtimeoutoption = tk.Entry(frame, width=15, bg="#1e1e1e", fg="white")
pingtimeoutoption.insert(0, "Ms to Timeout")  
pingtimeoutoption.config(fg="gray")

pinghopsoption = tk.Entry(frame, width=15, bg="#1e1e1e", fg="white")
pinghopsoption.insert(0, "Max # of Hops")  
pinghopsoption.config(fg="gray")

#all the buttons/options
pingversionoptionactual = tk.IntVar()
infiniteping = tk.IntVar()
pingcount = tk.IntVar()
pingsize = tk.IntVar()
pingtimeout = tk.IntVar()
pinghops = tk.IntVar()
pingversion = tk.IntVar()

pingversionoption = tk.Radiobutton(frame, text="IPv4", variable=pingversionoptionactual, value=0)
pingversionoption2 = tk.Radiobutton(frame, text="IPv6", variable=pingversionoptionactual, value=1)
check_ping_infinite = tk.Checkbutton(ping_options_frame, variable=infiniteping, text="-t")
check_ping_count = tk.Checkbutton(ping_options_frame, variable=pingcount, command=pingcountfunction, text= "-n")
check_ping_size = tk.Checkbutton(ping_options_frame, variable=pingsize, command=pingsizefunction, text="-l")
check_ping_timeout = tk.Checkbutton(ping_options_frame, variable=pingtimeout, command=pingtimeoutfunction, text="-w (ms)")
check_ping_hops = tk.Checkbutton(ping_options_frame, variable=pinghops, command=pinghopsfunction, text="-i")
check_ping_version = tk.Checkbutton(ping_options_frame, variable=pingversion, command=pingversionfunction, text="-4 or -6")

check_ping_infinite.pack(side=tk.LEFT, padx=4)
check_ping_count.pack(side=tk.LEFT, padx=4)
check_ping_size.pack(side=tk.LEFT, padx=4)
check_ping_timeout.pack(side=tk.LEFT, padx=4)
check_ping_hops.pack(side=tk.LEFT, padx=4)
check_ping_version.pack(side=tk.LEFT, padx=4)

#trace stuff --------------------------------------------------------------
#entries with placeholder text
tracemaxhopsoption = tk.Entry(frame, width=15, bg="#1e1e1e", fg="white")
tracemaxhopsoption.insert(0, "Max # of Hops")  
tracemaxhopsoption.config(fg="gray")

tracetimeoutoption = tk.Entry(frame, width=15, bg="#1e1e1e", fg="white")
tracetimeoutoption.insert(0, "Ms to Timeout")  
tracetimeoutoption.config(fg="gray") 

#all the actual tracert buttons/options
tracenoresolve = tk.IntVar()
tracemaxhops = tk.IntVar()
tracetimeout = tk.IntVar()
traceversion = tk.IntVar()
traceversionoptionactual = tk.IntVar()

check_trace_no_hostnames = tk.Checkbutton(tracert_options_frame, variable=tracenoresolve, text="-d")
check_trace_max_hops = tk.Checkbutton(tracert_options_frame, variable=tracemaxhops, command=tracemaxhopsfunction, text="-h")
check_trace_timeout = tk.Checkbutton(tracert_options_frame, variable=tracetimeout, command=tracetimeoutfunction, text="-w (ms)")
check_trace_version = tk.Checkbutton(tracert_options_frame, variable=traceversion, command=traceversionfunction, text="-4 or -6")
traceversionoption = tk.Radiobutton(frame, text="IPv4", variable=traceversionoptionactual, value=0)
traceversionoption2 = tk.Radiobutton(frame, text="IPv6", variable=traceversionoptionactual, value=1)

check_trace_max_hops.pack(side=tk.LEFT, padx=4)
check_trace_no_hostnames.pack(side=tk.LEFT, padx=4)
check_trace_timeout.pack(side=tk.LEFT, padx=4)
check_trace_version.pack(side=tk.LEFT, padx=4)

#Function Barf ------------------------------------------------------------
ip_entry.pack()
execute_btn.pack()
save_output_btn.pack()
options_listbox.pack()
command_textbox.pack()

show_ping_options()
hide_ping_options()

show_tracert_options()
hide_tracert_options()

#owen talking: i got the bind command from chatgpt ------------------------
# all the bindings for the placeholder text
ip_entry.bind("<FocusIn>", on_focus_in_ip_entry)
ip_entry.bind("<FocusOut>", on_focus_out_ip_entry)

pingcountoption.bind("<FocusIn>", on_focus_in_ping_count)
pingcountoption.bind("<FocusOut>", on_focus_out_ping_count)

pingsizeoption.bind("<FocusIn>", on_focus_in_ping_size)
pingsizeoption.bind("<FocusOut>", on_focus_out_ping_size)

pingtimeoutoption.bind("<FocusIn>", on_focus_in_ping_timeout)
pingtimeoutoption.bind("<FocusOut>", on_focus_out_ping_timeout)

pinghopsoption.bind("<FocusIn>", on_focus_in_ping_hops)
pinghopsoption.bind("<FocusOut>", on_focus_out_ping_hops)

#tracert options ----------------------------------------------------------
tracemaxhopsoption.bind("<FocusIn>", on_focus_in_tracert_hops)
tracemaxhopsoption.bind("<FocusOut>", on_focus_out_tracert_hops)

tracetimeoutoption.bind("<FocusIn>", on_focus_in_tracert_timeout)
tracetimeoutoption.bind("<FocusOut>", on_focus_out_tracert_timeout)

# the rest ----------------------------------------------------------------
options_listbox.bind("<<ListboxSelect>>", on_select)
root.mainloop()