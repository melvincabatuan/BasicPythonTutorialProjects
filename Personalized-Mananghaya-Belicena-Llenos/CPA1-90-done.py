#!/usr/bin/env python
# coding: utf-8

# In[8]:


from tkinter import *

#from PIL import Image, ImageTk

window = Tk()
window.title("Assessment Test")

#Header
myLabel1 = Label(window, text = "HELLO! BEFORE WE START ")
myLabel1.grid(row = 0, column = 0)
myLabel2 = Label(window, text = "WE NEED TO ASSESS YOUR SKILLS ")
myLabel2.grid(row = 1 , column = 0) 
myLabel3 = Label(window, text = "IN PROGRAMMING")
myLabel3.grid(row = 2, column = 0)

A1 = Label(window,text = "---------------------------")
A1.grid(row = 3, column = 0)
#-------------------------------------------------------------------------------------------------------------------------------
def gameE():
    exit(0)
        
#-------------------------------------------------------------------------------------------------------------------------------
def gameT(): #Part Test
    game_T = Tk()
    game_T.title("Pythomon")
    game_T_1 = Label(game_T, text = "Badge test").grid(row=1)
    game_T_2 = Label(game_T, text = " ").grid(row=2)
    game_T_3 = Label(game_T, text = " ").grid(row=3)
#type here
    problem = StringVar()
    game_T_4 = Label(game_T, text = " Answer this problem:\n\t Write a line of code that will output the string python").grid(row=3)
    game_T_5 = Entry(game_T, width = 30, borderwidth = 2, textvariable = problem)
    game_T_5.grid(row = 4)
    
    def Submit():
        submitRoot= Tk()
        a = r'print("python")'
        submitframe = Frame(submitRoot,padx =5, pady = 5)
        submitframe.grid(row = 0)
        
        if game_T_5.get() == a :
            correct = Label(submitframe, text = "The Police: You are a true python coder").grid(row = 0)
            badge1 = Label(submitframe, text ="The Police: Here you earned this badge..." ).grid(row = 1)
            badge1name = Label(submitframe, text ="You Have unlocked the Magaling Badge no.1...." ).grid(row = 1)
            badge1series = Label(submitframe, text ="You Have unlocked the Magaling Badge Series...." ).grid(row = 3)
        else:
            wrong = Label(submitRoot, text = "The Police: You are a fraud! Don't challenge us if you're not ready yet").grid(row = 0) 
            backbutton = Button(submitRoot, text = "Try Again", command = gameT).grid(row = 2)
            
    game_T_6 = Button(game_T, text = "Submit", command = Submit).grid(row=5)

    #game_T_a = Button(game_P2,text="continue",command = gameE ).grid(row=3)
#-------------------------------------------------------------------------------------------------------------------------------
def gameP2(): #part two
    game_P2 = Tk()
    game_P2.title("Pythomon")
    game_P2_1 = Label(game_P2,text = "Congratulations you beat the cat").grid(row=1)
    game_P2_2 = Label(game_P2,text = " ").grid(row=2)
    game_P2_3 = Label(game_P2,text = "But suddenly you were surprised by the police").grid(row=3)
    game_P2_4 = Label(game_P2,text = "Police: Are you a pytho trainer").grid(row=4)
    game_P2_5 = Label(game_P2,text = "To prove if you are worthy you must undergo the test").grid(row=5)
    game_P2_6 = Button(game_P2,text="continue",command = gameT).grid(row=6)
#-------------------------------------------------------------------------------------------------------------------------------
def gameP2a():#part two lose
    game_P2a = Tk()
    game_P2a.title("Pythomon")
    game_P2a1 = Label(game_P2a,text = "Try Again").grid(row=1)
    game_P2a2 = Button(game_P2a,text="continue",command = gameP).grid(row=2)
#-------------------------------------------------------------------------------------------------------------------------------
def gameP():  #game proper
    game_P = Tk()
    game_P.title("Pythomon")

    PlayerH = 0
    EnemyH = 0

    #Enemy Data
    EnemyH = 5
    Enemy_1 = Label(game_P,text = " LVL 5 Stray Cat").grid(row = 1, column = 0)
    Enemy_1_H = Label(game_P,text = "/-----/ HP 5/5").grid(row = 2, column = 0)
    Enemy_1_2 = Label(game_P,text = "Cat").grid(row = 1, column = 1)
    Enemy_1_2_0 = Label(game_P,text = " ").grid(row = 2, column = 1)

    game_P_1_3 = Label(game_P,text = " ").grid(row = 3, column = 0)

    #Player Data Start from 4
    PlayerH = 5
    Player_1 = Label(game_P,text = "LVL 1 Snake").grid(row = 4, column = 1)
    Player_1_H = Label(game_P,text = "/-----/ HP 5/5").grid(row = 5, column = 1)
    Player_1_2 = Label(game_P,text = "Snake").grid(row = 4, column = 0)
    Player_1_2_0 = Label(game_P,text = " ").grid(row = 5, column = 0)

    game_P_1_4 = Label(game_P,text = " ").grid(row = 6, column = 0)

    #Condition Text 
    game_P_1_5 = Label(game_P,text = "A wild stray cat appeared").grid(row = 7, column = 0)
    game_P_1_6 = Label(game_P,text = "Use a move to defeat it").grid(row = 8, column = 0)

    game_P_1_7 = Label(game_P,text = " ").grid(row = 9, column = 0)

    #Updating Text
    game_P_1_7 = Label(game_P,text = "The cat is weak against").grid(row = 11, column = 0)
    game_P_1_8 = Label(game_P,text = "data storage").grid(row = 12, column = 0)

    #Movesets
    Move_1 = Button(game_P, text = "Print", command = gameP2a).grid(row =13, column = 0)
    Move_2 = Button(game_P, text = "Variable", command = gameP2).grid(row =14, column = 0)
    Move_3 = Button(game_P, text = "Manipulate", command = gameP2a).grid(row =13, column = 1)
    Move_4 = Button(game_P, text = "Function", command = gameP2a).grid(row =14, column = 1)
#-------------------------------------------------------------------------------------------------------------------------------
def gameI4(): #Intro part 4
    game_I4    = Tk()
    game_I4_1  = Label(game_I4, text = "Introduction 4").grid(row=1)
    game_I4_2  = Label(game_I4, text = " ").grid(row=2)
    game_I4_3  = Label(game_I4, text = "The fourth and final technique is").grid(row=3)
    game_I4_4  = Label(game_I4, text = "Function").grid(row=4)
    game_I4_5  = Label(game_I4, text = " ").grid(row=5)
    game_I4_6  = Label(game_I4, text = "In the last module we taught you some of python's built-in functions, but did you know you can create your own functions?").grid(row=6)
    game_I4_7  = Label(game_I4, text = "These are called user-defined funcitons.").grid(row=7)
    game_I4_8  = Label(game_I4, text = "he idea is to create a set of statements for a task that is continoulsy repeated throughout your program.").grid(row=8)
    game_I4_9  = Label(game_I4, text = "This makes it a lot easier and efficient becasue instead of writing the same code over and over again for different inputs, you can just call that function.").grid(row=9)
    game_I4_10 = Label(game_I4, text = " ").grid(row=10)
    game_I4_11 = Label(game_I4, text = " ").grid(row=11)
    game_I4_12 = Label(game_I4, text = "The way you write it is like this:\ndef name():\nstatements \nstatements \nreturn statements").grid(row=12)
    game_I4_13  = Label(game_I4, text = "In Python, a function is defined using the def keyword. After doing that step, you must name your function.").grid(row=13) 
    game_I4_14 = Label(game_I4, text = "Remember when naming a function, remember the rules when you name a variable.  Then you can also either pass in arguments or parameters in the parentheses.").grid(row=14) 
    game_I4_15 = Label(game_I4, text = "After that, you can now create the statements that your function will do. ").grid(row=15)
    game_I4_16 = Label(game_I4, text = " ").grid(row=16)
    game_I4_17 = Button(game_I4, text = "continue", command = gameP ).grid(row =17)
    game_I4_18 = Button(game_I4, text = "back", command = gameI3 ).grid(row =17,column = 1)
#-------------------------------------------------------------------------------------------------------------------------------
def gameI3(): #Intro part 3
    game_I3    = Tk()
    game_I3_1  = Label(game_I3, text = "Introduction 3").grid(row=1)
    game_I3_2  = Label(game_I3, text = " ").grid(row=2)
    game_I3_3  = Label(game_I3, text = "The third technique I will show you is").grid(row=3)
    game_I3_4  = Label(game_I3, text = "Manipulation").grid(row=4)
    game_I3_5  = Label(game_I3, text = " ").grid(row=5)
    game_I3_5A = Label(game_I3, text = "As I said before Strings are a special type of python class.").grid(row=6) 
    game_I3_5b = Label(game_I3, text = "The string class is already built-in python so you do not need to import a statement to use the the object interface to strings.").grid(row=7)
    game_I3_6  = Label(game_I3, text = "Dave_3 = Hello World").grid(row=8) 
    game_I3_7  = Label(game_I3, text = "print(Dave_3)").grid(row=9)
    game_I3_8  = Label(game_I3, text = " ").grid(row=10)
    game_I3_9  = Label(game_I3, text = "In python there are various string methods or functions that you can use to manipulate your string.").grid(row=11)
    game_I3_10 = Label(game_I3, text = "However we will not tackle all of them yet, we will first discuss the basics").grid(row=12)
    game_I3_11 = Label(game_I3, text = " ").grid(row=13)
    game_I3_12 = Label(game_I3, text = "You can put 2 strings together print (Hello  +  World!)").grid(row=14)
    game_I3_13 = Label(game_I3, text = " ").grid(row=15)   
    game_I3_14 = Button(game_I3,text = "continue", command = gameI4).grid(row=16)
    game_I3_15 = Button(game_I3,text = "back", command = gameI2).grid(row=16,column = 1)
#-------------------------------------------------------------------------------------------------------------------------------
def gameI2(): #Intro part 2
    game_I2    = Tk()
    game_I2_1  = Label(game_I2, text = "Introduction 2").grid(row=1,column=0)
    game_I2_2  = Label(game_I2, text = " ").grid(row=2,column=0)
    game_I2_3  = Label(game_I2, text = "The second technique I will show you is").grid(row=3,column=0)
    game_I2_4  = Label(game_I2, text = "The Variable!").grid(row=4,column=0)
    game_I2_5  = Label(game_I2, text = "This a declaration of data that could be used for other spells.").grid(row=5,column=0)
    game_I2_6  = Label(game_I2, text = "But I warn you there are rules.").grid(row=6,column=0)
    game_I2_7  = Label(game_I2, text = " ").grid(row=7,column=0)
    game_I2_8  = Label(game_I2, text = "1. A variable name cannot be started with a number").grid(row=8,column=0)
    game_I2_9  = Label(game_I2, text = "2. A variable should not have the same name with another variable ").grid(row=9,column=0)
    game_I2_10 = Label(game_I2, text = "3. A variable name should not have the same name with built-in functions ").grid(row=10,column=0)
    game_I2_11 = Label(game_I2, text = "4. A variable can be named with letters and numbers, but cannot be named with only numbers ").grid(row=11,column=0)
    game_I2_12 = Label(game_I2, text = "5. A variable can store be inputted with data by the user and output the same data. ").grid(row=12,column=0)
    game_I2_13 = Label(game_I2, text = "6. Keep the variable name simple and easy to read ").grid(row=13,column=0)
    game_I2_14 = Label(game_I2, text = "7. To see the output of the data use the print function, and inside the parentheses you input the name of the variable ").grid(row=14,column=0)
    game_I2_141= Label(game_I2, text = " ").grid(row=15,column=0)
    game_I2_15 = Button(game_I2, text= "continue", command = gameI3).grid(row=16,column=0)
    game_I2_16 = Button(game_I2, text= "back", command = gameI).grid(row=16,column=1)
#-------------------------------------------------------------------------------------------------------------------------------
def gameI():  #Intro part 1
    game_I = Tk()
    game_I.title("Introduction")
    game_I_1 = Label(game_I, text = "Introduction").grid(row=1,column=0)
    game_I_2 = Label(game_I, text = " ").grid(row=2,column=0)
    game_I_3 = Label(game_I, text = "Hello I'm SSSSSSam the Python, Heir to the Pythomon Clan").grid(row=3,column=0)
    game_I_4 = Label(game_I, text = " ").grid(row=4,column=0)
    game_I_5 = Label(game_I, text = "I need your help to avenge my family").grid(row=5,column=0)
    game_I_6 = Label(game_I, text = " ").grid(row=6,column=0)
    game_I_7 = Label(game_I, text = "The first move is called print").grid(row=7,column=0)
    game_I_7a= Label(game_I, text = " ").grid(row=8,column=0)
    game_I_8 = Label(game_I, text = "An easy move yet reliable one").grid(row=9,column=0)
    game_I_8a= Label(game_I, text = " ").grid(row=10,column=0)
    game_I_9 = Label(game_I, text = """type print("Hello Beginner!")""").grid(row=11,column=0)
    game_I_10= Label(game_I, text = "It will return Hello Beginner").grid(row=12,column=0)
    game_I_11= Button(game_I, text = "Continue", command = gameI2).grid(row=13,column=0)
#-------------------------------------------------------------------------------------------------------------------------------
def Level1():
    Level_1 = Tk()
    Level_1.title("Novice Testing")
    Label_Level_1_1 = Label(Level_1, text = " ").grid(row = 1,column =0)
    Label_Level_1_2 = Label(Level_1, text = "In the bushes....").grid(row = 2,column =0)
    Label_Level_1_3 = Label(Level_1, text = " ").grid(row = 3,column =0)
    Label_Level_1_4 = Label(Level_1, text = " ").grid(row = 4,column =0)
    
    #load = Image.open("snake2.jpg")
    #render = ImageTk.PhotoImage(load)
    #Label_Level_1_5 = Label(Level_1, image = render ).grid(row = 5,column =0)
    #img.image = render
    Label_Level_1_5 = Label(Level_1, text = "Snake").grid(row = 5,column = 0)
    
    Label_Level_1_6 = Label(Level_1, text = " ").grid(row = 6,column =0)
    Label_Level_1_7 = Label(Level_1, text = "You have discovered a LVL 1 Python").grid(row = 7, column = 0)
    Label_Level_1_8 = Label(Level_1, text = " ").grid(row = 8, column = 0)
    Label_Level_1_9 = Button(Level_1, text = "Continue", command = gameI ).grid(row = 9, column = 0)
#-------------------------------------------------------------------------------------------------------------------------------
def Level2():
    Level_2 = Tk()
    Level_2.title("Beginner Testing")
    Label_Level_2_1 = Label(Level_2, text = " ").grid(row = 1,column =0)
    Label_Level_2_2 = Label(Level_2, text = "In the bushes....").grid(row = 2,column =0)
    Label_Level_2_3 = Label(Level_2, text = " ").grid(row = 3,column =0)
    Label_Level_2_4 = Label(Level_2, text = " ").grid(row = 4,column =0)
    
    #load = Image.open("snake2.jpg")
    #render = ImageTk.PhotoImage(load)
    #Label_Level_1_5 = Label(Level_1, image = render ).grid(row = 5,column =0)
    #img.image = render
    Label_Level_2_5 = Label(Level_2, text = "Snake").grid(row = 5,column = 0)
    
    Label_Level_2_6 = Label(Level_2, text = " ").grid(row = 6,column =0)
    Label_Level_2_7 = Label(Level_2, text = "You have discovered a LVL 10 Python").grid(row = 7, column = 0)
    Label_Level_2_8 = Label(Level_2, text = " ").grid(row = 8, column = 0)
    Label_Level_2_9 = Button(Level_2, text = "Continue", command = gameI ).grid(row = 9, column = 0)
#-------------------------------------------------------------------------------------------------------------------------------
def Level3():
    Level_3 = Tk()
    Level_3.title("Comp Testing")
    Label_Level_3_1 = Label(Level_3, text = " ").grid(row = 1,column =0)
    Label_Level_3_2 = Label(Level_3, text = "In the bushes....").grid(row = 2,column =0)
    Label_Level_3_3 = Label(Level_3, text = " ").grid(row = 3,column =0)
    Label_Level_3_4 = Label(Level_3, text = " ").grid(row = 4,column =0)
    
    #load = Image.open("snake2.jpg")
    #render = ImageTk.PhotoImage(load)
    #Label_Level_1_5 = Label(Level_1, image = render ).grid(row = 5,column =0)
    #img.image = render
    Label_Level_3_5 = Label(Level_3, text = "Snake").grid(row = 5,column = 0)
    
    Label_Level_3_6 = Label(Level_3, text = " ").grid(row = 6,column =0)
    Label_Level_3_7 = Label(Level_3, text = "You have discovered a LVL 20 Python").grid(row = 7, column = 0)
    Label_Level_3_8 = Label(Level_3, text = " ").grid(row = 8, column = 0)
    Label_Level_3_9 = Button(Level_3, text = "Continue", command = gameI ).grid(row = 9, column = 0)
#-------------------------------------------------------------------------------------------------------------------------------
def EntryBoxFunc():
    name = EntryBox.get()
    A2.config(text = "Hello %s!! Please continue and finish your survey!" % (name))

A2 = Label(window, text = "What is your name?")
A2.grid(row = 4, column = 0)

EntryBox = Entry(window)
EntryBox.grid(row = 5, column = 0)
B1 = Button(window, text = "Enter", command = EntryBoxFunc)
B1.grid(row = 6, column = 0)
#-------------------------------------------------------------------------------------------------------------------------------
def Results():
    ReviewRoot = Tk()
    ReviewRoot.title("Your Results")
    Count = 0
    name = EntryBox.get()
    A1 = Label(ReviewRoot, text = "Hello %s These are your results" % (name))
    A1.grid(row = 1,column = 0)
    #Question 1 Review.
    #"Have you ever done programming before? (Y/N)"
    while True:
        if (Q1Y.get() == 0) and (Q1N.get() == 0):
            Label(ReviewRoot, text = "-You forgot to choose one for Question 1").grid(row = 2,column = 0)
            break
        elif (Q1Y.get() == 1) and (Q1N.get() == 1):
            Label(ReviewRoot, text = "-You can only pick one for Question 1").grid(row = 2,column = 0)
            break
        elif (Q1Y.get() == 1):
            Label(ReviewRoot, text = "-You did programming before (1)").grid(row = 2,column = 0)
            Count += 1
            break
        elif (Q1N.get() == 1):
            Label(ReviewRoot, text = "You did not do programming before (1)").grid(row = 2,column = 0)
            break
    #Correct Type (Copypaste)
            
    #Question 2 Review.
    #"Have you taken a programming course before (Y/N)")
    while True:
        if (Q2Y.get() == 0) and (Q2N.get() == 0):
            Label(ReviewRoot, text = "-You forgot to choose for Question 2").grid(row = 3,column = 0)
            break
        elif (Q2Y.get() == 1) and (Q2N.get() == 1):
            Label(ReviewRoot, text = "-You can only pick one for Question 2").grid(row = 3,column = 0)
            break
        elif (Q2Y.get() == 1):
            Label(ReviewRoot, text = "-You did take a programming course before (2)").grid(row = 3,column = 0)
            Count += 1
            break
        elif (Q2N.get() == 1):
            Label(ReviewRoot, text = "You did not do a programming course before (2)").grid(row = 3,column = 0)
            break

    #Question 3 Review.
    #"Have you used python as a language before? (Y/N)"
    while True:
        if (Q3Y.get() == 0) and (Q3N.get() == 0):
            Label(ReviewRoot, text = "-You forgot to choose one for Question 3").grid(row = 4,column = 0)
            break
        elif (Q3Y.get() == 1) and (Q1N.get() == 1):
            Label(ReviewRoot, text = "-You can only pick one for Question 3").grid(row = 4,column = 0)
            break
        elif (Q3Y.get() == 1):
            Label(ReviewRoot, text = "-You did use python before (3)").grid(row = 4,column = 0)
            Count += 1
            break
        elif (Q3N.get() == 1):
            Label(ReviewRoot, text = "You did not use python (3)").grid(row = 4,column = 0)
            break
            
    #Question 4 Review.
    #"Have you used other languages beside python? (Y/N)"
    while True:
        if (Q4Y.get() == 0) and (Q4N.get() == 0):
            Label(ReviewRoot, text = "-You forgot to choose one for Question 4").grid(row = 5,column = 0)
            break
        elif (Q4Y.get() == 1) and (Q4N.get() == 1):
            Label(ReviewRoot, text = "-You can only pick one for Question 4").grid(row = 5,column = 0)
            break
        elif (Q4Y.get() == 1):
            Label(ReviewRoot, text = "-You did use other languages (4)").grid(row = 5,column = 0)
            Count += 1
            break
        elif (Q4N.get() == 1):
            Label(ReviewRoot, text = "-You did not (4)").grid(row = 5,column = 0)
            break
            
    #Question 5 Review.
    #"Have you created a programming project before? (Y/N)"
    while True:
        if (Q5Y.get() == 0) and (Q5N.get() == 0):
            Label(ReviewRoot, text = "-You forgot to choose one for Question 5").grid(row = 6,column = 0)
            break
        elif (Q5Y.get() == 1) and (Q5N.get() == 1):
            Label(ReviewRoot, text = "-You can only pick one for Question 5").grid(row = 6,column = 0)
            break
        elif (Q5Y.get() == 1):
            Label(ReviewRoot, text = "-You did create a programming project before (5)").grid(row = 6,column = 0)
            Count += 1
            break
        elif (Q5N.get() == 1):
            Label(ReviewRoot, text = "-You did not (5)").grid(row = 6,column = 0)
            break
    A2 = Label(ReviewRoot, text = "Your Score is: %s" % (Count))
    A2.grid(row = 7,column= 0)
    
    #Review
    while True:
        if (Count <= 1):
            Label(ReviewRoot, text = "Recommended Difficulty: Novice").grid(row = 8,column = 0)
            break
        elif (Count <= 3):
            Label(ReviewRoot, text = "Recommended Difficulty: Beginner").grid(row = 8,column = 0)
            break
        elif (Count <= 5):
            Label(ReviewRoot, text = "Recommended Difficulty: Coder").grid(row = 8,column = 0)
            break
    
    Label(ReviewRoot, text = "Choose your Difficulty").grid(row = 9,column = 0)
    
    TestButton = Button(ReviewRoot, text = "Novice", command = Level1)
    TestButton.grid(row=11, column = 0)
    TestButton = Button(ReviewRoot, text = "Beginner", command = Level2)
    TestButton.grid(row=12, column = 0)
    TestButton = Button(ReviewRoot, text = "Competent Coder", command = Level3)
    TestButton.grid(row=13, column = 0)   
#-------------------------------------------------------------------------------------------------------------------------------
#Question No.1
Label2 = Label(window, text = "Have you ever done programming before? (Y/N)")
Q1Y = IntVar()
Q1N = IntVar()
CB1 = Checkbutton(window, text = "Yes", variable = Q1Y)
CB2 = Checkbutton(window, text = "No", variable = Q1N)
Label2.grid(row = 7,column = 0)
CB1.grid(row = 8,column = 0)
CB2.grid(row = 9,column = 0)
#Correct Archetype (Copypaste)
#-------------------------------------------------------------------------------------------------------------------------------
#Question No.2
Label3 = Label(window, text = "Have you taken a programming course before (Y/N)")
Q2Y = IntVar()
Q2N = IntVar()
CB3 = Checkbutton(window, text = "Yes", variable = Q2Y)
CB4 = Checkbutton(window, text = "No", variable = Q2N)
Label3.grid(row = 10,column = 0)
CB3.grid(row = 11,column = 0)
CB4.grid(row = 12,column = 0)
#-------------------------------------------------------------------------------------------------------------------------------
#Question No.3
Label4 = Label(window, text = "Have you used python as a language before? (Y/N)")
Q3Y = IntVar()
Q3N = IntVar()
CB5 = Checkbutton(window, text = "Yes", variable = Q3Y)
CB6 = Checkbutton(window, text = "No", variable = Q3N)
Label4.grid(row = 13,column = 0)
CB5.grid(row = 14,column = 0)
CB6.grid(row = 15,column = 0)
#-------------------------------------------------------------------------------------------------------------------------------
#Question No.4
Label5 = Label(window, text = "Have you used other languages beside python? (Y/N)")
Q4Y = IntVar()
Q4N = IntVar()
CB7 = Checkbutton(window, text = "Yes", variable = Q4Y)
CB8 = Checkbutton(window, text = "No", variable = Q4N)
Label5.grid(row = 16,column = 0)
CB7.grid(row = 17,column = 0)
CB8.grid(row = 18,column = 0)
#-------------------------------------------------------------------------------------------------------------------------------
#Question No.5
Label6 = Label(window, text = "Have you created a programming project before? (Y/N)")
Q5Y = IntVar()
Q5N = IntVar()
CB9 = Checkbutton(window, text = "Yes", variable = Q5Y)
CB10 = Checkbutton(window, text = "No", variable = Q5N)
Label6.grid(row = 19,column = 0)
CB9.grid(row = 20,column = 0)
CB10.grid(row = 21,column = 0)
#-------------------------------------------------------------------------------------------------------------------------------
#Last Button 
ResultsButton = Button(window, text = "Results", command = Results)
ResultsButton.grid(row=22, column = 0)
#-------------------------------------------------------------------------------------------------------------------------------
#Main
window.mainloop()

