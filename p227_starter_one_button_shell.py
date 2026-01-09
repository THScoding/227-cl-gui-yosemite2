import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

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
            root1 = tk.Tk()
            root1.wm_geometry("200x200")
            root1.title("No command destined")
            frame_wrong = tk.Frame(root1)
            frame_wrong.grid()
    
            lbl_wrong = tk.Label(frame_wrong, text="Please enter a valid command.", font="Times, 26")
            lbl_wrong.pack()
    else:
        root1 = tk.Tk()
        root1.wm_geometry("200x200")
        root1.title("No IP destined")
        frame_wrong = tk.Frame(root1)
        frame_wrong.grid()
        lbl_wrong = tk.Label(frame_wrong, text="Please enter an IP address.", font="Times, 26")
        lbl_wrong.pack()
    # Mac version to limit to 4 requests:     command = ["ping", "localhost", "-n", "4"]
    try:
        global command_textbox
    
        command_textbox.delete(1.0, tk.END)
        command_textbox.update()

        with subprocess.Popen(command,stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                command_textbox.insert(tk.END,line)
                command_textbox.update()
    except BaseException:
            root1 = tk.Tk()
            root1.wm_geometry("200x200")
            root1.title("An Error Occured")
            frame_wrong = tk.Frame(root1)
            frame_wrong.grid()
    
            lbl_wrong = tk.Label(frame_wrong, text="An Error Occured. Please double-check your selected options.", font="Times, 26")
            lbl_wrong.pack()
def get_text():
    ip = ip_entry.get()
    option_selected = options_listbox.get()
    do_command(ip, option_selected)
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

# set up button to run the do_command function
execute_btn = tk.Button(frame, text="Execute Operation", command=get_text)
ip = ""
options = ('ping', 'nslookup', 'tracert', 'nmap')
ip_entry = tk.Entry(frame, width=16, textvariable=ip)
command_textbox = tksc.ScrolledText(frame, height=10, width=100) 
options_spinbox = tk.Spinbox(frame, values=options, state="readonly")
save_output_btn = tk.Button(frame, text="Save Output", command=mSave)
ip_entry.pack()
execute_btn.pack()
save_output_btn.pack()
options_spinbox.pack()
command_textbox.pack()
root.mainloop()
