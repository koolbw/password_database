import tkinter as tk
# import tkinter.tkk as ttk

def submit_credentials():
   username = user_entry.get()
   password = pass_entry.get()

   if username == "admin" and password == "0":
      open_new_window()
      # print("Valid Credentials")
   else:
      error_label.config(text="Invalid username or password")

def open_new_window():
   new_window = tk.Toplevel(window)
   new_window.title("Password Database")
   new_window.geometry("500x300")

   # Create a label widget in the new window
   label = tk.Label(new_window, text="Welcome to the application!")
   label.pack()
   # window.destroy()

window = tk.Tk()
window.title("Login")
window.geometry("300x150")

# greeting = tk.Label(text="Hello, Tkinter")
# greeting.pack()

user_label = tk.Label(text="Username")
# user_label.grid(row=0, column=0, padx=5, pady=5)
user_entry = tk.Entry()
# user_entry.grid(row=0, column=0, padx=5, pady=5)

pass_label = tk.Label(text="Password")
# pass_label.grid(row=0, column=0, padx=5, pady=5)
pass_entry = tk.Entry(show="*")
# pass_entry.grid(row=0, column=0, padx=5, pady=5)


submit_button = tk.Button(text="OK", command=submit_credentials)
# submit_button.grid(row=2, columnspan=2, padx=5, pady=5)

# Label to display error message for invalid credentials
error_label = tk.Label(fg="red")


user_label.pack()
user_entry.pack()
pass_label.pack()
pass_entry.pack()
submit_button.pack()
error_label.pack()
 

window.mainloop()