import tkinter as tk
from tkinter import messagebox
import string as st
import secrets as sc
import random as rand
import pyperclip

version = 0.2
author = "Updated Cake"

##############################
### Main Code - Generating ###
##############################

# Variables to save characters for multiple usage
lowAlp = st.ascii_lowercase
upAlp = st.ascii_uppercase
digits = st.digits
specialChars = st.punctuation

# Main generating function of passwords
def generatePassword():
    mainX = int(AlpSpin.get())
    mainY = int(digitsSpin.get())
    mainZ = int(charSpecSpin.get())

    totalLength = mainX
    mainX = mainX - mainY - mainZ
    #print(mainX)
    #print(int(mainX/2))
    mainLowAlp = 0
    mainUpAlp = 0

    # Workaround for odd numbers to have same number of UpChars and LowChars
    # This might be considered for a change as it's weak side of this function
    if(mainX%2 == 0):
        mainLowAlp = int(mainX/2)
        mainUpAlp = int(mainX/2)
    else:
        mainLowAlp = int(mainX/2)
        mainUpAlp = int(mainX/2) + 1

    # Generating and randomizing password
    # Check whether total length is bigger or the same as spec. char./digits count
    # to prevent errors and nonsenses
    if(totalLength >= (mainY + mainZ)):

        pswd2 = ""
        pswd2 += "".join(sc.choice(lowAlp) for i in range(mainLowAlp))
        pswd2 += "".join(sc.choice(upAlp) for i in range(mainUpAlp))
        pswd2 += "".join(sc.choice(digits) for i in range(mainY))
        pswd2 += "".join(sc.choice(specialChars) for i in range(mainZ))

        global password
        password = "".join(rand.sample(pswd2,len(pswd2)))

        #print("password: ",password, "length: ",len(password))

        ### GUI part controlling password output label ###
        # This will turn on when everything is alright and password is successfully generated to paste
        # it into password field
        passwordOutputField.config(state="normal")
        passwordOutputField.delete(1.0, tk.END)
        passwordOutputField.insert(tk.END, password)
        passwordOutputField.tag_configure("center", justify="center", foreground=basicFG)
        passwordOutputField.tag_add("center", "1.0", "end")
        passwordOutputField.config(state="disabled")

    else:

        # This will turn on when count of spec. char. and/or digits together is higher than
        # total desired length of password
        # Error function with output
        passwordOutputField.config(state="normal")
        passwordOutputField.delete(1.0, tk.END)
        passwordOutputField.insert(tk.END, "Number of spec. char. and/or digits together is greater than the total length of the password.")
        passwordOutputField.tag_configure("center", justify="center", foreground="red")
        passwordOutputField.tag_add("center", "1.0", "end")
        passwordOutputField.config(state="disabled")

# Pop-up window to confirm copying password into clipboard
# Should be controlled by check-box in future
def copyToClipboard():
    pyperclip.copy(password)
    messagebox.showinfo("Clipboard", "Password successfully copied into clipboard.")
    

###########
### GUI ###
###########


# Basic colors for GUI
basicBG = "#191d30" # dark-blueish color, for backgrounds, etc.
basicBGlight = "#333b61" # light version of it, under for text backgrounds and such things
basicFG = "#d9dfff" # white-blueish color, for text
buttonBG = "#85dcde" # background for buttons inside app, light blue
activeButtonBG = "#3ce85c" # background for active/pushed buttons, light green

window = tk.Tk(className="PasswordGenerator")
window.title("Password Generator")
#window.iconbitmap("lock.ico")
icon = tk.PhotoImage(file="678129.png")
window.iconphoto(True, icon)

# Section to define window size and also put it into middle of the screen
app_width = 760
app_height = 540
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_x = (screen_width - app_width) / 2
position_y = (screen_height - app_height) / 2
window.geometry(f"{app_width}x{app_height}+{int(position_x)}+{int(position_y)}")
window.resizable(False,False) # Turn off resizing window by user

window.configure(bg=basicBG)


### Widgets ###

# Fill labels to define first 2 rows and make things centered
# !!! this is also configured with app_width and app_height of the window !!!
fillLabel1 = tk.Label(
    window,
    text="",
    foreground=basicFG,
    background=basicBG
).grid(row=0, column=0, columnspan=2, rowspan=2)

fillLabel2 = tk.Label(
    window,
    text="",
    foreground=basicFG,
    background=basicBG
).grid(row=0, column=4, columnspan=2, rowspan=2)

# Name label of the software
infoLabel = tk.Label(
    window,
    text="Password Generator",
    font=("Arial",25,"bold"),
    foreground=basicFG,
    background=basicBG
)

# Version and author label
infoVersion = tk.Label(
    window,
    text="v {}, author: {}\n".format(version, author),
    font=("Arial",10,"italic"),
    foreground=basicFG,
    background=basicBG
)

spinLabel = tk.Label(
    window,
    text="Password length:\n(0-60)",
    font=("Arial",10,"bold"),
    foreground=basicFG,
    background=basicBG,
    padx=50
)

AlpSpin = tk.Spinbox(
    window,
    from_=0,
    to=60,
    increment=1,
    validate="key",
    font=("Arial", 12),
    bg=basicBGlight,
    fg=basicFG,
    bd=0,
    width=5
)

AlpSpin.delete(0)
AlpSpin.insert(0, 16)

spinLabel2 = tk.Label(
    window,
    text="Number count:",
    font=("Arial",10,"bold"),
    foreground=basicFG,
    background=basicBG,
    padx=50
)

digitsSpin = tk.Spinbox(
    window,
    from_=0,
    to=60,
    increment=1,
    validate="key",
    font=("Arial", 12),
    bg=basicBGlight,
    fg=basicFG,
    bd=0,
    width=5
)

digitsSpin.delete(0)
digitsSpin.insert(0, 5)

spinLabel3 = tk.Label(
    window,
    text="Spec. char. count:",
    font=("Arial",10,"bold"),
    foreground=basicFG,
    background=basicBG,
    padx=50
)

charSpecSpin = tk.Spinbox(
    window,
    from_=0,
    to=60,
    increment=1,
    validate="key",
    font=("Arial", 12),
    bg=basicBGlight,
    fg=basicFG,
    bd=0,
    width=5,
)

charSpecSpin.delete(0)
charSpecSpin.insert(0, 5)

passwordOutputField = tk.Text(
    window,
    height=5,
    width=40,
    bd=0,
    font=("Arial",11,"bold"),
    foreground=basicFG,
    background=basicBG,
    wrap="word"
)

passwordOutputField.insert(tk.END, "Generated pasword will be here...")
passwordOutputField.tag_configure("center", justify="center")
passwordOutputField.tag_add("center", "1.0", "end")
passwordOutputField.config(state="disabled")

generateButton = tk.Button(
    window,
    text="Generate a password",
    font=("Arial",12,"bold"),
    bd=0,
    background=buttonBG,
    activebackground=activeButtonBG,
    command=generatePassword
)


copyButton = tk.Button(
    window,
    text="Copy to clipboard",
    font=("Arial",10,"bold"),
    bd=0,
    background=buttonBG,
    activebackground=activeButtonBG,
    command=copyToClipboard
)






### Grid system and positions ###

infoLabel.grid(row=0, column=2)
infoVersion.grid(row=1, column=2)
spinLabel.grid(row=2, column=0)
AlpSpin.grid(row=3, column=0)
spinLabel2.grid(row=4, column=0)
digitsSpin.grid(row=5, column=0)
spinLabel3.grid(row=6, column=0)
charSpecSpin.grid(row=7, column=0)
passwordOutputField.grid(row=8, column=2)
generateButton.grid(row=5, column=2)
copyButton.grid(row=9, column=2)




window.mainloop()