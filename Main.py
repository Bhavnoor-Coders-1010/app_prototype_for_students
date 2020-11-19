import webbrowser
from tkinter import *
import time
import turtle
import pandas as pd
from pandastable import Table
def timer_game():
    def timer_study():
        hours = int(input("Enter hours for the timer: "))
        minutes = int(input("Enter minutes for the timer: "))
        seconds = int(input("Enter seconds for the timer: "))

        t1 = turtle.Turtle()
        t1.hideturtle()
        screen1 = t1.getscreen()
        screen1.bgcolor("#39FF14")
        h = str(hours)
        m = str(minutes)
        s = str(seconds)

        while True:
            t1.clear()
            t1.write("Total Time for Studying: " + h.zfill(2) + ":" + m.zfill(2) + ":" + s.zfill(2), align = "center", font=("courier", 25, "normal"))
            t1.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2), align = "center", font = ("courier", 90 ,"normal"))
            seconds -= 1
            time.sleep(1)
            if seconds == -1:
                minutes -= 1
                seconds = 59
            if minutes == -1:
                hours -= 1
                minutes = 59
            if hours == -1:
                break

    def main():
        window = turtle.Screen()
        my_turtle = turtle.Turtle()
        screen = my_turtle.getscreen()
        screen.title("Congratualtions!!")
        screen.bgcolor("purple")
        my_turtle.speed(4)
        my_turtle.hideturtle()

        my_turtle.color("green")
        my_turtle.pensize(5)
        my_turtle.begin_fill()

        my_turtle.forward(100)
        my_turtle.left(135)
        my_turtle.forward(90)
        my_turtle.right(135)
        my_turtle.forward(60)
        my_turtle.left(135)
        my_turtle.forward(60)
        my_turtle.right(135)
        my_turtle.forward(40)
        my_turtle.left(135)
        my_turtle.forward(100)

        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.left(135)
        my_turtle.forward(40)
        my_turtle.right(135)
        my_turtle.forward(60)
        my_turtle.left(135)
        my_turtle.forward(60)
        my_turtle.right(135)
        my_turtle.forward(90)
        my_turtle.left(135)
        my_turtle.forward(95)
        my_turtle.end_fill()

        my_turtle.color("green")
        my_turtle.pensize(1)
        my_turtle.right(90)
        my_turtle.forward(2.5)
        my_turtle.color("brown")
        my_turtle.begin_fill()
        my_turtle.forward(67.5)
        my_turtle.right(90)
        my_turtle.forward(33)
        my_turtle.right(90)
        my_turtle.forward(67.5)
        my_turtle.end_fill()

        my_turtle.speed(1)
        my_turtle.penup()
        msg = "Congratulations! One tree added to your Garden!!!"
        my_turtle.goto(0, -200)  # y is in minus because tree trunk was below x axis
        my_turtle.color("white")
        my_turtle.pendown()
        my_turtle.write(msg, move=False, align="center", font=("Arial", 20, "bold"))

        window.mainloop()

    if __name__ == "__main__":
        timer_study()
    if __name__ == "__main__":
        main()
def class_10():
    class1 = Toplevel(root)
    class1.title("Class 10")
    class1.geometry("330x320+10+150")
    bg_class1_Image = PhotoImage(file=r"bg1.png")
    Label(class1, image=bg_class1_Image).place(relwidth=1, relheight=1)
    def time_table():
        df = pd.read_excel("C:\\Users\\Lenovo\\PycharmProjects\\ATLHackathon\\TIME TABLE IMPLANT - 1.xlsx", "Sheet1")
        timetable = Toplevel(root)
        timetable.title("Time Table")

        frame = Frame(timetable)
        frame.pack()
        pt = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)
        pt.show()

        timetable.mainloop()

    def resources():
        def NCERT():
            new = 2

            url = "https://ncert.nic.in/textbook.php"

            webbrowser.open(url, new=new)

        def sp():
            new = 2

            url = "http://cbseacademic.nic.in/SQP_CLASSX_2020-21.html"

            webbrowser.open(url, new=new)

        def eng():
            new = 2
            webbrowser.open("https://www.youtube.com/playlist?list=PLhK_C4ZNRLNlUp6Z-YRahE9QxFojtOC7j", new=new)

        def hin():
            new = 2
            webbrowser.open("https://www.youtube.com/playlist?list=PL9vL8QnJ37pLd3BkbjfAc-1SGzIjRsrgy", new=new)

        def maths():
            new = 2

            url = "https://www.youtube.com/playlist?list=PLPFrn0ppwwkRgFOztQ-gB910Erc0J_LCv"

            webbrowser.open(url, new=new)

        def science():
            new = 2

            url = "https://www.youtube.com/playlist?list=PLqnSbN61X78ztUToQw4ydvFsfXBwRxeUI"

            webbrowser.open(url, new=new)

        def sst():
            new = 2

            url = "https://www.youtube.com/playlist?list=PLiPy3hM238v7sC_OfTKZi1sJ8YkfUpLq9"

            webbrowser.open(url, new=new)

        def ai():
            new = 2

            url = "https://www.youtube.com/playlist?list=PLrAh6mFoZNYl6XO9UNgbF3GsOs5x-BkYR"

            webbrowser.open(url, new=new)

        def main_subj():
            mainsubj = Toplevel(root)
            mainsubj.title("Main Subjects")
            mainsubj.geometry("400x300+10+150")
            bg_mainsubj_Image = PhotoImage(file=r"bg1.png")
            Label(mainsubj, image=bg_mainsubj_Image).place(relwidth=1, relheight=1)
            greetings_2 = Label(mainsubj, text="Main Subjects", font=("Courier", 20, "bold"))
            greetings_2.grid(row=0, column=0)
            button__1 = Button(mainsubj, text="English", relief=RAISED, bg="cyan", width=10, height=2, bd=5, fg='black',
                               font=("Courier", 20, "bold"), command=lambda: eng())
            button__2 = Button(mainsubj, text="Hindi", relief=RAISED, bg="cyan", width=10, height=2, bd=5,
                               fg='black',
                               font=("Courier", 20, "bold"), command=lambda: hin())
            button__3 = Button(mainsubj, text="Maths", relief=RAISED, bg="cyan", width=10, height=2, bd=5, fg='black',
                               font=("Courier", 20, "bold"), command=lambda: maths())
            button__4 = Button(mainsubj, text="Science", relief=RAISED, bg="cyan", width=10, height=2, bd=5, fg='black',
                               font=("Courier", 20, "bold"), command=lambda: science())
            button__5 = Button(mainsubj, text="SST", relief=RAISED, bg="cyan", width=10, height=2, bd=5,
                               fg='black', font=("Courier", 20, "bold"), command=lambda: sst())

            button__1.grid(row=1, column=0)
            button__2.grid(row=1, column=1)
            button__3.grid(row=3, column=0)
            button__4.grid(row=2, column=0)
            button__5.grid(row=2, column=1)

            mainsubj.mainloop()

        def skill_subj():
            skillsubj = Toplevel(root)
            skillsubj.title("Skill Based")
            skillsubj.geometry("215x215+10+150")
            bg_skillsubj_Image = PhotoImage(file=r"bg1.png")
            Label(skillsubj, image=bg_skillsubj_Image).place(relwidth=1, relheight=1)
            greetings_3 = Label(skillsubj, text="Skill Based", font=("Courier", 20, "bold"))
            greetings_3.grid(row=0, column=0)
            button__6 = Button(skillsubj, text="AI", relief=RAISED, bg="cyan", width=10,padx = 10, height=2, bd=5, fg='black',
                               font=("Courier", 20, "bold"), command=lambda: ai())

            button__6.grid(row=1, column=0)

            skillsubj.mainloop()

        def video():
            video_subj = Toplevel(root)
            video_subj.title("Videos")
            video_subj.geometry("525x200+10+150")
            bg_video_subj_Image = PhotoImage(file=r"bg1.png")
            Label(video_subj, image=bg_video_subj_Image).place(relwidth=1, relheight=1)
            welcome = Label(video_subj, text="Check out videos", font=("Courier", 20, "bold"))
            welcome2= Label(video_subj, text="for all subjects!", font=("Courier", 20, "bold"))
            welcome.grid(row=0, column=0)
            welcome2.grid(row = 1, column = 0)

            button_1 = Button(video_subj, text="Main Subjects", relief=RAISED, bg="cyan", width=14, height=2, bd=5,
                              fg='black', font=("Courier", 20, "bold"), command=lambda: main_subj())
            button_2 = Button(video_subj, text="Skill Based", relief=RAISED, bg="cyan", width=14, height=2, bd=5,
                              fg='black', font=("Courier", 20, "bold"), command=lambda: skill_subj())

            button_1.grid(row=2, column=0)
            button_2.grid(row=2, column=1)

            video_subj.mainloop()

        res = Toplevel(root)
        res.title("Resources")
        res.geometry("400x320+10+150")
        bg_res_Image = PhotoImage(file=r"bg1.png")
        Label(res, image=bg_res_Image).place(relwidth=1, relheight=1)
        welcome = Label(res, text="Use the resources as much as you can!!", font=("Courier", 12, "bold"))
        welcome.grid(row=0, column=0)

        button_1 = Button(res, text="NCERT", relief=RAISED, bg="cyan", width=13, height=2, bd = 5, fg='black',
                          font=("Courier", 20, "bold"), command=lambda: NCERT())
        button_2 = Button(res, text="Sample Papers", relief=RAISED, bg="cyan", width=13, height=2, bd=5,
                          fg='black',
                          font=("Courier", 20, "bold"), command=lambda: sp())
        button_3 = Button(res, text="Videos", relief=RAISED, bg="cyan", width=13, height=2, bd=5, fg='black',
                          font=("Courier", 20, "bold"), command=lambda: video())

        button_1.grid(row=1, column=0)
        button_2.grid(row=2, column=0)
        button_3.grid(row=3, column=0)

        res.mainloop()
    welcome = Label(class1, text="Welcome to Class 10!", font=("Courier", 20, "bold"))
    welcome.grid(row = 0, column = 0)

    button_1 = Button(class1, text="Resources", relief=RAISED, bg="cyan", width=12, height=2, bd=5, fg='black', font=("Courier", 20, "bold"), command=lambda: resources())
    button_2 = Button(class1, text="Study Timer", relief=RAISED, bg="cyan", width=12, height=2, bd=5, fg='black', font=("Courier", 20, "bold"), command=lambda: timer_game())
    button_3 = Button(class1, text="Time Table", relief=RAISED, bg="cyan", width=12, height=2, bd=5, fg='black', font=("Courier", 20, "bold"), command=lambda: time_table())

    button_1.grid(row = 1, column = 0)
    button_2.grid(row=2, column=0)
    button_3.grid(row=3, column=0)

    class1.mainloop()
def select_class():
    selectclass = Toplevel(root)
    selectclass.title("Select Your Class")
    selectclass.geometry("760x450+10+10")
    bg_select_class_Image = PhotoImage(file=r"bg1.png")
    Label(selectclass, image=bg_select_class_Image).place(relwidth=1, relheight=1)
    choose_class = Label(selectclass, text="Dear User, Please select your class!", font=("Courier", 14, "bold"))
    choose_class.grid(row=0, column=1)
    button1 = Button(selectclass, text="Class 1", relief=RAISED, bg="cyan", width=10, height=2, bd=7, fg='black',
                     font=("Courier", 20, "bold"))
    button2 = Button(selectclass, text="Class 2", relief=RAISED, bg="cyan", width=10, height=2, bd=7, fg='black',
                     font=("Courier", 20, "bold"))
    button3 = Button(selectclass, text="Class 3", relief=RAISED, bg="cyan", width=10, height=2, bd=7, fg='black',
                     font=("Courier", 20, "bold"))
    button4 = Button(selectclass, text="Class 4", relief=RAISED, bg="cyan", width=10, height=2, bd=7, fg='black',
                     font=("Courier", 20, "bold"))
    button5 = Button(selectclass, text="Class 5", relief=RAISED, bg="cyan", width=10, height=2, bd=7, fg='black',
                     font=("Courier", 20, "bold"))
    button6 = Button(selectclass, text="Class 6", relief=RAISED, bg="cyan", width=10, height=2, bd=7, fg='black',
                     font=("Courier", 20, "bold"))
    button7 = Button(selectclass, text="Class 7", relief=RAISED, bg="cyan", width=10, height=2, bd=7, fg='black',
                     font=("Courier", 20, "bold"))
    button8 = Button(selectclass, text="Class 8", relief=RAISED, bg="cyan", width=10, height=2, bd=7, fg='black',
                     font=("Courier", 20, "bold"))
    button9 = Button(selectclass, text="Class 9", relief=RAISED, bg="cyan", width=10, height=2, bd=7, fg='black',
                     font=("Courier", 20, "bold"))
    button10 = Button(selectclass, text="Class 10", relief=RAISED, bg="cyan", width=10, height=2, bd=7, fg='black',
                      font=("Courier", 20, "bold"), command=lambda: class_10())
    button11 = Button(selectclass, text="Class 11", relief=RAISED, bg="cyan", width=10, height=2, bd=7, fg='black',
                      font=("Courier", 20, "bold"))
    button12 = Button(selectclass, text="Class 12", relief=RAISED, bg="cyan", width=10, height=2, bd=7, fg='black',
                      font=("Courier", 20, "bold"))

    button1.grid(row=2, column=0)
    button2.grid(row=2, column=1)
    button3.grid(row=2, column=2)
    button4.grid(row=3, column=0)
    button5.grid(row=3, column=1)
    button6.grid(row=3, column=2)
    button7.grid(row=4, column=0)
    button8.grid(row=4, column=1)
    button9.grid(row=4, column=2)
    button10.grid(row=5, column=0)
    button11.grid(row=5, column=1)
    button12.grid(row=5, column=2)

    selectclass.mainloop()
root=Tk()
root.title("Home Screen")
root.geometry("358x300+10+10")

bgImage = PhotoImage(file = r"bg1.png")
Label(root, image = bgImage).place(relwidth = 1, relheight = 1)
greetings = Label(root, text = "Greetings! Glad to see you here!",font=("Courier", 14, "bold"))
greetings.grid(row = 0, column = 1)

button_main = Button(root,text="Select Class",relief=RAISED,bg="cyan",width = 20, height = 3, bd=7,fg='black',font=("Courier", 20, "bold"), command = lambda: select_class())
button_main.grid(row = 2, column = 1)

root.mainloop()