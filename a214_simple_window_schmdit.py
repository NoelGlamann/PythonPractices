#!/usr/bin/python3
#T Schmidt
#December 4, 2019

''' Mr. Schmidts Version of my 
                 a214_simple_window1.py
    Copied directly from repository
    to use as a resource for my code. 
'''

#!/usr/bin/python3
# Thorin Schmidt
# 11/21/2019

''' program to experiment with tkinter, frames, and widgets '''
import pickle
import tkinter as tk

#global variables
DEFAULT = ("Arial", 15)

class Catalog(object):
    
    def __init__(self):
        try:
            credentials_file = open("images.pic", "rb")
            self.credentials = pickle.load(credentials_file)
        except:
            credentials_file = open("images.pic", "wb")
            self.credentials = {'admin':['secret', 'What is 1 plus 1?', '42'],
                                'ghopper': ['cricket', "What is your favorite animal?", '42']}
            pickle.dump(self.credentials, credentials_file)
        credentials_file.close()

class Login(tk.Frame):
    login_tries = 0
    
    def __init__(self):
        tk.Frame.__init__(self)
         
        #create login frame stuff
        self.lbl_username = tk.Label(self, text = "Username:", font = DEFAULT)
        self.lbl_username.grid(row = 0, column = 0)
               
        self.ent_username = tk.Entry(self, font = DEFAULT)
        self.ent_username.grid(row = 0, column = 1)
        self.background = self.ent_username.cget("bg")
                               
        self.lbl_password = tk.Label(self, text = "Password:", font = DEFAULT)
        self.lbl_password.grid(row = 1, column = 0)
        
        self.ent_password = tk.Entry(self, show="*", font = DEFAULT)
        self.ent_password.grid(row = 1, column = 1)
        
        self.lbl_instruction_1 = tk.Label(self, font = DEFAULT,
                                     text = "To login, fill out the")
        self.lbl_instruction_1.grid(row = 2, column = 0, columnspan = 2)
        
        self.lbl_instruction_2 = tk.Label(self, font = DEFAULT,
                                     text = "boxes and click Login.")
        self.lbl_instruction_2.grid(row = 3, column = 0, columnspan = 2)     
        
        self.btn_login = tk.Button(self, text = "LOGIN", bg="green",
                              command = self.raise_authenticate, font = DEFAULT)
        self.btn_login.grid(row = 4, column = 0, columnspan = 2) 
        
        self.btn_add_user = tk.Button(self, text ="Add User", font = DEFAULT,
                                      command = "")
        self.btn_add_user.grid(row = 5, column = 0)
        
        self.btn_update_user = tk.Button(self, text ="Update User", font = DEFAULT,
                                      command = "")
        self.btn_update_user.grid(row = 5, column = 1)        
        
        
    def raise_authenticate(self):
        if Login.login_tries >= 2:
            self.btn_login.configure(state = "disabled")
        key = self.ent_username.get() 
        if key in users.credentials.keys():
            details = users.credentials[key]
            
            if  self.ent_password.get() == details[0]:
                Login.login_tries = 0 
                self.ent_username.configure(bg = self.background)
                self.ent_password.configure(bg = self.background)
                frame_authenticate.answer = details[2]
                frame_authenticate.lbl_question.configure(text = details[1])
                frame_authenticate.tkraise()
            else:
                self.ent_username.configure(bg = "red")
                self.ent_password.configure(bg = "red")
                Login.login_tries += 1
        else:
            self.ent_username.configure(bg = "red")
            self.ent_password.configure(bg = "red")
            Login.login_tries += 1            

class Authenticate(tk.Frame):
        
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.answer = None
        self.auth_tries = 0
        
        #Create authentication frame widgets
        self.lbl_question_label = tk.Label(self, font = DEFAULT,
                                     text = "Question: ").grid(
                                         row = 0, column = 0)
                                         
        self.lbl_question = tk.Label(self, font = DEFAULT,
                                     text = "Something's Wrong:(")
        self.lbl_question.grid(row = 0, column = 1) 
        
        self.lbl_answer = tk.Label(self, font = DEFAULT, 
                                   text = "Answer: ").grid(
                                         row = 1, column = 0)
        self.ent_answer = tk.Entry(self, font = DEFAULT, show = '*')
        self.ent_answer.grid(row = 1, column = 1)
        
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = DEFAULT,
                                    bg="yellow",  command = self.raise_login).grid(
                                        row = 2, column = 0)
        
        self.btn_submit = tk.Button(self, text = "Submit", font = DEFAULT,
                                    bg="green",  command = self.raise_app).grid(
                                        row = 2, column = 1)
        
    
    def raise_login(self):
        frame_login.tkraise()
        
    def raise_app(self):
        if self.auth_tries >= 2:
            root.destroy()
            
        if self.ent_answer.get() == self.answer:
            frame_app.tkraise()
        else:
            self.auth_tries += 1
            self.ent_answer.configure(bg = "red")
        
class App(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        #Create widgets for app frame
        self.grid_columnconfigure(0, weight=1)
        self.lbl_intro = tk.Label(self, font = DEFAULT,
                                  text = "Click the button!").grid(
                                      row = 0, column = 0)
        
        self.ent_counter = tk.Entry(self,
                                    font = ("Arial", 24))
        self.ent_counter.grid(row = 1, column =0)
        self.ent_counter.insert(0, "0")

        
        self.btn_clicker = tk.Button(self, text = "Click Me!", font = DEFAULT,
                                    command = self.click_it).grid(
                                        row = 2, column = 0)      
          
    def click_it(self):
        clicks = int(self.ent_counter.get())
        clicks += 1
        self.ent_counter.delete(0, 'end')
        self.ent_counter.insert(0, str(clicks))
    

# main window
root = tk.Tk()
#root.wm_geometry("200x100")
root.title("Activity 214")

users = Catalog()
 
frame_login = Login()
frame_login.grid(row = 0, column = 0, sticky = "news")


#Create Authentication frame stuff
frame_authenticate = Authenticate()
frame_authenticate.grid(row = 0, column = 0, sticky = "news")

frame_app = App()
frame_app.grid(row = 0, column = 0, sticky = "news")

frame_login.tkraise()
root.mainloop()