import tkinter as tk
from tkinter import messagebox
import string as st
import secrets as sc
import random as rand
import pyperclip

version = 0.3
author = "Updated Cake"

##############################
### Main Code - Generating ###
##############################

# Variables to save characters for multiple usage
lowAlp = st.ascii_lowercase
upAlp = st.ascii_uppercase
digits = st.digits
specialChars = st.punctuation

maxLength = 60
maxDigits = 30
maxSpecChar = 30

# Main generating function of passwords
def generatePassword():
    global mainY
    global mainZ
    mainX = int(AlpSpin.get())
    mainY = int(digitsSpin.get())
    mainZ = int(charSpecSpin.get())

    global totalLength
    totalLength = mainX
    mainX = mainX - mainY - mainZ
    #print(mainX)
    #print(int(mainX/2))
    mainLowAlp = 0
    mainUpAlp = 0

    # Workaround for odd numbers to have same number of UpChars and LowChars
    # !! This might be considered for a change as it's weak side of this generating function
    if(mainX%2 == 0):
        mainLowAlp = int(mainX/2)
        mainUpAlp = int(mainX/2)
    else:
        mainLowAlp = int(mainX/2)
        mainUpAlp = int(mainX/2) + 1

    # Generating and randomizing password
    # Check whether total length is bigger or the same as spec. char./digits count
    # to prevent errors and nonsenses

    if(totalLength > maxLength or mainY > maxDigits or mainZ > maxSpecChar):

        ### GUI part controlling password output label ###
        # This will trigger if some inputs are over limits
        passwordOutputField.config(state="normal")
        passwordOutputField.delete(1.0, tk.END)
        passwordOutputField.insert(tk.END, "Maximum length of password is " + str(maxLength) + 
                                   " characters, maximum count of digits is " + str(maxDigits) +
                                   " characters and maximum count of spec. chars. is " + str(maxSpecChar) + " characters.")
        passwordOutputField.tag_configure("center", justify="center", foreground="red")
        passwordOutputField.tag_add("center", "1.0", "end")
        passwordOutputField.config(state="disabled")
        complexityReset()


    elif(totalLength >= (mainY + mainZ)):
        
        # This section will trigger if everything works as intended and it will generate password
        pswd2 = ""
        pswd2 += "".join(sc.choice(lowAlp) for i in range(mainLowAlp))
        pswd2 += "".join(sc.choice(upAlp) for i in range(mainUpAlp))
        pswd2 += "".join(sc.choice(digits) for i in range(mainY))
        pswd2 += "".join(sc.choice(specialChars) for i in range(mainZ))

        global password
        password = "".join(rand.sample(pswd2,len(pswd2)))
        complexity()

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
    pyperclip.copy(password) # Copy content of password variable into clipboard
    messagebox.showinfo("Clipboard", "Password successfully copied into clipboard.")
    

### Calculate complexity of the password ###
def complexity():

    totalChars = 0

    # Determine if password is created also with alphabet or not
    # Return totalChars possible on every position
    if(totalLength > (mainY + mainZ)):

        if(int(AlpSpin.get()) > 0):
            totalChars += len(lowAlp) + len(upAlp)
        if(int(digitsSpin.get()) > 0):
            totalChars += len(digits)
        if(int(charSpecSpin.get()) > 0):
            totalChars += len(specialChars)
    else:

        if(int(digitsSpin.get()) > 0):
            totalChars += len(digits)
        if(int(charSpecSpin.get()) > 0):
            totalChars += len(specialChars)

    # C = N^L => return total number of possible combinations of characters in entire password
    # C = total complexity of password (possible combinations)
    # N = total possible characters (94 if it's digits + low/up alphabet + spec. char.)
    # L = length of the password
    complexityReturn = (totalChars ** totalLength)

    ### GUI part controlling password complexity output text field ###
    passwordComplexity.config(state="normal")
    passwordComplexity.delete(1.0, tk.END)
    passwordComplexity.insert(tk.END, "The complexity of your password is " + str(complexityReturn) + f" character combinations, which is " + switchQuote(complexityReturn) + ".")
    switchQuoteColor(complexityReturn)
    passwordComplexity.tag_add("center", "1.0", "end")
    passwordComplexity.config(state="disabled")

# Change quote of complexity text field based on password strength - working together with switchQuoteColor
def switchQuote(complexityNumber):
    if complexityNumber >= 24415814458511853031212217774297452627359068628009699173162412638385920137458858765365344460498378437353024168893874176:
        return "definitely an overkill. It's fancy to generate it and you can be sure nobody will crack it, however good luck finding out where to use it"
    elif complexityNumber >= 51302316161984144419861195565637095800805982753435183363003680415173369919685218532657532502016:
        return "... an overkill? This password is for sure really secure but you won't be able to use it for a lot of services"
    elif complexityNumber >= 1380674536088650126365233338290905239051505147118049339937652736:
        return "an extremely strong password, but it might be too long for some services"
    elif complexityNumber >= 37157429083410091685945089785856:
        return "a very strong password, would be truly difficult to guess by brute-force password cracking method"
    elif complexityNumber >= 475920314814253376475136:
        return "a strong password, would be difficult to guess it by brute-force password cracking method" 
    elif complexityNumber >= 6095689385410816:
        return "not a very strong password, still more secure than \"qwerty123\", but it wouldn't be that hard to crack"
    elif complexityNumber >= 689869781056:
        return "a very weak password and would be easy to crack. This score also won't pass the password security requirements of most sites"

# Change color of pass complexity text field based on password strength - working together with switchQuote 
def switchQuoteColor(complexityNumber):
    if complexityNumber >= 24415814458511853031212217774297452627359068628009699173162412638385920137458858765365344460498378437353024168893874176:
        return passwordComplexity.tag_configure("center", justify="center", foreground="#3ce85c")
    elif complexityNumber >= 51302316161984144419861195565637095800805982753435183363003680415173369919685218532657532502016:
        return passwordComplexity.tag_configure("center", justify="center", foreground="#3ce85c")
    elif complexityNumber >= 1380674536088650126365233338290905239051505147118049339937652736:
        return passwordComplexity.tag_configure("center", justify="center", foreground="#3ce85c")
    elif complexityNumber >= 37157429083410091685945089785856:
        return passwordComplexity.tag_configure("center", justify="center", foreground="#3ce85c")
    elif complexityNumber >= 475920314814253376475136:
        return passwordComplexity.tag_configure("center", justify="center", foreground="#95b01e") 
    elif complexityNumber >= 6095689385410816:
        return passwordComplexity.tag_configure("center", justify="center", foreground="#d15e17")
    elif complexityNumber >= 689869781056:
        return passwordComplexity.tag_configure("center", justify="center", foreground="#a61212")

# Function to reset complexity text field (in case of error of other fields, etc.)
def complexityReset():

    passwordComplexity.config(state="normal")
    passwordComplexity.delete(1.0, tk.END)
    passwordComplexity.insert(tk.END, "Complexity of your password...")
    passwordComplexity.tag_configure("center", justify="center", foreground=basicFG)
    passwordComplexity.tag_add("center", "1.0", "end")
    passwordComplexity.config(state="disabled")

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
appWidth = 780
appHeight = 540
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
positionX = (screenWidth - appWidth) / 2
positionY = (screenHeight - appHeight) / 2
window.geometry(f"{appWidth}x{appHeight}+{int(positionX)}+{int(positionY)}")
window.resizable(False,False) # Turn off resizing window by user

window.configure(bg=basicBG)


### Widgets ###

# Fill labels to define first 2 rows and make things centered
# !!! this is also configured with appWidth and appHeight of the window !!!
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

fillLabel3 = tk.Label(
    window,
    text="",
    foreground=basicFG,
    background=basicBG
)

passwordComplexity = tk.Text(
    window,
    height=8,
    width=50,
    bd=0,
    font=("Arial",10,"italic", "bold"),
    foreground=basicFG,
    background=basicBG,
    wrap="word"
)

passwordComplexity.insert(tk.END, "Complexity of your password...")
passwordComplexity.tag_configure("center", justify="center")
passwordComplexity.tag_add("center", "1.0", "end")
passwordComplexity.config(state="disabled")




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
fillLabel3.grid(row=10, column=2, rowspan=2)
passwordComplexity.grid(row=12, column=2)



window.mainloop()