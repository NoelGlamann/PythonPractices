#!/usr/bin/python3
#Noel Glamann
#11/21/2019 

'''last updated :
          by Noel Glamann
          12/18/2019'''

#a214_TR_simple_window1.py
import pickle
import tkinter as tk

#global_variables
login_tries = 0
DEFAULT = ("Arial", 15)

class Catalog(object):
    
    def __init__(self):
        try:
            credentials_file = open("images.pic", "rb")
            self.credentials = pickle.load(credentials_file)
        except:
            credentials_file = open("images.pic", "wb")
            self.credentials = {"admin":["secret", "What is your favorite number in Life?", "thr33"], 
                                "dnoble":["incorrect", "howdy?", "howdy"]}
            pickle.dump(self.credentials, credentials_file)
        credentials_file.close()
               
class Login(tk.Frame):
    login_tries = 0
    global DEFAULT
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        #create login frame stuff
        self.lbl_username = tk.Label(self, 
                                text = "Username:", 
                                font = DEFAULT)
        self.lbl_username.grid(row = 0, 
                               column = 0)
        
        self.ent_username = tk.Entry(self, 
                                bd = 3, 
                                font = DEFAULT)
        self.background = self.ent_username.cget("bg")
        self.ent_username.grid(row = 0, 
                               column = 1)  
        self.lbl_password = tk.Label(self,
                                text="Password:", 
                                font = DEFAULT)
        self.lbl_password.grid(row = 1, 
                               column = 0)
        self.ent_password = tk.Entry(self,
                                bd = 3, 
                                font = DEFAULT,
                                show = "*")
        self.background = self.ent_password.cget("bg")
        self.ent_password.grid(row = 1, 
                               column = 1)
        self.lbl_instruction_1 = tk.Label(self, 
                                          font = ("Arial", 12),
                                          text = "To login, fill out the")
        self.lbl_instruction_1.grid(row = 2, 
                                    column = 0, 
                                    columnspan = 2)
        
        self.lbl_instruction_2 = tk.Label(self, 
                                          font = ("Arial", 12),
                                          text = "boxes and click Login.")
        self.lbl_instruction_2.grid(row = 3, 
                                    column = 0, 
                                    columnspan = 2)
        
        self.btn_login = tk.Button(self, 
                                   text = "LOGIN", 
                                   bg="green",
                                   command = self.login_button, 
                                   font = DEFAULT)
        self.btn_login.grid(row = 4, 
                            column = 0, 
                            columnspan = 2)
        
        self.btn_login = tk.Button(self, 
                              text = "Login", 
                              font = DEFAULT, 
                              command = self.login_button)
        self.btn_login.grid(row = 4, 
                            column = 0, 
                            columnspan = 2)    
    
        
        
    def login_button(self): 
        if Login.login_tries == 2:
            self.btn_login.configure(state = "disabled")
        key = self.ent_username.get()
        if key in users.credentials.keys():
            details = users.credentials[key]
            
            if  self.ent_password.get() == details[0]:
                Login.login_tries = 0 
                self.ent_username.configure(bg = self.background)
                self.ent_password.configure(bg = self.background)
                frame_authenticate.user = key
                frame_authenticate.credentials = users.credentials
                '''frame_authenticate.answer = details[2]'''
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
    auth_tries = 0 
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.user = None
        self.credentials = None

        
        #authenticate screen stuff
        self.lbl_questionlabel = tk. Label(self, 
                                      font = ("Arial", 12), 
                                      text = "Question: ")
        self.lbl_questionlabel.grid(row = 0, 
                               column = 0, 
                               columnspan = 2)
        self.lbl_question = tk.Label(self, 
                                font = DEFAULT, 
                                text = "Something's wrong :(")
        self.lbl_question.grid(row = 1, 
                          column = 0,
                          columnspan = 2)
        self.ent_answer = tk.Entry(self, 
                              bd = 3, 
                              font = DEFAULT, 
                              bg = "blue", 
                              show = "*")
        self.ent_answer.grid(row = 2, 
                        column = 0,
                        columnspan = 2)
        self.btn_cancel = tk.Button(self, 
                                    font = DEFAULT,
                                    text = "Cancel",
                                    command = self.raise_login)
        self.btn_cancel.grid(row = 3, 
                             column = 0)
        self.btn_submit = tk.Button(self, 
                                    font = DEFAULT,
                                    text = "Submit",
                                    command = self.raise_app)
                                        
        self.btn_submit.grid(row = 3,
                             column = 1)
       
        self.btn_add_user = tk.Button(self,
                                      text = "Add User",
                                      font = DEFAULT)
        self.btn_add_user.grid(row = 4,
                               column = 0)
        self.btn_update_user = tk.Button(self, 
                                         text = "Update User",
                                         font = DEFAULT,
                                         command = self.update_user)
        self.btn_update_user.grid(row = 4,
                                  column = 1,
                                  sticky = "E")
        
    def update_user(self):
        if self.auth_tries >= 2:
            root.destroy()
            
        if self.ent_answer.get() == self.credentials[self.user][2]:
            new_password = input("Enter your new password: ")
            new_question = input("Enter your new challenge question: ")
            new_answer = input("Enter the answer to your question: ")
            self.credentials[self.user] = [new_password, new_question, new_answer]
            self.raise_login()
            
        else:
            self.auth_tries += 1
            self.ent_answer.configure(bg = "red")        
        
    def raise_login(self):
        if Authenticate.auth_tries >= 2:
            root.destroy()        
        frame_login.tkraise()
    
    def raise_app(self):
        if self.auth_tries >= 2:
            root.destroy()
            
        if self.ent_answer.get() == self.credentials[self.user][2]:
            frame_app.tkraise()
        else:
            self.auth_tries += 1
            self.ent_answer.configure(bg = "red")
                                    
        

class App(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)

        #Create widgets for app frame
        self.grid_columnconfigure(0, 
                                  weight=1)
        self.lbl_intro = tk.Label(self, 
                                  font = DEFAULT,
                                  text = "Click the button!")
        self.lbl_intro.grid(row = 0, 
                            column = 0)
        self.ent_counter = tk.Entry(self,
                                    font = ("Arial", 24))
        self.ent_counter.grid(row = 1, 
                              column =0)
        self.ent_counter.insert(0, "0")
        self.btn_clicker = tk.Button(self, text = "Click Me!", 
                                     font = DEFAULT,
                                     command = self.click_it)
        self.btn_clicker.grid(row = 2, 
                              column = 0)      


    def click_it(self):
        clicks = int(self.ent_counter.get())
        clicks += 1
        print(clicks)
        self.ent_counter.delete(0, 'end')
        self.ent_counter.insert(0, str(clicks))     

        

  
# main window

# main window

# main window

# main window

# main window

# main window

# main window

root = tk.Tk()

root.title("Activity 2.1.4")

users = Catalog()

frame_login = Login()
frame_login.grid(row=0, 
                 column=0, 
                 sticky="news")

frame_authenticate = Authenticate()
frame_authenticate.grid(row =0,
                        column = 0,
                        sticky = "news")

frame_app = App()
frame_app.grid(row = 0, 
               column = 0, 
               sticky = "news")

frame_login.tkraise()

root.mainloop()