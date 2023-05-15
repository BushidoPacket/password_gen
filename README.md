# Python project: Password Generator

This password generator is my pilot project for Python and Tkinter GUI. I tried few smaller projects before this, however I decided to create something a bit more complex and to add some value to it in every new version.
Basically I wanted to start on a "simple project" and upgrade it with more ideas and different approaches. 

### Full release of stable version of small password generator Python project. 

Password generator is built on secret module from Python, so it should be safe and not predictable as it's based on PRNG. Entire project is created with GUI for user's input so they can change input variables for password's length, digits count or count of special characters. 

Basic principle and settings is trying to push user to use strong combined password. However by manual tweaking of variables user can generate even random stream of alphabet or numbers or special characters alone. Of course there are conditions which will prevent the code or the logic of program from breaking. 

GUI is based on dark mode style with blueish colors to be easy to use. GUI also contains complexity algorithm to determine strength of the password and button to copy password into clipboard. Password generator is also using settings file to store settings of user's inputs if they wish to. 

How the GUI looks like:

![image](https://github.com/UpdatedCake/password_gen/assets/120878764/2990ecc6-b1b6-47e8-97ef-c83782599d06)

![image](https://github.com/UpdatedCake/password_gen/assets/120878764/89631b5f-a5a9-48cc-9f2d-0a06a009f07b)



_File pwd_gen_v1.0_folder.zip contains entire folder with modules and other files._

_Password Generator v 1.0 has been tested only on Windows 10 v22H2 OS without containers._

