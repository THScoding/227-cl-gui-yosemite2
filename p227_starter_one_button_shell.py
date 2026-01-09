import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command(ip):
    if ip != "":
        command = ["ping", ip, "-n", "4"]
    else:
        root1 = tk.Tk()
        root1.wm_geometry("200x200")
        root1.title("No IP destined")
        frame_wrong = tk.Frame(root1)
        frame_wrong.grid()
    
        lbl_wrong = tk.Label(frame_wrong, text="Please enter an IP address", font="Times, 26")
        lbl_wrong.pack()
    # Mac version to limit to 4 requests:     command = ["ping", "localhost", "-n", "4"]
    
    subprocess.run(command)
def get_text():
    ip = ip_entry.get()
    do_command(ip)
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# set up button to run the do_command function
ping_btn = tk.Button(frame, text="ping", command=get_text)
ping_btn.pack()
ip = ""
ip_entry = tk.Entry(frame, width=16, textvariable=ip)
ip_entry.pack()

root.mainloop()
