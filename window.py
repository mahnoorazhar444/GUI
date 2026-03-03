import tkinter as tk
window = tk.Tk()
window.title("login window")
window.geometry("300x200")
label_username=tk.Label(window, text="username",font=("Arial",20),fg="black",bg="white")
label_username.pack()

def get_text():
    input_text = entry.get()
    print("you entered",input_text)
entry =tk.Entry(window,width=30)
entry.pack()
label_password=tk.Label(window, text="password",font=("Arial",20),fg="black",bg="white")
label_password.pack()

def get_text():
    input_text = entry.get()
    print("you entered",input_text)
entry =tk.Entry(window,width=30)
entry.pack()

label_login=tk.Label(window, text="login",font=("Arial",20),fg="black",bg="white")
label_login.pack()
window.mainloop()
if ((username )_entry.get()=="MAHNOOR") & (password_entry.get()=="123")
    print("login successfully")
    message_label.config(text="login successfully",fg="green")
    else:
    print("lodin failed plz try again")
    message_label.config(text="login failed plz try again",fg="red")
    window.mainloop()

