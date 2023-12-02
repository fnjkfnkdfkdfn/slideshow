from tkinter import Tk, Button
def click_button():
    print("Button clicked!")
root = Tk()
root.title("Hello M00 ICI")
root.geometry("310x310")




def ClickButton():
    if len(inputField.get()):
      labelOne["text"] = "Please Enter Your Name!!"
    else:
        labelOne["text"] = "Hello" + inputField.get()


inputField= Entry(root, width=50,font=("Arial,22"), bg="coral", fg="black", justify="center")
buttonOne = Button(root, text="Click Me", podx=50, pody=5, command=ClickButton, bg="gold", font=("Arial, 14"))
labelOne= Label(root, text="?????????", font=("Arial,14"), fg="purple", pody=20)

inputField.pack(pady=20)
buttonOne.pack(padx=10)
labelOne.pack()

root.mainloop()