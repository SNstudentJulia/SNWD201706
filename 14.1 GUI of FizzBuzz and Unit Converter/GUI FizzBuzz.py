import Tkinter
import tkMessageBox


def fizzbuzz():
    start = 0
    answer = entry.get()
    try:
        if int(answer) >= 101:
            tkMessageBox.showwarning("Result", "Please only enter valid numbers between 1 and 100.")
        elif int(answer) == 0:
            tkMessageBox.showwarning("Result", "Please only enter valid numbers between 1 and 100.")
        else:
            number = int(answer)
            tkMessageBox.showinfo("Result", "You did it! Check your result in the console!")
            while True:
                start += 1

                if start > number:
                    break
                elif (start % 3) + (start % 5) == 0:
                    print "fizzbuzz"
                elif start % 3 == 0:
                    print "fizz"
                elif start % 5 == 0:
                    print "buzz"
                else:
                    print start

    except ValueError:
        tkMessageBox.showerror("Result", "Please only enter valid numbers.")


window = Tkinter.Tk()


# greeting text
greeting = Tkinter.Label(window, text="Enter a number!")
greeting.pack()

# entry field
entry = Tkinter.Entry(window)
entry.pack()

# button
button = Tkinter.Button(window, text="FizzBuzz!", command=fizzbuzz)
button.pack()

window.mainloop()
