from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.ttk import Progressbar
from code import *
import ast

global ques, ques_boolean, ques_str, ques_gui, ques_exep, ques_basic, ques_func, ques_modyul, ques_numpy, ques_dfs, ques_library, ques_sequence
ques = 1
ques_basic = 1
ques_func = 1
ques_modyul = 1
ques_numpy = 1
ques_dfs = 1
ques_library = 1
ques_exep = 1
ques_str = 1
ques_boolean = 1
ques_gui = 1
ques_library = 1
ques_sequence = 1


def exit_pre_test():
    test.destroy()
    dash()


def showresult(score):
    global test, username_info, password1, next_pt_b

    lblquestion.destroy()
    radio1.destroy()
    radio2.destroy()
    radio3.destroy()
    radio4.destroy()
    next_pt_b.destroy()
    gold = Image.open("gold.png")
    gold = gold.resize((200, 300), Image.ANTIALIAS)
    gold = ImageTk.PhotoImage(gold)

    silver = Image.open("silver.png")
    silver = silver.resize((200, 300), Image.ANTIALIAS)
    silver = ImageTk.PhotoImage(silver)

    bronze = Image.open("bronze.png")
    bronze = bronze.resize((200, 300), Image.ANTIALIAS)
    bronze = ImageTk.PhotoImage(bronze)

    if score >= 7 and score <= 10:

        file = open(username1 + ".txt", "w")
        file.write('{"username" :' + "\"" + str(username1) + "\"" + ', "password" :' + "\"" + str(
            password1) + "\"" + ',"pretest_score":' + "\"" + str(

            score) + "\"" + ', "mode" : "hard"' +
                   ', "Intro" : "done"' +
                   ', "Basic" : "done"' +
                   ', "Function" : "done"' +
                   ', "Modules" : "done"'
                   ', "Numpy" : "done"' +
                   ', "Boolean" : "done"' +
                   ', "Sequences" : "done"' +
                   ', "Strings" : "undone"' +
                   ', "Dictionary" : "undone"' +
                   ', "Exceptions" : "undone"' +
                   ', "Gui" : "undone"' +
                   ', "Final": "undone"' +
                   '}')
        file.close()

        g_label = Label(test, image=gold)
        g_label.image = gold
        g_label.pack()

        Label(test, text="\n\nYou are an advanced learner!! Your score is:" + str(score), font=(36)).pack()

        Button(test, text="Proceed to Dashboard", font=(36), command=exit_pre_test).pack()






    elif score >= 4 and score < 7:
        file = open(username1 + ".txt", "w")
        file.write('{"username" :' + "\"" + str(username1) + "\"" + ', "password" :' + "\"" + str(
            password1) + "\"" + ',"pretest_score":' + "\"" + str(

            score) + "\"" + ', "mode" : "medium"' +
                   ', "Intro" : "done"' +
                   ', "Basic" : "done"' +
                   ', "Function" : "done"' +
                   ', "Modules" : "done"'
                   ', "Numpy" : "done"' +
                   ', "Boolean" : "done"' +
                   ', "Sequences" : "undone"' +
                   ', "Strings" : "undone"' +
                   ', "Dictionary" : "undone"' +
                   ', "Exceptions" : "undone"' +
                   ', "Gui" : "undone"' +
                   ', "Final": "undone"' +

                   '}')
        file.close()

        s_label = Label(test, image=silver)
        s_label.image = silver
        s_label.pack()

        Label(test, text="\n\nYou are intermediate learner!! \n You can do better!! Your Score is:" + str(score),
              font=(36)).pack()

        Button(test, text="Proceed to Dashboard", font=(36), command=exit_pre_test).pack()


    elif score >= 0 and score < 4:
        file = open(username1 + ".txt", "w")
        file.write('{"username" :' + "\"" + str(username1) + "\"" + ', "password" :' + "\"" + str(
            password1) + "\"" + ',"pretest_score":' + "\"" + str(

            score) + "\"" + ', "mode" : "easy"' +
                   ', "Intro" : "done"' +
                   ', "Basic" : "undone"' +
                   ', "Function" : "undone"' +
                   ', "Modules" : "undone"'
                   ', "Numpy" : "undone"' +
                   ', "Boolean" : "undone"' +
                   ', "Sequences" : "undone"' +
                   ', "Strings" : "undone"' +
                   ', "Dictionary" : "undone"' +
                   ', "Exceptions" : "undone"' +
                   ', "Gui" : "undone"' +
                   ' ,"Final": "undone"' +
                   '}')
        file.close()

        b_label = Label(test, image=bronze)
        b_label.image = bronze
        b_label.pack()

        Label(test, text="\n\nYou are a beginning student \n You need to work Hard Your score is:" + str(score),
              font=(36)).pack()

        Button(test, text="Proceed to Dashboard", font=(36), command=exit_pre_test).pack()


def score_basic():
    score_test_basic = 0
    for i in range(5):
        if user_answer_basic[i] == answers_basic[i]:
            score_test_basic = score_test_basic + 1

    showresult_basic(score_test_basic)


def selected_basic_test():
    global ques_basic
    x = radio_var_basic.get()
    user_answer_basic.append(x)

    if ques_basic < 5:
        radio_var_basic.set(-1)
        lblquestion_basic.config(text=questions_basic_test[indexes_basic[ques_basic]])
        lblimage_basic.config(image=img_list_basic[indexes_basic[ques_basic]])
        r1_basic['text'] = answer_choice_basic_test[indexes_basic[ques_basic]][0]
        r2_basic['text'] = answer_choice_basic_test[indexes_basic[ques_basic]][1]
        r3_basic['text'] = answer_choice_basic_test[indexes_basic[ques_basic]][2]
        r4_basic['text'] = answer_choice_basic_test[indexes_basic[ques_basic]][3]
        ques_basic += 1
    else:
        score_basic()


def test_basic():
    global ques_basic, basic_test, user_answer_basic, lblquestion_basic, lblimage_basic, r1_basic, r2_basic, r3_basic, r4_basic, questions_basic_test, indexes_basic, img_list_basic, answers_basic, answer_choice_basic_test
    basic_test = Toplevel(basic)
    basic_test.title("Proficiency-Test")
    basic_test.geometry("700x700")
    basic_test.iconbitmap('icon.ico')
    indexes_basic = [0, 1, 2, 3, 4]

    ques_basic = 1

    user_answer_basic = []

    file1 = open(username1 + ".txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))
    if "easy" == (dicc.get("mode")):
        questions_basic_test = [
            r"How do we display a value in python?",
            "A method of storing values in a specific call",
            "A method of adding a value multiple times",
            """What will the code output below""",
            "Choose the correct output", ]
        answer_choice_basic_test = [
            ["A. Display", "B. Out", "C.Show", "D.Print"],
            ["A. Cache", "B. Symbol ", "C. Integer", "D. Variable", ],
            ["A. Summation", r" B. Addition", " C. Concatenations", " D. Increment", ],
            [r"A. 7", " B. 3A ", " C. 3+a", r" D. 10", ],
            [r'A. a  ', r' B. 4 ', r' C. 6 ', r'D. no output', ],
        ]

        basic_test_1 = Image.open("basic_medium_1.PNG")
        basic_test_1 = basic_test_1.resize((189, 88), Image.ANTIALIAS)
        basic_test_1 = ImageTk.PhotoImage(basic_test_1)

        basic_test_2 = Image.open("basic_easy_2.PNG")
        basic_test_2 = basic_test_2.resize((166, 101), Image.ANTIALIAS)
        basic_test_2 = ImageTk.PhotoImage(basic_test_2)

        img_list_basic = ["", "", "", basic_test_1, basic_test_2]
        answers_basic = [3, 3, 3, 3, 1]

        Label(basic_test, text="Proficiency Test for BASIC Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(basic_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_basic = Label(basic_test, text=questions_basic_test[indexes_basic[0]], font=("16"),
                                  justify="center", wraplength=400, )
        lblquestion_basic.pack()

        lblimage_basic = Label(basic_test, image="")
        lblimage_basic.pack()

        global radio_var_basic
        radio_var_basic = IntVar()
        radio_var_basic.set(-1)

        r1_basic = Radiobutton(basic_test, text=answer_choice_basic_test[indexes_basic[0]][0], font=("12"),
                               variable=radio_var_basic, value=0)
        r1_basic.pack()

        r2_basic = Radiobutton(basic_test, text=answer_choice_basic_test[indexes_basic[0]][1], font=("12"),
                               variable=radio_var_basic, value=1)
        r2_basic.pack()

        r3_basic = Radiobutton(basic_test, text=answer_choice_basic_test[indexes_basic[0]][2], font=("12"),
                               variable=radio_var_basic, value=2)
        r3_basic.pack()

        r4_basic = Radiobutton(basic_test, text=answer_choice_basic_test[indexes_basic[0]][3], font=("12"),
                               variable=radio_var_basic, value=3)
        r4_basic.pack()

        pques_basic_b = Button(basic_test, text="Submit!", command=selected_basic_test)
        pques_basic_b.pack()

    elif "hard" == (dicc.get("mode")):
        questions_basic_test = [
            r"A method of mathematics that can be used in Python?",
            "Check the code below, what is the output?",
            "Indicate the output of the code below",
            """What does the Code below print? """,
            "What is the output of the code?", ]
        answer_choice_basic_test = [
            ["A. Modulus", "B. Boolean", "C. Analytic", "D. Arithmetic"],
            ["A. 3", r"B. '3.0'", "C. 3.0", "D. None/Incorrect Code", ],
            [r"A. -0.166666662", "B. -0.6666666666666665", " C. 4.5", " D. None/Incorrect Code", ],
            [r"A. 1269", "B. 510", " C. 740.5", r" D. None/Incorrect Code", ],
            [r'A. 370.5', r'B. 248.5', r' C. 12192', r'D. None/Incorrect Code', ],
        ]

        basic_hard_2 = Image.open("basic_hard_2.PNG")
        basic_hard_2 = basic_hard_2.resize((145, 83), Image.ANTIALIAS)
        basic_hard_2 = ImageTk.PhotoImage(basic_hard_2)

        basic_hard_3 = Image.open("basic_hard_3.PNG")
        basic_hard_3 = basic_hard_3.resize((92, 84), Image.ANTIALIAS)
        basic_hard_3 = ImageTk.PhotoImage(basic_hard_3)

        basic_hard_4 = Image.open("basic_hard_4.PNG")
        basic_hard_4 = basic_hard_4.resize((189, 166), Image.ANTIALIAS)
        basic_hard_4 = ImageTk.PhotoImage(basic_hard_4)

        basic_hard_5 = Image.open("basic_hard_5.PNG")
        basic_hard_5 = basic_hard_5.resize((192, 168), Image.ANTIALIAS)
        basic_hard_5 = ImageTk.PhotoImage(basic_hard_5)

        img_list_basic = ["", basic_hard_2, basic_hard_3, basic_hard_4, basic_hard_5]
        answers_basic = [3, 2, 1, 3, 0]

        Label(basic_test, text="Proficiency Test for BASIC Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(basic_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_basic = Label(basic_test, text=questions_basic_test[indexes_basic[0]], font=("16"),
                                  justify="center", wraplength=400, )
        lblquestion_basic.pack()

        lblimage_basic = Label(basic_test, image="")
        lblimage_basic.pack()

        radio_var_basic = IntVar()
        radio_var_basic.set(-1)

        r1_basic = Radiobutton(basic_test, text=answer_choice_basic_test[indexes_basic[0]][0], font=("12"),
                               variable=radio_var_basic, value=0)
        r1_basic.pack()

        r2_basic = Radiobutton(basic_test, text=answer_choice_basic_test[indexes_basic[0]][1], font=("12"),
                               variable=radio_var_basic, value=1)
        r2_basic.pack()

        r3_basic = Radiobutton(basic_test, text=answer_choice_basic_test[indexes_basic[0]][2], font=("12"),
                               variable=radio_var_basic, value=2)
        r3_basic.pack()

        r4_basic = Radiobutton(basic_test, text=answer_choice_basic_test[indexes_basic[0]][3], font=("12"),
                               variable=radio_var_basic, value=3)
        r4_basic.pack()

        pques_basic_b = Button(basic_test, text="Submit!", command=selected_basic_test)
        pques_basic_b.pack()

    elif "medium" == (dicc.get("mode")):
        questions_basic_test = [
            r"A form of divsion wherein we only get the whole number",
            "How do we Print variables?",
            "What will be the output of the code below?",
            """What does the code below print?""",
            "What does the code below display?", ]
        answer_choice_basic_test = [
            ["A. Floor Division", "B. Whole Division", "C. Decimal Division", "D. Modulus Division"],
            [r"A. print('variable')", r"B. print(variable)", r"A. print variable", r"A. print 'variable'", ],
            ["A. 25392", r' B. "25392"', " C. 12192", r' D. "12192"', ],
            ["A. 24", r' B. "24"', " C. 23", r' D. "23"', ],
            ["A. 0", r' B. "0"', " C. 2", r' D. "2"', ],
        ]

        basic_medium_1 = Image.open("basic_medium_1.PNG")
        basic_medium_1 = basic_medium_1.resize((206, 101), Image.ANTIALIAS)
        basic_medium_1 = ImageTk.PhotoImage(basic_medium_1)

        basic_medium_2 = Image.open("basic_medium_2.PNG")
        basic_medium_2 = basic_medium_2.resize((145, 83), Image.ANTIALIAS)
        basic_medium_2 = ImageTk.PhotoImage(basic_medium_2)

        basic_medium_3 = Image.open("basic_medium_3.PNG")
        basic_medium_3 = basic_medium_3.resize((185, 81), Image.ANTIALIAS)
        basic_medium_3 = ImageTk.PhotoImage(basic_medium_3)

        img_list_basic = ["", "", basic_medium_1, basic_medium_2, basic_medium_3, ]
        answers_basic = [0, 1, 2, 0, 0]

        Label(basic_test, text="Proficiency Test for BASIC Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(basic_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_basic = Label(basic_test, text=questions_basic_test[indexes_basic[0]], font=("16"),
                                  justify="center", wraplength=400, )
        lblquestion_basic.pack()

        lblimage_basic = Label(basic_test, image="")
        lblimage_basic.pack()

        radio_var_basic = IntVar()
        radio_var_basic.set(-1)

        r1_basic = Radiobutton(basic_test, text=answer_choice_basic_test[indexes_basic[0]][0], font=("12"),
                               variable=radio_var_basic, value=0)
        r1_basic.pack()

        r2_basic = Radiobutton(basic_test, text=answer_choice_basic_test[indexes_basic[0]][1], font=("12"),
                               variable=radio_var_basic, value=1)
        r2_basic.pack()

        r3_basic = Radiobutton(basic_test, text=answer_choice_basic_test[indexes_basic[0]][2], font=("12"),
                               variable=radio_var_basic, value=2)
        r3_basic.pack()

        r4_basic = Radiobutton(basic_test, text=answer_choice_basic_test[indexes_basic[0]][3], font=("12"),
                               variable=radio_var_basic, value=3)
        r4_basic.pack()

        pques_basic_b = Button(basic_test, text="Submit!", command=selected_basic_test)
        pques_basic_b.pack()


def score():
    score = 0
    for i in range(10):
        if user_answer[i] == answers[i]:
            score = score + 1
    showresult(score)


def selected():
    global ques
    x = radio_var.get()
    user_answer.append(x)

    if ques < 10:
        radio_var.set(-1)
        lblquestion.config(text=questions[indexes[ques]])
        radio1['text'] = answers_choice[indexes[ques]][0]
        radio2['text'] = answers_choice[indexes[ques]][1]
        radio3['text'] = answers_choice[indexes[ques]][2]
        radio4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        score()


def start_pre_test():
    global test, questions, answers_choice, radio_var, answers, indexes, user_answer, radio1, radio2, radio3, radio4, lblquestion, screen1
    messagebox.showinfo("Pre-Test",
                        "Welcome to the beginning of your python Journey!" + "\n\n" + "First, to have a personal learning experience, you need to answer a set of questions will  gauge your prior knowledge in the subject.  \n\nThe test is 10 items that range from easy to difficult. Once you clicked on your answer you advanced to the next question so enter your answers carefully. \n\nGood Luck!")
    screen1.destroy()
    test = Toplevel(screen)
    test.title("Pre-Test")
    test.geometry("700x700")
    test.iconbitmap('icon.ico')
    test.protocol("WM_DELETE_WINDOW", ask_quit)

    questions = [
        " It is a common operator in programming that performs division, \nbut returns only the whole number portion of the answer ",
        "A program that translates AND executes the instructions in a program",
        " A vocabulary and set of grammatical rules to instruct a computer to perform tasks ?",
        "What is the output of this code?  \n >>>spam = “7”\n>>>spam = spam +”0”\n>>>eggs = int(spam) +3\n>>>print(float(eggs))",
        "How would you refer to the randint function if it was imported like this? \n from random import randint as rnd_int",
        "What does this code output? \n  Sum = “1” +”2” +”3” ",
        "What is the output of this code? \n" +
        """strng= "string123"
        lst=[]
        for i in strng:
            lst.append(i)
        lst.sort()  
        print(lst)
        """,
        "What is the output of this code?\n" + """string= "778*%"
    string1="".join(string.split())
    lnt = len(string1)
    print(string*lnt)
    ”""",
        "Which is a Float??",
        "What is the output of this code?\n\n" +
        """nums = (55,44,33,22)
        print(max(min(nums[:2]),abs(-42)))
        """,
    ]
    answers_choice = [
        ["A. Integer Division", "B. Floor Division", "C. Modulo Division", "D. Float Division"],
        ["A. IDE", "B. Compiler", "C. Interpreter", "D. Executer", ],
        ["A. Programming Language", " B. Computer Language", " B. Compiler Language", " D. Markup Language", ],
        ["A. 73.0", "B. 703 ", "C. 10.0 ", " eggs ", ],
        ["A. random_rnd_int", "B. A. random.rnd_int ", "C. randint ", " D. randint.rnd_int ", ],
        ["""A. "6" """, """B. 6""", "C. 123", """D. "123" """, ],
        [""""A. ['1', '2', '3', 't', 'i', 'n', 'r', 's', 'g'] """,
         """ B. ['1', '2', '3', 'g', 'i', 'n', 'r', 's', 't'] """,
         """ C. ['s', 't', 'r', 'i', 'n', 'g', '1', '2', '3'] """,
         """ C. ['s', 't', 'r', 'i', 'n', 'g', '1', '2', '3']"""],
        [""" A. “778*%778*%778*%778*%778*%”""",
         """B.”778*%778*%778*%778*%778*%778*%”   """,
         """C. 778*%778*%    """,
         """D.”778*%778*%778*%778*%” """
         ],
        ["""A. 7.0  """,
         """B. 7 """,
         """C.2/4  """,
         """ D. π"""
         ],
        ["A. 55", " B. 44", "C. 33", " D. 22", ],
    ]
    answers = [0, 2, 0, 0, 1, 3, 1, 1, 2, 1]

    indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    user_answer = []

    logo = Image.open("logo.png")
    logo = logo.resize((100, 100), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)

    l_image = Label(test, image=logo)
    l_image.image = logo
    l_image.pack()

    Label(test, text="Pre-Test", font=("Helvetica", 24)).pack()

    lblquestion = Label(test, text=questions[indexes[0]], font=("16"), justify="center", wraplength=400, )
    lblquestion.pack()

    radio_var = IntVar()
    radio_var.set(-1)

    radio1 = Radiobutton(test, text=answers_choice[indexes[0]][0], font=("12"), variable=radio_var, value=0)
    radio1.pack()

    radio2 = Radiobutton(test, text=answers_choice[indexes[0]][1], font=("12"), variable=radio_var, value=1)
    radio2.pack()

    radio3 = Radiobutton(test, text=answers_choice[indexes[0]][2], font=("12"), variable=radio_var, value=2)
    radio3.pack()

    radio4 = Radiobutton(test, text=answers_choice[indexes[0]][3], font=("12"), variable=radio_var, value=3)
    radio4.pack()

    global next_pt_b
    next_pt_b = Button(test, text="Next", command=selected)
    next_pt_b.pack()


def empty_entry():
    messagebox.showwarning("Registration Error", "Please fill in your details")
    screen1.destroy()
    register()


def user_recognized():
    messagebox.showwarning("Registration Error", "User is already registered")
    screen1.destroy()
    register()


def ruser():
    global username1, password1
    username1 = username.get()
    password1 = password.get()
    userlst = [file for file in os.listdir() if file.endswith(".txt")]
    userlst_lower = [x.lower() for x in userlst]
    while True:
        if username1 == "" or password1 == "":
            empty_entry()
            break

        if username1.lower() + ".txt" in userlst_lower:
            user_recognized()
            break


        else:
            file = open(username1 + ".txt", "w")
            file.write('{"username" :' + "\"" + str(username1) + "\"" + ', "password" :' + "\"" + str(
                password1) + "\"" + ',"pretest_score":' + "\"" + "\"" + '}')
            file.close()
            messagebox.showinfo("Status", "Registration successful")
            start_pre_test()
            break


class ScrolledFrame(Frame):

    def __init__(self, parent, vertical=True, horizontal=False):
        super().__init__(parent)

        # canvas for inner frame
        self._canvas = Canvas(self)
        self._canvas.grid(row=0, column=0, sticky='news')  # changed

        # create right scrollbar and connect to canvas Y
        self._vertical_bar = Scrollbar(self, orient='vertical', command=self._canvas.yview)
        if vertical:
            self._vertical_bar.grid(row=0, column=1, sticky='ns')
        self._canvas.configure(yscrollcommand=self._vertical_bar.set)

        # create bottom scrollbar and connect to canvas X
        self._horizontal_bar = Scrollbar(self, orient='horizontal', command=self._canvas.xview)
        if horizontal:
            self._horizontal_bar.grid(row=1, column=0, sticky='we')
        self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

        # inner frame for widgets
        self.inner = Frame(self._canvas)
        self._window = self._canvas.create_window((0, 0), window=self.inner, anchor='nw')

        # autoresize inner frame
        self.columnconfigure(0, weight=1)  # changed
        self.rowconfigure(0, weight=1)  # changed

        # resize when configure changed
        self.inner.bind('<Configure>', self.resize)
        self._canvas.bind('<Configure>', self.frame_width)

    def frame_width(self, event):
        # resize inner frame to canvas size
        canvas_width = event.width
        self._canvas.itemconfig(self._window, width=canvas_width)

    def resize(self, event=None):
        self._canvas.configure(scrollregion=self._canvas.bbox('all'))


def showresult_basic(score_test_basic):
    if score_test_basic >= 4 and score_test_basic <= 5:

        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['Basic'] = "done"
        b_image['bg'] = "green"
        f_image['state'] = NORMAL

        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()

        pgbar['value']+= 1

        messagebox.showinfo("Result",
                            "Your result is:" + str(score_test_basic) + "\nYou are ready for the next Module!")
        basic_test.destroy()
        basic.destroy()

    elif score_test_basic >= 2 and score_test_basic <= 3:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_basic) + "\nPractice makes Perfect! Take the quiz again to get a better score!")
        basic_test.destroy()
        basic.destroy()
    elif score_test_basic >= 0 and score_test_basic <= 1:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_basic) + "\nYou need to study the module again! Take the quiz again to get a better score!")
        basic_test.destroy()
        basic.destroy()


def showresult_boolean(score):
    if score >= 4 and score <= 5:
        pgbar['value'] += 1
        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['Boolean'] = "done"
        bool_button['bg'] = "green"
        seq_b['state'] = NORMAL

        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()

        messagebox.showinfo("Result", "Your result is:" + str(score) + "\nYou are ready for the next Module!")
        boolean_test.destroy()
        bool.destroy()
    elif score >= 2 and score <= 3:
        messagebox.showinfo("Result", "Your result is:" + str(
            score) + "\nPractice makes Perfect! Take the quiz again to get a better score!")
        boolean_test.destroy()
        bool.destroy()
    elif score >= 0 and score <= 1:

        messagebox.showinfo("Result", "Your result is:" + str(
            score) + "\nYou need to study the module again! Take the quiz again to get a better score!")
        boolean_test.destroy()
        bool.destroy()


def score_boolean():
    global user_answer_boolean, user_answer_boolean, score, answers_boolean
    score = 0
    for i in range(5):
        if user_answer_boolean[i] == answers_boolean[i]:
            score = score + 1

    showresult_boolean(score)


def selected_boolean_test():
    global ques_boolean, radio_var_boolean, user_answer_boolean, boolean_test, ques_boolean, indexes_boolean, answer_choice_boolean_test, questions_booleantest, r1_boolean, r2_boolean, r3_boolean, r4_boolean, lblquestion_boolean, lblimage_boolean, img_list_boolean
    x = radio_var_boolean.get()
    user_answer_boolean.append(x)

    if ques_boolean < 5:
        radio_var_boolean.set(-1)
        lblquestion_boolean.config(text=questions_booleantest[indexes_boolean[ques_boolean]])
        lblimage_boolean.config(image=img_list_boolean[indexes_boolean[ques_boolean]])
        r1_boolean['text'] = answer_choice_boolean_test[indexes_boolean[ques_boolean]][0]
        r2_boolean['text'] = answer_choice_boolean_test[indexes_boolean[ques_boolean]][1]
        r3_boolean['text'] = answer_choice_boolean_test[indexes_boolean[ques_boolean]][2]
        r4_boolean['text'] = answer_choice_boolean_test[indexes_boolean[ques_boolean]][3]
        ques_boolean += 1
    else:
        score_boolean()


def test_boolean():
    global ques_boolean, boolean_test, ques_boolean, radio_var_boolean, user_answer_boolean, boolean_test, ques_boolean, indexes_boolean, answer_choice_boolean_test, questions_booleantest, r1_boolean, r2_boolean, r3_boolean, r4_boolean, lblquestion_boolean, lblimage_boolean, img_list_boolean, answers_boolean, pques_b_2
    boolean_test = Toplevel(bool)
    boolean_test.title("Proficiency-Test")
    boolean_test.geometry("700x700")
    boolean_test.iconbitmap('icon.ico')
    # boolean_test.protocol("WM_DELETE_WINDOW", ask_quit)
    indexes_boolean = [0, 1, 2, 3, 4]

    user_answer_boolean = []
    ques_boolean = 1

    file1 = open("felix.txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))
    if "easy" == (dicc.get("mode")):
        questions_booleantest = [
            """ What does "~" mean?""",
            "What are the only Boolean Values?",
            " What is the boolean equivalent of 1?",
            """ Determine the result of this code""",
            "Determine the result of this code", ]
        answer_choice_boolean_test = [
            ["A. Between", "B. tilde", "C. Bitwise one's compliment", "D. Difference"],
            ["A. True and False", "B. 'True' and 'False' ", "C. There are more than two types",
             "D. None of the above", ],
            ["A. 'True'  ", " B.  'False' ", " B. True", " D. False", ],
            ["A. 'True'  ", " B.  'False' ", " B. True", " D. False", ],
            ["A. 'True'  ", " B.  'False' ", " B. True", " D. False", ],
        ]
        bool_1 = Image.open("boolean_easy_1.png")
        bool_1 = bool_1.resize((150, 40), Image.ANTIALIAS)
        bool_1 = ImageTk.PhotoImage(bool_1)

        bool_2 = Image.open("boolean_easy_2.png")
        bool_2 = bool_2.resize((150, 40), Image.ANTIALIAS)
        bool_2 = ImageTk.PhotoImage(bool_2)

        img_list_boolean = ["", "", "", bool_1, bool_2]
        answers_boolean = [2, 0, 2, 2, 3]

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(boolean_test, image=logo)
        l_image.image = logo
        l_image.pack()

        Label(boolean_test, text="Proficiency Test for Boolean Module", font=("Helvetica", 18)).pack()

        lblquestion_boolean = Label(boolean_test, text=questions_booleantest[indexes_boolean[0]], font=("16"),
                                    justify="center", wraplength=400, )
        lblquestion_boolean.pack()

        lblimage_boolean = Label(boolean_test, image="")
        lblimage_boolean.pack()

        radio_var_boolean = IntVar()
        radio_var_boolean.set(-1)

        r1_boolean = Radiobutton(boolean_test, text=answer_choice_boolean_test[indexes_boolean[0]][0], font=("12"),
                                 variable=radio_var_boolean, value=0)
        r1_boolean.pack()

        r2_boolean = Radiobutton(boolean_test, text=answer_choice_boolean_test[indexes_boolean[0]][1], font=("12"),
                                 variable=radio_var_boolean, value=1)
        r2_boolean.pack()

        r3_boolean = Radiobutton(boolean_test, text=answer_choice_boolean_test[indexes_boolean[0]][2], font=("12"),
                                 variable=radio_var_boolean, value=2)
        r3_boolean.pack()

        r4_boolean = Radiobutton(boolean_test, text=answer_choice_boolean_test[indexes_boolean[0]][3], font=("12"),
                                 variable=radio_var_boolean, value=3)
        r4_boolean.pack()

        global pques_b_2
        pques_b_2 = Button(boolean_test, text="Submit!", command=selected_boolean_test)
        pques_b_2.pack()
    elif "medium" == (dicc.get("mode")):
        questions_booleantest = [
            """ Determine the result of the following code""",
            "Determine the value of x",
            " Determine the result of the following code",
            """Determine the result of the following code""",
            "Determine the result of this code", ]
        answer_choice_boolean_test = [
            ["A. [ True  False  True  False]", "B. [ True  False  True  False]", "C.  [1,1,1,1] ",
             "D.  [ True  True  True  True]"],
            ["A. False", "B. True ", "C.  'False' ", "D. 'True' "],
            ["A. [0,0,1,1]  ", " B.   [ False  False  True  True] ", " C.  [1,1,1,1]",
             " D. [False False  True  True]", ],
            ["A. False  ", " B.  True ", " B. 1", " D. 0", ],
            ["A. False  ", " B. True ", " B. 'True'", " D. 'False'", ],
        ]
        bool_1 = Image.open("boolean_medium_1.PNG")
        bool_1 = bool_1.resize((281, 126), Image.ANTIALIAS)
        bool_1 = ImageTk.PhotoImage(bool_1)

        bool_2 = Image.open("boolean_medium_2.PNG")
        bool_2 = bool_2.resize((120, 130), Image.ANTIALIAS)
        bool_2 = ImageTk.PhotoImage(bool_2)

        bool_3 = Image.open("boolean_medium_3.PNG")
        bool_3 = bool_3.resize((392, 101), Image.ANTIALIAS)
        bool_3 = ImageTk.PhotoImage(bool_3)

        bool_4 = Image.open("boolean_medium_4.PNG")
        bool_4 = bool_4.resize((570, 45), Image.ANTIALIAS)
        bool_4 = ImageTk.PhotoImage(bool_4)

        bool_5 = Image.open("boolean_medium_5.PNG")
        bool_5 = bool_5.resize((179, 165), Image.ANTIALIAS)
        bool_5 = ImageTk.PhotoImage(bool_5)

        img_list_boolean = [bool_1, bool_2, bool_3, bool_4, bool_5]
        answers_boolean = [2, 1, 3, 0, 1]

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(boolean_test, image=logo)
        l_image.image = logo
        l_image.pack()

        Label(boolean_test, text="Proficiency Test for Boolean Module", font=("Helvetica", 18)).pack()

        lblquestion_boolean = Label(boolean_test, text=questions_booleantest[indexes_boolean[0]], font=("16"),
                                    justify="center", wraplength=400, )
        lblquestion_boolean.pack()

        lblimage_boolean = Label(boolean_test, image=bool_1)
        lblimage_boolean.pack()

        radio_var_boolean = IntVar()
        radio_var_boolean.set(-1)

        r1_boolean = Radiobutton(boolean_test, text=answer_choice_boolean_test[indexes_boolean[0]][0], font=("12"),
                                 variable=radio_var_boolean, value=0)
        r1_boolean.pack()

        r2_boolean = Radiobutton(boolean_test, text=answer_choice_boolean_test[indexes_boolean[0]][1], font=("12"),
                                 variable=radio_var_boolean, value=1)
        r2_boolean.pack()

        r3_boolean = Radiobutton(boolean_test, text=answer_choice_boolean_test[indexes_boolean[0]][2], font=("12"),
                                 variable=radio_var_boolean, value=2)
        r3_boolean.pack()

        r4_boolean = Radiobutton(boolean_test, text=answer_choice_boolean_test[indexes_boolean[0]][3], font=("12"),
                                 variable=radio_var_boolean, value=3)
        r4_boolean.pack()

        pques_b_2 = Button(boolean_test, text="Submit!", command=selected_boolean_test)
        pques_b_2.pack()
    elif "hard" == (dicc.get("mode")):
        questions_booleantest = [
            """ Complete THE Truth Table""",
            "Determine the result of the following code",
            " Determine the result of the following code",
            """Determine the result of the following code""",
            "Determine the result of this code", ]
        answer_choice_boolean_test = [
            ["A. TTFF", "B. FTTF", "C.  TFTT ", "D.  TTTF"],
            ["A. [ True  False  False  False]", "B. [ True  False  False  False] ", "C.   [1,0,1,0] ",
             "D. [ True, False,  True, False] "],
            ["A.  [False, False, False,  True] ", " B.    [ True  False  False  True]", " C.   [1,0,1,0]",
             " D. [ False, False,  True, False]", ],
            ["A.  [False, False, False,  True] ", " B.  [ True  False  False  True]",
             " B. [False, False,  True, False]", " D.  [ False, False,  False, False]", ],
            ["A. [False, False, False, False]  ", " B. [ True  False  False  True] ",
             " B.  [False, False,  True, False]", " D.   [ False, False,  False, False]", ],
        ]
        bool_1 = Image.open("boolean_hard_1.PNG")
        bool_1 = bool_1.resize((74, 138), Image.ANTIALIAS)
        bool_1 = ImageTk.PhotoImage(bool_1)

        bool_2 = Image.open("boolean_hard_2.PNG")
        bool_2 = bool_2.resize((388, 129), Image.ANTIALIAS)
        bool_2 = ImageTk.PhotoImage(bool_2)

        bool_3 = Image.open("boolean_hard_3.PNG")
        bool_3 = bool_3.resize((409, 129), Image.ANTIALIAS)
        bool_3 = ImageTk.PhotoImage(bool_3)

        bool_4 = Image.open("boolean_hard_4.PNG")
        bool_4 = bool_4.resize((416, 125), Image.ANTIALIAS)
        bool_4 = ImageTk.PhotoImage(bool_4)

        bool_5 = Image.open("boolean_hard_5.PNG")
        bool_5 = bool_5.resize((392, 126), Image.ANTIALIAS)
        bool_5 = ImageTk.PhotoImage(bool_5)

        img_list_boolean = [bool_1, bool_2, bool_3, bool_4, bool_5]
        answers_boolean = [3, 3, 0, 2, 0]

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(boolean_test, image=logo)
        l_image.image = logo
        l_image.pack()

        Label(boolean_test, text="Proficiency Test for Boolean Module", font=("Helvetica", 18)).pack()

        lblquestion_boolean = Label(boolean_test, text=questions_booleantest[indexes_boolean[0]], font=("16"),
                                    justify="center", wraplength=400, )
        lblquestion_boolean.pack()

        lblimage_boolean = Label(boolean_test, image=bool_1)
        lblimage_boolean.pack()

        radio_var_boolean = IntVar()
        radio_var_boolean.set(-1)

        r1_boolean = Radiobutton(boolean_test, text=answer_choice_boolean_test[indexes_boolean[0]][0], font=("12"),
                                 variable=radio_var_boolean, value=0)
        r1_boolean.pack()

        r2_boolean = Radiobutton(boolean_test, text=answer_choice_boolean_test[indexes_boolean[0]][1], font=("12"),
                                 variable=radio_var_boolean, value=1)
        r2_boolean.pack()

        r3_boolean = Radiobutton(boolean_test, text=answer_choice_boolean_test[indexes_boolean[0]][2], font=("12"),
                                 variable=radio_var_boolean, value=2)
        r3_boolean.pack()

        r4_boolean = Radiobutton(boolean_test, text=answer_choice_boolean_test[indexes_boolean[0]][3], font=("12"),
                                 variable=radio_var_boolean, value=3)
        r4_boolean.pack()

        pques_b_2 = Button(boolean_test, text="Submit!", command=selected_boolean_test)
        pques_b_2.pack()


def showresult_modyul(score_test_modyul):
    if score_test_modyul >= 4 and score_test_modyul <= 5:
        pgbar['value'] += 1

        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['Modules'] = "done"
        m_image['bg'] = "green"
        nump_button['state'] = NORMAL

        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()

        messagebox.showinfo("Result",
                            "Your result is:" + str(score_test_modyul) + "\nYou are ready for the next Module!")
        modyul_test.destroy()
        modyul.destroy()



    elif score_test_modyul >= 2 and score_test_modyul <= 3:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_modyul) + "\nPractice makes Perfect! Take the quiz again to get a better score!")
        modyul_test.destroy()
        modyul.destroy()
    elif score_test_modyul >= 0 and score_test_modyul <= 1:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_modyul) + "\nYou need to study the module again! Take the quiz again to get a better score!")
        modyul_test.destroy()
        modyul.destroy()


def score_modyul():
    score_test_modyul = 0
    for i in range(5):
        if user_answer_modyul[i] == answers_modyul[i]:
            score_test_modyul = score_test_modyul + 1

    showresult_modyul(score_test_modyul)


def selected_modyul_test():
    global ques_modyul
    x = radio_var_modyul.get()
    user_answer_modyul.append(x)

    if ques_modyul < 5:
        radio_var_modyul.set(-1)
        lblquestion_modyul.config(text=questions_modyul_test[indexes_modyul[ques_modyul]])
        lblimage_modyul.config(image=img_list_modyul[indexes_modyul[ques_modyul]])
        r1_modyul['text'] = answer_choice_modyul_test[indexes_modyul[ques_modyul]][0]
        r2_modyul['text'] = answer_choice_modyul_test[indexes_modyul[ques_modyul]][1]
        r3_modyul['text'] = answer_choice_modyul_test[indexes_modyul[ques_modyul]][2]
        r4_modyul['text'] = answer_choice_modyul_test[indexes_modyul[ques_modyul]][3]
        ques_modyul += 1
    else:
        score_modyul()


def test_modyul():
    global ques_modyul, modyul_test, user_answer_modyul, lblquestion_modyul, lblimage_modyul, r1_modyul, r2_modyul, r3_modyul, r4_modyul, questions_modyul_test, indexes_modyul, img_list_modyul, answers_modyul, answer_choice_modyul_test
    modyul_test = Toplevel(modyul)
    modyul_test.title("Proficiency-Test")
    modyul_test.geometry("700x700")
    modyul_test.iconbitmap('icon.ico')
    indexes_modyul = [0, 1, 2, 3, 4]

    ques_modyul = 1

    user_answer_modyul = []

    file1 = open(username1 + ".txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))
    if "easy" == (dicc.get("mode")):
        questions_modyul_test = [
            r"it is something we can call to be able to use it's functions",
            "How do we import a  *WHOLE* library?",
            "A method where in we can check the definition of a specific function ",
            """Syntax to check all available functions in a certain library""",
            "What we use to do specific tasks", ]
        answer_choice_modyul_test = [
            ["A. functions", "B. Library", "C.Collection", "D.Asset"],
            ["A. help <library>", "B. from <library> ", "C. import <library>", "D. as <library>", ],
            ["A. help", r" B. from", " C. import", " D. as", ],
            [r"A. dir()", " B. directory() ", " C. help()", r" D. None of the above", ],
            [r'A. Built in directories  ', r' B. User-defined libraries ', r' C. functions ', r'D. All of the above', ],
        ]

        img_list_modyul = ["", "", "", "", ""]
        answers_modyul = [1, 2, 0, 0, 2]

        Label(modyul_test, text="Proficiency Test for Modules", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(modyul_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_modyul = Label(modyul_test, text=questions_modyul_test[indexes_modyul[0]], font=("16"),
                                   justify="center", wraplength=400, )
        lblquestion_modyul.pack()

        lblimage_modyul = Label(modyul_test, image="")
        lblimage_modyul.pack()

        global radio_var_modyul
        radio_var_modyul = IntVar()
        radio_var_modyul.set(-1)

        r1_modyul = Radiobutton(modyul_test, text=answer_choice_modyul_test[indexes_modyul[0]][0], font=("12"),
                                variable=radio_var_modyul, value=0)
        r1_modyul.pack()

        r2_modyul = Radiobutton(modyul_test, text=answer_choice_modyul_test[indexes_modyul[0]][1], font=("12"),
                                variable=radio_var_modyul, value=1)
        r2_modyul.pack()

        r3_modyul = Radiobutton(modyul_test, text=answer_choice_modyul_test[indexes_modyul[0]][2], font=("12"),
                                variable=radio_var_modyul, value=2)
        r3_modyul.pack()

        r4_modyul = Radiobutton(modyul_test, text=answer_choice_modyul_test[indexes_modyul[0]][3], font=("12"),
                                variable=radio_var_modyul, value=3)
        r4_modyul.pack()

        pques_modyul_b = Button(modyul_test, text="Submit!", command=selected_modyul_test)
        pques_modyul_b.pack()

    elif "hard" == (dicc.get("mode")):
        questions_modyul_test = [
            r"State the output of the program below",
            "What do we input in <here> and <here2> to make this code work?",
            "Check the code below, identify which line there could be an error",
            """Identify which line there could be an error in the code""",
            "Which of the following libraries doesn't explicitly deal with numbers?", ]
        answer_choice_modyul_test = [
            ["A. -0.62", "B. -1.2407", "C. NONE/ERROR", "D. -0.6275191383215223"],
            ["A. math, math ", r"B. math, mathematics", "C. function, math",
             "D. The code will work/not work either way.", ],
            [r"A. 1", "B. 2", " C. 3", " D. Code is correct/Not in the choices", ],
            [r"A. 1 and 2", "B. 3 and 4", " C. 5 and 7", r" D. The code will run properly", ],
            [r'A. NumPy', r'B. String', r' C. Random', r'D. Math', ],
        ]

        modyul_hard_1 = Image.open("modyul_hard_1.PNG")
        modyul_hard_1 = modyul_hard_1.resize((260, 149), Image.ANTIALIAS)
        modyul_hard_1 = ImageTk.PhotoImage(modyul_hard_1)

        modyul_hard_2 = Image.open("modyul_hard_2.PNG")
        modyul_hard_2 = modyul_hard_2.resize((396, 67), Image.ANTIALIAS)
        modyul_hard_2 = ImageTk.PhotoImage(modyul_hard_2)

        modyul_hard_3 = Image.open("modyul_hard_3.PNG")
        modyul_hard_3 = modyul_hard_3.resize((435, 99), Image.ANTIALIAS)
        modyul_hard_3 = ImageTk.PhotoImage(modyul_hard_3)

        modyul_hard_4 = Image.open("modyul_hard_4.PNG")
        modyul_hard_4 = modyul_hard_4.resize((239, 131), Image.ANTIALIAS)
        modyul_hard_4 = ImageTk.PhotoImage(modyul_hard_4)

        img_list_modyul = [modyul_hard_1, modyul_hard_2, modyul_hard_3, modyul_hard_4, ""]
        answers_modyul = [2, 0, 2, 3, 1]

        Label(modyul_test, text="Proficiency Test for Modules", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(modyul_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_modyul = Label(modyul_test, text=questions_modyul_test[indexes_modyul[0]], font=("16"),
                                   justify="center", wraplength=400, )
        lblquestion_modyul.pack()

        lblimage_modyul = Label(modyul_test, image=modyul_hard_1)
        lblimage_modyul.pack()

        radio_var_modyul = IntVar()
        radio_var_modyul.set(-1)

        r1_modyul = Radiobutton(modyul_test, text=answer_choice_modyul_test[indexes_modyul[0]][0], font=("12"),
                                variable=radio_var_modyul, value=0)
        r1_modyul.pack()

        r2_modyul = Radiobutton(modyul_test, text=answer_choice_modyul_test[indexes_modyul[0]][1], font=("12"),
                                variable=radio_var_modyul, value=1)
        r2_modyul.pack()

        r3_modyul = Radiobutton(modyul_test, text=answer_choice_modyul_test[indexes_modyul[0]][2], font=("12"),
                                variable=radio_var_modyul, value=2)
        r3_modyul.pack()

        r4_modyul = Radiobutton(modyul_test, text=answer_choice_modyul_test[indexes_modyul[0]][3], font=("12"),
                                variable=radio_var_modyul, value=3)
        r4_modyul.pack()

        pques_modyul_b = Button(modyul_test, text="Submit!", command=selected_modyul_test)
        pques_modyul_b.pack()

    elif "medium" == (dicc.get("mode")):
        questions_modyul_test = [
            r"How do we import a specific function in a library?",
            "How do we call a function differently from its name?",
            "What do we input in <here> to make the code functional?",
            """In what line is there a syntax error?""",
            "Given the code below, identify what line has an error", ]
        answer_choice_modyul_test = [
            ["A. from <library> import <function>", "B. import <library> from <function> ",
             "C. from <library> call <function>", "D. import <function> as <label>"],
            ["A. from <library> import <function>", "B. import <library> from <function> ",
             "C. from <library> call <function>", "D. import <function> as <label>"],
            ["A. None of the above", r' B. call', " C. import", r' D. as', ],
            ["A. 3", r' B. 2', " C. 1", r' D. No Error', ],
            ["A. 1", r' B. 2', " C. 3", r' D. No Error', ],
        ]

        modyul_medium_1 = Image.open("modyul_medium_1.PNG")
        modyul_medium_1 = modyul_medium_1.resize((164, 85), Image.ANTIALIAS)
        modyul_medium_1 = ImageTk.PhotoImage(modyul_medium_1)

        modyul_medium_2 = Image.open("modyul_medium_2.PNG")
        modyul_medium_2 = modyul_medium_2.resize((282, 99), Image.ANTIALIAS)
        modyul_medium_2 = ImageTk.PhotoImage(modyul_medium_2)

        modyul_medium_3 = Image.open("modyul_medium_3.PNG")
        modyul_medium_3 = modyul_medium_3.resize((434, 99), Image.ANTIALIAS)
        modyul_medium_3 = ImageTk.PhotoImage(modyul_medium_3)

        img_list_modyul = ["", "", modyul_medium_1, modyul_medium_2, modyul_medium_3, ]
        answers_modyul = [0, 3, 0, 2, 3]

        Label(modyul_test, text="Proficiency Test for Modules", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(modyul_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_modyul = Label(modyul_test, text=questions_modyul_test[indexes_modyul[0]], font=("16"),
                                   justify="center", wraplength=400, )
        lblquestion_modyul.pack()

        lblimage_modyul = Label(modyul_test, image="")
        lblimage_modyul.pack()

        radio_var_modyul = IntVar()
        radio_var_modyul.set(-1)

        r1_modyul = Radiobutton(modyul_test, text=answer_choice_modyul_test[indexes_modyul[0]][0], font=("12"),
                                variable=radio_var_modyul, value=0)
        r1_modyul.pack()

        r2_modyul = Radiobutton(modyul_test, text=answer_choice_modyul_test[indexes_modyul[0]][1], font=("12"),
                                variable=radio_var_modyul, value=1)
        r2_modyul.pack()

        r3_modyul = Radiobutton(modyul_test, text=answer_choice_modyul_test[indexes_modyul[0]][2], font=("12"),
                                variable=radio_var_modyul, value=2)
        r3_modyul.pack()

        r4_modyul = Radiobutton(modyul_test, text=answer_choice_modyul_test[indexes_modyul[0]][3], font=("12"),
                                variable=radio_var_modyul, value=3)
        r4_modyul.pack()

        pques_modyul_b = Button(modyul_test, text="Submit!", command=selected_modyul_test)
        pques_modyul_b.pack()


def showresult_func(score_test_func):
    if score_test_func >= 4 and score_test_func <= 5:
        pgbar['value'] += 1

        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['Function'] = "done"
        f_image['bg'] = "green"
        m_image['state'] = NORMAL

        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()

        messagebox.showinfo("Result", "Your result is:" + str(score_test_func) + "\nYou are ready for the next Module!")
        func_test.destroy()
        func.destroy()

    elif score_test_func >= 2 and score_test_func <= 3:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_func) + "\nPractice makes Perfect! Take the quiz again to get a better score!")
        func_test.destroy()
        func.destroy()
    elif score_test_func >= 0 and score_test_func <= 1:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_func) + "\nYou need to study the module again! Take the quiz again to get a better score!")
        func_test.destroy()
        func.destroy()


def score_func():
    score_test_func = 0
    for i in range(5):
        if user_answer_func[i] == answers_func[i]:
            score_test_func = score_test_func + 1

    showresult_func(score_test_func)


def selected_func_test():
    global ques_func
    x = radio_var_func.get()
    user_answer_func.append(x)

    if ques_func < 5:
        radio_var_func.set(-1)
        lblquestion_func.config(text=questions_func_test[indexes_func[ques_func]])
        lblimage_func.config(image=img_list_func[indexes_func[ques_func]])
        r1_func['text'] = answer_choice_func_test[indexes_func[ques_func]][0]
        r2_func['text'] = answer_choice_func_test[indexes_func[ques_func]][1]
        r3_func['text'] = answer_choice_func_test[indexes_func[ques_func]][2]
        r4_func['text'] = answer_choice_func_test[indexes_func[ques_func]][3]
        ques_func += 1
    else:
        score_func()


def test_func():
    global ques_func, func_test, user_answer_func, lblquestion_func, lblimage_func, r1_func, r2_func, r3_func, r4_func, questions_func_test, indexes_func, img_list_func, answers_func, answer_choice_func_test
    func_test = Toplevel(func)
    func_test.title("Proficiency-Test")
    func_test.geometry("700x800")
    func_test.iconbitmap('icon.ico')
    indexes_func = [0, 1, 2, 3, 4]

    ques_func = 1

    user_answer_func = []

    file1 = open(username1 + ".txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))
    if "easy" == (dicc.get("mode")):
        questions_func_test = [
            r"A line of code that only runs when called",
            "A method of passing by value(s) through functions",
            "A way of running certain functions ",
            """A type of function which is already defined inside Python""",
            "What is the output of the code below?", ]
        answer_choice_func_test = [
            ["A. Parameters", "B. Lines", "C. Functions", "D. Codes"],
            ["A. Return", "B. Passby ", "C. Argument", "D. Print", ],
            ["A. Function", r" B. Call", " C. Return", " D. Declaring", ],
            [r"A. In-house Function", " B. Built-in Function", " C. Pre-Determined Function",
             r" D. Pre-Defined Function", ],
            [r'A. B  ', r' B. "YO" ', r' C. YO ', r'D. There is no output.', ],
        ]

        func_easy_1 = Image.open("func_easy_1.png")
        func_easy_1 = func_easy_1.resize((175, 81), Image.ANTIALIAS)
        func_easy_1 = ImageTk.PhotoImage(func_easy_1)

        img_list_func = ["", "", "", "", func_easy_1]
        answers_func = [2, 0, 1, 1, 3]

        Label(func_test, text="Proficiency Test for Function Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(func_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_func = Label(func_test, text=questions_func_test[indexes_func[0]], font=("16"),
                                 justify="center", wraplength=400, )
        lblquestion_func.pack()

        lblimage_func = Label(func_test, image="")
        lblimage_func.pack()

        global radio_var_func
        radio_var_func = IntVar()
        radio_var_func.set(-1)

        r1_func = Radiobutton(func_test, text=answer_choice_func_test[indexes_func[0]][0], font=("12"),
                              variable=radio_var_func, value=0)
        r1_func.pack()

        r2_func = Radiobutton(func_test, text=answer_choice_func_test[indexes_func[0]][1], font=("12"),
                              variable=radio_var_func, value=1)
        r2_func.pack()

        r3_func = Radiobutton(func_test, text=answer_choice_func_test[indexes_func[0]][2], font=("12"),
                              variable=radio_var_func, value=2)
        r3_func.pack()

        r4_func = Radiobutton(func_test, text=answer_choice_func_test[indexes_func[0]][3], font=("12"),
                              variable=radio_var_func, value=3)
        r4_func.pack()

        pques_func_b = Button(func_test, text="Submit!", command=selected_func_test)
        pques_func_b.pack()

    elif "hard" == (dicc.get("mode")):
        questions_func_test = [
            r"What is the output of the code?",
            "What will the code display?",
            "What is the output of this code?",
            """What would be the output of the code below""",
            "Analyze the code, what is the output?", ]
        answer_choice_func_test = [
            ["A. a", "B. Gotchu", "C. Here!", "D. None"],
            ["A. SHIROU", r"B. EMIYA! SHIROU!", "C. EMIYA!", "D. The code will work/not work either way.", ],
            [r"A. 'A Dream!'", "B. A Dream!", " C. 'Life could be'", " D. Life could be", ],
            ["A. Do you feel it?", r' B. JA', " C. Do you feel it? JA", r' D. There is no output/Incorrect Code', ],
            [r'A. FLOP, CLEARSKIN', r'B. CLEARSKIN, FLOP', r' C. FLOP ', r'D. CLEARSKIN  ', ],
        ]

        func_hard_1 = Image.open("func_hard_1.PNG")
        func_hard_1 = func_hard_1.resize((223, 252), Image.ANTIALIAS)
        func_hard_1 = ImageTk.PhotoImage(func_hard_1)

        func_hard_2 = Image.open("func_hard_2.PNG")
        func_hard_2 = func_hard_2.resize((237, 183), Image.ANTIALIAS)
        func_hard_2 = ImageTk.PhotoImage(func_hard_2)

        func_hard_3 = Image.open("func_hard_3.PNG")
        func_hard_3 = func_hard_3.resize((298, 184), Image.ANTIALIAS)
        func_hard_3 = ImageTk.PhotoImage(func_hard_3)

        func_hard_4 = Image.open("func_hard_4.PNG")
        func_hard_4 = func_hard_4.resize((313, 238), Image.ANTIALIAS)
        func_hard_4 = ImageTk.PhotoImage(func_hard_4)

        func_hard_5 = Image.open("func_hard_5.PNG")
        func_hard_5 = func_hard_5.resize((350, 271), Image.ANTIALIAS)
        func_hard_5 = ImageTk.PhotoImage(func_hard_5)

        img_list_func = [func_hard_1, func_hard_2, func_hard_3, func_hard_4, func_hard_5]
        answers_func = [3, 2, 3, 3, 3]

        Label(func_test, text="Proficiency Test for Function Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(func_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_func = Label(func_test, text=questions_func_test[indexes_func[0]], font=("16"),
                                 justify="center", wraplength=400, )
        lblquestion_func.pack()

        lblimage_func = Label(func_test, image=func_hard_1)
        lblimage_func.pack()

        radio_var_func = IntVar()
        radio_var_func.set(-1)

        r1_func = Radiobutton(func_test, text=answer_choice_func_test[indexes_func[0]][0], font=("12"),
                              variable=radio_var_func, value=0)
        r1_func.pack()

        r2_func = Radiobutton(func_test, text=answer_choice_func_test[indexes_func[0]][1], font=("12"),
                              variable=radio_var_func, value=1)
        r2_func.pack()

        r3_func = Radiobutton(func_test, text=answer_choice_func_test[indexes_func[0]][2], font=("12"),
                              variable=radio_var_func, value=2)
        r3_func.pack()

        r4_func = Radiobutton(func_test, text=answer_choice_func_test[indexes_func[0]][3], font=("12"),
                              variable=radio_var_func, value=3)
        r4_func.pack()

        pques_func_b = Button(func_test, text="Submit!", command=selected_func_test)
        pques_func_b.pack()

    elif "medium" == (dicc.get("mode")):
        questions_func_test = [
            """What form of conditional statement should we use if we want 
            to be checked only once the first statement is false?""",
            "Conditional statement that is last in the level of priority of execution:",
            "A method to instantly close a function:",
            """What is the output of the code below:""",
            "What is the output of the code below:", ]
        answer_choice_func_test = [
            ["A. Switch", "B. Operator", "C. Else If", "D. Else"],
            ["A. If", "B. Then", "C. Elif", "D. Else"],
            ["A. end", r' B. call', " C. return", r' D. pass', ],
            ["A. S24-DAWN!", r' B. S24-DAWN!, REPRESENT!', " C. REPRESENT!", r' D. No output', ],
            ["A. 'Eli'", r' B. Eli', " C. Say", r" D. 'Say'", ],
        ]

        func_medium_1 = Image.open("func_medium_1.PNG")
        func_medium_1 = func_medium_1.resize((230, 135), Image.ANTIALIAS)
        func_medium_1 = ImageTk.PhotoImage(func_medium_1)

        func_medium_2 = Image.open("func_medium_2.PNg")
        func_medium_2 = func_medium_2.resize((202, 166), Image.ANTIALIAS)
        func_medium_2 = ImageTk.PhotoImage(func_medium_2)

        img_list_func = ["", "", "", func_medium_1, func_medium_2, ]
        answers_func = [2, 3, 2, 0, 2]

        Label(func_test, text="Proficiency Test for Function Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(func_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_func = Label(func_test, text=questions_func_test[indexes_func[0]], font=("16"),
                                 justify="center", wraplength=400, )
        lblquestion_func.pack()

        lblimage_func = Label(func_test, image="")
        lblimage_func.pack()

        radio_var_func = IntVar()
        radio_var_func.set(-1)

        r1_func = Radiobutton(func_test, text=answer_choice_func_test[indexes_func[0]][0], font=("12"),
                              variable=radio_var_func, value=0)
        r1_func.pack()

        r2_func = Radiobutton(func_test, text=answer_choice_func_test[indexes_func[0]][1], font=("12"),
                              variable=radio_var_func, value=1)
        r2_func.pack()

        r3_func = Radiobutton(func_test, text=answer_choice_func_test[indexes_func[0]][2], font=("12"),
                              variable=radio_var_func, value=2)
        r3_func.pack()

        r4_func = Radiobutton(func_test, text=answer_choice_func_test[indexes_func[0]][3], font=("12"),
                              variable=radio_var_func, value=3)
        r4_func.pack()

        pques_func_b = Button(func_test, text="Submit!", command=selected_func_test)
        pques_func_b.pack()


def submit_2():
    global lbl_questions, pques_b_2, basic
    x = radio_var_2.get()
    if x == 0:
        Label(lbl_questions, text="Correct\n You are ready for your Proficiency Test", fg="green").pack()
        pques_b_2["state"] = "disabled"
        test_boolean_b = Button(lbl_questions, text="Proceed to Test", command=test_boolean)
        test_boolean_b.pack()

    elif x == 3 or x == 1 or x == 2:
        Label(lbl_questions, text="Wrong answer\n Strings are not Boolean types!", fg="red").pack()


def pques_2():
    Label(lbl_questions,
          text="""Determine the result of the following code""", font=("Helvetica", "13")).pack()

    pques_2 = Image.open("pques_b_2.png")
    pques_2 = pques_2.resize((200, 100), Image.ANTIALIAS)
    pques_2 = ImageTk.PhotoImage(pques_2)

    pques_2_i = Label(lbl_questions, image=pques_2)
    pques_2_i.image = pques_2
    pques_2_i.pack()

    global radio_var_2
    radio_var_2 = IntVar()
    radio_var_2.set(-1)
    radio1_2 = Radiobutton(lbl_questions, text="True", font=("12"), variable=radio_var_2,
                           value=0)
    radio1_2.pack()

    radio2_2 = Radiobutton(lbl_questions, text="False", font=("12"), variable=radio_var_2,
                           value=1)
    radio2_2.pack()

    radio3_2 = Radiobutton(lbl_questions, text='"True"', font=("12"), variable=radio_var_2, value=2)
    radio3_2.pack()

    radio4_2 = Radiobutton(lbl_questions, text='"False"', font=("12"), variable=radio_var_2, value=3)
    radio4_2.pack()

    global pques_b_2
    pques_b_2 = Button(lbl_questions, text="Submit!", command=submit_2)
    pques_b_2.pack()


def submit_1():
    global lbl_questions, pques_b_1
    x = radio_var_1.get()
    if x == 3:
        Label(lbl_questions, text="Correct", fg="green").pack()
        pques_b_1["state"] = "disabled"
        pques_2()
    elif x == 0 or x == 1 or x == 2:
        Label(lbl_questions, text="Wrong answer\n Remember the proper data types!", fg="red").pack()


def start_boolean_module():
    global bool, fwd
    bool = Toplevel(screen)
    width_value = bool.winfo_screenmmwidth()
    height_value = bool.winfo_screenheight()
    bool.geometry("1280x720")
    bool.iconbitmap('icon.ico')
    Label(bool, text="Welcome " + username1.title() + " to your Boolean Lesson!",
          font=("Helvetica", "13", "bold")).pack()

    window = ScrolledFrame(bool)
    window.pack(expand=True, fill='both')

    lbl = LabelFrame(window.inner, padx=80, pady=80)
    lbl.pack()

    Label(lbl, text="""The bool() method is used to return or convert a value to a Boolean value.
    A Boolean variable has only two possible values: "True" or "False". 
    These values can also be represented as ' or 0.The boolean syntax is "bool([x])" """, font=("13")).pack()

    b_1 = Image.open("b_1.png")
    b_1 = b_1.resize((600, 100), Image.ANTIALIAS)
    b_1 = ImageTk.PhotoImage(b_1)

    b_1_image = Label(lbl, image=b_1)
    b_1_image.image = b_1
    b_1_image.pack()

    Label(lbl,
          text="""\n\nIn Python you will learn that there are many logical operators that can be used with thier respective character.""",
          anchor=W, font=("13")).pack()

    table_b = Image.open("table_b.PNG")
    table_b = table_b.resize((600, 200), Image.ANTIALIAS)
    table_b = ImageTk.PhotoImage(table_b)

    table_b_image = Label(lbl, image=table_b)
    table_b_image.image = table_b
    table_b_image.pack()

    table_summ_i = Image.open("table_summ.png")
    table_summ_i = table_summ_i.resize((600, 600), Image.ANTIALIAS)
    table_summ_i = ImageTk.PhotoImage(table_summ_i)

    table_summ_image = Label(lbl, image=table_summ_i)
    table_summ_image.image = table_summ_i
    table_summ_image.pack()

    Label(lbl,
          text="""\n\nBOOLEAN in if statements.""",
          anchor=W, font=("20")).pack()

    ex_2 = Image.open("example_2.png")
    ex_2 = ex_2.resize((547, 150), Image.ANTIALIAS)
    ex_2 = ImageTk.PhotoImage(ex_2)

    ex_2_i = Label(lbl, image=ex_2)
    ex_2_i.image = ex_2
    ex_2_i.pack()

    Label(lbl,
          text="""\n\nPractive Questions""",
          anchor=W, font=("20")).pack()
    global lbl_questions
    lbl_questions = LabelFrame(lbl, text="Domanda:", padx=80, pady=80)
    lbl_questions.pack()

    Label(lbl_questions,
          text="""Determine the result of the following code""", font=("13")).pack()

    pques_1 = Image.open("pques_b_1.png")
    pques_1 = pques_1.resize((300, 114), Image.ANTIALIAS)
    pques_1 = ImageTk.PhotoImage(pques_1)

    pques_1_i = Label(lbl_questions, image=pques_1)
    pques_1_i.image = pques_1
    pques_1_i.pack()

    global radio_var_1
    radio_var_1 = IntVar()
    radio_var_1.set(-1)
    radio1_1 = Radiobutton(lbl_questions, text="[ True  False  True  False]", font=("12"), variable=radio_var_1,
                           value=0)
    radio1_1.pack()

    radio2_1 = Radiobutton(lbl_questions, text="[ False  False  False  False]", font=("12"), variable=radio_var_1,
                           value=1)
    radio2_1.pack()

    radio3_1 = Radiobutton(lbl_questions, text="[1,1,1,1]", font=("12"), variable=radio_var_1, value=2)
    radio3_1.pack()

    radio4_1 = Radiobutton(lbl_questions, text="[ True  True  True  True]", font=("12"), variable=radio_var_1, value=3)
    radio4_1.pack()

    global pques_b_1
    pques_b_1 = Button(lbl_questions, text="Submit!", command=submit_1)
    pques_b_1.pack()


def showresult_sequence(score_test_sequence):
    if score_test_sequence >= 4 and score_test_sequence <= 5:
        pgbar['value'] += 1

        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['Sequences'] = "done"
        seq_b['bg'] = "green"
        string_b['state'] = NORMAL

        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()

        messagebox.showinfo("Result",
                            "Your result is:" + str(score_test_sequence) + "\nYou are ready for the next Module!")
        sequence_test.destroy()
        sequence.destroy()


    elif score_test_sequence >= 2 and score_test_sequence <= 3:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_sequence) + "\nPractice makes Perfect! Take the quiz again to get a better score!")
        sequence_test.destroy()
        sequence.destroy()
    elif score_test_sequence >= 0 and score_test_sequence <= 1:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_sequence) + "\nYou need to study the module again! Take the quiz again to get a better score!")
        sequence_test.destroy()
        sequence.destroy()


def score_sequence():
    score_test_sequence = 0
    for i in range(5):
        if user_answer_sequence[i] == answers_sequence[i]:
            score_test_sequence = score_test_sequence + 1

    showresult_sequence(score_test_sequence)


def selected_sequence_test():
    global ques_sequence
    x = radio_var_sequence.get()
    user_answer_sequence.append(x)

    if ques_sequence < 5:
        radio_var_sequence.set(-1)
        lblquestion_sequence.config(text=questions_sequence_test[indexes_sequence[ques_sequence]])
        lblimage_sequence.config(image=img_list_sequence[indexes_sequence[ques_sequence]])
        r1_sequence['text'] = answer_choice_sequence_test[indexes_sequence[ques_sequence]][0]
        r2_sequence['text'] = answer_choice_sequence_test[indexes_sequence[ques_sequence]][1]
        r3_sequence['text'] = answer_choice_sequence_test[indexes_sequence[ques_sequence]][2]
        r4_sequence['text'] = answer_choice_sequence_test[indexes_sequence[ques_sequence]][3]
        ques_sequence += 1
    else:
        score_sequence()


def test_sequence():
    global ques_sequence, sequence_test, user_answer_sequence, lblquestion_sequence, lblimage_sequence, r1_sequence, r2_sequence, r3_sequence, r4_sequence, questions_sequence_test, indexes_sequence, img_list_sequence, answers_sequence, answer_choice_sequence_test
    sequence_test = Toplevel(sequence)
    sequence_test.title("Proficiency-Test")
    sequence_test.geometry("700x900")
    sequence_test.iconbitmap('icon.ico')
    indexes_sequence = [0, 1, 2, 3, 4]

    user_answer_sequence = []
    ques_sequence = 1

    file1 = open(username1 + ".txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))
    if "easy" == (dicc.get("mode")):
        questions_sequence_test = [
            r"They can store different data types and add them",
            "A method of accessing specific elements of a string,object or even container",
            "An ordered collection of other objects",
            """How do we check for the length of a string?""",
            "What is the output of the code below?", ]
        answer_choice_sequence_test = [
            ["A. Strings", "B. Lists", "C. Tuples", "D. None"],
            ["A. Indexing", "B. In ", "C. Appending", "D. Len", ],
            ["A. Iteration", r" B. Sequences", " C. Looping", " D. Conditionals", ],
            [r"A. Range", " B. Indexing", " C. Backslashing", r" D. Len", ],
            [r'A. 3,6,9', r' B. 3,6,9,12', r' C. 0,3,6,9,12', r'D. 0,3,6,9', ],
        ]

        sequence_easy_1 = Image.open("sequence_easy_1.png")
        sequence_easy_1 = sequence_easy_1.resize((242, 45), Image.ANTIALIAS)
        sequence_easy_1 = ImageTk.PhotoImage(sequence_easy_1)

        img_list_sequence = ["", "", "", "", sequence_easy_1]
        answers_sequence = [1, 0, 1, 3, 3]

        Label(sequence_test, text="Proficiency Test for Sequences Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(sequence_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_sequence = Label(sequence_test, text=questions_sequence_test[indexes_sequence[0]], font=("16"),
                                     justify="center", wraplength=400, )
        lblquestion_sequence.pack()

        lblimage_sequence = Label(sequence_test, image="")
        lblimage_sequence.pack()

        global radio_var_sequence
        radio_var_sequence = IntVar()
        radio_var_sequence.set(-1)

        r1_sequence = Radiobutton(sequence_test, text=answer_choice_sequence_test[indexes_sequence[0]][0], font=("12"),
                                  variable=radio_var_sequence, value=0)
        r1_sequence.pack()

        r2_sequence = Radiobutton(sequence_test, text=answer_choice_sequence_test[indexes_sequence[0]][1], font=("12"),
                                  variable=radio_var_sequence, value=1)
        r2_sequence.pack()

        r3_sequence = Radiobutton(sequence_test, text=answer_choice_sequence_test[indexes_sequence[0]][2], font=("12"),
                                  variable=radio_var_sequence, value=2)
        r3_sequence.pack()

        r4_sequence = Radiobutton(sequence_test, text=answer_choice_sequence_test[indexes_sequence[0]][3], font=("12"),
                                  variable=radio_var_sequence, value=3)
        r4_sequence.pack()

        pques_sequence_b = Button(sequence_test, text="Submit!", command=selected_sequence_test)
        pques_sequence_b.pack()

    elif "hard" == (dicc.get("mode")):
        questions_sequence_test = [
            r"What is the output of the code?",
            "What will the code display?",
            "What is the output of this code?",
            """Identify the error in the code (Corresponding Line)""",
            "What is the output of the code?", ]
        answer_choice_sequence_test = [
            ["A. 0,1,2,3,4", "B. 0,1,2,3", "C. 1,2,3,4", "D. No output"],
            ["A. 232232232", r"B. 232232", "C. 53824", "D. 12487168", ],
            [r"A. VIBE", "B. 343211", "C. 6", "D. No output", ],
            ['A. 1 and 2 ', r' B. 2 and 3 ', ' C. 3 and 5 ', r' D. There is no error', ],
            ['A. "DRIP"', r' B. DRIP DRIP DRIP', ' C. "DRIP" "DRIP" "DRIP"  ',
             r' D. There is no output/Incorrect Code', ],
        ]

        sequence_hard_1 = Image.open("sequence_hard_1.PNG")
        sequence_hard_1 = sequence_hard_1.resize((283, 182), Image.ANTIALIAS)
        sequence_hard_1 = ImageTk.PhotoImage(sequence_hard_1)

        sequence_hard_2 = Image.open("sequence_hard_2.PNG")
        sequence_hard_2 = sequence_hard_2.resize((306, 236), Image.ANTIALIAS)
        sequence_hard_2 = ImageTk.PhotoImage(sequence_hard_2)

        sequence_hard_3 = Image.open("sequence_hard_3.PNg")
        sequence_hard_3 = sequence_hard_3.resize((320, 269), Image.ANTIALIAS)
        sequence_hard_3 = ImageTk.PhotoImage(sequence_hard_3)

        sequence_hard_4 = Image.open("sequence_hard_4.PNG")
        sequence_hard_4 = sequence_hard_4.resize((237, 134), Image.ANTIALIAS)
        sequence_hard_4 = ImageTk.PhotoImage(sequence_hard_4)

        img_list_sequence = [sequence_hard_1, sequence_hard_2, sequence_hard_3, sequence_hard_4, sequence_hard_4]

        answers_sequence = [0, 0, 2, 3, 2]

        Label(sequence_test, text="Proficiency Test for Sequences Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(sequence_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_sequence = Label(sequence_test, text=questions_sequence_test[indexes_sequence[0]], font=("16"),
                                     justify="center", wraplength=400, )
        lblquestion_sequence.pack()

        lblimage_sequence = Label(sequence_test, image=sequence_hard_1)
        lblimage_sequence.pack()

        radio_var_sequence = IntVar()
        radio_var_sequence.set(-1)

        r1_sequence = Radiobutton(sequence_test, text=answer_choice_sequence_test[indexes_sequence[0]][0], font=("12"),
                                  variable=radio_var_sequence, value=0)
        r1_sequence.pack()

        r2_sequence = Radiobutton(sequence_test, text=answer_choice_sequence_test[indexes_sequence[0]][1], font=("12"),
                                  variable=radio_var_sequence, value=1)
        r2_sequence.pack()

        r3_sequence = Radiobutton(sequence_test, text=answer_choice_sequence_test[indexes_sequence[0]][2], font=("12"),
                                  variable=radio_var_sequence, value=2)
        r3_sequence.pack()

        r4_sequence = Radiobutton(sequence_test, text=answer_choice_sequence_test[indexes_sequence[0]][3], font=("12"),
                                  variable=radio_var_sequence, value=3)
        r4_sequence.pack()

        pques_sequence_b = Button(sequence_test, text="Submit!", command=selected_sequence_test)
        pques_sequence_b.pack()

    elif "medium" == (dicc.get("mode")):
        questions_sequence_test = [
            """A type of data collection more commonly used for optimized programs""",
            "What would be the output of this code?",
            "What would correct the error in the code?",
            """The translation of characters into unique numbers""",
            "What operation cannot be done on strings", ]
        answer_choice_sequence_test = [
            ["A. Dictionaries", "B. Variables", "C. Lists", "D. Tuples"],
            ["A. 110", "B. [55]", "C. [25,30]", "D. None"],
            ["A. No error in the code", r' B. Int()', " C. list declaration", r' D. quotations in print ""', ],
            ["A. Binary", r' B. Hexadecimal', " C. Boolean", r' D. ASCII', ],
            ["A. Concatenation", r' B. Repetition', " C. Multiplication", r" D. Subtraction", ],
        ]

        sequence_medium_1 = Image.open("sequence_medium_1.PNG")
        sequence_medium_1 = sequence_medium_1.resize((223, 80), Image.ANTIALIAS)
        sequence_medium_1 = ImageTk.PhotoImage(sequence_medium_1)

        img_list_sequence = ["", sequence_medium_1, sequence_medium_1, "", "", ]
        answers_sequence = [3, 2, 0, 3, 3]

        Label(sequence_test, text="Proficiency Test for Sequences Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(sequence_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_sequence = Label(sequence_test, text=questions_sequence_test[indexes_sequence[0]], font=("16"),
                                     justify="center", wraplength=400, )
        lblquestion_sequence.pack()

        lblimage_sequence = Label(sequence_test, image="")
        lblimage_sequence.pack()

        radio_var_sequence = IntVar()
        radio_var_sequence.set(-1)

        r1_sequence = Radiobutton(sequence_test, text=answer_choice_sequence_test[indexes_sequence[0]][0], font=("12"),
                                  variable=radio_var_sequence, value=0)
        r1_sequence.pack()

        r2_sequence = Radiobutton(sequence_test, text=answer_choice_sequence_test[indexes_sequence[0]][1], font=("12"),
                                  variable=radio_var_sequence, value=1)
        r2_sequence.pack()

        r3_sequence = Radiobutton(sequence_test, text=answer_choice_sequence_test[indexes_sequence[0]][2], font=("12"),
                                  variable=radio_var_sequence, value=2)
        r3_sequence.pack()

        r4_sequence = Radiobutton(sequence_test, text=answer_choice_sequence_test[indexes_sequence[0]][3], font=("12"),
                                  variable=radio_var_sequence, value=3)
        r4_sequence.pack()

        pques_sequence_b = Button(sequence_test, text="Submit!", command=selected_sequence_test)
        pques_sequence_b.pack()


def showresult_str(score_test_string):
    if score_test_string >= 4 and score_test_string <= 5:
        pgbar['value'] += 1
        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['Strings'] = "done"
        string_b['bg'] = "green"
        dicc_b['state'] = NORMAL

        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()

        messagebox.showinfo("Result",
                            "Your result is:" + str(score_test_string) + "\nYou are ready for the next Module!")
        string_test.destroy()
        strings.destroy()

    elif score_test_string >= 2 and score_test_string <= 3:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_string) + "\nPractice makes Perfect! Take the quiz again to get a better score!")
        string_test.destroy()
        strings.destroy()

    elif score_test_string >= 0 and score_test_string <= 1:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_string) + "\nYou need to study the module again! Take the quiz again to get a better score!")
        string_test.destroy()
        strings.destroy()


def score_string():
    global score_test_string
    print(user_answer_str)
    score_test_string = 0
    for i in range(5):
        if user_answer_str[i] == answers_string[i]:
            score_test_string = score_test_string + 1

    showresult_str(score_test_string)


def selected_string_test():
    global ques_str
    x = radio_var_string.get()
    user_answer_str.append(x)

    if ques_str < 5:
        radio_var_string.set(-1)
        lblquestion_string.config(text=questions_string_test[indexes_str[ques_str]])
        lblimage_string.config(image=img_list_string[indexes_str[ques_str]])
        r1_string['text'] = answer_choice_string_test[indexes_str[ques_str]][0]
        r2_string['text'] = answer_choice_string_test[indexes_str[ques_str]][1]
        r3_string['text'] = answer_choice_string_test[indexes_str[ques_str]][2]
        r4_string['text'] = answer_choice_string_test[indexes_str[ques_str]][3]
        ques_str += 1
    else:
        score_string()


def test_string():
    global ques_str, string_test, strings, radio_var_string, pques_str_b, user_answer_str, questions_string_test, indexes_str, lblquestion_string, lblimage_string, img_list_string, answer_choice_string_test, r1_string, r2_string, r3_string, r4_string, answers_string
    string_test = Toplevel(strings)
    string_test.title("Proficiency-Test")
    string_test.geometry("700x700")
    string_test.iconbitmap('icon.ico')
    indexes_str = [0, 1, 2, 3, 4]
    ques_str = 1

    user_answer_str = []

    file1 = open("felix.txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))
    if "easy" == (dicc.get("mode")):
        questions_string_test = [
            r" What does '\t' mean?",
            "What method can you use for multi-line strings?",
            " what letter is used for raw strings",
            """ Determine the result of this code""",
            "What is the correct code to output this result", ]
        answer_choice_string_test = [
            ["A.Single Quote", "B. Tab", "C. Backslash T", "D. Null"],
            ["A. r", "B. Triple Quotes ", "C. in and Not in", "D. Tab", ],
            ["A. r ", r" B.  \n ", " B. t", " D. n", ],
            [r"A. 'That is joshua\'s string.'  ", " B.  Invalid Syntax ", " B. That is joshua",
             r" D. That is joshua\'s string.", ],
            [r'A. ("\n Where are \n the new lines?")  ', r' B.print("Where are \n the new lines?") ',
             r' C. ("Where are \n the new lines?")', r'D. print("\n Where are \n the new lines?")', ],
        ]
        str_test_1 = Image.open("string_easy_1.PNG")
        str_test_1 = str_test_1.resize((373, 40), Image.ANTIALIAS)
        str_test_1 = ImageTk.PhotoImage(str_test_1)

        str_test_2 = Image.open("string_easy_2.PNG")
        str_test_2 = str_test_2.resize((184, 95), Image.ANTIALIAS)
        str_test_2 = ImageTk.PhotoImage(str_test_2)

        img_list_string = ["", "", "", str_test_1, str_test_2]
        answers_string = [1, 1, 0, 0, 3]

        Label(string_test, text="Proficiency Test for Strings Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(string_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_string = Label(string_test, text=questions_string_test[indexes_str[0]], font=("16"),
                                   justify="center", wraplength=400, )
        lblquestion_string.pack()

        lblimage_string = Label(string_test, image="")
        lblimage_string.pack()

        radio_var_string = IntVar()
        radio_var_string.set(-1)

        r1_string = Radiobutton(string_test, text=answer_choice_string_test[indexes_str[0]][0], font=("12"),
                                variable=radio_var_string, value=0)
        r1_string.pack()

        r2_string = Radiobutton(string_test, text=answer_choice_string_test[indexes_str[0]][1], font=("12"),
                                variable=radio_var_string, value=1)
        r2_string.pack()

        r3_string = Radiobutton(string_test, text=answer_choice_string_test[indexes_str[0]][2], font=("12"),
                                variable=radio_var_string, value=2)
        r3_string.pack()

        r4_string = Radiobutton(string_test, text=answer_choice_string_test[indexes_str[0]][3], font=("12"),
                                variable=radio_var_string, value=3)
        r4_string.pack()

        pques_str_b = Button(string_test, text="Submit!", command=selected_string_test)
        pques_str_b.pack()
    elif "medium" == (dicc.get("mode")):
        questions_string_test = [
            "Determine the result of the following code",
            "Determine the result of the following code",
            "Determine the result of the following code",
            """ Determine the result of this code""",
            "What is the correct code to output this result", ]
        answer_choice_string_test = [
            ['A."name@gmail.com" ', 'B. "name" + "@gmail.com"', 'C. "name+gmail.com"', 'D. Error'],
            ['A.  "This is a string" ', "B. ['This,', ' is,', ' a,', ' string,'] ", "C.Error",
             "D. ['This', ' is', ' a', ' string', '']", ],
            ['A. "True" ', '  B."False" ', " C. False", " D. True", ],
            [r"A. ['This is string', 'with new lines'] ", " B. ['This is stringwith new lines'] ",
             " B. ['This', 'is', 'string', 'with\n', 'new', 'lines']", r" D. Error", ],
            [r'A. "N" ', r' B."A" ', r' C. "a"', r'D. "s"', ]
        ]
        str_test_1 = Image.open("string_medium_1.PNG")
        str_test_1 = str_test_1.resize((243, 45), Image.ANTIALIAS)
        str_test_1 = ImageTk.PhotoImage(str_test_1)

        str_test_2 = Image.open("string_medium_2.PNG")
        str_test_2 = str_test_2.resize((216, 66), Image.ANTIALIAS)
        str_test_2 = ImageTk.PhotoImage(str_test_2)

        str_test_3 = Image.open("string_medium_3.PNG")
        str_test_3 = str_test_3.resize((184, 45), Image.ANTIALIAS)
        str_test_3 = ImageTk.PhotoImage(str_test_3)

        str_test_4 = Image.open("string_medium_4.PNG")
        str_test_4 = str_test_4.resize((379, 86), Image.ANTIALIAS)
        str_test_4 = ImageTk.PhotoImage(str_test_4)

        str_test_5 = Image.open("string_medium_5.PNG")
        str_test_5 = str_test_5.resize((320, 58), Image.ANTIALIAS)
        str_test_5 = ImageTk.PhotoImage(str_test_5)

        img_list_string = [str_test_1, str_test_2, str_test_3, str_test_4, str_test_5]
        answers_string = [0, 3, 2, 0, 0]

        Label(string_test, text="Proficiency Test for Strings Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(string_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_string = Label(string_test, text=questions_string_test[indexes_str[0]], font=("16"),
                                   justify="center", wraplength=400, )
        lblquestion_string.pack()

        lblimage_string = Label(string_test, image=img_list_string[0])
        lblimage_string.pack()

        radio_var_string = IntVar()
        radio_var_string.set(-1)

        r1_string = Radiobutton(string_test, text=answer_choice_string_test[indexes_str[0]][0], font=("12"),
                                variable=radio_var_string, value=0)
        r1_string.pack()

        r2_string = Radiobutton(string_test, text=answer_choice_string_test[indexes_str[0]][1], font=("12"),
                                variable=radio_var_string, value=1)
        r2_string.pack()

        r3_string = Radiobutton(string_test, text=answer_choice_string_test[indexes_str[0]][2], font=("12"),
                                variable=radio_var_string, value=2)
        r3_string.pack()

        r4_string = Radiobutton(string_test, text=answer_choice_string_test[indexes_str[0]][3], font=("12"),
                                variable=radio_var_string, value=3)
        r4_string.pack()

        pques_str_b = Button(string_test, text="Submit!", command=selected_string_test)
        pques_str_b.pack()
    elif "hard" == (dicc.get("mode")):
        questions_string_test = [
            "Determine the result of the following code",
            "Determine the result of the following code",
            "Determine the result of the following code",
            """ Determine the result of this code""",
            "What is the correct code to output this result", ]
        answer_choice_string_test = [
            ["A. ['1.new line', '2.new line', '3.new line']", "B.  ['1.new line2.new line3.new line'] ",
             r"C. ['1', 'new line\n2', 'new line\n3', 'new line'] ",
             "D. ['1.new', 'line', '2.new', 'line', '3.new', 'line']"],
            ["A.  ['string', 'is', 'th1s'] ", "B. 'string is th1s' ", "C.['StRIng', 'is', 'Th1s']", "D. Error", ],
            ["A. ['This', 's word'] ", "B.['Th', 's ', 's word'] ", " C. ['This is word']",
             " D. ['This', 'is', 'word']", ],
            ["A. 'letter 0 : s' ", " B. 'letter 1 : t' ", " C. 'letter 2 : r'", r" D. list index out of range", ],
            ['A. "0: This is string\n1: with new lines\n2: this is second line" ',
             r" B. ['0: This is string\n', '1: with new lines\n', '2: this is second line\n'] ", r' C. Invalid Syntax',
             "D. ['0: This is string', '1: with new lines', '2: this is second line', ''] "]
        ]
        str_test_1 = Image.open("string_hard_1.PNG")
        str_test_1 = str_test_1.resize((191, 124), Image.ANTIALIAS)
        str_test_1 = ImageTk.PhotoImage(str_test_1)

        str_test_2 = Image.open("string_hard_2.PNG")
        str_test_2 = str_test_2.resize((191, 63), Image.ANTIALIAS)
        str_test_2 = ImageTk.PhotoImage(str_test_2)

        str_test_3 = Image.open("string_hard_3.PNG")
        str_test_3 = str_test_3.resize((203, 67), Image.ANTIALIAS)
        str_test_3 = ImageTk.PhotoImage(str_test_3)

        str_test_4 = Image.open("string_hard_4.PNG")
        str_test_4 = str_test_4.resize((510, 119), Image.ANTIALIAS)
        str_test_4 = ImageTk.PhotoImage(str_test_4)

        str_test_5 = Image.open("string_hard_5.PNG")
        str_test_5 = str_test_5.resize((595, 125), Image.ANTIALIAS)
        str_test_5 = ImageTk.PhotoImage(str_test_5)

        img_list_string = [str_test_1, str_test_2, str_test_3, str_test_4, str_test_5]
        answers_string = [0, 0, 0, 0, 0]

        Label(string_test, text="Proficiency Test for Strings Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(string_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_string = Label(string_test, text=questions_string_test[indexes_str[0]], font=("16"),
                                   justify="center", wraplength=400, )
        lblquestion_string.pack()

        lblimage_string = Label(string_test, image=img_list_string[0])
        lblimage_string.pack()

        radio_var_string = IntVar()
        radio_var_string.set(-1)

        r1_string = Radiobutton(string_test, text=answer_choice_string_test[indexes_str[0]][0], font=("12"),
                                variable=radio_var_string, value=0)
        r1_string.pack()

        r2_string = Radiobutton(string_test, text=answer_choice_string_test[indexes_str[0]][1], font=("12"),
                                variable=radio_var_string, value=1)
        r2_string.pack()

        r3_string = Radiobutton(string_test, text=answer_choice_string_test[indexes_str[0]][2], font=("12"),
                                variable=radio_var_string, value=2)
        r3_string.pack()

        r4_string = Radiobutton(string_test, text=answer_choice_string_test[indexes_str[0]][3], font=("12"),
                                variable=radio_var_string, value=3)
        r4_string.pack()

        pques_str_b = Button(string_test, text="Submit!", command=selected_string_test)
        pques_str_b.pack()


def submit_2_str():
    global lbl_questions_strings, pques_str_2
    x = radio_var_2_str.get()
    if x == 0:
        Label(lbl_questions_strings, text="Correct\n You are ready for your Proficiency Test", fg="green").pack()
        pques_str_2["state"] = "disabled"
        test_str_b = Button(lbl_questions_strings, text="Proceed to Test", command=test_string)
        test_str_b.pack()

    elif x == 3 or x == 1 or x == 2:
        Label(lbl_questions_strings, text="Wrong answer\n Look at their initials", fg="red").pack()


def pques_2_str():
    Label(lbl_questions_strings,
          text="""Which escape character is used for new line?""", font=("Helvetica", "13")).pack()

    global radio_var_2_str
    radio_var_2_str = IntVar()
    radio_var_2_str.set(-1)
    radio1_2 = Radiobutton(lbl_questions_strings, text=r'\n', font=("12"), variable=radio_var_2_str,
                           value=0)
    radio1_2.pack()

    radio2_2 = Radiobutton(lbl_questions_strings, text=r'\t', font=("12"), variable=radio_var_2_str,
                           value=1)
    radio2_2.pack()

    radio3_2 = Radiobutton(lbl_questions_strings, text=r'\t', font=("12"), variable=radio_var_2_str, value=2)
    radio3_2.pack()

    radio4_2 = Radiobutton(lbl_questions_strings, text=r'\\', font=("12"), variable=radio_var_2_str, value=3)
    radio4_2.pack()

    global pques_str_2
    pques_str_2 = Button(lbl_questions_strings, text="Submit!", command=submit_2_str)
    pques_str_2.pack()


def submit_1_str():
    global lbl_questions_strings, pques_b_1, radio_var_strings
    x = radio_var_strings.get()
    if x == 2:
        Label(lbl_questions_strings, text="Correct", fg="green").pack()
        pques_str_1["state"] = "disabled"
        pques_2_str()
    elif x == 0 or x == 1 or x == 3:
        Label(lbl_questions_strings, text="len() is the length of the string", fg="red").pack()


def start_strings_module():
    global strings, fwd
    strings = Toplevel(screen)
    strings.geometry("1280x720")
    strings.iconbitmap('icon.ico')
    Label(strings, text="Welcome " + username1.title() + " to your Strings Lesson!",
          font=("Helvetica", "13", "bold")).pack()

    window = ScrolledFrame(strings)
    window.pack(expand=True, fill='both')

    lbl = LabelFrame(window.inner)
    lbl.pack()

    Label(lbl, text="""Strings are array of characters which be accessed by using the method of Indexing.
Indexing allows the use of address references to access characters from the array of characters
Indexing in Python always start with 0. """, font=("13")).pack()

    str_1 = Image.open("st_1.png")
    str_1 = str_1.resize((114, 99), Image.ANTIALIAS)
    str_1 = ImageTk.PhotoImage(str_1)

    str_1_i = Label(lbl, image=str_1)
    str_1_i.image = str_1
    str_1_i.pack()

    Label(lbl,
          text="""\nYou can also use negative number to start from the back.""",
          anchor=W, font=("13")).pack()

    str_2 = Image.open("st_2.PNG")
    str_2 = str_2.resize((119, 95), Image.ANTIALIAS)
    str_2 = ImageTk.PhotoImage(str_2)

    str_2_image = Label(lbl, image=str_2)
    str_2_image.image = str_2
    str_2_image.pack()

    Label(lbl,
          text="""\nAn escape character lets you use characters that are otherwise impossible to put into a string.
An escape character consists of a backslash (\) followed by the character you want to add to the string.

There are situations when you want to output a string that uses special characters that cannot be put into a string. 
Using raw strings completely ignores all escape charcters.""",
          anchor=W, font=("13")).pack()

    str_12 = Image.open("st_12.PNG")
    str_12 = str_12.resize((469, 308), Image.ANTIALIAS)
    str_12 = ImageTk.PhotoImage(str_12)

    str_12_i = Label(lbl, image=str_12)
    str_12_i.image = str_12
    str_12_i.pack()

    str_3 = Image.open("st_3.PNG")
    str_3 = str_3.resize((455, 83), Image.ANTIALIAS)
    str_3 = ImageTk.PhotoImage(str_3)

    str_3_i = Label(lbl, image=str_3)
    str_3_i.image = str_3
    str_3_i.pack()

    Label(lbl,
          text="""\n\nIf you have multi-line strings you can use triple quotation marks. """,
          anchor=W, font=("13")).pack()

    str_4 = Image.open("st_4.PNG")
    str_4 = str_4.resize((160, 344), Image.ANTIALIAS)
    str_4 = ImageTk.PhotoImage(str_4)

    str_4_i = Label(lbl, image=str_4)
    str_4_i.image = str_4
    str_4_i.pack()

    Label(lbl,
          text="""\n\nUsing not and not in. Remeber 

          boolean functions? Using in and not in finds a string inside another string. """,
          anchor=W, font=("13")).pack()

    str_5 = Image.open("st_5.PNG")
    str_5 = str_5.resize((231, 75), Image.ANTIALIAS)
    str_5 = ImageTk.PhotoImage(str_5)

    str_5_i = Label(lbl, image=str_5)
    str_5_i.image = str_5
    str_5_i.pack()

    Label(lbl,
          text="""\n\nlen() function return the length of a string.""",
          font=("13")).pack()

    str_8 = Image.open("st_8.PNG")
    str_8 = str_8.resize((152, 87), Image.ANTIALIAS)
    str_8 = ImageTk.PhotoImage(str_8)

    str_8_i = Label(lbl, image=str_8)
    str_8_i.image = str_8
    str_8_i.pack()

    Label(lbl,
          text="""\nsplit(x) is a method that returns a list of strings where x is the separator.""",
          font=("13")).pack()

    str_9 = Image.open("st_9.PNG")
    str_9 = str_9.resize((314, 97), Image.ANTIALIAS)
    str_9 = ImageTk.PhotoImage(str_9)

    str_9_i = Label(lbl, image=str_9)
    str_9_i.image = str_9
    str_9_i.pack()

    str_10 = Image.open("st_10.PNG")
    str_10 = str_10.resize((346, 163), Image.ANTIALIAS)
    str_10 = ImageTk.PhotoImage(str_10)

    str_10_i = Label(lbl, image=str_10)
    str_10_i.image = str_10
    str_10_i.pack()

    Label(lbl,
          text="""\nThe replace() method accepts two arguments: (1) the string to be replaced and (2) the string to be substituted.""",
          font=("13")).pack()

    str_11 = Image.open("st_11.PNG")
    str_11 = str_11.resize((303, 96), Image.ANTIALIAS)
    str_11 = ImageTk.PhotoImage(str_11)

    str_11_i = Label(lbl, image=str_11)
    str_11_i.image = str_11
    str_11_i.pack()

    Label(lbl,
          text="""\n\n Useful string methods """,
          anchor=W, font=("13")).pack()

    str_6 = Image.open("st_6.PNG")
    str_6 = str_6.resize((814, 277), Image.ANTIALIAS)
    str_6 = ImageTk.PhotoImage(str_6)

    str_6_i = Label(lbl, image=str_6)
    str_6_i.image = str_6
    str_6_i.pack()

    str_7 = Image.open("st_7.PNG")
    str_7 = str_7.resize((361, 527), Image.ANTIALIAS)
    str_7 = ImageTk.PhotoImage(str_7)

    str_7_i = Label(lbl, image=str_7)
    str_7_i.image = str_7
    str_7_i.pack()

    Label(lbl, text="""\n\nPractice Questions""",
          anchor=W, font=("20")).pack()
    global lbl_questions_strings, radio_var_strings, pques_str_1
    lbl_questions_strings = LabelFrame(lbl, padx=80, pady=80)
    lbl_questions_strings.pack()

    Label(lbl_questions_strings,
          text="""Determine the result of the following code""", font=("13")).pack()

    pques_string_1 = Image.open("pques_st_1.png")
    pques_string_1 = pques_string_1.resize((136, 34), Image.ANTIALIAS)
    pques_string_1 = ImageTk.PhotoImage(pques_string_1)

    pques_string_1_i = Label(lbl_questions_strings, image=pques_string_1)
    pques_string_1_i.image = pques_string_1
    pques_string_1_i.pack()

    radio_var_strings = IntVar()
    radio_var_strings.set(-1)
    radio1_1_str = Radiobutton(lbl_questions_strings, text="1", font=("12"), variable=radio_var_strings,
                               value=0)
    radio1_1_str.pack()

    radio2_1_str = Radiobutton(lbl_questions_strings, text="4", font=("12"), variable=radio_var_strings,
                               value=1)
    radio2_1_str.pack()

    radio3_1_str = Radiobutton(lbl_questions_strings, text="5", font=("12"), variable=radio_var_strings, value=2)
    radio3_1_str.pack()

    radio4_1_str = Radiobutton(lbl_questions_strings, text="6", font=("12"), variable=radio_var_strings, value=3)
    radio4_1_str.pack()

    pques_str_1 = Button(lbl_questions_strings, text="Submit!", command=submit_1_str)
    pques_str_1.pack()


def showresult_dfs(score_test_dfs):
    if score_test_dfs >= 4 and score_test_dfs <= 5:
        pgbar['value'] += 1

        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['Dictionary'] = "done"
        dicc_b['bg'] = "green"
        exep_b['state'] = NORMAL

        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()

        messagebox.showinfo("Result", "Your result is:" + str(score_test_dfs) + "\nYou are ready for the next Module!")
        dfs_test.destroy()
        dfs.destroy()
    elif score_test_dfs >= 2 and score_test_dfs <= 3:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_dfs) + "\nPractice makes Perfect! Take the quiz again to get a better score!")
        dfs_test.destroy()
        dfs.destroy()
    elif score_test_dfs >= 0 and score_test_dfs <= 1:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_dfs) + "\nYou need to study the module again! Take the quiz again to get a better score!")
        dfs_test.destroy()
        dfs.destroy()


def score_dfs():
    score_test_dfs = 0
    for i in range(5):
        if user_answer_dfs[i] == answers_dfs[i]:
            score_test_dfs = score_test_dfs + 1

    showresult_dfs(score_test_dfs)


def selected_dfs_test():
    global ques_dfs
    x = radio_var_dfs.get()
    user_answer_dfs.append(x)

    if ques_dfs < 5:
        radio_var_dfs.set(-1)
        lblquestion_dfs.config(text=questions_dfs_test[indexes_dfs[ques_dfs]])
        lblimage_dfs.config(image=img_list_dfs[indexes_dfs[ques_dfs]])
        r1_dfs['text'] = answer_choice_dfs_test[indexes_dfs[ques_dfs]][0]
        r2_dfs['text'] = answer_choice_dfs_test[indexes_dfs[ques_dfs]][1]
        r3_dfs['text'] = answer_choice_dfs_test[indexes_dfs[ques_dfs]][2]
        r4_dfs['text'] = answer_choice_dfs_test[indexes_dfs[ques_dfs]][3]
        ques_dfs += 1
    else:
        score_dfs()


def test_dfs():
    global dfs_test, ques_dfs, user_answer_dfs, lblquestion_dfs, lblimage_dfs, r1_dfs, r2_dfs, r3_dfs, r4_dfs, questions_dfs_test, indexes_dfs, img_list_dfs, answers_dfs, answer_choice_dfs_test
    dfs_test = Toplevel(dfs)
    dfs_test.title("Proficiency-Test")
    dfs_test.geometry("700x900")
    dfs_test.iconbitmap('icon.ico')
    indexes_dfs = [0, 1, 2, 3, 4]

    ques_dfs = 1
    user_answer_dfs = []

    file1 = open(username1 + ".txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))
    if "easy" == (dicc.get("mode")):
        questions_dfs_test = [
            r"Collection that can store different data types",
            "Uses curly braces `{}` to set up the collection",
            "Method of avoiding error when not in entry",
            """An unordered collection WITHOUT duplicate elements""",
            "What is the output of the code below", ]
        answer_choice_dfs_test = [
            ["A. Sets", "B. Dictionaries", "C. Dictionaries and Sets", "D. None"],
            ["A. Sets", "B. Dictionaries ", "C. Dictionaries and Sets", "D. None", ],
            ["A. Get()", r" B. Put()", " C. Call()", " D. Cast()", ],
            [r"A. Set", " B. Tuples", " C. Dictionaries", r" D. Lists", ],
            [r"A. 'My,2','first,5' ", r' B. My:2, first:5', r" C.{'My': 2, 'first': 5}", r'D. My,2,first,5', ],
        ]

        dfs_easy_1 = Image.open("dfs_easy_1.png")
        dfs_easy_1 = dfs_easy_1.resize((362, 47), Image.ANTIALIAS)
        dfs_easy_1 = ImageTk.PhotoImage(dfs_easy_1)

        img_list_dfs = ["", "", "", "", dfs_easy_1]
        answers_dfs = [2, 2, 0, 0, 2]

        Label(dfs_test, text="Proficiency Test for Dictionaries, Files and Sets module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(dfs_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_dfs = Label(dfs_test, text=questions_dfs_test[indexes_dfs[0]], font=("16"),
                                justify="center", wraplength=400, )
        lblquestion_dfs.pack()

        lblimage_dfs = Label(dfs_test, image="")
        lblimage_dfs.pack()

        global radio_var_dfs
        radio_var_dfs = IntVar()
        radio_var_dfs.set(-1)

        r1_dfs = Radiobutton(dfs_test, text=answer_choice_dfs_test[indexes_dfs[0]][0], font=("12"),
                             variable=radio_var_dfs, value=0)
        r1_dfs.pack()

        r2_dfs = Radiobutton(dfs_test, text=answer_choice_dfs_test[indexes_dfs[0]][1], font=("12"),
                             variable=radio_var_dfs, value=1)
        r2_dfs.pack()

        r3_dfs = Radiobutton(dfs_test, text=answer_choice_dfs_test[indexes_dfs[0]][2], font=("12"),
                             variable=radio_var_dfs, value=2)
        r3_dfs.pack()

        r4_dfs = Radiobutton(dfs_test, text=answer_choice_dfs_test[indexes_dfs[0]][3], font=("12"),
                             variable=radio_var_dfs, value=3)
        r4_dfs.pack()

        pques_dfs_b = Button(dfs_test, text="Submit!", command=selected_dfs_test)
        pques_dfs_b.pack()

    elif "hard" == (dicc.get("mode")):
        questions_dfs_test = [
            r"Which of the following aren't file mode descriptors",
            "WWhat is the output of the code below?",
            "What will code below display??",
            """Identify the error in the code (Corresponding Line)""",
            "IF the code were working, what is the output?", ]
        answer_choice_dfs_test = [
            ["A. r", "B. a", "C. x", "D. z"],
            ["A.  {'t', 'r', 'd', 'b', 's', 'i', 'k', 'm'}", r"B. {'r', 'm', 't', 's'}", "C. {'e','a','o'}",
             "D. {'e','a','o','i','n','o','s'}", ],
            ["A. {'b','e','g','h'} ", r" B. {'g','l','o','s'} ", "C. {'i','n','o','s'} ", r" D. {'b','o','s','s'}", ],
            ["A. 5 ", r" B. 11 ", "C. 2 ", r" D. 9", ],
            ['A. Yes! 7 Yes! 4!', r' B.Yes! 7 Yes! 4! My 3', ' C. Yes! 7 My 3  ', r' D. My 3', ],
        ]

        dfs_hard_1 = Image.open("dfs_hard_1.PNG")
        dfs_hard_1 = dfs_hard_1.resize((412, 66), Image.ANTIALIAS)
        dfs_hard_1 = ImageTk.PhotoImage(dfs_hard_1)

        dfs_hard_2 = Image.open("dfs_hard_2.PNG")
        dfs_hard_2 = dfs_hard_2.resize((302, 59), Image.ANTIALIAS)
        dfs_hard_2 = ImageTk.PhotoImage(dfs_hard_2)

        dfs_hard_3 = Image.open("dfs_hard_3.PNg")
        dfs_hard_3 = dfs_hard_3.resize((409, 224), Image.ANTIALIAS)
        dfs_hard_3 = ImageTk.PhotoImage(dfs_hard_3)

        img_list_dfs = ["", dfs_hard_1, dfs_hard_2, dfs_hard_3, dfs_hard_3]

        answers_dfs = [3, 1, 2, 0, 2]

        Label(dfs_test, text="Proficiency Test for Dictionaries, Files and Sets Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(dfs_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_dfs = Label(dfs_test, text=questions_dfs_test[indexes_dfs[0]], font=("16"),
                                justify="center", wraplength=400, )
        lblquestion_dfs.pack()

        lblimage_dfs = Label(dfs_test, image=''
                                             '')
        lblimage_dfs.pack()

        radio_var_dfs = IntVar()
        radio_var_dfs.set(-1)

        r1_dfs = Radiobutton(dfs_test, text=answer_choice_dfs_test[indexes_dfs[0]][0], font=("12"),
                             variable=radio_var_dfs, value=0)
        r1_dfs.pack()

        r2_dfs = Radiobutton(dfs_test, text=answer_choice_dfs_test[indexes_dfs[0]][1], font=("12"),
                             variable=radio_var_dfs, value=1)
        r2_dfs.pack()

        r3_dfs = Radiobutton(dfs_test, text=answer_choice_dfs_test[indexes_dfs[0]][2], font=("12"),
                             variable=radio_var_dfs, value=2)
        r3_dfs.pack()

        r4_dfs = Radiobutton(dfs_test, text=answer_choice_dfs_test[indexes_dfs[0]][3], font=("12"),
                             variable=radio_var_dfs, value=3)
        r4_dfs.pack()

        pques_dfs_b = Button(dfs_test, text="Submit!", command=selected_dfs_test)
        pques_dfs_b.pack()

    elif "medium" == (dicc.get("mode")):
        questions_dfs_test = [
            """Which container type doesn't use relative positioning?""",
            "Is there any error in the code?",
            "What is the syntax for iteration over keys?",
            """What error is returned when get() doesn't find the entry?""",
            "How to we remove a key and/or value in a dictionary? ", ]
        answer_choice_dfs_test = [
            ["A. Dictionaries", "B. Variables", "C. Lists", "D. Tuples"],
            ["A. Yes, the file was not opened", "Yes, the file was not closed", "C. No, the file with open properly",
             "D. The error cannot be determined with given syntax."],
            ["A. for letter in dictionary.values()", r' B. for letter in dictionary.keysvalue()',
             " C. for letter in dictionary.keys()", r' D. for letter in dictionary.items()', ],
            ["A. File not found", r' B. Entry not found', " C. Value not found", r' D. Key not found', ],
            ["A. Remove()", r' B. Delete()', " C. Append()", r" D. Pop()", ],
        ]

        dfs_medium_1 = Image.open("dfs_medium_1.PNG")
        dfs_medium_1 = dfs_medium_1.resize((303, 45), Image.ANTIALIAS)
        dfs_medium_1 = ImageTk.PhotoImage(dfs_medium_1)

        img_list_dfs = ["", dfs_medium_1, "", "", "", ]
        answers_dfs = [1, 1, 3, 1, 4]

        Label(dfs_test, text="Proficiency Test for Dictionaries, Files and Sets Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(dfs_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_dfs = Label(dfs_test, text=questions_dfs_test[indexes_dfs[0]], font=("16"),
                                justify="center", wraplength=400, )
        lblquestion_dfs.pack()

        lblimage_dfs = Label(dfs_test, image="")
        lblimage_dfs.pack()

        radio_var_dfs = IntVar()
        radio_var_dfs.set(-1)

        r1_dfs = Radiobutton(dfs_test, text=answer_choice_dfs_test[indexes_dfs[0]][0], font=("12"),
                             variable=radio_var_dfs, value=0)
        r1_dfs.pack()

        r2_dfs = Radiobutton(dfs_test, text=answer_choice_dfs_test[indexes_dfs[0]][1], font=("12"),
                             variable=radio_var_dfs, value=1)
        r2_dfs.pack()

        r3_dfs = Radiobutton(dfs_test, text=answer_choice_dfs_test[indexes_dfs[0]][2], font=("12"),
                             variable=radio_var_dfs, value=2)
        r3_dfs.pack()

        r4_dfs = Radiobutton(dfs_test, text=answer_choice_dfs_test[indexes_dfs[0]][3], font=("12"),
                             variable=radio_var_dfs, value=3)
        r4_dfs.pack()

        pques_dfs_b = Button(dfs_test, text="Submit!", command=selected_dfs_test)
        pques_dfs_b.pack()


def showresult_gui(score_test_gui):
    if score_test_gui >= 4 and score_test_gui <= 5:
        pgbar['value'] += 1
        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['Gui'] = "done"
        graph_b['bg'] = "green"

        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()

        final_button_act()
        messagebox.showinfo("Result", "Your result is:" + str(score_test_gui) + "\nYou are ready for the next Module!")
        gui_test.destroy()
        gui.destroy()

    elif score_test_gui >= 2 and score_test_gui <= 3:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_gui) + "\nPractice makes Perfect! Take the quiz again to get a better score!")
        gui_test.destroy()
        gui.destroy()
    elif score_test_gui >= 0 and score_test_gui <= 1:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_gui) + "\nYou need to study the module again! Take the quiz again to get a better score!")
        gui_test.destroy()
        gui.destroy()


def score_gui():
    score_test_gui = 0
    for i in range(5):
        if user_answer_gui[i] == answers_gui[i]:
            score_test_gui = score_test_gui + 1

    showresult_gui(score_test_gui)


def selected_gui_test():
    global ques_gui
    x = radio_var_gui.get()
    user_answer_gui.append(x)

    if ques_gui < 5:
        radio_var_gui.set(-1)
        lblquestion_gui.config(text=questions_gui_test[indexes_gui[ques_gui]])
        lblimage_gui.config(image=img_list_gui[indexes_gui[ques_gui]])
        r1_gui['text'] = answer_choice_gui_test[indexes_gui[ques_gui]][0]
        r2_gui['text'] = answer_choice_gui_test[indexes_gui[ques_gui]][1]
        r3_gui['text'] = answer_choice_gui_test[indexes_gui[ques_gui]][2]
        r4_gui['text'] = answer_choice_gui_test[indexes_gui[ques_gui]][3]
        ques_gui += 1
    else:
        score_gui()


def test_gui():
    global gui_test,ques_gui,user_answer_gui, lblquestion_gui, lblimage_gui, r1_gui, r2_gui, r3_gui, r4_gui, questions_gui_test, indexes_gui, img_list_gui, answers_gui, answer_choice_gui_test, gui
    gui_test = Toplevel(gui)
    gui_test.title("Proficiency-Test")
    gui_test.geometry("700x700")
    gui_test.iconbitmap('icon.ico')
    indexes_gui = [0, 1, 2, 3, 4]

    user_answer_gui = []
    ques_gui = 1

    file1 = open("felix.txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))
    if "easy" == (dicc.get("mode")):
        questions_gui_test = [
            r"What are ways to display wdigets?",
            "How do you add buttons in tkinter? ",
            "How do you create an entry field in tkinter? ",
            """How do you get input data from entry?""",
            "What should you initialize first before making an entry widget", ]
        answer_choice_gui_test = [
            ["A.grid", "B. pack", "C.grid and pack", "D.Display"],
            ["A. Button(root widget, **options)", "B. Button(text) ", "C. add_button()", "D. command=add_button()", ],
            ["A. Entry(root_widget).pack()", r" B. Entry(root_widget)", " C.add_entry()",
             " D. command=entry_button()", ],
            [r"A.get method  ", " B. entry.gets ", " C.entry.gets()", r" D. obtain function", ],
            [r'A. StringVar  ', r' B.string ', r' C.entry variable', r'D. None', ],
        ]

        img_list_gui = ["", "", "", "", ""]
        answers_gui = [2, 0, 0, 0, 0]

        Label(gui_test, text="Proficiency Test for GUI Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(gui_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_gui = Label(gui_test, text=questions_gui_test[indexes_gui[0]], font=("16"),
                                justify="center", wraplength=400, )
        lblquestion_gui.pack()

        lblimage_gui = Label(gui_test, image="")
        lblimage_gui.pack()

        global radio_var_gui
        radio_var_gui = IntVar()
        radio_var_gui.set(-1)

        r1_gui = Radiobutton(gui_test, text=answer_choice_gui_test[indexes_gui[0]][0], font=("12"),
                             variable=radio_var_gui, value=0)
        r1_gui.pack()

        r2_gui = Radiobutton(gui_test, text=answer_choice_gui_test[indexes_gui[0]][1], font=("12"),
                             variable=radio_var_gui, value=1)
        r2_gui.pack()

        r3_gui = Radiobutton(gui_test, text=answer_choice_gui_test[indexes_gui[0]][2], font=("12"),
                             variable=radio_var_gui, value=2)
        r3_gui.pack()

        r4_gui = Radiobutton(gui_test, text=answer_choice_gui_test[indexes_gui[0]][3], font=("12"),
                             variable=radio_var_gui, value=3)
        r4_gui.pack()

        pques_gui_b = Button(gui_test, text="Submit!", command=selected_gui_test)
        pques_gui_b.pack()

    elif "hard" == (dicc.get("mode")):
        questions_gui_test = [
            r"This function needs to clear the input value. What is missing from the code?",
            "Window root needs to have a title. What is missing from the code?",
            "Your root window needs a button named with text exit to close the window.What code is correct?",
            """You need to add a text label in your label frame. Which code is correct? """,
            "What is wrong with this code", ]
        answer_choice_gui_test = [
            ["A.username_entry.delete()", "B.username_entry.destroy(0, END)", "C.username_entry.clear(0, END)",
             "D.username_entry.delete(0, END)"],
            ["A. root.title('Title')", "B. title('title') ", "C. title.pack()", "D. title.change('title')", ],
            ["A. Button(root, text='Exit', command=window.destroy).pack()",
             r" B. Button(root, text='Exit', command=root.destroy).pack()", " C.window.destroy",
             " D. window.destroy()", ],
            [r"A.Label(lbl, text='Text') ", " B.Label(lbl, text='Text').pack()", " C. (lbl, text='Text')",
             r" D. (labelFrame, text='Text')", ],
            [r'A. The code works', r' Wrong string value', r' C.wrong command syntax', r'D.wrong entry syntax', ],
        ]
        gui_test_1 = Image.open("gui_hard_1.PNG")
        gui_test_1 = gui_test_1.resize((485, 79), Image.ANTIALIAS)
        gui_test_1 = ImageTk.PhotoImage(gui_test_1)

        gui_test_2 = Image.open("gui_hard_2.PNG")
        gui_test_2 = gui_test_2.resize((232, 96), Image.ANTIALIAS)
        gui_test_2 = ImageTk.PhotoImage(gui_test_2)

        gui_test_3 = Image.open("gui_hard_3.PNG")
        gui_test_3 = gui_test_3.resize((250, 187), Image.ANTIALIAS)
        gui_test_3 = ImageTk.PhotoImage(gui_test_3)

        gui_test_4 = Image.open("gui_hard_4.PNG")
        gui_test_4 = gui_test_4.resize((538, 398), Image.ANTIALIAS)
        gui_test_4 = ImageTk.PhotoImage(gui_test_4)

        img_list_gui = [gui_test_1, gui_test_2, "", gui_test_3, gui_test_4]
        answers_gui = [1, 0, 1, 1, 2]

        Label(gui_test, text="Proficiency Test for GUI Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(gui_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_gui = Label(gui_test, text=questions_gui_test[indexes_gui[0]], font=("16"),
                                justify="center", wraplength=400, )
        lblquestion_gui.pack()

        lblimage_gui = Label(gui_test, image=gui_test_1)
        lblimage_gui.pack()

        radio_var_gui = IntVar()
        radio_var_gui.set(-1)

        r1_gui = Radiobutton(gui_test, text=answer_choice_gui_test[indexes_gui[0]][0], font=("12"),
                             variable=radio_var_gui, value=0)
        r1_gui.pack()

        r2_gui = Radiobutton(gui_test, text=answer_choice_gui_test[indexes_gui[0]][1], font=("12"),
                             variable=radio_var_gui, value=1)
        r2_gui.pack()

        r3_gui = Radiobutton(gui_test, text=answer_choice_gui_test[indexes_gui[0]][2], font=("12"),
                             variable=radio_var_gui, value=2)
        r3_gui.pack()

        r4_gui = Radiobutton(gui_test, text=answer_choice_gui_test[indexes_gui[0]][3], font=("12"),
                             variable=radio_var_gui, value=3)
        r4_gui.pack()

        pques_gui_b = Button(gui_test, text="Submit!", command=selected_gui_test)
        pques_gui_b.pack()

    elif "medium" == (dicc.get("mode")):
        questions_gui_test = [
            r"What is wrong with this code?",
            "What function is used to exit the window?",
            "What command is used to make a default size for your window?",
            """Which of these is the proper way to create a command to exit windows""",
            "How do you loop the whole program until the program is closed?", ]
        answer_choice_gui_test = [
            ["A.Nothing wrong", "B. wrong syntax with Label", "C.No variable name for Label",
             "D.Did not import tkinter"],
            ["A. window.exit", "B. window.destroy() ", "C. window.exit()", "D. window.destroy", ],
            ["A. window.geometry()", r" B. window.resize()", " C.window.geometry(size)", " D. window.resize(size)", ],
            [r"A.command=root.destroy() ", " B. command=root.destroy", " C. root.destroy", r" D. root.destroy()", ],
            [r'A. mainloop() ', r' B.mainloop ', r' C.root.mainloop()', r'D.root.mainloop', ],
        ]
        gui_test_1 = Image.open("gui_medium_1.PNG")
        gui_test_1 = gui_test_1.resize((265, 115), Image.ANTIALIAS)
        gui_test_1 = ImageTk.PhotoImage(gui_test_1)

        img_list_gui = [gui_test_1, "", "", "", ""]
        answers_gui = [3, 1, 2, 1, 2]

        Label(gui_test, text="Proficiency Test for GUI Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(gui_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_gui = Label(gui_test, text=questions_gui_test[indexes_gui[0]], font=("16"),
                                justify="center", wraplength=400, )
        lblquestion_gui.pack()

        lblimage_gui = Label(gui_test, image=gui_test_1)
        lblimage_gui.pack()

        radio_var_gui = IntVar()
        radio_var_gui.set(-1)

        r1_gui = Radiobutton(gui_test, text=answer_choice_gui_test[indexes_gui[0]][0], font=("12"),
                             variable=radio_var_gui, value=0)
        r1_gui.pack()

        r2_gui = Radiobutton(gui_test, text=answer_choice_gui_test[indexes_gui[0]][1], font=("12"),
                             variable=radio_var_gui, value=1)
        r2_gui.pack()

        r3_gui = Radiobutton(gui_test, text=answer_choice_gui_test[indexes_gui[0]][2], font=("12"),
                             variable=radio_var_gui, value=2)
        r3_gui.pack()

        r4_gui = Radiobutton(gui_test, text=answer_choice_gui_test[indexes_gui[0]][3], font=("12"),
                             variable=radio_var_gui, value=3)
        r4_gui.pack()

        pques_gui_b = Button(gui_test, text="Submit!", command=selected_gui_test)
        pques_gui_b.pack()


def showresult_numpy(score_test_numpy):
    if score_test_numpy >= 4 and score_test_numpy <= 5:
        pgbar['value'] += 1
        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['Numpy'] = "done"
        nump_button['bg'] = "green"
        bool_button['state'] = NORMAL

        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()

        messagebox.showinfo("Result",
                            "Your result is:" + str(score_test_numpy) + "\nYou are ready for the next Module!")

        numpy_test.destroy()
        numpy.destroy()

    elif score_test_numpy >= 2 and score_test_numpy <= 3:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_numpy) + "\nPractice makes Perfect! Take the quiz again to get a better score!")
        numpy_test.destroy()
        numpy.destroy()
    elif score_test_numpy >= 0 and score_test_numpy <= 1:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_numpy) + "\nYou need to study the module again! Take the quiz again to get a better score!")
        numpy_test.destroy()
        numpy.destroy()


def score_numpy():
    score_test_numpy = 0
    for i in range(5):
        if user_answer_numpy[i] == answers_numpy[i]:
            score_test_numpy = score_test_numpy + 1

    showresult_numpy(score_test_numpy)


def selected_numpy_test():
    global ques_numpy
    x = radio_var_numpy.get()
    user_answer_numpy.append(x)

    if ques_numpy < 5:
        radio_var_numpy.set(-1)
        lblquestion_numpy.config(text=questions_numpy_test[indexes_numpy[ques_numpy]])
        lblimage_numpy.config(image=img_list_numpy[indexes_numpy[ques_numpy]])
        r1_numpy['text'] = answer_choice_numpy_test[indexes_numpy[ques_numpy]][0]
        r2_numpy['text'] = answer_choice_numpy_test[indexes_numpy[ques_numpy]][1]
        r3_numpy['text'] = answer_choice_numpy_test[indexes_numpy[ques_numpy]][2]
        r4_numpy['text'] = answer_choice_numpy_test[indexes_numpy[ques_numpy]][3]
        ques_numpy += 1
    else:
        score_numpy()


def test_numpy():
    global ques_numpy, numpy_test, user_answer_numpy, lblquestion_numpy, lblimage_numpy, r1_numpy, r2_numpy, r3_numpy, r4_numpy, questions_numpy_test, indexes_numpy, img_list_numpy, answers_numpy, answer_choice_numpy_test
    numpy_test = Toplevel(numpy)
    numpy_test.title("Proficiency-Test")
    numpy_test.geometry("700x900")
    numpy_test.iconbitmap('icon.ico')
    indexes_numpy = [0, 1, 2, 3, 4]
    ques_numpy = 1
    user_answer_numpy = []

    file1 = open(username1 + ".txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))
    if "easy" == (dicc.get("mode")):
        questions_numpy_test = [
            r"Numpy provides functions for _____ types of container",
            "What would be the value of the syntax below?",
            "Numpy tackles with the manipulation of:",
            """It is impossible to do arithmetic functions on element containers of not the same shape.""",
            "This is the method of handling data piece by piece", ]
        answer_choice_numpy_test = [
            ["A. List", "B. Dictionary", "C. Tuple", "D. Array"],
            ["A. [1,2,3,4,5]", "B. [1,2,3,4,5,1,1,1,1]", "C. [2,3,4,5,1,1,1,1]", "D. There is no output", ],
            ["A. Lists", r" B. Arrays", " C. Sets", " D. Tuples", ],
            [r"A. True", " B. False", " C. Not enough information", r" D. Depends", ],
            [r"A. piecewise", r' B. element wise', r" C. broadcasting method", r'D. sorting wise', ],
        ]

        numpy_easy_1 = Image.open("numpy_easy_1.png")
        numpy_easy_1 = numpy_easy_1.resize((274, 58), Image.ANTIALIAS)
        numpy_easy_1 = ImageTk.PhotoImage(numpy_easy_1)

        img_list_numpy = ["", numpy_easy_1, "", "", ""]
        answers_numpy = [3, 1, 1, 1, 1]

        Label(numpy_test, text="Proficiency Test for Numpy Module",
              font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(numpy_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_numpy = Label(numpy_test, text=questions_numpy_test[indexes_numpy[0]], font=("16"),
                                  justify="center", wraplength=400, )
        lblquestion_numpy.pack()

        lblimage_numpy = Label(numpy_test, image="")
        lblimage_numpy.pack()

        global radio_var_numpy
        radio_var_numpy = IntVar()
        radio_var_numpy.set(-1)

        r1_numpy = Radiobutton(numpy_test, text=answer_choice_numpy_test[indexes_numpy[0]][0], font=("12"),
                               variable=radio_var_numpy, value=0)
        r1_numpy.pack()

        r2_numpy = Radiobutton(numpy_test, text=answer_choice_numpy_test[indexes_numpy[0]][1], font=("12"),
                               variable=radio_var_numpy, value=1)
        r2_numpy.pack()

        r3_numpy = Radiobutton(numpy_test, text=answer_choice_numpy_test[indexes_numpy[0]][2], font=("12"),
                               variable=radio_var_numpy, value=2)
        r3_numpy.pack()

        r4_numpy = Radiobutton(numpy_test, text=answer_choice_numpy_test[indexes_numpy[0]][3], font=("12"),
                               variable=radio_var_numpy, value=3)
        r4_numpy.pack()

        pques_numpy_b = Button(numpy_test, text="Submit!", command=selected_numpy_test)
        pques_numpy_b.pack()

    elif "hard" == (dicc.get("mode")):
        questions_numpy_test = [
            r"Analyze the code below, identify if there are any errors, choose the line below",
            "What would be the output of the program?",
            "What would be the size of bytes of the program?",
            """Analyze the code below, identify if there are any errors in the lines of code""",
            "What is the output of the code?", ]
        answer_choice_numpy_test = [
            ["A. 6 and/or 7", "B. 2 and/or 3", "C. 4 and/or 5", "D. No error"],
            ["A. []", r"B. [6,7,8,9]", "C. [0,1,2,3,4,5]", "D. Program has an error.", ],
            ["A. 7", r" B. 8", "C. 9", r" D. 10", ],
            ["A. 2 and/or 3", r" B. 1 and/or 4", "C. 5 and/or 6", r" D. No error in the code", ],
            ['A. No Output / Code is wrong', r' B. [1 2],[1 2]', ' C. [2 1],[7 2[,[1 8]', r' D. [7 8 7 8]', ],
        ]

        numpy_hard_1 = Image.open("numpy_hard_1.PNG")
        numpy_hard_1 = numpy_hard_1.resize((312, 136), Image.ANTIALIAS)
        numpy_hard_1 = ImageTk.PhotoImage(numpy_hard_1)

        numpy_hard_2 = Image.open("numpy_hard_2.PNG")
        numpy_hard_2 = numpy_hard_2.resize((281, 58), Image.ANTIALIAS)
        numpy_hard_2 = ImageTk.PhotoImage(numpy_hard_2)

        numpy_hard_3 = Image.open("numpy_hard_3.PNg")
        numpy_hard_3 = numpy_hard_3.resize((391, 117), Image.ANTIALIAS)
        numpy_hard_3 = ImageTk.PhotoImage(numpy_hard_3)

        img_list_numpy = [numpy_hard_1, numpy_hard_1, numpy_hard_2, numpy_hard_3, numpy_hard_3]

        answers_numpy = [3, 0, 1, 3, 3]

        Label(numpy_test, text="Proficiency Test for NUMPY Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(numpy_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_numpy = Label(numpy_test, text=questions_numpy_test[indexes_numpy[0]], font=("16"),
                                  justify="center", wraplength=400, )
        lblquestion_numpy.pack()

        lblimage_numpy = Label(numpy_test, image=numpy_hard_1)
        lblimage_numpy.pack()

        radio_var_numpy = IntVar()
        radio_var_numpy.set(-1)

        r1_numpy = Radiobutton(numpy_test, text=answer_choice_numpy_test[indexes_numpy[0]][0], font=("12"),
                               variable=radio_var_numpy, value=0)
        r1_numpy.pack()

        r2_numpy = Radiobutton(numpy_test, text=answer_choice_numpy_test[indexes_numpy[0]][1], font=("12"),
                               variable=radio_var_numpy, value=1)
        r2_numpy.pack()

        r3_numpy = Radiobutton(numpy_test, text=answer_choice_numpy_test[indexes_numpy[0]][2], font=("12"),
                               variable=radio_var_numpy, value=2)
        r3_numpy.pack()

        r4_numpy = Radiobutton(numpy_test, text=answer_choice_numpy_test[indexes_numpy[0]][3], font=("12"),
                               variable=radio_var_numpy, value=3)
        r4_numpy.pack()

        pques_numpy_b = Button(numpy_test, text="Submit!", command=selected_numpy_test)
        pques_numpy_b.pack()

    elif "medium" == (dicc.get("mode")):
        questions_numpy_test = [
            """Numpy provides functions for ____ types of containers""",
            "What would be the value of the syntax below?",
            "What would be the output of the code below?",
            """Supposedly, this program will make a 3x2 array. identify if there are any errors in any line""",
            "What value do we replace to circumvent the error?", ]
        answer_choice_numpy_test = [
            ["A. One Dimension", "B. Two Dimension", "C. Three Dimension", "D. All of the above"],
            ["A. [2,3,4,5]", "B. [1,3,4,5,1,1,1,1]", "C. [3,4,5,1,1,1,1]", "D. There is no output"],
            ["A. 5", r' B. 2', " C. 4", r' D. 3', ],
            ["A. 1", r' B. 2', " C. 3", r' D. No error', ],
            ["A. arrange(2,3)", r' B. from numpy import np', " C. reshape(3,2)", r" D. No error", ],
        ]

        numpy_medium_1 = Image.open("numpy_medium_1.PNG")
        numpy_medium_1 = numpy_medium_1.resize((278, 71), Image.ANTIALIAS)
        numpy_medium_1 = ImageTk.PhotoImage(numpy_medium_1)

        numpy_medium_2 = Image.open("numpy_medium_2.PNG")
        numpy_medium_2 = numpy_medium_2.resize((342, 59), Image.ANTIALIAS)
        numpy_medium_2 = ImageTk.PhotoImage(numpy_medium_2)

        numpy_medium_3 = Image.open("numpy_medium_3.PNG")
        numpy_medium_3 = numpy_medium_3.resize((297, 75), Image.ANTIALIAS)
        numpy_medium_3 = ImageTk.PhotoImage(numpy_medium_3)

        img_list_numpy = ["", numpy_medium_1, numpy_medium_2, numpy_medium_3, "", ]
        answers_numpy = [3, 1, 0, 2, 2]

        Label(numpy_test, text="Proficiency Test for NUMPY Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(numpy_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_numpy = Label(numpy_test, text=questions_numpy_test[indexes_numpy[0]], font=("16"),
                                  justify="center", wraplength=400, )
        lblquestion_numpy.pack()

        lblimage_numpy = Label(numpy_test, image="")
        lblimage_numpy.pack()

        radio_var_numpy = IntVar()
        radio_var_numpy.set(-1)

        r1_numpy = Radiobutton(numpy_test, text=answer_choice_numpy_test[indexes_numpy[0]][0], font=("12"),
                               variable=radio_var_numpy, value=0)
        r1_numpy.pack()

        r2_numpy = Radiobutton(numpy_test, text=answer_choice_numpy_test[indexes_numpy[0]][1], font=("12"),
                               variable=radio_var_numpy, value=1)
        r2_numpy.pack()

        r3_numpy = Radiobutton(numpy_test, text=answer_choice_numpy_test[indexes_numpy[0]][2], font=("12"),
                               variable=radio_var_numpy, value=2)
        r3_numpy.pack()

        r4_numpy = Radiobutton(numpy_test, text=answer_choice_numpy_test[indexes_numpy[0]][3], font=("12"),
                               variable=radio_var_numpy, value=3)
        r4_numpy.pack()

        pques_numpy_b = Button(numpy_test, text="Submit!", command=selected_numpy_test)
        pques_numpy_b.pack()


def showresult_exep(score_test_exep):
    if score_test_exep >= 4 and score_test_exep <= 5:
        pgbar['value'] += 1
        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['Exceptions'] = "done"
        exep_b['bg'] = "green"
        graph_b['state'] = NORMAL

        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()

        messagebox.showinfo("Result", "Your result is:" + str(score_test_exep) + "\nYou are ready for the next Module!")
        excep_test.destroy()
        excep.destroy()

    elif score_test_exep >= 2 and score_test_exep <= 3:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_exep) + "\nPractice makes Perfect! Take the quiz again to get a better score!")
        excep_test.destroy()
        excep.destroy()
    elif score_test_exep >= 0 and score_test_exep <= 1:
        messagebox.showinfo("Result", "Your result is:" + str(
            score_test_exep) + "\nYou need to study the module again! Take the quiz again to get a better score!")
        excep_test.destroy()
        excep.destroy()


def score_exep():
    score_test_exep = 0
    for i in range(5):
        if user_answer_excep[i] == answers_exep[i]:
            score_test_exep = score_test_exep + 1

    showresult_exep(score_test_exep)


def selected_exep_test():
    global ques_exep
    x = radio_var_exep.get()
    user_answer_excep.append(x)

    if ques_exep < 5:
        radio_var_exep.set(-1)
        lblquestion_exep.config(text=questions_exep_test[indexes_excep[ques_exep]])
        lblimage_exep.config(image=img_list_exep[indexes_excep[ques_exep]])
        r1_exep['text'] = answer_choice_exep_test[indexes_excep[ques_exep]][0]
        r2_exep['text'] = answer_choice_exep_test[indexes_excep[ques_exep]][1]
        r3_exep['text'] = answer_choice_exep_test[indexes_excep[ques_exep]][2]
        r4_exep['text'] = answer_choice_exep_test[indexes_excep[ques_exep]][3]
        ques_exep += 1
    else:
        score_exep()


def test_exep():
    global excep_test, ques_exep, excep, user_answer_excep, lblquestion_exep, lblimage_exep, r1_exep, r2_exep, r3_exep, r4_exep, answer_choice_exep_test, indexes_excep, questions_exep_test, img_list_exep, answers_exep
    excep_test = Toplevel(excep)
    excep_test.title("Proficiency-Test")
    excep_test.geometry("700x700")
    excep_test.iconbitmap('icon.ico')
    indexes_excep = [0, 1, 2, 3, 4]

    ques_exep = 1

    user_answer_excep = []

    file1 = open("felix.txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))
    if "easy" == (dicc.get("mode")):
        questions_exep_test = [
            r"What is a method that combines for loops and list?",
            "Which statement is used to handle exceptions ",
            "which statement runs whether or not the try statement produces an exception. ",
            """Determine the result of this code""",
            "What kind of error is encountered", ]
        answer_choice_exep_test = [
            ["A.Exceptions", "B. Lists", "C. Dictionaries", "D. List Comprehensions"],
            ["A. try", "B. except ", "C. try and except", "D. finally", ],
            ["A. try ", r" B. except", " B. try and except", " D. finally", ],
            [r"A. 'Error'  ", " B.  Invalid Syntax ", " B.11", r" D. 2", ],
            [r'A. Logical  ', r' B.Syntax ', r' C. No error', r'D. Wrong data type', ],
        ]
        exp_test_1 = Image.open("ex_easy_1.PNG")
        exp_test_1 = exp_test_1.resize((199, 144), Image.ANTIALIAS)
        exp_test_1 = ImageTk.PhotoImage(exp_test_1)

        exp_test_2 = Image.open("ex_easy_2.PNG")
        exp_test_2 = exp_test_2.resize((141, 66), Image.ANTIALIAS)
        exp_test_2 = ImageTk.PhotoImage(exp_test_2)

        img_list_exep = ["", "", "", exp_test_1, exp_test_2]
        answers_exep = [3, 2, 3, 0, 1]

        Label(excep_test, text="Proficiency Test for Exceptions Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(excep_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_exep = Label(excep_test, text=questions_exep_test[indexes_excep[0]], font=("16"),
                                 justify="center", wraplength=400, )
        lblquestion_exep.pack()

        lblimage_exep = Label(excep_test, image="")
        lblimage_exep.pack()

        global radio_var_exep
        radio_var_exep = IntVar()
        radio_var_exep.set(-1)

        r1_exep = Radiobutton(excep_test, text=answer_choice_exep_test[indexes_excep[0]][0], font=("12"),
                              variable=radio_var_exep, value=0)
        r1_exep.pack()

        r2_exep = Radiobutton(excep_test, text=answer_choice_exep_test[indexes_excep[0]][1], font=("12"),
                              variable=radio_var_exep, value=1)
        r2_exep.pack()

        r3_exep = Radiobutton(excep_test, text=answer_choice_exep_test[indexes_excep[0]][2], font=("12"),
                              variable=radio_var_exep, value=2)
        r3_exep.pack()

        r4_exep = Radiobutton(excep_test, text=answer_choice_exep_test[indexes_excep[0]][3], font=("12"),
                              variable=radio_var_exep, value=3)
        r4_exep.pack()

        pques_exep_b = Button(excep_test, text="Submit!", command=selected_exep_test)
        pques_exep_b.pack()
    elif "medium" == (dicc.get("mode")):
        questions_exep_test = [
            r"Determine the error of this code",
            "Determine the result of this code ",
            "Determine the result of this code ",
            """Determine the result of this code""",
            "Determine the result of this code", ]
        answer_choice_exep_test = [
            ["A.No errors", "B. Wrong variable name", "C. Wrong data type ", "D.Logical error"],
            ["A. Wrong data type", r'B. "You are 2 years old\nhappy birthday"', 'C. "You are 2 years old"',
             "D.Logical error", ],
            ["A. Wrong data type ", r" B. [54, 56, 58] ", " C. [54, 56, 58, 60]", " D. [56, 58, 60]", ],
            [r"A. 'Error\ni will still print'  ", " B. 'Error i will still print' ", " B.Error",
             r" D.'i will still print' ", ],
            [r"A. 1: '1' ", r' B."5" ', r' C. Error', r"D. 5: '5' ", ],
        ]
        exp_test_1 = Image.open("ex_medium_1.PNG")
        exp_test_1 = exp_test_1.resize((482, 227), Image.ANTIALIAS)
        exp_test_1 = ImageTk.PhotoImage(exp_test_1)

        exp_test_2 = Image.open("ex_medium_2.PNG")
        exp_test_2 = exp_test_2.resize((470, 188), Image.ANTIALIAS)
        exp_test_2 = ImageTk.PhotoImage(exp_test_2)

        exp_test_3 = Image.open("ex_medium_3.PNG")
        exp_test_3 = exp_test_3.resize((420, 59), Image.ANTIALIAS)
        exp_test_3 = ImageTk.PhotoImage(exp_test_3)

        exp_test_4 = Image.open("ex_medium_4.PNG")
        exp_test_4 = exp_test_4.resize((310, 163), Image.ANTIALIAS)
        exp_test_4 = ImageTk.PhotoImage(exp_test_4)

        exp_test_5 = Image.open("ex_medium_5.PNG")
        exp_test_5 = exp_test_5.resize((445, 61), Image.ANTIALIAS)
        exp_test_5 = ImageTk.PhotoImage(exp_test_5)

        img_list_exep = [exp_test_1, exp_test_2, exp_test_3, exp_test_4, exp_test_5]
        answers_exep = [3, 1, 3, 0, 1]

        Label(excep_test, text="Proficiency Test for Exceptions Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(excep_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_exep = Label(excep_test, text=questions_exep_test[indexes_excep[0]], font=("16"),
                                 justify="center", wraplength=400, )
        lblquestion_exep.pack()

        lblimage_exep = Label(excep_test, image=exp_test_1)
        lblimage_exep.pack()

        radio_var_exep = IntVar()
        radio_var_exep.set(-1)

        r1_exep = Radiobutton(excep_test, text=answer_choice_exep_test[indexes_excep[0]][0], font=("12"),
                              variable=radio_var_exep, value=0)
        r1_exep.pack()

        r2_exep = Radiobutton(excep_test, text=answer_choice_exep_test[indexes_excep[0]][1], font=("12"),
                              variable=radio_var_exep, value=1)
        r2_exep.pack()

        r3_exep = Radiobutton(excep_test, text=answer_choice_exep_test[indexes_excep[0]][2], font=("12"),
                              variable=radio_var_exep, value=2)
        r3_exep.pack()

        r4_exep = Radiobutton(excep_test, text=answer_choice_exep_test[indexes_excep[0]][3], font=("12"),
                              variable=radio_var_exep, value=3)
        r4_exep.pack()

        pques_exep_b = Button(excep_test, text="Submit!", command=selected_exep_test)
        pques_exep_b.pack()
    elif "hard" == (dicc.get("mode")):
        questions_exep_test = [
            r"Determine the result of this code",
            "Determine the result of this code ",
            "Determine the the respective values of x and y",
            """Determine the result of this code""",
            "Determine the result of this code", ]
        answer_choice_exep_test = [
            ["A.[[1, 3]]", "B. [[1, 3], [2, 4]]", "C.[] ", "D.[1,2]"],
            ["A. [[1, 3], [2, 4]]", r'B. [[1, 3]]', 'C. "[1,2]', "D.[]"],
            ["A. 8 and 9 ", r" B. 4 and 3 ", " C. 6 and 3", " D. 5 and 1", ],
            [r"A. '101'  ", " B. 101 ", " B. 5:101", r" D. 5:'101' ", ],
            [r"A. No output ", r' B."101" ', r' C. "Index out of range"', r"D.  '5' ", ],
        ]
        exp_test_1 = Image.open("ex_hard_1.PNG")
        exp_test_1 = exp_test_1.resize((556, 59), Image.ANTIALIAS)
        exp_test_1 = ImageTk.PhotoImage(exp_test_1)

        exp_test_2 = Image.open("ex_hard_2.PNG")
        exp_test_2 = exp_test_2.resize((492, 59), Image.ANTIALIAS)
        exp_test_2 = ImageTk.PhotoImage(exp_test_2)

        exp_test_3 = Image.open("ex_hard_3.PNG")
        exp_test_3 = exp_test_3.resize((491, 79), Image.ANTIALIAS)
        exp_test_3 = ImageTk.PhotoImage(exp_test_3)

        exp_test_4 = Image.open("ex_hard_4.PNG")
        exp_test_4 = exp_test_4.resize((483, 55), Image.ANTIALIAS)
        exp_test_4 = ImageTk.PhotoImage(exp_test_4)

        exp_test_5 = Image.open("ex_hard_5.PNG")
        exp_test_5 = exp_test_5.resize((531, 126), Image.ANTIALIAS)
        exp_test_5 = ImageTk.PhotoImage(exp_test_5)

        img_list_exep = [exp_test_1, exp_test_2, exp_test_3, exp_test_4, exp_test_5]
        answers_exep = [0, 0, 0, 0, 0]

        Label(excep_test, text="Proficiency Test for Exceptions Module", font=("Helvetica", 18)).pack()

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        l_image = Label(excep_test, image=logo)
        l_image.image = logo
        l_image.pack()

        lblquestion_exep = Label(excep_test, text=questions_exep_test[indexes_excep[0]], font=("16"),
                                 justify="center", wraplength=400, )
        lblquestion_exep.pack()

        lblimage_exep = Label(excep_test, image=exp_test_1)
        lblimage_exep.pack()

        radio_var_exep = IntVar()
        radio_var_exep.set(-1)

        r1_exep = Radiobutton(excep_test, text=answer_choice_exep_test[indexes_excep[0]][0], font=("12"),
                              variable=radio_var_exep, value=0)
        r1_exep.pack()

        r2_exep = Radiobutton(excep_test, text=answer_choice_exep_test[indexes_excep[0]][1], font=("12"),
                              variable=radio_var_exep, value=1)
        r2_exep.pack()

        r3_exep = Radiobutton(excep_test, text=answer_choice_exep_test[indexes_excep[0]][2], font=("12"),
                              variable=radio_var_exep, value=2)
        r3_exep.pack()

        r4_exep = Radiobutton(excep_test, text=answer_choice_exep_test[indexes_excep[0]][3], font=("12"),
                              variable=radio_var_exep, value=3)
        r4_exep.pack()

        pques_exep_b = Button(excep_test, text="Submit!", command=selected_exep_test)
        pques_exep_b.pack()


def submit_pques1_ex():
    x = radio_var_pques_ex.get()
    if x == 2:
        Label(lbl_questions_excep, text="Correct", fg="green").pack()
        pques_b_ex["state"] = "disabled"
        pques_2_ex()
    elif x == 0 or x == 1 or x == 3:
        Label(lbl_questions_excep, text="There is a syntax error", fg="red").pack()


def pques_2_ex():
    Label(lbl_questions_excep,
          text="""Determine the result of this code""", font=("Helvetica", "13")).pack()

    pques_2_exp = Image.open("pques_ex_2.png")
    pques_2_exp = pques_2_exp.resize((475, 189), Image.ANTIALIAS)
    pques_2_exp = ImageTk.PhotoImage(pques_2_exp)

    pques_2_ex_i = Label(lbl_questions_excep, image=pques_2_exp)
    pques_2_ex_i.image = pques_2_exp
    pques_2_ex_i.pack()
    global radio_var_2_str
    radio_var_2_str = IntVar()
    radio_var_2_str.set(-1)
    radio1_2 = Radiobutton(lbl_questions_excep, text=r' "You are 2 years old"', font=("12"), variable=radio_var_2_str,
                           value=0)
    radio1_2.pack()

    radio2_2 = Radiobutton(lbl_questions_excep, text=r'Wrong variable name', font=("12"), variable=radio_var_2_str,
                           value=1)
    radio2_2.pack()

    radio3_2 = Radiobutton(lbl_questions_excep, text=r'"You are "2" years old"', font=("12"), variable=radio_var_2_str,
                           value=2)
    radio3_2.pack()

    radio4_2 = Radiobutton(lbl_questions_excep, text='"That\'s not a number"', font=("12"), variable=radio_var_2_str,
                           value=3)
    radio4_2.pack()

    global pques_exp_2
    pques_exp_2 = Button(lbl_questions_excep, text="Submit!", command=submit_2_ex)
    pques_exp_2.pack()


def submit_2_ex():
    x = radio_var_2_str.get()
    if x == 3:
        Label(lbl_questions_excep, text="Correct\n You are ready for your Proficiency Test", fg="green").pack()
        pques_exp_2["state"] = "disabled"
        test_str_b = Button(lbl_questions_excep, text="Proceed to Test", command=test_exep)
        test_str_b.pack()

    elif x == 0 or x == 1 or x == 2:
        Label(lbl_questions_excep, text="Wrong answer\n Remember data types", fg="red").pack()


def start_exceptions_module():
    global excep
    excep = Toplevel(screen)
    excep.geometry("1280x720")
    excep.iconbitmap('icon.ico')
    Label(excep, text="Welcome " + username1.title() + " to your Exceptions, Testing and Comprehensions module Lesson!",
          font=("Helvetica", "13", "bold")).pack()

    window = ScrolledFrame(excep)
    window.pack(expand=True, fill='both')

    lbl_excep = LabelFrame(window.inner)
    lbl_excep.pack()

    Label(lbl_excep, text="""List comprehension is efficient way incorporating for loops and lists. It is a feature in python 
that has many uses. For example we want to create a list of the first 10 multiples of 2 """, font=("13")).pack()

    exep_1 = Image.open("ex_1.PNG")
    exep_1 = exep_1.resize((395, 158), Image.ANTIALIAS)
    exep_1 = ImageTk.PhotoImage(exep_1)

    exep_1_i = Label(lbl_excep, image=exep_1)
    exep_1_i.image = exep_1
    exep_1_i.pack()

    Label(lbl_excep, text="The main purpose of using list comprehension is making your code more efficient",
          font=("13")).pack()

    exep_2 = Image.open("ex_2.PNG")
    exep_2 = exep_2.resize((365, 99), Image.ANTIALIAS)
    exep_2 = ImageTk.PhotoImage(exep_2)

    exep_2_i = Label(lbl_excep, image=exep_2)
    exep_2_i.image = exep_2
    exep_2_i.pack()

    Label(lbl_excep,
          text="Both will yield the same result but List comprehension is more shorter.\n\nYou can also add if statements to filter out your results.",
          font=("13")).pack()

    exep_3 = Image.open("ex_3.PNG")
    exep_3 = exep_3.resize((483, 99), Image.ANTIALIAS)
    exep_3 = ImageTk.PhotoImage(exep_3)

    exep_3_i = Label(lbl_excep, image=exep_3)
    exep_3_i.image = exep_3
    exep_3_i.pack()
    Label(lbl_excep, text=""" \n\n""", font=("20")).pack()

    lbl_excep_testing = LabelFrame(lbl_excep, borderwidth=5, bg="black")
    lbl_excep_testing.pack()

    Label(lbl_excep_testing, text=""" TESTING """, font=("20")).pack()

    Label(lbl_excep,
          text="""You may encounter an error while creating your code. Logical error is an error that sill runs the program\n but yields the wrong result. Syntax error happens when you misused a function""",
          font=("13")).pack()

    exep_4 = Image.open("ex_4.PNG")
    exep_4 = exep_4.resize((750, 169), Image.ANTIALIAS)
    exep_4 = ImageTk.PhotoImage(exep_4)

    exep_4_i = Label(lbl_excep, image=exep_4)
    exep_4_i.image = exep_4
    exep_4_i.pack()

    Label(lbl_excep,
          text="""Always check your function to avoid syntax error. Here there is no parenthesis in the print function.""",
          font=("13")).pack()
    Label(lbl_excep,
          text="""\n\nThis code has a logical error because you used a different variable""",
          font=("13")).pack()

    exep_5 = Image.open("ex_5.PNG")
    exep_5 = exep_5.resize((96, 123), Image.ANTIALIAS)
    exep_5 = ImageTk.PhotoImage(exep_5)

    exep_5_i = Label(lbl_excep, image=exep_5)
    exep_5_i.image = exep_5
    exep_5_i.pack()

    lbl_excep_Exceptions = LabelFrame(lbl_excep, borderwidth=5, bg="black")
    lbl_excep_Exceptions.pack()

    Label(lbl_excep_Exceptions, text=""" EXCEPTIONS """, font=("20")).pack()

    Label(lbl_excep,
          text="""\nBecause of errors your code may stop working. A way to handle this is using error handling.Error handling 
          handles specific error conditions to make your code still run even with an error present.\n""",
          anchor=W, font=("13")).pack()

    exep_6 = Image.open("ex_6.PNG")
    exep_6 = exep_6.resize((613, 187), Image.ANTIALIAS)
    exep_6 = ImageTk.PhotoImage(exep_6)

    exep_6_i = Label(lbl_excep, image=exep_6)
    exep_6_i.image = exep_6
    exep_6_i.pack()

    Label(lbl_excep,
          text="""\nTry function execute the statements and if there is an error encountered 
except function will handle the error and execute the statements below\n\n\n""",
          anchor=W, font=("13")).pack()

    exep_7 = Image.open("ex_7.PNG")
    exep_7 = exep_7.resize((432, 205), Image.ANTIALIAS)
    exep_7 = ImageTk.PhotoImage(exep_7)

    exep_7_i = Label(lbl_excep, image=exep_7)
    exep_7_i.image = exep_7
    exep_7_i.pack()

    Label(lbl_excep,
          text="Because there is no file 'unknownfile.txt', it executes the except function and prints 'Unknown "
               "\nexception occurred.'Exceptions are useful for making your program user-friendly by showing what the "
               "\nerror encountered is rather than your program stopping or crashing\n\n\n", font=("13")).pack()

    Label(lbl_excep,
          text="finally is a clause that will run wheter or not try produces an exception.\n", font=("13")).pack()

    exep_8 = Image.open("ex_8.PNG")
    exep_8 = exep_8.resize((360, 171), Image.ANTIALIAS)
    exep_8 = ImageTk.PhotoImage(exep_8)

    exep_8_i = Label(lbl_excep, image=exep_8)
    exep_8_i.image = exep_8
    exep_8_i.pack()

    Label(lbl_excep,
          text="""\n\nPractice Questions""",
          anchor=W, font=("20")).pack()
    global lbl_questions_excep
    lbl_questions_excep = LabelFrame(lbl_excep, padx=80, pady=80)
    lbl_questions_excep.pack()

    Label(lbl_questions_excep,
          text="""Determine the error of this code""", font=("13")).pack()

    pques_1_ex = Image.open("pques_ex_1.png")
    pques_1_ex = pques_1_ex.resize((413, 103), Image.ANTIALIAS)
    pques_1_ex = ImageTk.PhotoImage(pques_1_ex)

    pques_1_ex_i = Label(lbl_questions_excep, image=pques_1_ex)
    pques_1_ex_i.image = pques_1_ex
    pques_1_ex_i.pack()

    global radio_var_pques_ex
    radio_var_pques_ex = IntVar()
    radio_var_pques_ex.set(-1)
    radio1_1 = Radiobutton(lbl_questions_excep, text="There is no print", font=("12"), variable=radio_var_pques_ex,
                           value=0)
    radio1_1.pack()

    radio2_1 = Radiobutton(lbl_questions_excep, text="Wrong variable name", font=("12"), variable=radio_var_pques_ex,
                           value=1)
    radio2_1.pack()

    radio3_1 = Radiobutton(lbl_questions_excep, text="No function math.round ", font=("12"),
                           variable=radio_var_pques_ex, value=2)
    radio3_1.pack()

    radio4_1 = Radiobutton(lbl_questions_excep, text="Wrong data type", font=("12"), variable=radio_var_pques_ex,
                           value=3)
    radio4_1.pack()

    global pques_b_ex
    pques_b_ex = Button(lbl_questions_excep, text="Submit!", command=submit_pques1_ex)
    pques_b_ex.pack()


def submit_2_gui():
    x = radio_var_2_gui.get()
    if x == 2:
        Label(lbl_questions_gui, text="Correct\n You are ready for your Proficiency Test", fg="green").pack()
        pques_gui_2["state"] = "disabled"
        test_gui_b = Button(lbl_questions_gui, text="Proceed to Test", command=test_gui)
        test_gui_b.pack()

    elif x == 0 or x == 1 or x == 3:
        Label(lbl_questions_gui, text="Wrong answer\n Remember data types", fg="red").pack()


def pques_2_gui():
    Label(lbl_questions_gui,
          text="""How do you clear user input in entry""", font=("13")).pack()

    global radio_var_2_gui
    radio_var_2_gui = IntVar()
    radio_var_2_gui.set(-1)
    radio1_2 = Radiobutton(lbl_questions_gui, text=r' (0, END)', font=("12"), variable=radio_var_2_gui,
                           value=0)
    radio1_2.pack()

    radio2_2 = Radiobutton(lbl_questions_gui, text=r'delete(0, END)', font=("12"), variable=radio_var_2_gui,
                           value=1)
    radio2_2.pack()

    radio3_2 = Radiobutton(lbl_questions_gui, text=r'"entry.delete(0, END)"', font=("12"), variable=radio_var_2_gui,
                           value=2)
    radio3_2.pack()

    radio4_2 = Radiobutton(lbl_questions_gui, text='"BKSP"', font=("12"), variable=radio_var_2_gui,
                           value=3)
    radio4_2.pack()

    global pques_gui_2
    pques_gui_2 = Button(lbl_questions_gui, text="Submit!", command=submit_2_gui)
    pques_gui_2.pack()


def submit_pques1_gui():
    x = radio_var_pques_gui.get()
    if x == 0:
        Label(lbl_questions_gui, text="Correct", fg="green").pack()
        pques_b_gui["state"] = "disabled"
        pques_2_gui()
    elif x == 2 or x == 1 or x == 3:
        Label(lbl_questions_gui, text="There are 3 things!", fg="red").pack()


def start_gui_module():
    global gui
    gui = Toplevel(screen)
    gui.geometry("1280x720")
    gui.iconbitmap('icon.ico')
    Label(gui, text="Welcome " + username1.title() + " to your GUI module Lesson!",
          font=("Helvetica", "13", "bold")).pack()

    window = ScrolledFrame(gui)
    window.pack(expand=True, fill='both')

    lbl_gui = LabelFrame(window.inner)
    lbl_gui.pack()

    Label(lbl_gui, text="""\n GUI means graphical user interface which is a system of interactive visual components 
        for computer software. GUI displays information and represents actions that can be done by the user. GUIs can 
        help make your program more user-friendly that text only.\n\n One of the most common interfaces to create GUI is 
        tkinter. Tkinter is a module that is used to create gui in python. To use tkinter you must first import it""",
          font=("13")).pack()

    grui_1 = Image.open("gui_1.PNG")
    grui_1 = grui_1.resize((210, 36), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_gui, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_gui, text="""\n\nThe basic components of a tkinter program is to import tkinter, 
    create your root window and create the mainloop for your root widget.
    A mainloop will loop the program until you close the program.""",
          font=("13")).pack()

    grui_2 = Image.open("gui_2.PNG")
    grui_2 = grui_2.resize((223, 125), Image.ANTIALIAS)
    grui_2 = ImageTk.PhotoImage(grui_2)

    grui_2_i = Label(lbl_gui, image=grui_2)
    grui_2_i.image = grui_2
    grui_2_i.pack()
    Label(lbl_gui, text="").pack()

    Label(lbl_gui, text="""To display content in tkinter, there are two steps. To initialize 
    the content and to display it. To initialize conent you will use Label Widget
    Label widget displays text and images. To display your label widget you will either use
    pack or grid method. Pack method packs the widget in the middle of the screen, while grid 
    uses grid and column to display to the screen.""",
          font=("13")).pack()
    grui_12 = Image.open("gui_12.PNG")
    grui_12 = grui_12.resize((559, 225), Image.ANTIALIAS)
    grui_12 = ImageTk.PhotoImage(grui_12)

    grui_12_i = Label(lbl_gui, image=grui_12)
    grui_12_i.image = grui_12
    grui_12_i.pack()

    grui_3 = Image.open("gui_3.PNG")
    grui_3 = grui_3.resize((154, 70), Image.ANTIALIAS)
    grui_3 = ImageTk.PhotoImage(grui_3)

    grui_3_i = Label(lbl_gui, image=grui_3)
    grui_3_i.image = grui_3
    grui_3_i.pack()

    Label(lbl_gui, text="""You can also add frames to hold your content. To add Frame use Labelframe widget. 
        You can also add external padding by using padx or pady""",
          font=("13")).pack()

    grui_4 = Image.open("gui_4.PNG")
    grui_4 = grui_4.resize((412, 225), Image.ANTIALIAS)
    grui_4 = ImageTk.PhotoImage(grui_4)

    grui_4_i = Label(lbl_gui, image=grui_4)
    grui_4_i.image = grui_4
    grui_4_i.pack()

    grui_5 = Image.open("gui_5.PNG")
    grui_5 = grui_5.resize((156, 114), Image.ANTIALIAS)
    grui_5 = ImageTk.PhotoImage(grui_5)

    grui_5_i = Label(lbl_gui, image=grui_5)
    grui_5_i.image = grui_5
    grui_5_i.pack()

    Label(lbl_gui, text="You can also change the title and the size of a window.",
          font=("13")).pack()

    grui_9 = Image.open("gui_11.PNG")
    grui_9 = grui_9.resize((221, 124), Image.ANTIALIAS)
    grui_9 = ImageTk.PhotoImage(grui_9)

    grui_9_i = Label(lbl_gui, image=grui_9)
    grui_9_i.image = grui_9
    grui_9_i.pack()

    grui_10 = Image.open("gui_10.PNG")
    grui_10 = grui_10.resize((253, 167), Image.ANTIALIAS)
    grui_10 = ImageTk.PhotoImage(grui_10)

    grui_10_i = Label(lbl_gui, image=grui_10)
    grui_10_i.image = grui_10
    grui_10_i.pack()

    Label(lbl_gui, text="""Buttons are great tools to make your program more user friendly and interactive.
    Buttons can have commands which execute the function when the button is pressed"
    Remember that when you write your command DO NOT ADD PARENTHESIS.""",
          font=("13")).pack()

    grui_6 = Image.open("gui_6.PNG")
    grui_6 = grui_6.resize((706, 208), Image.ANTIALIAS)
    grui_6 = ImageTk.PhotoImage(grui_6)

    grui_6_i = Label(lbl_gui, image=grui_6)
    grui_6_i.image = grui_6
    grui_6_i.pack()

    grui_7 = Image.open("gui_7.PNG")
    grui_7 = grui_7.resize((253, 168), Image.ANTIALIAS)
    grui_7 = ImageTk.PhotoImage(grui_7)

    grui_7_i = Label(lbl_gui, image=grui_7)
    grui_7_i.image = grui_7
    grui_7_i.pack()

    Label(lbl_gui, text="""Entry widget is useful if you want to obtain information about the user.
    To create an entry widget you need to initiate a string variable to store the user
    input. Create an entry widget using the string variable as the text variable.
    To get the data input by the user use .get function. After submitting an input, you should 
    clear the input field to make the interface cleaner. Use delete function to clear the data field""",
          font=("13")).pack()
    grui_8 = Image.open("gui_8.PNG")
    grui_8 = grui_8.resize((702, 627), Image.ANTIALIAS)
    grui_8 = ImageTk.PhotoImage(grui_8)

    grui_8_i = Label(lbl_gui, image=grui_8)
    grui_8_i.image = grui_8
    grui_8_i.pack()

    grui_9 = Image.open("gui_9.PNG")
    grui_9 = grui_9.resize((256, 294), Image.ANTIALIAS)
    grui_9 = ImageTk.PhotoImage(grui_9)

    grui_9_i = Label(lbl_gui, image=grui_9)
    grui_9_i.image = grui_9
    grui_9_i.pack()

    Label(lbl_gui,
          text="""\n\nPractice Questions""",
          anchor=W, font=("20")).pack()
    global lbl_questions_gui
    lbl_questions_gui = LabelFrame(lbl_gui, padx=80, pady=80)
    lbl_questions_gui.pack()

    Label(lbl_questions_gui,
          text="""What is the first thing you have to do when using tkinter?""", font=("13")).pack()

    global radio_var_pques_gui
    radio_var_pques_gui = IntVar()
    radio_var_pques_gui.set(-1)
    radio1_1 = Radiobutton(lbl_questions_gui, text="Import tkinter module,create root widget and mainloop ",
                           font=("12"), variable=radio_var_pques_gui,
                           value=0)
    radio1_1.pack()

    radio2_1 = Radiobutton(lbl_questions_gui, text="Intialize Load order", font=("12"),
                           variable=radio_var_pques_gui,
                           value=1)
    radio2_1.pack()

    radio3_1 = Radiobutton(lbl_questions_gui, text="Import tkinter module", font=("12"),
                           variable=radio_var_pques_gui, value=2)
    radio3_1.pack()

    radio4_1 = Radiobutton(lbl_questions_gui, text="Create a Label", font=("12"), variable=radio_var_pques_gui,
                           value=3)
    radio4_1.pack()

    global pques_b_gui
    pques_b_gui = Button(lbl_questions_gui, text="Submit!", command=submit_pques1_gui)
    pques_b_gui.pack()


class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_space = text_widget

    def write(self, string):
        self.text_space.insert('end', string)
        self.text_space.see('end')


def buttonCallback():
    global outputWindow

    code = codeEditor.get('1.0', END + '-1c')

    stdout = sys.stdout
    stderr = sys.stderr

    outputWindow.delete('1.0', END)

    sys.stdout = StdoutRedirector(outputWindow)
    sys.stderr = StdoutRedirector(outputWindow)

    interp = InteractiveInterpreter()
    interp.runcode(code)

    sys.stdout = stdout
    sys.stderr = stderr


def open_ide():
    global outputWindow, codeEditor
    ide = Toplevel(screen)
    ide.iconbitmap('icon.ico')
    frame1 = Frame(ide)
    Label(ide, text="IDE", font=("24")).pack()
    frame1.pack(side=TOP, fill=Y)
    Button(ide, text='Run', command=buttonCallback).pack()
    frame2 = Frame(ide)
    frame2.pack(side=BOTTOM, fill=Y)

    codeEditor = Text(frame1)
    codeScroll = Scrollbar(frame1, command=codeEditor.yview)
    codeEditor.configure(yscrollcommand=codeScroll.set)
    codeEditor.pack(side=LEFT)
    codeScroll.pack(side=RIGHT, fill=Y)

    outputWindow = Text(frame2)
    outputScroll = Scrollbar(frame2, command=outputWindow.yview)
    outputWindow.configure(yscrollcommand=outputScroll.set)
    outputWindow.pack(side=LEFT)
    outputScroll.pack(side=RIGHT, fill=Y)


def log_out():
    screen.destroy()
    mscreen()

def change_diff():
    xy = radio_diff.get()
    if xy==0:
        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['mode'] = "easy"


        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()
        if messagebox.showinfo("Restart", "To apply changes the applications will restart"):

            os.execl(sys.executable, sys.executable, *sys.argv)


    elif xy == 1:
        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['mode'] = "medium"

        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()

        if messagebox.showinfo("Restart", "To apply changes the applications will restart"):

            os.execl(sys.executable, sys.executable, *sys.argv)
    elif xy == 2:
        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))

        dicc['mode'] = "hard"

        file = open(username1 + ".txt", "w")
        file.write(str(dicc))
        file.close()

        if messagebox.showinfo("Restart", "To apply changes the applications will restart"):

            os.execl(sys.executable, sys.executable, *sys.argv)

    else:
        print("eror")


def diff():
    global radio_diff,diff
    diff=Toplevel(screen)
    diff.title("Difficulty Change")
    diff.geometry("500x500")
    diff.iconbitmap('icon.ico')

    diff_label=LabelFrame(diff)
    diff_label.pack()

    file1 = open(username1 + ".txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))

    mod = dicc['mode']


    radio_diff = IntVar()
    if mod== "easy":
        radio_diff.set(0)
    elif mod=="medium":
        radio_diff.set(1)
    elif mod=="hard":
        radio_diff.set(1)


    radio1_diff = Radiobutton(diff_label, text='easy', font=("12"), variable=radio_diff, value=0)
    radio1_diff.pack()

    radio2_diff = Radiobutton(diff_label, text="medium" ,font=("12"), variable=radio_diff, value=1)
    radio2_diff.pack()

    radio3_diff = Radiobutton(diff_label, text="hard", font=("12"), variable=radio_diff, value=2)
    radio3_diff.pack()

    Button(diff_label,text="Change Difficulty",command=change_diff).pack()


def dash():
    global test, username1, bool_button, b_image, f_image, m_image, nump_button, bool_button, seq_b, string_b, dicc_b, exep_b, graph_b,lbl,pgbar
    screen.geometry("1500x1500")
    main_L.destroy()
    frame.destroy()

    menubar = Menu(screen)
    screen.configure(menu=menubar)

    # crete the submenus

    file_menu = Menu(menubar, tearoff=0)
    scores_menu = Menu(menubar)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Difficulty", command=diff)
    file_menu.add_command(label="Log Out", command=log_out)
    file_menu.add_command(label="Exit", command=ask_quit)

    screen.grid_columnconfigure(2, weight=1)
    Label(screen, text="Welcome " + username1.title() + " to your personal Dashboard!\n\n\n",
          font=("Helvetica", "13", "bold")).grid(row=2, column=2)

    # create a menu bar

    lbl = LabelFrame(screen, padx=20, pady=20)
    lbl.grid(row=4, column=2)
    ### create images
    logo = Image.open("logo.png")
    logo = logo.resize((50, 50), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)

    boolean = Image.open("boolean.png")
    boolean = boolean.resize((50, 50), Image.ANTIALIAS)
    boolean = ImageTk.PhotoImage(boolean)

    sequences = Image.open("sequences.png")
    sequences = sequences.resize((50, 50), Image.ANTIALIAS)
    sequences = ImageTk.PhotoImage(sequences)

    string = Image.open("string.png")
    string = string.resize((50, 50), Image.ANTIALIAS)
    string = ImageTk.PhotoImage(string)

    dict = Image.open("dictionary.png")
    dict = dict.resize((50, 50), Image.ANTIALIAS)
    dict = ImageTk.PhotoImage(dict)

    exep = Image.open("exceptions.png")
    exep = exep.resize((50, 50), Image.ANTIALIAS)
    exep = ImageTk.PhotoImage(exep)

    graph_i = Image.open("gui.png")
    graph_i = graph_i.resize((50, 50), Image.ANTIALIAS)
    graph_i = ImageTk.PhotoImage(graph_i)

    func = Image.open("functions.png")
    func = func.resize((50, 50), Image.ANTIALIAS)
    func = ImageTk.PhotoImage(func)

    nump = Image.open("array.png")
    nump = nump.resize((50, 50), Image.ANTIALIAS)
    nump = ImageTk.PhotoImage(nump)

    basic_prog = Image.open("basic prog.png")
    basic_prog = basic_prog.resize((50, 50), Image.ANTIALIAS)
    basic_prog = ImageTk.PhotoImage(basic_prog)

    modle = Image.open("module.png")

    modle = modle.resize((50, 50), Image.ANTIALIAS)
    modle = ImageTk.PhotoImage(modle)

    ### Buttons
    file1 = open(username1 + ".txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))

    l_image = Button(lbl, image=logo, bg="green", command=start_intro_module)
    l_image.image = logo
    l_image.grid(row=5, column=2)

    l_label = Label(lbl, text="Intro to Python").grid(row=7, column=2)

    filler = Label(lbl, text="\t").grid(row=5, column=3)  # filler

    b_image = Button(lbl, image=basic_prog, bg="white", command=start_basic_module)
    b_image.image = basic_prog
    b_image.grid(row=5, column=4)

    if dicc.get("Basic") == "done":
        b_image['bg'] = "green"

    f_label = Label(lbl, text="Basic Programming").grid(row=7, column=4)

    filler = Label(lbl, text="\t").grid(row=5, column=5)  ##filler

    f_image = Button(lbl, image=func, bg="white", command=start_func_module)
    f_image.image = func
    f_image.grid(row=5, column=6)

    if dicc.get("Function") == "done":
        f_image['bg'] = "green"

    if dicc.get("Basic") == "undone":
        f_image['state'] = DISABLED

    s_label = Label(lbl, text="Functions").grid(row=7, column=6)

    filler = Label(lbl, text="\t").grid(row=8, column=2)  ##filler

    m_image = Button(lbl, image=modle, bg="white", command=start_modyul_module)
    m_image.image = modle
    m_image.grid(row=9, column=2)

    if dicc.get("Modules") == "done":
        m_image['bg'] = "green"

    if dicc.get("Function") == "undone":
        m_image['state'] = DISABLED

    st_label = Label(lbl, text="Modules").grid(row=10, column=2)

    filler = Label(lbl, text="\t").grid(row=9, column=3)  ##filler

    nump_button = Button(lbl, image=nump, bg="white", command=start_numpy_module)
    nump_button.image = nump
    nump_button.grid(row=9, column=4)

    if dicc.get("Numpy") == "done":
        nump_button['bg'] = "green"

    if dicc.get("Modules") == "undone":
        nump_button['state'] = DISABLED

    d_label = Label(lbl, text="Numpy").grid(row=10, column=4)

    filler = Label(lbl, text="\t").grid(row=9, column=5)  ##filler

    bool_button = Button(lbl, image=boolean, bg="white", command=start_boolean_module)
    bool_button.image = boolean
    bool_button.grid(row=9, column=6)

    if dicc.get("Boolean") == "done":
        bool_button['bg'] = "green"

    if dicc.get("Numpy") == "undone":
        bool_button['state'] = DISABLED

    l_label = Label(lbl, text="Boolean").grid(row=10, column=6)

    filler = Label(lbl, text="\t").grid(row=11, column=4)  ##filler

    seq_b = Button(lbl, image=sequences, bg="white", command=start_sequence_module)
    seq_b.image = sequences
    seq_b.grid(row=12, column=2)

    if dicc.get("Sequences") == "done":
        seq_b['bg'] = "green"

    if dicc.get("Boolean") == "undone":
        seq_b['state'] = DISABLED

    l_label = Label(lbl, text="Sequences").grid(row=13, column=2)

    string_b = Button(lbl, image=string, bg="white", command=start_strings_module)
    string_b.image = string
    string_b.grid(row=12, column=4)

    if dicc.get("Strings") == "done":
        string_b['bg'] = "green"

    if dicc.get("Sequences") == "undone":
        string_b['state'] = DISABLED

    l_label = Label(lbl, text="Strings").grid(row=13, column=4)

    dicc_b = Button(lbl, image=dict, bg="white", command=start_dfs_module)
    dicc_b.image = dict
    dicc_b.grid(row=12, column=6)

    if dicc.get("Dictionary") == "done":
        dicc_b['bg'] = "green"

    if dicc.get("Strings") == "undone":
        dicc_b['state'] = DISABLED

    l_label = Label(lbl, text="Dictionary").grid(row=13, column=6)

    filler = Label(lbl, text="\t").grid(row=14, column=4)  ##filler

    exep_b = Button(lbl, image=exep, bg="white", command=start_exceptions_module)
    exep_b.image = exep
    exep_b.grid(row=15, column=2)

    if dicc.get("Exceptions") == "done":
        exep_b['bg'] = "green"

    if dicc.get("Dictionary") == "undone":
        exep_b['state'] = DISABLED

    l_label = Label(lbl, text="Exceptions").grid(row=16, column=2)

    graph_b = Button(lbl, image=graph_i, bg="white", command=start_gui_module)
    graph_b.image = graph_i
    graph_b.grid(row=15, column=4)

    if dicc.get("Gui") == "done":
        graph_b['bg'] = "green"

    if dicc.get("Exceptions") == "undone":
        graph_b['state'] = DISABLED

    l_label = Label(lbl, text="GUI").grid(row=16, column=4)

    filler = Label(lbl, text="\t").grid(row=17, column=4)  ##filler
    filler = Label(lbl, text="Complete your lessons to increase your Progress Bar!").grid(row=18, column=4)  ##filler

    pgbar = Progressbar(lbl, length=500, orient=HORIZONTAL, maximum=11, value=0)
    pgbar.grid(row=19, column=4)

    filler = Label(lbl, text="\t").grid(row=20, column=4)

    lst = []
    for key in dicc:
        lst.append(dicc[key])

    pgbar['value']= lst.count("done")

    filler = Label(lbl, text="\t").grid(row=21, column=4)  ##filler

    ide_b =Button(lbl, text="Open IDE",command=open_ide)
    ide_b.grid(row=22, column=4)

    filler = Label(lbl, text="\t").grid(row=23, column=4)  ##filler



    

    if (dicc.get('Basic') == "done") & (dicc.get('Function') == 'done') & (dicc.get('Modules') == 'done') & \
            (dicc.get('Numpy') == 'done') & (dicc.get('Boolean') == 'done') & (dicc.get('Sequences') == 'done') & \
            (dicc.get('Strings') == 'done') & (dicc.get('Dictionary') == 'done') & (dicc.get('Exceptions') == 'done') & \
            (dicc.get('Gui') == 'done'):
        final_button_act()



def final_button_act():
    global passed_b
    file1 = open(username1 + ".txt", "r")
    verify = file1.read()
    dicc = ast.literal_eval((verify))

    passed_i = Image.open("passed.png")
    passed_i = passed_i.resize((50, 50), Image.ANTIALIAS)
    passed_i = ImageTk.PhotoImage(passed_i)

    passed_b = Button(lbl, image=passed_i, bg="white", command=start_final_test)
    passed_b.image = passed_i
    passed_b.grid(row=24, column=4)

    filler = Label(lbl, text="FINAL TEST").grid(row=25, column=4)  ##filler


    if dicc.get("Final") == "done":
        passed_b['bg'] = "green"

def buttonCallback5():
    global outputWindow5,codeEditor5
    input = outputWindow5.get("1.0", END)




    code = codeEditor5.get('1.0', END + '-1c')

    stdout = sys.stdout
    stderr = sys.stderr

    outputWindow5.delete('1.0', END)

    sys.stdout = StdoutRedirector(outputWindow5)
    sys.stderr = StdoutRedirector(outputWindow5)

    interp = InteractiveInterpreter()
    interp.runcode(code)

    sys.stdout = stdout
    sys.stderr = stderr

def buttonCallback4():
    global outputWindow4,codeEditor4
    input = outputWindow4.get("1.0", END)




    code = codeEditor4.get('1.0', END + '-1c')

    stdout = sys.stdout
    stderr = sys.stderr

    outputWindow4.delete('1.0', END)

    sys.stdout = StdoutRedirector(outputWindow4)
    sys.stderr = StdoutRedirector(outputWindow4)

    interp = InteractiveInterpreter()
    interp.runcode(code)

    sys.stdout = stdout
    sys.stderr = stderr

def buttonCallback3():
    global outputWindow3,codeEditor3
    input = outputWindow3.get("1.0", END)




    code = codeEditor3.get('1.0', END + '-1c')

    stdout = sys.stdout
    stderr = sys.stderr

    outputWindow3.delete('1.0', END)

    sys.stdout = StdoutRedirector(outputWindow3)
    sys.stderr = StdoutRedirector(outputWindow3)

    interp = InteractiveInterpreter()
    interp.runcode(code)

    sys.stdout = stdout
    sys.stderr = stderr

def buttonCallback2():
    global outputWindow2,codeEditor2
    input = outputWindow2.get("1.0", END)




    code = codeEditor2.get('1.0', END + '-1c')

    stdout = sys.stdout
    stderr = sys.stderr

    outputWindow2.delete('1.0', END)

    sys.stdout = StdoutRedirector(outputWindow2)
    sys.stderr = StdoutRedirector(outputWindow2)

    interp = InteractiveInterpreter()
    interp.runcode(code)

    sys.stdout = stdout
    sys.stderr = stderr
def buttonCallback():
    global outputWindow,input,codeEditor
    input = outputWindow.get("1.0", END)




    code = codeEditor.get('1.0', END + '-1c')

    stdout = sys.stdout
    stderr = sys.stderr

    outputWindow.delete('1.0', END)

    sys.stdout = StdoutRedirector(outputWindow)
    sys.stderr = StdoutRedirector(outputWindow)

    interp = InteractiveInterpreter()
    interp.runcode(code)

    sys.stdout = stdout
    sys.stderr = stderr

class ScrolledFrame(Frame):

    def __init__(self, parent, vertical=True, horizontal=False):
        super().__init__(parent)

        # canvas for inner frame
        self._canvas = Canvas(self)
        self._canvas.grid(row=0, column=0, sticky='news')  # changed

        # create right scrollbar and connect to canvas Y
        self._vertical_bar = Scrollbar(self, orient='vertical', command=self._canvas.yview)
        if vertical:
            self._vertical_bar.grid(row=0, column=1, sticky='ns')
        self._canvas.configure(yscrollcommand=self._vertical_bar.set)

        # create bottom scrollbar and connect to canvas X
        self._horizontal_bar = Scrollbar(self, orient='horizontal', command=self._canvas.xview)
        if horizontal:
            self._horizontal_bar.grid(row=1, column=0, sticky='we')
        self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

        # inner frame for widgets
        self.inner = Frame(self._canvas)
        self._window = self._canvas.create_window((0, 0), window=self.inner, anchor='nw')

        # autoresize inner frame
        self.columnconfigure(0, weight=1)  # changed
        self.rowconfigure(0, weight=1)  # changed

        # resize when configure changed
        self.inner.bind('<Configure>', self.resize)
        self._canvas.bind('<Configure>', self.frame_width)

    def frame_width(self, event):
        # resize inner frame to canvas size
        canvas_width = event.width
        self._canvas.itemconfig(self._window, width=canvas_width)

    def resize(self, event=None):
        self._canvas.configure(scrollregion=self._canvas.bbox('all'))

def end():
    final_test.destroy()
def check_answer5():
    code = codeEditor5.get('1.0', END + '-1c')

    try:
        save_stdout = sys.stdout  # save old value so we can restore it later
        sys.stdout = open('answers.txt', 'w')
        exec(code, {})
        sys.stdout.close()
        sys.stdout = save_stdout


    except:
        messagebox.showwarning("Error", "Error in code")
    file1 = open("answers.txt", "r")
    verify = file1.read()
    if ("5" in verify) & ("7" in  verify):
        if messagebox.showinfo("Correct", "You have finished the whole program!\n Congratulations!"):
            file1 = open(username1 + ".txt", "r")
            verify = file1.read()
            dicc = ast.literal_eval((verify))

            dicc['Final'] = "done"


            file = open(username1 + ".txt", "w")
            file.write(str(dicc))
            file.close()

            passed_b['bg']="green"
            run_b5["state"] = DISABLED
            chk_b5["state"] = DISABLED
            end()
    else:
        messagebox.showwarning("Wrong!!", "Wrong output")



def final_ques5():
    global run_b5, chk_b5, codeEditor5, outputWindow5

    lbl_final_test5 = LabelFrame(lbl_final_test)
    lbl_final_test5.pack()

    lbl_question_final = Label(lbl_final_test5,
                               text="""Given 

first_dictionary = {"My": 2,"first": 5,"Dictionary": 10,"Yes!": 4, "Yes!": 7}

Create a program that would get the int values, and only return values with a modulo that is equal to one""",
                               font="24").pack()

    frame1_5 = Frame(lbl_final_test5)
    frame1_5.pack(side=TOP, fill=Y)
    run_b5 = Button(lbl_final_test5, text='Run', command=buttonCallback5)
    run_b5.pack()
    frame2_5 = Frame(lbl_final_test5)
    frame2_5.pack(side=BOTTOM, fill=Y)

    codeEditor5 = Text(frame1_5, height=10)
    codeScroll = Scrollbar(frame1_5, command=codeEditor5.yview)
    codeEditor5.configure(yscrollcommand=codeScroll.set)
    codeEditor5.pack(side=LEFT)
    codeScroll.pack(side=RIGHT, fill=Y)

    outputWindow5 = Text(frame2_5, height=10)
    outputScroll = Scrollbar(frame2_5, command=outputWindow5.yview)
    outputWindow5.configure(yscrollcommand=outputScroll.set)
    outputWindow5.pack(side=LEFT)
    outputScroll.pack(side=RIGHT, fill=Y)

    chk_b5 = Button(lbl_final_test5, text='Check answer', command=check_answer5)
    chk_b5.pack()



def check_answer4():
    code = codeEditor4.get('1.0', END + '-1c')

    try:
        save_stdout = sys.stdout  # save old value so we can restore it later
        sys.stdout = open('answers.txt', 'w')
        exec(code, {})
        sys.stdout.close()
        sys.stdout = save_stdout


    except:
        messagebox.showwarning("Error", "Error in code")
    file1 = open("answers.txt", "r")
    verify = file1.read()
    if ("[12, 4, 3]" in verify) & ( "[7, 5, 8]" in verify):
        if messagebox.showinfo("Correct", "Correct Answer!"):
            run_b4["state"] = DISABLED
            chk_b4["state"] = DISABLED
            final_ques5()
    else:
        messagebox.showwarning("Wrong!!", "Wrong output")

def final_ques4():
    global run_b4, chk_b4, codeEditor4, outputWindow4

    lbl_final_test4 = LabelFrame(lbl_final_test)
    lbl_final_test4.pack()

    lbl_question_final = Label(lbl_final_test4,
                               text="""Transposing is the interchanging of rows and columns.

Meaning if a matrix has 2 rows and 3 columns, it will be converted to 3 rows and 2 columns
Given:
[[12,7],
[4 ,5],
[3 ,8]]

WITHOUT using NumPy, create a program 
that would transpose this matrix.""",
                               font="24").pack()

    frame1_4 = Frame(lbl_final_test4)
    frame1_4.pack(side=TOP, fill=Y)
    run_b4 = Button(lbl_final_test4, text='Run', command=buttonCallback4)
    run_b4.pack()
    frame2_4 = Frame(lbl_final_test4)
    frame2_4.pack(side=BOTTOM, fill=Y)

    codeEditor4 = Text(frame1_4, height=10)
    codeScroll = Scrollbar(frame1_4, command=codeEditor4.yview)
    codeEditor4.configure(yscrollcommand=codeScroll.set)
    codeEditor4.pack(side=LEFT)
    codeScroll.pack(side=RIGHT, fill=Y)

    outputWindow4 = Text(frame2_4, height=10)
    outputScroll = Scrollbar(frame2_4, command=outputWindow4.yview)
    outputWindow4.configure(yscrollcommand=outputScroll.set)
    outputWindow4.pack(side=LEFT)
    outputScroll.pack(side=RIGHT, fill=Y)

    chk_b4 = Button(lbl_final_test4, text='Check answer', command=check_answer4)
    chk_b4.pack()




def check_answer3():
    code = codeEditor3.get('1.0', END + '-1c')

    try:
        save_stdout = sys.stdout  # save old value so we can restore it later
        sys.stdout = open('answers.txt', 'w')
        exec(code, {})
        sys.stdout.close()
        sys.stdout = save_stdout


    except:
        messagebox.showwarning("Error", "Error in code")
    file1 = open("answers.txt", "r")
    verify = file1.read()
    if "160" in verify:
        if messagebox.showinfo("Correct", "Correct Answer!"):
            run_b3["state"] = DISABLED
            chk_b3["state"] = DISABLED
            final_ques4()
    else:
        messagebox.showwarning("Wrong!!", "Wrong output")

def final_ques3():
    global run_b3,chk_b3,codeEditor3,outputWindow3


    lbl_final_test3 = LabelFrame(lbl_final_test)
    lbl_final_test3.pack()

    lbl_question_final = Label(lbl_final_test3,
                               text="""ASCII character encoding provides 
a standard way to represent characters using numeric codes.

Using the word "ATLAS"

Create a program when given a word, will get the ASCII of each letter, 
then only return the summation of the even ASCII values.""",
                               font="24").pack()

    frame1_3 = Frame(lbl_final_test3)
    frame1_3.pack(side=TOP, fill=Y)
    run_b3= Button(lbl_final_test3, text='Run', command=buttonCallback3)
    run_b3.pack()
    frame2_3 = Frame(lbl_final_test3)
    frame2_3.pack(side=BOTTOM, fill=Y)

    codeEditor3 = Text(frame1_3, height=10)
    codeScroll = Scrollbar(frame1_3, command=codeEditor3.yview)
    codeEditor3.configure(yscrollcommand=codeScroll.set)
    codeEditor3.pack(side=LEFT)
    codeScroll.pack(side=RIGHT, fill=Y)

    outputWindow3 = Text(frame2_3, height=10)
    outputScroll = Scrollbar(frame2_3, command=outputWindow3.yview)
    outputWindow3.configure(yscrollcommand=outputScroll.set)
    outputWindow3.pack(side=LEFT)
    outputScroll.pack(side=RIGHT, fill=Y)

    chk_b3 = Button(lbl_final_test3, text='Check answer', command=check_answer3)
    chk_b3.pack()

def check_answer2():
    code = codeEditor2.get('1.0', END + '-1c')

    try:
        save_stdout = sys.stdout  # save old value so we can restore it later
        sys.stdout = open('answers.txt', 'w')
        exec(code, {})
        sys.stdout.close()
        sys.stdout = save_stdout


    except:
        messagebox.showwarning("Error", "Error in code")
    file1 = open("answers.txt", "r")
    verify = file1.read()
    if "11" in verify:
        if messagebox.showinfo("Correct", "Correct Answer!"):
            run_b2["state"] = DISABLED
            chk_b2["state"] = DISABLED
            final_ques3()
    else:
        messagebox.showwarning("Wrong!!", "Wrong output")

def final_ques2():
    global run_b2,chk_b2,codeEditor2,outputWindow2


    lbl_final_test2 = LabelFrame(lbl_final_test)
    lbl_final_test2.pack()

    lbl_question_final = Label(lbl_final_test2,
                               text="Multiplicative Persistence. Multiply all the digits of a number by each other\n, "
                                    "repeating with the product until a single digit is obtained. Find the \n"
                                    "multiplicative persistence of 277777788888899 ",
                               font="24").pack()

    frame1_2 = Frame(lbl_final_test2)
    frame1_2.pack(side=TOP, fill=Y)
    run_b2= Button(lbl_final_test2, text='Run', command=buttonCallback2)
    run_b2.pack()
    frame2_2 = Frame(lbl_final_test2)
    frame2_2.pack(side=BOTTOM, fill=Y)

    codeEditor2 = Text(frame1_2, height=10)
    codeScroll = Scrollbar(frame1_2, command=codeEditor2.yview)
    codeEditor2.configure(yscrollcommand=codeScroll.set)
    codeEditor2.pack(side=LEFT)
    codeScroll.pack(side=RIGHT, fill=Y)

    outputWindow2 = Text(frame2_2, height=10)
    outputScroll = Scrollbar(frame2_2, command=outputWindow2.yview)
    outputWindow2.configure(yscrollcommand=outputScroll.set)
    outputWindow2.pack(side=LEFT)
    outputScroll.pack(side=RIGHT, fill=Y)

    chk_b2 = Button(lbl_final_test2, text='Check answer', command=check_answer2)
    chk_b2.pack()


def check_answer():

    code = codeEditor.get('1.0', END + '-1c')

    try:
        save_stdout = sys.stdout  # save old value so we can restore it later
        sys.stdout = open('answers.txt', 'w')
        exec(code, {})
        sys.stdout.close()
        sys.stdout = save_stdout


    except:
        messagebox.showwarning("Error","Error in code")
    file1 = open("answers.txt", "r")
    verify = file1.read()
    if "[(2, 28), (4, 26), (6, 24), (8, 22), (10, 20), (12, 18), (14, 16), (16, 14), (18, 12), (20, 10), (22, 8), (24, 6), (26, 4), (28, 2)]" in verify:
        if messagebox.showinfo("Correct", "Correct Answer!"):
            run_b1["state"] = DISABLED
            chk_b1["state"] = DISABLED
            final_ques2()
    else:
        messagebox.showwarning("Wrong!!", "Wrong output")




def start_final_test():
    global run_b1,chk_b1,lbl_final_test,outputWindow,codeEditor,final_test
    final_test = Toplevel(screen)
    final_test.title("Final Test")
    final_test.geometry("700x700")
    final_test.iconbitmap('icon.ico')

    window = ScrolledFrame(final_test)
    window.pack(expand=True, fill='both')

    lbl_final_test = LabelFrame(window.inner)
    lbl_final_test.pack(padx=10, pady=10)

    Label(lbl_final_test, text="Final Test", font=("Helvetica", 18)).pack()

    logo = Image.open("logo.png")
    logo = logo.resize((50, 50), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)

    l_image = Label(lbl_final_test, image=logo)
    l_image.image = logo
    l_image.pack()

    lbl_final_test1 = LabelFrame(lbl_final_test)
    lbl_final_test1.pack(padx=10, pady=10)

    lbl_question_final = Label(lbl_final_test1,
                               text="Create a code that returns a list of all two whole even numbers that sum to 30",
                               font="24").pack()

    frame1 = Frame(lbl_final_test1)
    frame1.pack(side=TOP, fill=Y)
    run_b1 = Button(lbl_final_test1, text='Run', command=buttonCallback)
    run_b1.pack()
    frame2 = Frame(lbl_final_test1)
    frame2.pack(side=BOTTOM, fill=Y)

    codeEditor = Text(frame1, height=10)
    codeScroll = Scrollbar(frame1, command=codeEditor.yview)
    codeEditor.configure(yscrollcommand=codeScroll.set)
    codeEditor.pack(side=LEFT)
    codeScroll.pack(side=RIGHT, fill=Y)

    outputWindow = Text(frame2, height=10)
    outputScroll = Scrollbar(frame2, command=outputWindow.yview)
    outputWindow.configure(yscrollcommand=outputScroll.set)
    outputWindow.pack(side=LEFT)
    outputScroll.pack(side=RIGHT, fill=Y)

    chk_b1 = Button(lbl_final_test1, text='Check answer', command=check_answer)
    chk_b1.pack()
def successful_login():
    messagebox.showinfo("STATUS", "Log in successful!")
    screen2.destroy()
    dash()


def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_files = [file for file in os.listdir() if file.endswith(".txt")]
    userlst_lower = [x.lower() for x in list_files]
    if username1.lower() + ".txt" in userlst_lower:
        file1 = open(username1 + ".txt", "r")
        verify = file1.read()
        dicc = ast.literal_eval((verify))
        if password1 == dicc.get("password"):
            successful_login()


        else:
            messagebox.showwarning("STATUS", "Password not recognized")
    else:
        messagebox.showwarning("STATUS", "User not found")


def register():
    global screen1, username, password_entry, username_entry, password
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    screen1.iconbitmap('icon.ico')
    screen1.resizable(False, False)
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details").pack()
    Label(screen1, text="Username *").pack()
    Label(screen1, text="").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, show="*", textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=ruser).pack()


def login():
    global screen2, password_entry1, username_entry1, password_verify, username_verify
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    screen2.iconbitmap('icon.ico')
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()
    Label(screen2, text="Username *").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password *").pack()
    password_entry1 = Entry(screen2, show="*", textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def ask_quit():
    if messagebox.askokcancel("Quit", "You want to quit now? "):
        screen.destroy()


def mscreen():
    global screen, frame
    screen = Tk()
    screen.geometry("600x600")
    screen.iconbitmap('icon.ico')
    screen.title("ATLAS")
    global main_L
    main_L = Label(screen, text="Welcome to ATLAS!" + "\n", borderwidth=2, relief="solid", bg="#1167b1", width="50",
                   height="2",
                   font=("Helvetica", 13))
    main_L.pack()

    frame = LabelFrame(screen, pady=50, padx=50)
    frame.pack()

    logo = Image.open("logo.png")
    logo = logo.resize((100, 100), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)
    logo_M_I = Label(frame, image=logo)
    logo_M_I.image = logo
    logo_M_I.pack()

    Label(frame, text="Welcome to your Python Journey!").pack()
    Label(frame, text="").pack()
    Button(frame, text="Login", width="30", height="2", command=login).pack()
    Label(frame, text="").pack()
    Button(frame, text="Register", width="30", height="2", command=register).pack()
    Label(frame, text="Don't have an account?" + "\n\n" + "Register now to start your Python Journey!").pack()

    screen.protocol("WM_DELETE_WINDOW", ask_quit)


def start_intro_module():
    global intro
    intro = Toplevel(screen)
    intro.geometry("1280x720")
    intro.iconbitmap('icon.ico')
    Label(intro, text="Welcome to your introduction to python, " + username1.title() + "\n",
          font=("Helvetica", "13", "bold")).pack()

    window = ScrolledFrame(intro)
    window.pack(expand=True, fill='both')

    lbl_intro = LabelFrame(window.inner)
    lbl_intro.pack()

    lbl_intro_header = LabelFrame(lbl_intro, borderwidth=5, bg="black")
    lbl_intro_header.pack()
    Label(lbl_intro_header, text=""" Programming Languages """, font=("20")).pack()

    Label(lbl_intro, text="""\n  It is a medium of instruction to be able to allow a set of instructions to produce different types of output.
   In other words, It is a way for us to communicate with the computer.
   All computer softwares are coded using Programming Languages, becoming the backbone of our systems.""",
          font=("13")).pack()

    lbl_intro_header = LabelFrame(lbl_intro, borderwidth=5, bg="black")
    lbl_intro_header.pack()
    Label(lbl_intro_header, text=""" What is Python? """, font=("20")).pack()

    Label(lbl_intro, text="""\n Python is an interpreted, object-oriented, high-level programming language. It is an object 
    oriented programming language that has multiple libraries, simple syntax, and making it one of the 
    most versatile programming languages to date.""",
          font=("13")).pack()

    Label(lbl_intro, text="""\n""").pack()

    lbl_intro_header = LabelFrame(lbl_intro, borderwidth=5, bg="black")
    lbl_intro_header.pack()
    Label(lbl_intro_header, text=""" Why Python? """, font=("20")).pack()

    Label(lbl_intro, text="""\nHaving simple syntax, Python is one of the most highly recommend starting languages, both for 
    beginners and experts in the field of programming. Deemed as having "syntatic simplicity" by it's 
    users, allowing more focus on logic formation as a whole.""",
          font=("13")).pack()

    Label(lbl_intro, text="""\n""").pack()

    lbl_intro_header = LabelFrame(lbl_intro, borderwidth=5, bg="black")
    lbl_intro_header.pack()
    Label(lbl_intro_header, text=""" Integrated Development Environments (IDE) """, font=("20")).pack()

    Label(lbl_intro, text="""\n To be able to code, we will need IDEs, These IDES are basically what "Translates" the 
    syntax we input. In other words, our "bridge" to communicate with the computer, allowing 
    us to compile and run our program

    Below are examples of popular IDEs for python:""",
          font=("13")).pack()

    pintro_1 = Image.open("intro.PNG")
    pintro_1 = pintro_1.resize((559, 225), Image.ANTIALIAS)
    pintro_1 = ImageTk.PhotoImage(pintro_1)

    pintro_1i = Label(lbl_intro, image=pintro_1)
    pintro_1i.image = pintro_1
    pintro_1i.pack()

    Label(lbl_intro, text="""\n""").pack()

    lbl_intro_header = LabelFrame(lbl_intro, borderwidth=5, bg="black")
    lbl_intro_header.pack()
    Label(lbl_intro_header, text=""" ATLAS """, font=("20")).pack()

    Label(lbl_intro, text="""\nATLAS, our application, aims to guide throughout you journey in Python programming! We will 
    be providing modules and adaptive tests to help you as you learn Python! Catered to even those without 
    knowledge in programming or experts at the field!\n\n""",
          font=("13")).pack()


def submit_2_basic():
    global lbl_questions_basic, pques_2_basic
    x = radio_var_2_basic.get()
    if x == 0:
        Label(lbl_questions_basic, text="Correct\n You are ready for your Proficiency Test", fg="green").pack()
        pques_basic_2["state"] = "disabled"
        test_basic_b = Button(lbl_questions_basic, text="Proceed to Test", command=test_basic)
        test_basic_b.pack()

    elif x != 0:
        Label(lbl_questions_basic, text="Incorrect \n Remember the functions we learned.", fg="red").pack()


def pques_2_basic():
    Label(lbl_questions_basic,
          text="""How is division done in python?""", font=("13")).pack()

    global radio_var_2_basic
    radio_var_2_basic = IntVar()
    radio_var_2_basic.set(-1)
    radio1_2 = Radiobutton(lbl_questions_basic, text=r'25/2', font=("12"), variable=radio_var_2_basic,
                           value=0)
    radio1_2.pack()

    radio2_2 = Radiobutton(lbl_questions_basic, text=r'23//2', font=("12"), variable=radio_var_2_basic,
                           value=1)
    radio2_2.pack()

    radio3_2 = Radiobutton(lbl_questions_basic, text=r'232%23', font=("12"), variable=radio_var_2_basic,
                           value=2)
    radio3_2.pack()

    radio4_2 = Radiobutton(lbl_questions_basic, text=r'34\3', font=("12"), variable=radio_var_2_basic,
                           value=3)
    radio4_2.pack()

    global pques_basic_2
    pques_basic_2 = Button(lbl_questions_basic, text="Submit!", command=submit_2_basic)
    pques_basic_2.pack()


def submit_pques1_basic():
    x = radio_var_pques_basic.get()
    if x == 1:
        Label(lbl_questions_basic, text="Correct", fg="green").pack()
        pques_b_basic["state"] = "disabled"
        pques_2_basic()
    elif x != 1:
        Label(lbl_questions_basic, text="Remember the functions we learned!", fg="red").pack()


def start_basic_module():
    global basic
    basic = Toplevel(screen)
    basic.geometry("1280x720")
    basic.iconbitmap('icon.ico')
    Label(basic, text="Welcome " + username1.title() + " to your basic programming Lesson!",
          font=("Helvetica", "13", "bold")).pack()

    window = ScrolledFrame(basic)
    window.pack(expand=True, fill='both')

    lbl_basic = LabelFrame(window.inner)
    lbl_basic.pack()

    Label(lbl_basic, text="""\n""").pack()

    lbl_basic_header = LabelFrame(lbl_basic, borderwidth=5, bg="black")
    lbl_basic_header.pack()
    Label(lbl_basic_header, text="""                        Print                           """, font=("20")).pack()

    Label(lbl_basic, text="""\nTo display text in python, we're required to use the function " print("") "
Print is a code that displays the text INSIDE the quotation and the parenthesis.
An example of such would be the syntax: print("ATLAS")
The syntax displayed would output the code atlas as seen below:
""",
          font=("13")).pack()

    grui_1 = Image.open("basic_1.PNG")
    grui_1 = grui_1.resize((187, 124), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_basic, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_basic, text="""\n""").pack()

    lbl_basic_header = LabelFrame(lbl_basic, borderwidth=5, bg="black")
    lbl_basic_header.pack()
    Label(lbl_basic_header, text="""                         Tip!                           """, font=("20")).pack()

    Label(lbl_basic, text="""\n\nWe can also store variables(which we will discuss later) inside `print()`without using 
    quotation marks. inside the parenthesis\n""",
          font=("13")).pack()

    grui_2 = Image.open("basic_2.PNG")
    grui_2 = grui_2.resize((78, 66), Image.ANTIALIAS)
    grui_2 = ImageTk.PhotoImage(grui_2)

    grui_2_i = Label(lbl_basic, image=grui_2)
    grui_2_i.image = grui_2
    grui_2_i.pack()
    Label(lbl_basic, text="").pack()

    Label(lbl_basic, text="""Anything virtually possible can be inputted inside the quotation and parenthesis,
     may it be numbers, text, or even variables, which we will go on to later""",
          font=("13")).pack()

    Label(lbl_basic, text="""\n""").pack()

    lbl_basic_header = LabelFrame(lbl_basic, borderwidth=5, bg="black")
    lbl_basic_header.pack()
    Label(lbl_basic_header, text="""                      Basic Arithmetic                       """,
          font=("20")).pack()

    Label(lbl_basic, text="""\nPython has the ability to do various operations. These include the 4 basic operations,and 
    more which will be discussed later\n""",
          font=("13")).pack()

    grui_12 = Image.open("basic_3.PNG")
    grui_12 = grui_12.resize((289, 966), Image.ANTIALIAS)
    grui_12 = ImageTk.PhotoImage(grui_12)

    grui_12_i = Label(lbl_basic, image=grui_12)
    grui_12_i.image = grui_12
    grui_12_i.pack()

    Label(lbl_basic, text="""\n""").pack()

    grui_3 = Image.open("basic_4.PNG")
    grui_3 = grui_3.resize((682, 360), Image.ANTIALIAS)
    grui_3 = ImageTk.PhotoImage(grui_3)

    grui_3_i = Label(lbl_basic, image=grui_3)
    grui_3_i.image = grui_3
    grui_3_i.pack()

    Label(lbl_basic, text="""\n""").pack()

    lbl_basic_header = LabelFrame(lbl_basic, borderwidth=5, bg="black")
    lbl_basic_header.pack()
    Label(lbl_basic_header, text="""                      Variables                       """,
          font=("20")).pack()

    Label(lbl_basic, text="""\nSimilar to mathematics, variables are where we can store a specific value inside a declared name
To do this, we put them inside the `=` symbol\n""",
          font=("13")).pack()

    grui_4 = Image.open("basic_5.PNG")
    grui_4 = grui_4.resize((158, 90), Image.ANTIALIAS)
    grui_4 = ImageTk.PhotoImage(grui_4)
    grui_4_i = Label(lbl_basic, image=grui_4)
    grui_4_i.image = grui_4
    grui_4_i.pack()

    Label(lbl_basic, text="""\n""").pack()

    lbl_basic_header = LabelFrame(lbl_basic, borderwidth=5, bg="black")
    lbl_basic_header.pack()
    Label(lbl_basic_header, text="""                       Tip!                        """,
          font=("20")).pack()

    Label(lbl_basic, text="""\nVariables aren't limited to set values, we also perform basic arithmetic on them!\n""",
          font=("13")).pack()

    grui_5 = Image.open("basic_6.PNG")
    grui_5 = grui_5.resize((180, 169), Image.ANTIALIAS)
    grui_5 = ImageTk.PhotoImage(grui_5)

    grui_5_i = Label(lbl_basic, image=grui_5)
    grui_5_i.image = grui_5
    grui_5_i.pack()

    Label(lbl_basic, text="""\n""").pack()

    lbl_basic_header = LabelFrame(lbl_basic, borderwidth=5, bg="black")
    lbl_basic_header.pack()
    Label(lbl_basic_header, text="""                      Increments and Decrements                      """,
          font=("20")).pack()

    Label(lbl_basic, text="""\n""").pack()

    Label(lbl_basic, text="""In python, we are allowed to continously add a value to a variable.

        but instead of typing the variable again as such:
    """,
          font=("13")).pack()

    grui_9 = Image.open("basic_7.png")
    grui_9 = grui_9.resize((162, 100), Image.ANTIALIAS)
    grui_9 = ImageTk.PhotoImage(grui_9)

    grui_9_i = Label(lbl_basic, image=grui_9)
    grui_9_i.image = grui_9
    grui_9_i.pack()

    Label(lbl_basic, text="""\n""").pack()

    Label(lbl_basic, text="""We can opt to do this instead:\n""", font=("13")).pack()

    grui_10 = Image.open("basic_8.png")
    grui_10 = grui_10.resize((164, 118), Image.ANTIALIAS)
    grui_10 = ImageTk.PhotoImage(grui_10)
    grui_10_i = Label(lbl_basic, image=grui_10)
    grui_10_i.image = grui_10
    grui_10_i.pack()

    Label(lbl_basic, text="""Though the benefit is miniscule, enforcing ourselves 
    to use this as early as now will help us in the long run!:
     """, font=("13")).pack()

    lbl_basic_header = LabelFrame(lbl_basic, borderwidth=5, bg="black")
    lbl_basic_header.pack()
    Label(lbl_basic_header, text="""                      Comments                     """,
          font=("20")).pack()

    Label(lbl_basic, text="""\nLastly we will talk about comments. these are lines of text in the code, but are 
    instead there to help add notes or as a reminder to the coder.

    They are inputted in the code by using the `#` logo before the syntax\n""", font=("13")).pack()

    grui_6 = Image.open("basic_9.png")
    grui_6 = grui_6.resize((671, 144), Image.ANTIALIAS)
    grui_6 = ImageTk.PhotoImage(grui_6)

    grui_6_i = Label(lbl_basic, image=grui_6)
    grui_6_i.image = grui_6
    grui_6_i.pack()

    Label(lbl_basic,
          text="""\n\nPractice Questions""",
          anchor=W, font=("20")).pack()
    global lbl_questions_basic
    lbl_questions_basic = LabelFrame(lbl_basic, padx=80, pady=80)
    lbl_questions_basic.pack()

    Label(lbl_questions_basic,
          text="""Which of the following has an incorrect syntax:?""", font=("13")).pack()

    global radio_var_pques_basic
    radio_var_pques_basic = IntVar()
    radio_var_pques_basic.set(-1)
    radio1_1 = Radiobutton(lbl_questions_basic, text="print('Yes')", font=("12"), variable=radio_var_pques_basic,
                           value=0)
    radio1_1.pack()

    radio2_1 = Radiobutton(lbl_questions_basic, text="display('Yes')", font=("12"), variable=radio_var_pques_basic,
                           value=1)
    radio2_1.pack()

    radio3_1 = Radiobutton(lbl_questions_basic, text="print('a+y')", font=("12"), variable=radio_var_pques_basic,
                           value=2)
    radio3_1.pack()

    radio4_1 = Radiobutton(lbl_questions_basic, text="a=0+1=+2", font=("12"), variable=radio_var_pques_basic, value=3)
    radio4_1.pack()

    global pques_b_basic
    pques_b_basic = Button(lbl_questions_basic, text="Submit!", command=submit_pques1_basic)
    pques_b_basic.pack()


def submit_2_func():
    x = radio_var_2_func.get()
    if x == 3:
        Label(lbl_questions_func, text="Correct\n You are ready for your Proficiency Test", fg="green").pack()
        pques_func_2["state"] = "disabled"
        test_func_b = Button(lbl_questions_func, text="Proceed to Test", command=test_func)
        test_func_b.pack()

    elif x != 3:
        Label(lbl_questions_func, text="Incorrect \n Remember the syntax!", fg="red").pack()


def pques_2_func():
    Label(lbl_questions_func,
          text="""\n\nHow do we declare a function?""", font=("13")).pack()

    global radio_var_2_func
    radio_var_2_func = IntVar()
    radio_var_2_func.set(-1)
    radio1_2 = Radiobutton(lbl_questions_func, text=r'declare my_function()', font=("12"), variable=radio_var_2_func,
                           value=0)
    radio1_2.pack()

    radio2_2 = Radiobutton(lbl_questions_func, text=r'dec my_function()', font=("12"), variable=radio_var_2_func,
                           value=1)
    radio2_2.pack()

    radio3_2 = Radiobutton(lbl_questions_func, text=r'set my_function()', font=("12"), variable=radio_var_2_func,
                           value=2)
    radio3_2.pack()

    radio4_2 = Radiobutton(lbl_questions_func, text=r'def my_function()', font=("12"), variable=radio_var_2_func,
                           value=3)
    radio4_2.pack()

    global pques_func_2
    pques_func_2 = Button(lbl_questions_func, text="Submit!", command=submit_2_func)
    pques_func_2.pack()


def submit_pques1_func():
    x = radio_var_pques_func.get()
    if x == 0:
        Label(lbl_questions_func, text="Correct", fg="green").pack()
        pques_b_func["state"] = "disabled"
        pques_2_func()
    elif x != 0:
        Label(lbl_questions_func, text="Remember the term!", fg="red").pack()


def start_func_module():
    global func
    func = Toplevel(screen)
    func.geometry("1280x720")
    func.iconbitmap('icon.ico')
    Label(func, text="Welcome " + username1.title() + " to your function programming Lesson!",
          font=("Helvetica", "13", "bold")).pack()

    window = ScrolledFrame(func)
    window.pack(expand=True, fill='both')

    lbl_func = LabelFrame(window.inner)
    lbl_func.pack()

    Label(lbl_func, text="""\n""").pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=5, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                        Functions                           """, font=("20")).pack()

    Label(lbl_func, text="""\nA function is a line of code that only runs when it is called. 
    It is a way to basically divide our code, making it both readable and reusable.

    These functions can return the values. Functions store all 
    the variables, functions, and arithmetic INSIDE the call. 
    meaning that declared variables, will only be kept INSIDE the function

    An example of such would be the syntax: def functionname():
    wherein functionname is any label you want.

    below is an example:
    """,
          font=("13")).pack()

    grui_1 = Image.open("func_1.png")
    grui_1 = grui_1.resize((309, 88), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_func, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_func, text="""\n\n\n""").pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=5, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                         Returning Values                           """,
          font=("20")).pack()

    Label(lbl_func, text="""\n\nthere are two(2) known types of functions:\n""",
          font=("13")).pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=2, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                   User-defined                     """, font=("20")).pack()

    Label(lbl_func, text="""\n\nFunction defined or in other words, made by the users(us) theirselves
    This is the type of function we are tackling right now!\n""",
          font=("13")).pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=2, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                    Built-in                     """, font=("20")).pack()

    Label(lbl_func, text="""\n\nFunctions that are built into python\n""",
          font=("13")).pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=2, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                   NOTE!                      """, font=("20")).pack()

    Label(lbl_func, text="""\n\nto declare any syntax inside a function, you must make sure they are >indented< using 
    TAB or SPACE

    and to simply stop inputting in the function, remove the INDENTATION or SPACE from the proceeding code.
    \n""", font=("13")).pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=5, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                    Calling Functions                     """, font=("20")).pack()

    Label(lbl_func, text="""\n\nto call a function, you must input the code: `functionname()`.
    doing this will execute the code that is found inside that function.
      \n""", font=("13")).pack()

    grui_2 = Image.open("func_2.PNG")
    grui_2 = grui_2.resize((437, 179), Image.ANTIALIAS)
    grui_2 = ImageTk.PhotoImage(grui_2)

    grui_2_i = Label(lbl_func, image=grui_2)
    grui_2_i.image = grui_2
    grui_2_i.pack()

    Label(lbl_func, text="""\n""").pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=5, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                      Arguments                       """, font=("20")).pack()

    Label(lbl_func, text="""\nyou can pass or in other words, input data to a function.
By inputting them into the parenthesis in the `functionname()`

these are called arguments

Below is an example:\n""",
          font=("13")).pack()

    grui_12 = Image.open("func_3.PNG")
    grui_12 = grui_12.resize((516, 179), Image.ANTIALIAS)
    grui_12 = ImageTk.PhotoImage(grui_12)

    grui_12_i = Label(lbl_func, image=grui_12)
    grui_12_i.image = grui_12
    grui_12_i.pack()

    Label(lbl_func, text="""\n""").pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=5, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                      Returning Values                      """, font=("20")).pack()

    Label(lbl_func, text="""\nusing `return()` in the function exits the function, possibly "passing back" an expression when it is called.

An example of such is:\n""",
          font=("13")).pack()

    grui_3 = Image.open("func_4.PNG")
    grui_3 = grui_3.resize((532, 161), Image.ANTIALIAS)
    grui_3 = ImageTk.PhotoImage(grui_3)

    grui_3_i = Label(lbl_func, image=grui_3)
    grui_3_i.image = grui_3
    grui_3_i.pack()

    Label(lbl_func, text="""\n""").pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=3, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                      Note!                       """,
          font=("20")).pack()

    Label(lbl_func, text="""\nVariables you declare inside a function only  <font color=red>STAY INSIDE THE FUNCTION</font> 

    Meaning that once you don't use the function, the variables declared will NOT carry on.\n""",
          font=("13")).pack()

    grui_4 = Image.open("func_5.PNG")
    grui_4 = grui_4.resize((508, 140), Image.ANTIALIAS)
    grui_4 = ImageTk.PhotoImage(grui_4)
    grui_4_i = Label(lbl_func, image=grui_4)
    grui_4_i.image = grui_4
    grui_4_i.pack()

    Label(lbl_func, text="""\nNotice  how the value of variable "a" is not equal to it's supposed value, 30.  
    this is because the variable declaration was inside the function, thus python ignores it\n""",
          font=("13")).pack()

    Label(lbl_func, text="""\n""").pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=5, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                      Operators                      """,
          font=("20")).pack()

    Label(lbl_func, text="""\nThese are mostly used to perform operations on variables and values
in the previous module, we have already tackled Arithmetic Operators, a specific type of operator.

Today we will further discuss their other subtypes.
    """,
          font=("13")).pack()

    Label(lbl_func, text="""\n""").pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=3, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                 Comparison Operators                    """,
          font=("20")).pack()

    Label(lbl_func, text="""\nComparison operators are used to compare two values, may 
    it be variables or set values. """,
          font=("13")).pack()
    grui_10 = Image.open("func_6.png")
    grui_10 = grui_10.resize((612, 273), Image.ANTIALIAS)
    grui_10 = ImageTk.PhotoImage(grui_10)
    grui_10_i = Label(lbl_func, image=grui_10)
    grui_10_i.image = grui_10
    grui_10_i.pack()

    Label(lbl_func, text="""\n""").pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=3, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                   Logical Operators                  """, font=("20")).pack()

    Label(lbl_func, text="""\n Logical operators are used to combine conditional statements""", font=("13")).pack()

    grui_10 = Image.open("func_7.png")
    grui_10 = grui_10.resize((709, 222), Image.ANTIALIAS)
    grui_10 = ImageTk.PhotoImage(grui_10)
    grui_10_i = Label(lbl_func, image=grui_10)
    grui_10_i.image = grui_10
    grui_10_i.pack()

    Label(lbl_func, text="""\n\n""").pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=5, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                   Conditional statements                 """, font=("20")).pack()

    Label(lbl_func, text="""\n  As we progress into much more complicated programs, There will be instances where 
    we will need to skip some lines of code, conduct repetition, or make a decision.

   These are where conditional statements come in.

   These conditional statements, or control structures, direct the flow of the execution of code in a program. 
   Today, we will be tackling the several types of structures, and how they can be used in our code.
   \n""", font=("13")).pack()

    grui_6 = Image.open("func_9.png")
    grui_6 = grui_6.resize((671, 144), Image.ANTIALIAS)
    grui_6 = ImageTk.PhotoImage(grui_6)

    grui_6_i = Label(lbl_func, image=grui_6)
    grui_6_i.image = grui_6
    grui_6_i.pack()

    Label(lbl_func, text="""\n""").pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=3, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                   "If" statements                 """, font=("20")).pack()

    Label(lbl_func, text="""\nThese kind of expressions have the following format:\n""", font=("13")).pack()

    grui_6 = Image.open("func_10.png")
    grui_6 = grui_6.resize((123, 53), Image.ANTIALIAS)
    grui_6 = ImageTk.PhotoImage(grui_6)

    grui_6_i = Label(lbl_func, image=grui_6)
    grui_6_i.image = grui_6
    grui_6_i.pack()

    Label(lbl_func, text="""\n where in <expression> is a expression evaluated to be either true or false, or in
    computer language, boolean.

    and <statement> is the code that would be executed is the expression is true. all the statements, much 
    like functions, require INDENTATION or SPACES to be considered inside the statement.
    here is an example:
      \n""", font=("13")).pack()

    grui_6 = Image.open("func_11.png")
    grui_6 = grui_6.resize((603, 132), Image.ANTIALIAS)
    grui_6 = ImageTk.PhotoImage(grui_6)

    grui_6_i = Label(lbl_func, image=grui_6)
    grui_6_i.image = grui_6
    grui_6_i.pack()

    Label(lbl_func, text="""\n\n""").pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=3, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                   "Elif" statements                 """, font=("20")).pack()

    Label(lbl_func, text="""\n Elif, is basically a condition that will be checked only when a prior "if" statement 
    was not true.
    similar to "If" statements, it follows the expression and statement format.

E.G:\n""", font=("13")).pack()

    grui_6 = Image.open("func_12.png")
    grui_6 = grui_6.resize((525, 163), Image.ANTIALIAS)
    grui_6 = ImageTk.PhotoImage(grui_6)

    grui_6_i = Label(lbl_func, image=grui_6)
    grui_6_i.image = grui_6
    grui_6_i.pack()

    Label(lbl_func, text="""\n\n""").pack()

    lbl_func_header = LabelFrame(lbl_func, borderwidth=3, bg="black")
    lbl_func_header.pack()
    Label(lbl_func_header, text="""                   "Else" statements                 """, font=("20")).pack()

    Label(lbl_func, text="""\n Else is another form of condition that will be executed when all the if and elif 
    statements are false. Unlike the aforementioned statements, "Else" statements 
    will always execute once all the "If" and "Elif" statements are false.

    E.G:\n""", font=("13")).pack()

    grui_6 = Image.open("func_13.png")
    grui_6 = grui_6.resize((553, 209), Image.ANTIALIAS)
    grui_6 = ImageTk.PhotoImage(grui_6)

    grui_6_i = Label(lbl_func, image=grui_6)
    grui_6_i.image = grui_6
    grui_6_i.pack()

    Label(lbl_func,
          text="""\n\nPractice Questions""",
          anchor=W, font=("20")).pack()
    global lbl_questions_func
    lbl_questions_func = LabelFrame(lbl_func, padx=80, pady=80)
    lbl_questions_func.pack()

    Label(lbl_questions_func,
          text="""Can be used to combine and compare values and variables\n""", font=("13")).pack()

    global radio_var_pques_func
    radio_var_pques_func = IntVar()
    radio_var_pques_func.set(-1)
    radio1_1 = Radiobutton(lbl_questions_func, text="Operators", font=("12"), variable=radio_var_pques_func, value=0)
    radio1_1.pack()

    radio2_1 = Radiobutton(lbl_questions_func, text="Booleans", font=("12"), variable=radio_var_pques_func, value=1)
    radio2_1.pack()

    radio3_1 = Radiobutton(lbl_questions_func, text="Comparators", font=("12"), variable=radio_var_pques_func, value=2)
    radio3_1.pack()

    radio4_1 = Radiobutton(lbl_questions_func, text="Conditionals", font=("12"), variable=radio_var_pques_func, value=3)
    radio4_1.pack()

    global pques_b_func
    pques_b_func = Button(lbl_questions_func, text="Submit!", command=submit_pques1_func)
    pques_b_func.pack()


def submit_2_modyul():
    x = radio_var_2_modyul.get()
    if x == 1:
        Label(lbl_questions_modyul, text="Correct\n You are ready for your Proficiency Test", fg="green").pack()
        pques_modyul_2["state"] = "disabled"
        test_modyul_b = Button(lbl_questions_modyul, text="Proceed to Test", command=test_modyul)
        test_modyul_b.pack()

    elif x != 1:
        Label(lbl_questions_modyul, text="Incorrect \n Check the module!", fg="red").pack()


def pques_2_modyul():
    Label(lbl_questions_modyul,
          text="""\n\nAll these types were discussed except:""", font=("13")).pack()

    global radio_var_2_modyul
    radio_var_2_modyul = IntVar()
    radio_var_2_modyul.set(-1)
    radio1_2 = Radiobutton(lbl_questions_modyul, text=r'dir()', font=("12"), variable=radio_var_2_modyul,
                           value=0)
    radio1_2.pack()

    radio2_2 = Radiobutton(lbl_questions_modyul, text=r'len()', font=("12"), variable=radio_var_2_modyul,
                           value=1)
    radio2_2.pack()

    radio3_2 = Radiobutton(lbl_questions_modyul, text=r'help()', font=("12"), variable=radio_var_2_modyul,
                           value=2)
    radio3_2.pack()

    radio4_2 = Radiobutton(lbl_questions_modyul, text=r'type()', font=("12"), variable=radio_var_2_modyul,
                           value=3)
    radio4_2.pack()

    global pques_modyul_2
    pques_modyul_2 = Button(lbl_questions_modyul, text="Submit!", command=submit_2_modyul)
    pques_modyul_2.pack()


def submit_pques1_modyul():
    x = radio_var_pques_modyul.get()
    if x == 3:
        Label(lbl_questions_modyul, text="Correct", fg="green").pack()
        pques_b_modyul["state"] = "disabled"
        pques_2_modyul()
    elif x != 3:
        Label(lbl_questions_modyul, text="Re-read the module, remember function rules!", fg="red").pack()


def start_modyul_module():
    global modyul
    modyul = Toplevel(screen)
    modyul.geometry("1280x720")
    modyul.iconbitmap('icon.ico')
    Label(modyul, text="Welcome " + username1.title() + " to your Library programming Lesson!",
          font=("Helvetica", "13", "bold")).pack()

    window = ScrolledFrame(modyul)
    window.pack(expand=True, fill='both')

    lbl_modyul = LabelFrame(window.inner)
    lbl_modyul.pack()

    Label(lbl_modyul, text="""\n""").pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=5, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""                        Libraries                          """, font=("20")).pack()

    Label(lbl_modyul, text="""\nWe have mentioned in the last module that there 2 types of functions: 
    Built-in functions and User-defined functions.

    Today, we will be discussing Built-in function that are not found from the original framework.

    These collections of functions are called modules. They have no limitations to their use, as we can use 
    these modules even inside of our own functions!
    """,
          font=("13")).pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=5, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""                        Importing                          """, font=("20")).pack()

    Label(lbl_modyul, text="""\nTo be able to use these built-in functions, we 
    must import them from their respective Modules.

    Think of modules as a huge storage area for various functions.

    """, font=("13")).pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=5, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""                     Importing library without name change                     """,
          font=("20")).pack()

    Label(lbl_modyul, text="""\n""").pack()

    grui_1 = Image.open("modyul_1.PNG")
    grui_1 = grui_1.resize((539, 179), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_modyul, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_modyul, text="""\n\n\n""").pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=5, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""                    Importing library with name change                    """,
          font=("20")).pack()

    Label(lbl_modyul, text="""\n""").pack()

    grui_1 = Image.open("modyul_2.PNG")
    grui_1 = grui_1.resize((248, 118), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_modyul, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_modyul, text="""\n""").pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=5, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""                    Importing specific function                   """,
          font=("20")).pack()

    Label(lbl_modyul, text="""\n""").pack()

    grui_1 = Image.open("modyul_3.PNG")
    grui_1 = grui_1.resize((252, 95), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_modyul, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_modyul, text="""\nThis will make the specific function not need 'function.' anymore.
    but still allows every other function to be called, albeit requiring 'function.'\n""", font=("13")).pack()

    Label(lbl_modyul, text="""\n\n\n\n""").pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=5, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""                    Libraries                   """, font=("20")).pack()

    Label(lbl_modyul, text="""\nHere are other libraries that can be found in Python:\n""", font=("13")).pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=3, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""Math""", font=("20")).pack()

    Label(lbl_modyul, text="""\nImports mathematical functions for our program\n""", font=("13")).pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=3, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""Random""", font=("20")).pack()

    Label(lbl_modyul, text="""\nDwells with probability and chance based functions\n""", font=("13")).pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=3, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""String""", font=("20")).pack()

    Label(lbl_modyul, text="""\nA Module that has functions that deal with the string datatype\n""", font=("13")).pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=3, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""NumPy""", font=("20")).pack()

    Label(lbl_modyul, text="""\nA library that focuses on scientific computing functions\n\n\n\n""", font=("13")).pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=3, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""                    Tips - Types                   """, font=("20")).pack()

    Label(lbl_modyul, text="""\nIn python, we are able to identify the variable type of any variable using
    the type() function. This will come in very handy later on!\n""", font=("13")).pack()

    grui_1 = Image.open("modyul_4.PNG")
    grui_1 = grui_1.resize((249, 185), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_modyul, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_modyul, text="""\n\n""").pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=3, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""                    Tips - dir                   """, font=("20")).pack()

    Label(lbl_modyul, text="""\nAfter importing a library, it is possible for us to identify all
    the available functions in it using the `dir()` function\n""", font=("13")).pack()

    grui_1 = Image.open("modyul_5.PNG")
    grui_1 = grui_1.resize((260, 532), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_modyul, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_modyul, text="""\n\n""").pack()

    lbl_modyul_header = LabelFrame(lbl_modyul, borderwidth=3, bg="black")
    lbl_modyul_header.pack()
    Label(lbl_modyul_header, text="""                    Tips - help                   """, font=("20")).pack()

    Label(lbl_modyul, text="""\nIf we want to check a specific functions' purpose in python, we 
    can use `help()` to check for that, even when not importing them from a module!\n""", font=("13")).pack()

    grui_1 = Image.open("modyul_6.PNG")
    grui_1 = grui_1.resize((474, 162), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_modyul, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_modyul, text="""\nAll these tips will help you discover functions and troubleshoot on your own.
    Not only for the sake of library importing but in your ATLAS and Python journey as a whole!\n""",
          font=("13")).pack()

    Label(lbl_modyul,
          text="""\n\nPractice Questions""",
          anchor=W, font=("20")).pack()
    global lbl_questions_modyul
    lbl_questions_modyul = LabelFrame(lbl_modyul, padx=80, pady=80)
    lbl_questions_modyul.pack()

    Label(lbl_questions_modyul, text="""Evaluate the code below:\n\n from math import cos \nhelp(math.sin)\n""",
          font=("13")).pack()

    global radio_var_pques_modyul
    radio_var_pques_modyul = IntVar()
    radio_var_pques_modyul.set(-1)
    radio1_1 = Radiobutton(lbl_questions_modyul, text="It will not run, only cos is imported", font=("12"),
                           variable=radio_var_pques_modyul, value=0)
    radio1_1.pack()

    radio2_1 = Radiobutton(lbl_questions_modyul, text="It will not run, improper syntax", font=("12"),
                           variable=radio_var_pques_modyul, value=1)
    radio2_1.pack()

    radio3_1 = Radiobutton(lbl_questions_modyul, text="It will run but with no output", font=("12"),
                           variable=radio_var_pques_modyul, value=2)
    radio3_1.pack()

    radio4_1 = Radiobutton(lbl_questions_modyul, text="It will run with no errors", font=("12"),
                           variable=radio_var_pques_modyul, value=3)
    radio4_1.pack()

    global pques_b_modyul
    pques_b_modyul = Button(lbl_questions_modyul, text="Submit!", command=submit_pques1_modyul)
    pques_b_modyul.pack()


def submit_2_sequence():
    x = radio_var_2_sequence.get()
    if x == 2:
        Label(lbl_questions_sequence, text="Correct\n You are ready for your Proficiency Test", fg="green").pack()
        pques_sequence_2["state"] = "disabled"
        test_sequence_b = Button(lbl_questions_sequence, text="Proceed to Test", command=test_sequence)
        test_sequence_b.pack()

    elif x != 2:
        Label(lbl_questions_sequence, text="Incorrect \n Check the module!", fg="red").pack()


def pques_2_sequence():
    Label(lbl_questions_sequence,
          text="""\nWhat would be the output of the code? \n\nfor i in range (20,10,-2):\nprint(i)\n""",
          font=("13")).pack()

    global radio_var_2_sequence
    radio_var_2_sequence = IntVar()
    radio_var_2_sequence.set(-1)
    radio1_2 = Radiobutton(lbl_questions_sequence, text=r'18,16,14,12,10', font=("12"), variable=radio_var_2_sequence,
                           value=0)
    radio1_2.pack()

    radio2_2 = Radiobutton(lbl_questions_sequence, text=r'18,16,14,12', font=("12"), variable=radio_var_2_sequence,
                           value=1)
    radio2_2.pack()

    radio3_2 = Radiobutton(lbl_questions_sequence, text=r'20,18,16,14,12', font=("12"), variable=radio_var_2_sequence,
                           value=2)
    radio3_2.pack()

    radio4_2 = Radiobutton(lbl_questions_sequence, text=r'20,18,16,14,12,10', font=("12"),
                           variable=radio_var_2_sequence,
                           value=3)
    radio4_2.pack()

    global pques_sequence_2
    pques_sequence_2 = Button(lbl_questions_sequence, text="Submit!", command=submit_2_sequence)
    pques_sequence_2.pack()


def submit_pques1_sequence():
    x = radio_var_pques_sequence.get()
    if x == 0:
        Label(lbl_questions_sequence, text="Correct", fg="green").pack()
        pques_b_sequence["state"] = "disabled"
        pques_2_sequence()
    elif x != 0:
        Label(lbl_questions_sequence, text="Remember the term!", fg="red").pack()


def start_sequence_module():
    global sequence
    sequence = Toplevel(screen)
    sequence.geometry("1280x720")
    sequence.iconbitmap('icon.ico')
    Label(sequence, text="Welcome " + username1.title() + " to your sequence and iterations programming Lesson!",
          font=("Helvetica", "13", "bold")).pack()

    window = ScrolledFrame(sequence)
    window.pack(expand=True, fill='both')

    lbl_sequence = LabelFrame(window.inner)
    lbl_sequence.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=5, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                       Sequence and Iteration                        """,
          font=("20")).pack()

    Label(lbl_sequence, text="""\nA sequence is a positionally ordered collection of other objects, 
    these sequence maintain a left to right order among the items in the container.
    Data fetched from such must be called by their relative position.

    Below is a list of operations supported by most sequence types.

    Python data types include: strings, lists, range objects, and tuples.
    """,
          font=("13")).pack()

    grui_1 = Image.open("sequence_1.PNG")
    grui_1 = grui_1.resize((557, 310), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\nThe operations in the following table are defined on mutable sequence types.\n""",
          font=("13")).pack()

    grui_1 = Image.open("sequence_2.PNG")
    grui_1 = grui_1.resize((659, 358), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=5, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                        Strings                          """, font=("20")).pack()

    Label(lbl_sequence, text="""\nStrings are basically text characters also commonly known as a collection of bytes 
    To make these in python, we will put them inside either quotations '' or double quotations ""
    \n""", font=("13")).pack()

    grui_1 = Image.open("sequence_3.PNG")
    grui_1 = grui_1.resize((253, 57), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=3, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                     Backslash                     """,
          font=("20")).pack()

    Label(lbl_sequence, text="""\nBut what if we want to input quotations inside our string? a simple answer to that is backslash! `\`
    backslashes make python ignore reading the quotations as a prompt for a new string. with the format:
      \n""", font=("13")).pack()

    grui_1 = Image.open("sequence_4.PNG")
    grui_1 = grui_1.resize((220, 68), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=3, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                     Linebreak                     """,
          font=("20")).pack()

    Label(lbl_sequence, text="""\nA linebreak is when we start a new line for the text. To do this, we use backslash n
         \n""", font=("13")).pack()

    grui_1 = Image.open("sequence_5.PNG")
    grui_1 = grui_1.resize((294, 79), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n\n\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=5, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                   Operations on strings                    """,
          font=("20")).pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=3, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                    Adding / Concatenation                   """,
          font=("20")).pack()

    Label(lbl_sequence, text="""\nStrings also have operables on them, one them is using the `+` sign, but 
    instead of adding the values, python will just join the number of strings together, combining both 
    variables into one big string.\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_6.PNG")
    grui_1 = grui_1.resize((255, 138), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=3, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                    Multiplication / Repetition                   """,
          font=("20")).pack()

    Label(lbl_sequence, text="""\nAnother function similar to arithmetic is using `*`, doing so to strings 
    will repeat the string an nth number of times.\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_7.PNG")
    grui_1 = grui_1.resize((486, 141), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=3, bg="black")
    lbl_sequence_header.pack()

    Label(lbl_sequence_header, text="""                    Indexing                   """, font=("20")).pack()

    Label(lbl_sequence, text="""\nIn python, the default type are strings, or basically words. But it is 
    possible for us to access their character, or in other words, the individual letter.

    This is done by the format `stringname[index]`

    where in index is the location of the character in a numerical value. Keep in mind that the counting 
    always starts at zero and follows a increasing order from LEFT to RIGHT\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_8.PNG")
    grui_1 = grui_1.resize((590, 130), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\nIt is also possible to input a negative value, making it 
    start from the rightmost instead\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_9.PNG")
    grui_1 = grui_1.resize((570, 116), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=3, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                    Slicing                   """, font=("20")).pack()

    Label(lbl_sequence, text="""\nSlicing is another method of indexing to get multiple characters 
    from a string. It is very similar to  indexing but rather than limiting itself to one character, 
    the programmer sets the limit the general format is `str[ind1:ind2]`.\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_10.PNG")
    grui_1 = grui_1.resize((363, 121), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    grui_1 = Image.open("sequence_11.PNG")
    grui_1 = grui_1.resize((589, 121), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=3, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                    Len                   """, font=("20")).pack()

    Label(lbl_sequence, text="""\nit is possible to find out the length, or how many index are there 
    in a string, this is achieveable using the `len()` function.\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_12.PNG")
    grui_1 = grui_1.resize((644, 102), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=3, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                    In operator                   """, font=("20")).pack()

    Label(lbl_sequence, text="""\n`in` is used to check if a certain letter or word in inside the 
    described string. Returning either a boolean value "True" or "False".\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_13.PNG")
    grui_1 = grui_1.resize((224, 174), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=3, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                    The ASCII Table                   """, font=("20")).pack()

    Label(lbl_sequence, text="""\nASCII stands for American Standard Code for Information Interchange, a 
    character encoding standard for electronic communication. This means that each character is 
    represented by a unique number for storage and manipulation by the computers.\n""", font=("13")).pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=5, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                    Range Objects                   """, font=("20")).pack()

    Label(lbl_sequence, text="""\nThe `range` type represents an immutable sequence of numbers and is 
    commonly used for looping a specific number of times in `for` loops. We use the `range()` function 
    to create a range type object.\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_14.PNG")
    grui_1 = grui_1.resize((225, 142), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n"i" in the forloop can be any variable, while range(index) is 
    what deterines how many times the syntax inside the loop is performed. And Since the range is "5", it will 
    print the value variable i 5 times, while increasing its value until variable i isnt less than 5 anymore.\n""",
          font=("13")).pack()

    grui_1 = Image.open("sequence_15.PNG")
    grui_1 = grui_1.resize((230, 127), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\nSimilar to the loop earlier, but a limiting 
    starting range, making the program print from 1 instead.\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_16_a.PNG")
    grui_1 = grui_1.resize((259, 139), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\nIt is also possible to add a increment number, wherein instead of 
    adding by values of 1, it instead increases by the 3rd value set inside `range()`\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_16.PNG")
    grui_1 = grui_1.resize((265, 141), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\nAnother possible feature is counting them in reverse, 
    by changing the [end] and [step] value to negative, we may be able to count backwards.\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_17.PNG")
    grui_1 = grui_1.resize((288, 212), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=3, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                    Lists                   """, font=("20")).pack()

    Label(lbl_sequence, text="""\na `list` is a sequence of data. these lists can hold different types of data inside them.
    Keep in mind that lists can store DIFFERENT data types in the same list

    Lists may be constructed in several ways:\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_18.PNG")
    grui_1 = grui_1.resize((570, 81), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    grui_1 = Image.open("sequence_19.PNG")
    grui_1 = grui_1.resize((648, 223), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=3, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                    Indexing                   """, font=("20")).pack()

    Label(lbl_sequence, text="""\nIt is also possible to index lists, using the same manner as indexing strings\n""",
          font=("13")).pack()

    grui_1 = Image.open("sequence_20.PNG")
    grui_1 = grui_1.resize((314, 115), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\nOr using for loops\n""",
          font=("13")).pack()

    grui_1 = Image.open("sequence_21.PNG")
    grui_1 = grui_1.resize((316, 190), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\nWith the use of for loops, it is possible to even 
    conduct arithmetic given the correct tables\n""", font=("13")).pack()

    grui_1 = Image.open("sequence_22.PNG")
    grui_1 = grui_1.resize((713, 181), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence,
          text="""\nIt is also possible to loop over every item in a list, this is called an "iteration"\n""",
          font=("13")).pack()

    grui_1 = Image.open("sequence_23.PNG")
    grui_1 = grui_1.resize((265, 148), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\n""").pack()

    lbl_sequence_header = LabelFrame(lbl_sequence, borderwidth=3, bg="black")
    lbl_sequence_header.pack()
    Label(lbl_sequence_header, text="""                    Tuples                   """, font=("20")).pack()

    Label(lbl_sequence, text="""\nTuples are very similar to lists, the only difference they have is that the 
    elements inside Tuples cannot be modified, added to lists, or removed. 

    Tuples are made using open and closed parenthesis `()`

    So, why use Tuples over Lists? Tuples are immutable, this makes them much more secure.
    This also makes it easier to optimize the program.\n""",
          font=("13")).pack()

    grui_1 = Image.open("sequence_24.PNG")
    grui_1 = grui_1.resize((578, 122), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\nWe can also iterate and index over tuples. even slice them\n""",
          font=("13")).pack()

    grui_1 = Image.open("sequence_25.PNG")
    grui_1 = grui_1.resize((346, 242), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_sequence, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_sequence, text="""\nAll these tips will help you discover functions and troubleshoot on your own.
    Not only for the sake of library importing but in your ATLAS and Python journey as a whole!\n""",
          font=("13")).pack()

    Label(lbl_sequence,
          text="""\n\nPractice Questions""",
          anchor=W, font=("20")).pack()
    global lbl_questions_sequence
    lbl_questions_sequence = LabelFrame(lbl_sequence, padx=80, pady=80)
    lbl_questions_sequence.pack()

    Label(lbl_questions_sequence, text="""A positionally ordered collection of other objects.\n""",
          font=("13")).pack()

    global radio_var_pques_sequence
    radio_var_pques_sequence = IntVar()
    radio_var_pques_sequence.set(-1)
    radio1_1 = Radiobutton(lbl_questions_sequence, text="Sequence", font=("12"),
                           variable=radio_var_pques_sequence, value=0)
    radio1_1.pack()

    radio2_1 = Radiobutton(lbl_questions_sequence, text="Iteration", font=("12"),
                           variable=radio_var_pques_sequence, value=1)
    radio2_1.pack()

    radio3_1 = Radiobutton(lbl_questions_sequence, text="Containers", font=("12"),
                           variable=radio_var_pques_sequence, value=2)
    radio3_1.pack()

    radio4_1 = Radiobutton(lbl_questions_sequence, text="Lists", font=("12"),
                           variable=radio_var_pques_sequence, value=3)
    radio4_1.pack()

    global pques_b_sequence
    pques_b_sequence = Button(lbl_questions_sequence, text="Submit!", command=submit_pques1_sequence)
    pques_b_sequence.pack()


def submit_2_dfs():
    x = radio_var_2_dfs.get()
    if x == 3:
        Label(lbl_questions_dfs, text="Correct\n You are ready for your Proficiency Test", fg="green").pack()
        pques_dfs_2["state"] = "disabled"
        test_dfs_b = Button(lbl_questions_dfs, text="Proceed to Test", command=test_dfs)
        test_dfs_b.pack()

    elif x != 3:
        Label(lbl_questions_dfs, text="Incorrect, remember the capabilities!", fg="red").pack()


def pques_2_dfs():
    Label(lbl_questions_dfs,
          text="""\nWhat can we iterate in?\n""", font=("13")).pack()

    global radio_var_2_dfs
    radio_var_2_dfs = IntVar()
    radio_var_2_dfs.set(-1)
    radio1_2 = Radiobutton(lbl_questions_dfs, text=r'Keys', font=("12"), variable=radio_var_2_dfs,
                           value=0)
    radio1_2.pack()

    radio2_2 = Radiobutton(lbl_questions_dfs, text=r'Values', font=("12"), variable=radio_var_2_dfs,
                           value=1)
    radio2_2.pack()

    radio3_2 = Radiobutton(lbl_questions_dfs, text=r'None of the above', font=("12"), variable=radio_var_2_dfs,
                           value=2)
    radio3_2.pack()

    radio4_2 = Radiobutton(lbl_questions_dfs, text=r'Both', font=("12"), variable=radio_var_2_dfs,
                           value=3)
    radio4_2.pack()

    global pques_dfs_2
    pques_dfs_2 = Button(lbl_questions_dfs, text="Submit!", command=submit_2_dfs)
    pques_dfs_2.pack()


def submit_pques1_dfs():
    x = radio_var_pques_dfs.get()
    if x == 2:
        Label(lbl_questions_dfs, text="Correct", fg="green").pack()
        pques_b_dfs["state"] = "disabled"
        pques_2_dfs()
    elif x != 2:
        Label(lbl_questions_dfs, text="Rememeber the term!!", fg="red").pack()


def start_dfs_module():
    global dfs
    dfs = Toplevel(screen)
    dfs.geometry("1280x720")
    dfs.iconbitmap('icon.ico')
    Label(dfs, text="Welcome " + username1.title() + " to your Dictionaries,files,and sets programming Lesson!",
          font=("Helvetica", "13", "bold")).pack()

    window = ScrolledFrame(dfs)
    window.pack(expand=True, fill='both')

    lbl_dfs = LabelFrame(window.inner)
    lbl_dfs.pack()

    Label(lbl_dfs, text="""\n""").pack()

    lbl_dfs_header = LabelFrame(lbl_dfs, borderwidth=5, bg="black")
    lbl_dfs_header.pack()
    Label(lbl_dfs_header, text="""                       Dictionaries                        """, font=("20")).pack()

    Label(lbl_dfs, text="""\nBack in module 3, we were able to discuss tuples and lists which can be used to store data. 
    But what if we wanted to store larger amounts of data? There's another collection up for the job, Dictionaries.

    Dictionaries, contrary to their aforementioned counterparts, mapp their data via key instead of relative position.

    Dictionaries are made using a pair of empty braces: `{}`
    """,
          font=("13")).pack()

    grui_1 = Image.open("dfs_1.png")
    grui_1 = grui_1.resize((623, 78), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\nAs you noticed above, these entries may come in pairs

    for example, "My" is what we would call the `entry` <br>
    paired with a 2 separated by a semicolon, we call the value 2 the `key`

    with this setup in mind, we can now call for a specific entry:\n""",
          font=("13")).pack()

    grui_1 = Image.open("dfs_2.PNG")
    grui_1 = grui_1.resize((297, 77), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\nNotice how we called for the entry "My" . But the 
    output, rather than the entry, was the key value associated to it, which is 2 

    But what if the entry isn't found in the dictionary? normally it would return an error
    One way to supplement this is using get(). this function avoids an error, allowing us 
    to set a default return value. Think of it as an else statement just in case the entry isn't in the dictionary.

    \n""", font=("13")).pack()

    lbl_dfs_header = LabelFrame(lbl_dfs, borderwidth=5, bg="black")
    lbl_dfs_header.pack()
    Label(lbl_dfs_header, text="""                       Not using get()                       """, font=("20")).pack()

    Label(lbl_dfs, text="""\n""").pack()

    grui_1 = Image.open("dfs_3.PNg")
    grui_1 = grui_1.resize((604, 146), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\n""").pack()

    lbl_dfs_header = LabelFrame(lbl_dfs, borderwidth=5, bg="black")
    lbl_dfs_header.pack()
    Label(lbl_dfs_header, text="""                       Using get()                       """, font=("20")).pack()

    Label(lbl_dfs, text="""\n""").pack()

    grui_1 = Image.open("dfs_4.PNG")
    grui_1 = grui_1.resize((683, 68), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\n\n\n""").pack()

    lbl_dfs_header = LabelFrame(lbl_dfs, borderwidth=5, bg="black")
    lbl_dfs_header.pack()
    Label(lbl_dfs_header, text="""                       Iteration                       """, font=("20")).pack()

    Label(lbl_dfs, text="""\nWe can also use `in` to iterate over, keys, values, or even both\n""", font=("13")).pack()

    grui_1 = Image.open("dfs_5.PNG")
    grui_1 = grui_1.resize((486, 398), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\nIf we want to, we can also re-assign a specific value by specifying their key\n""",
          font=("13")).pack()

    grui_1 = Image.open("dfs_6.PNG")
    grui_1 = grui_1.resize((628, 132), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\nThe syntax above also adds a new value and key into the dictionary if it does not exist yet

    It is also possible to remove a key and value inside the dictionary using the 'pop()' method\n""",
          font=("13")).pack()

    grui_1 = Image.open("dfs_7.PNG")
    grui_1 = grui_1.resize((628, 139), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\n""").pack()

    lbl_dfs_header = LabelFrame(lbl_dfs, borderwidth=5, bg="black")
    lbl_dfs_header.pack()
    Label(lbl_dfs_header, text="""                    Sets                   """, font=("20")).pack()

    Label(lbl_dfs, text="""\nSets, unlike their previous counterparts, is an unordered collection with no 
    duplicate elements, meaning that it will not accept the same entry more than once.

    the format for creating a set is using `set()` or curly braces `{}`\n""", font=("13")).pack()

    grui_1 = Image.open("dfs_8.PNG")
    grui_1 = grui_1.resize((374, 132), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\n""").pack()

    lbl_dfs_header = LabelFrame(lbl_dfs, borderwidth=5, bg="black")
    lbl_dfs_header.pack()
    Label(lbl_dfs_header, text="""                    Set Operations                   """, font=("20")).pack()

    Label(lbl_dfs, text="""\nSets are allowed to have the mathematical operations done on them\n""", font=("13")).pack()

    grui_1 = Image.open("dfs_9.PNG")
    grui_1 = grui_1.resize((391, 571), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\n""").pack()

    lbl_dfs_header = LabelFrame(lbl_dfs, borderwidth=3, bg="black")
    lbl_dfs_header.pack()
    Label(lbl_dfs_header, text="""                    Files                   """, font=("20")).pack()

    Label(lbl_dfs, text="""\nAnother versatile tool by python is it's ability to read, modify, and even create files.

    To open and read files in python we can use the following format:

    variable1 = open('Filename') 
    variable2 = variable.read() 

    print(variable2)\n""", font=("13")).pack()

    grui_1 = Image.open("dfs_10.PNG")
    grui_1 = grui_1.resize((519, 102), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\nOf course, anything that starts must come to a close. 
    Using the .close() function, we can close our file\n""", font=("13")).pack()

    grui_1 = Image.open("dfs_11.PNG")
    grui_1 = grui_1.resize((166, 62), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\nAnother method of opening files is using the with...as format, this method
    removes the need to close the file\n""", font=("13")).pack()

    grui_1 = Image.open("dfs_12.PNG")
    grui_1 = grui_1.resize((511, 117), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\n""").pack()

    lbl_dfs_header = LabelFrame(lbl_dfs, borderwidth=3, bg="black")
    lbl_dfs_header.pack()
    Label(lbl_dfs_header, text="""                    Creating our own file                   """, font=("20")).pack()

    Label(lbl_dfs, text="""\nIn Python, we are also able to write in our file, editing the 
    content and saving it as such\n""", font=("13")).pack()

    grui_1 = Image.open("dfs_13.PNG")
    grui_1 = grui_1.resize((591, 155), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\n Similar to "w", there are different modes available to open()\n""", font=("13")).pack()

    grui_1 = Image.open("dfs_14.PNG")
    grui_1 = grui_1.resize((865, 551), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)
    grui_1_i = Label(lbl_dfs, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_dfs, text="""\n""").pack()

    Label(lbl_dfs,
          text="""\n\nPractice Questions""",
          anchor=W, font=("20")).pack()
    global lbl_questions_dfs
    lbl_questions_dfs = LabelFrame(lbl_dfs, padx=80, pady=80)
    lbl_questions_dfs.pack()

    Label(lbl_questions_dfs, text="""The value that usually pairs with the entry\n""",
          font=("13")).pack()

    global radio_var_pques_dfs
    radio_var_pques_dfs = IntVar()
    radio_var_pques_dfs.set(-1)
    radio1_1 = Radiobutton(lbl_questions_dfs, text="Value", font=("12"),
                           variable=radio_var_pques_dfs, value=0)
    radio1_1.pack()

    radio2_1 = Radiobutton(lbl_questions_dfs, text="Boolean", font=("12"),
                           variable=radio_var_pques_dfs, value=1)
    radio2_1.pack()

    radio3_1 = Radiobutton(lbl_questions_dfs, text="Key", font=("12"),
                           variable=radio_var_pques_dfs, value=2)
    radio3_1.pack()

    radio4_1 = Radiobutton(lbl_questions_dfs, text="Declaration", font=("12"),
                           variable=radio_var_pques_dfs, value=3)
    radio4_1.pack()

    global pques_b_dfs
    pques_b_dfs = Button(lbl_questions_dfs, text="Submit!", command=submit_pques1_dfs)
    pques_b_dfs.pack()


def submit_2_numpy():
    x = radio_var_2_numpy.get()
    if x == 3:
        Label(lbl_questions_numpy, text="Correct\n You are ready for your Proficiency Test", fg="green").pack()
        pques_numpy_2["state"] = "disabled"
        test_numpy_b = Button(lbl_questions_numpy, text="Proceed to Test", command=test_numpy)
        test_numpy_b.pack()

    elif x != 3:
        Label(lbl_questions_numpy, text="Incorrect! Check the terms", fg="red").pack()


def pques_2_numpy():
    Label(lbl_questions_numpy,
          text="""\nWhich of the following is NOT a function in NumPy?""", font=("13")).pack()

    global radio_var_2_numpy
    radio_var_2_numpy = IntVar()
    radio_var_2_numpy.set(-1)
    radio1_2 = Radiobutton(lbl_questions_numpy, text=r'np.concatenate', font=("12"), variable=radio_var_2_numpy,
                           value=0)
    radio1_2.pack()

    radio2_2 = Radiobutton(lbl_questions_numpy, text=r'np.delete', font=("12"), variable=radio_var_2_numpy,
                           value=1)
    radio2_2.pack()

    radio3_2 = Radiobutton(lbl_questions_numpy, text=r'np.remainder', font=("12"), variable=radio_var_2_numpy,
                           value=2)
    radio3_2.pack()

    radio4_2 = Radiobutton(lbl_questions_numpy, text=r'np.repetition', font=("12"), variable=radio_var_2_numpy,
                           value=3)
    radio4_2.pack()

    global pques_numpy_2
    pques_numpy_2 = Button(lbl_questions_numpy, text="Submit!", command=submit_2_numpy)
    pques_numpy_2.pack()


def submit_pques1_numpy():
    x = radio_var_pques_numpy.get()
    if x == 0:
        Label(lbl_questions_numpy, text="Correct", fg="green").pack()
        pques_b_numpy["state"] = "disabled"
        pques_2_numpy()
    elif x != 0:
        Label(lbl_questions_numpy, text="Remember the term!", fg="red").pack()


def start_numpy_module():
    global numpy
    numpy = Toplevel(screen)
    numpy.geometry("1280x720")
    numpy.iconbitmap('icon.ico')
    Label(numpy, text="Welcome " + username1.title() + " to your numpy and iteration programming Lesson!",
          font=("Helvetica", "13", "bold")).pack()

    window = ScrolledFrame(numpy)
    window.pack(expand=True, fill='both')

    lbl_numpy = LabelFrame(window.inner)
    lbl_numpy.pack()

    Label(lbl_numpy, text="""\n""").pack()

    lbl_numpy_header = LabelFrame(lbl_numpy, borderwidth=5, bg="black")
    lbl_numpy_header.pack()
    Label(lbl_numpy_header, text="""                       What is NumPy?                        """,
          font=("20")).pack()

    Label(lbl_numpy, text="""\nNumpy is a core library for scientific computing in python. This library provides 
    multiple multidimensional array objects. Providing array data structure specially useful for data science.
    Furthermore, as it is more compact and easier to read and write on, making this library very convenient and efficient.
    """,
          font=("13")).pack()

    lbl_numpy_header = LabelFrame(lbl_numpy, borderwidth=5, bg="black")
    lbl_numpy_header.pack()
    Label(lbl_numpy_header, text="""                       Importing NumPy                        """,
          font=("20")).pack()

    Label(lbl_numpy, text="""\nAccording to what we learned in the libraries module,
     we will need to import the library first before being able to use it.
     """,
          font=("13")).pack()

    grui_1 = Image.open("numpy_1.PNG")
    grui_1 = grui_1.resize((199, 47), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_numpy, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_numpy, text="""\n""", font=("13")).pack()

    lbl_numpy_header = LabelFrame(lbl_numpy, borderwidth=5, bg="black")
    lbl_numpy_header.pack()
    Label(lbl_numpy_header, text="""                       Declaring Arrays                        """,
          font=("20")).pack()

    Label(lbl_numpy, text="""\nTo fully utilize this library, we learn about the concept of arrays.

    But for this module we will further focus on 2D arrays
    these arrays follow the concept of the XY axis coordinate system
       """,
          font=("13")).pack()

    grui_1 = Image.open("numpy_2.PNG")
    grui_1 = grui_1.resize((226, 80), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_numpy, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_numpy, text="""\nThe array above would print in the form of:

 [2,5,-6]
 [4,-4,3]
 [1,3,-5] 

Similar to the form of rows and columns, all these files cabn be accesed in the 2d axis form of slicing, as such:

           """,
          font=("13")).pack()

    grui_1 = Image.open("numpy_3.PNG")
    grui_1 = grui_1.resize((226, 88), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_numpy, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_numpy, text="""\nUsing print(A:[0,1]), where in A is the 2d array and [0,1] is the slicing parameter:

0 identifies the first row, as slicing starts from 0. <br>
1:2 which is seperated by comma: , where in 1 identifies the second element from the first row

Due to these parameters, the syntax above will display "5"
""",
          font=("13")).pack()

    Label(lbl_numpy, text="""\nBelow are more examples of functions that show the attributes of numpy arrays
    with `array` to represent numpy arrays:

1. array.ndim
Displays the number of axis the array has

2. array.shape
Shows the dimensions of the array using the syntax n rows and m columns by default (n,m)

3. array.size
Outputs the total number of elements in the array, equaling to the product of the elements

4. array.dtype
Describes the type of the elements/content inside the arary.

5. array.itemsize
Displays the size of bytes in each eelement of the array (this depends on the type of the items inside the array)

             """,
          font=("13")).pack()

    grui_1 = Image.open("numpy_4.PNG")
    grui_1 = grui_1.resize((230, 368), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_numpy, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    lbl_numpy_header = LabelFrame(lbl_numpy, borderwidth=5, bg="black")
    lbl_numpy_header.pack()
    Label(lbl_numpy_header, text="""                       Basic NumPy Arithmetic                        """,
          font=("20")).pack()

    Label(lbl_numpy, text="""\nIt is also possible to perform arithmetic functions on these
     arrays. Keep in mind they need to be the SAME shape or it result to broadcasting rules (distributing smaller array to bigger array)
    \n""",
          font=("13")).pack()

    lbl_numpy_header = LabelFrame(lbl_numpy, borderwidth=3, bg="black")
    lbl_numpy_header.pack()
    Label(lbl_numpy_header, text="""                       In Library Arithmetic                        """,
          font=("20")).pack()

    Label(lbl_numpy, text="""\nnp.add(a,b)
- Performs basic addition on the arrays

np.subtract(a,b)
- Performs subtraction on the arrays

np.multiply(a,b)
- performs multiplication on the arrays

np.divide(a,b)
- performs division

    \n""",
          font=("13")).pack()

    grui_1 = Image.open("numpy_5.PNG")
    grui_1 = grui_1.resize((405, 553), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_numpy, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_numpy, text="""\n""").pack()

    lbl_numpy_header = LabelFrame(lbl_numpy, borderwidth=5, bg="black")
    lbl_numpy_header.pack()
    Label(lbl_numpy_header, text="""                        Other useful Functions                          """,
          font=("20")).pack()

    Label(lbl_numpy, text="""\nSnp.sort()
- similar to other containers, it is also possible to sort items inside the array, arranging them in increasing to decreasing / alphabetical order depending on the items.

np.concatenate()
- As the functions says, it is used to concatenate arrays, adding them to each other

array.flatten()
- "Flattens" multiple arrays, meaning that they would all be commbined into one, big array

np.append(a,b)
- Adds items to the array, similar to list appending

np.insert(a,1,5)
- inserts items to array
wherein 1 is how many objects are being inserted and 5 is the value you want to add.

np.delete(a,[0])
- deletes items from the array, keep in note `[]` uses the indexing/slicing format
    \n""", font=("13")).pack()

    grui_1 = Image.open("numpy_6.PNG")
    grui_1 = grui_1.resize((327, 531), Image.ANTIALIAS)
    grui_1 = ImageTk.PhotoImage(grui_1)

    grui_1_i = Label(lbl_numpy, image=grui_1)
    grui_1_i.image = grui_1
    grui_1_i.pack()

    Label(lbl_numpy, text="""\n""").pack()

    Label(lbl_numpy,
          text="""\n\nPractice Questions""",
          anchor=W, font=("20")).pack()
    global lbl_questions_numpy
    lbl_questions_numpy = LabelFrame(lbl_numpy, padx=80, pady=80)
    lbl_questions_numpy.pack()

    Label(lbl_questions_numpy, text="""Container that NumPy generally uses\n""",
          font=("13")).pack()

    global radio_var_pques_numpy
    radio_var_pques_numpy = IntVar()
    radio_var_pques_numpy.set(-1)
    radio1_1 = Radiobutton(lbl_questions_numpy, text="Arrays", font=("12"),
                           variable=radio_var_pques_numpy, value=0)
    radio1_1.pack()

    radio2_1 = Radiobutton(lbl_questions_numpy, text="2d Arrays", font=("12"),
                           variable=radio_var_pques_numpy, value=1)
    radio2_1.pack()

    radio3_1 = Radiobutton(lbl_questions_numpy, text="3d Arrays", font=("12"),
                           variable=radio_var_pques_numpy, value=2)
    radio3_1.pack()

    radio4_1 = Radiobutton(lbl_questions_numpy, text="Matrices", font=("12"),
                           variable=radio_var_pques_numpy, value=3)
    radio4_1.pack()

    global pques_b_numpy
    pques_b_numpy = Button(lbl_questions_numpy, text="Submit!", command=submit_pques1_numpy)
    pques_b_numpy.pack()


mscreen()

screen.mainloop()
