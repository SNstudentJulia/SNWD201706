import Tkinter
import tkMessageBox


def test_function():

    try:
            convert = entry.get()
            convert = float(convert)
            miles = convert * 0.621
            tkMessageBox.showinfo("Result", "That equals {} miles.".format(miles))
    except ValueError:
            print "Please only use valid numbers!"
            tkMessageBox.showerror("Result", "Please only use valid numbers!")


window = Tkinter.Tk()


# greeting text
greeting = Tkinter.Label(window, text="Please enter the kilometers you want to convert here:")
greeting.pack()

# entry field
entry = Tkinter.Entry(window)
entry.pack()

# button
button = Tkinter.Button(window, text="Convert!", command=test_function)
button.pack()

# goodbye text
goodbye = Tkinter.Label(window, text=" ")
goodbye.pack()

window.mainloop()