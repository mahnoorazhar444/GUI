# import tkinter as tk
# window=tk.Tk()
# window.geometry("300x200")
# label=tk.Label(window,text="hello tkinter",fg="blue",bg="yellow",padx=10,pady=5)
# label.pack()
# button=tk.Button(window,text="click me",width=15,command=lambda:
#      print("button clicked"))
# button.pack()
# window.mainloop()
# import tkinter as tk
# window = tk.Tk()
# window.geometry("300x200")
# label = tk.Label(window, text="Initial Text",bg="white",fg="black")
# label.pack()
# current_text = label.cget("text") # Using cget()
# print(f"Current_text: {current_text}")
# current_bg = label.config()["bg"][-1] # Using config() and dictionary access
# print(f"Current background: {current_bg}")


# import tkinter as tk
# window=tk.Tk()
# window.geometry("300x200")
# def colour():
#     current_colour=button.cget("bg")
#     if current_colour=="red":
#          button.config(bg="green")
#     else:
#
#         button.config(bg="red")
#
#
# button=tk.Button(window,text="colour changing",bg="red",command=colour )
# button.pack()
# window.mainloop()
import tkinter as tk

def handle_click(event):
print(f "button clicked at X={event.x}, Y={event.y}")

def handle_key(event):
print(f" Key pressed: {event.char}")

window = tk.Tk()
button = tk.Button(window, text="Click Me")
button.pack()

entry = tk.Entry(window)
entry.pack()

# Bind a function to a left mouse click on the button
button.bind("<Button-1>", handle_click)

# Bind a function to any key press on the entry widget
entry.bind("<Key>", handle_key)

window.mainloop()



