import tkinter as tk
def button_clicked():
    print("Button clicked")
window = tk.Tk()
window.title("my first gui")
window.geometry("300x200")
label_MAHNOOR=tk.Label(window, text="MAHNOOR",font=("Arial",20),fg="red",bg="yellow")
label_MAHNOOR.pack()
button=tk.Button(window,text="click me",command=button_clicked)
button.pack()

def login_successfully():

   print("login successfully")
button=tk.Button(window,text="login ",command=login_successfully)
button.pack()


def get_text():
    input_text = entry.get()
    print("you entered",input_text)
entry =tk.Entry(window,width=30)
entry.pack()

window.mainloop()