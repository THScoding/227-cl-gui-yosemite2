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
            command = ["ping", ip, "-n", "4"]
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
frame = tk.Frame(root)
frame.pack()

#owen here, got the (event) from chatgpt
def on_focus_in(event):
    if ip_entry.get() == "Enter IP Adress":
        ip_entry.delete(0, "end")
        ip_entry.config(foreground="white")
    
def on_focus_out(event):
    if ip_entry.get() == "":
        ip_entry.insert(0, "Enter IP Adress")
        ip_entry.config(foreground="grey")
    
# set up button to run the do_command function
execute_btn = tk.Button(frame, text="Execute Operation", command=get_text)
ip = ""
options = ['ping', 'nslookup', 'tracert', 'nmap']
ip_entry = tk.Entry(frame, width=16, textvariable=ip, foreground="grey")
ip_entry.insert(0, "Enter IP Adress")
command_textbox = tksc.ScrolledText(frame, height=10, width=50) 
options_listbox = tk.Listbox(frame, height=4)
save_output_btn = tk.Button(frame, text="Save Output", command=mSave)
# info_label = tk.Label(frame, text="")
for option in options:
    options_listbox.insert(tk.END, option)

# info_label.pack()
ip_entry.pack()
execute_btn.pack()
save_output_btn.pack()
options_listbox.pack()
command_textbox.pack()
#owen talking: i got the bind command from chatgpt 
ip_entry.bind("<FocusIn>", on_focus_in)
ip_entry.bind("<FocusOut>", on_focus_out)
root.mainloop()