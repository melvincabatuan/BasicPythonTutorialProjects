from sampleoutput import basicHtmlParse, quizHtmlParse

import tkinter as tk

root = tk.Tk()
root.geometry('1280x720')
root.title("IndiePy: A Personalized Learning Platform")

# --- Create Banner ---
banner=tk.Frame(root, height=170, bg="#%02x%02x%02x"%(0,51,102) )
banner.pack(fill='both')


# --- Event Bindings ---
def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    content.configure(scrollregion=content.bbox('all'))


def on_configure_table(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    table.configure(scrollregion=table.bbox('all'))
    
    
# --- Refresh Page Function ---
def update(file):
  global contentFrame
  contentFrame.destroy()
  contentFrame = tk.Frame(content, padx=50, pady=20, bg="white")
  content.create_window((0,0), window=contentFrame, anchor="nw", width=1035)
  contentFrame.bind("<Configure>", on_configure)
  if file.lower().startswith("sample") or file.lower().startswith("assess"):
    quizHtmlParse(file, contentFrame, content)  
  else:
    basicHtmlParse(file, contentFrame)  
  
# --- create table canvas with scrollbar ---
table = tk.Canvas(root)
table.pack(side=tk.LEFT, fill="y")

tableScrollbar = tk.Scrollbar(root, command=table.yview)
tableScrollbar.pack(side=tk.LEFT, fill='y')

table.configure(width=200)
table.configure(yscrollcommand = tableScrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
table.bind('<Configure>', on_configure_table)


# --- create content canvas with scrollbar ---

content = tk.Canvas(root)
content.configure(width=1035, bg="white")

content.pack(side=tk.LEFT, fill="both")

scrollbar = tk.Scrollbar(root, command=content.yview)
scrollbar.pack(side=tk.LEFT, fill='y')

content.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
content.bind('<Configure>', on_configure)

# --- put contentFrame in content---

contentFrame = tk.Frame(content, padx=50, pady=20, bg="white")

#the width part is ugly, but necessary 
content.create_window((0,0), window=contentFrame, anchor="nw", width=1035)


# --- put tableFrame in table ---

tableFrame = tk.Frame(table, bg="white")
table.create_window((0,0), window=tableFrame, anchor='nw', width=200 )

# --- initialize list of file names in dictionary ---
tableContent={
    
    "Introduction": "intro.txt",
	"User's Manual": "userManual.txt",
    "Assessment Test": "assess.txt",
    "Print and Comment": "PrintComment.txt",
    "Print and Comment Challenge Exercises": "PrintCommentChallenge.txt",
    "Arithmetic Operators": "ArithmeticOperators.txt",
    "Practice Exercise For Arithmetic & Assignment Operators": "samplearithmetic.txt",
    "Relational Operators": "RelationalOperators.txt",
    "Logical Operators": "LogicalOperators.txt",
    "Practice Exercise For Relational & Logical Operators": "samplerelalogi.txt",
    "Bitwise Operators": "BitwiseOperators.txt",
    "Challenge Exercise For Basic Operators": "ChallengeOperators.txt",
    "Some Helpful Functions": "SomeHelpfulFunctions.txt",
    "Decision Statements": "DecisionStatements.txt",
    "Practice Exercises For Decision Statements": "sampledecisionstatement.txt",
    "Challenge Exercises For Decision Statements": "DecisionStatementsChallenge.txt",
    "Loop Structures": "loops1.txt",
    "Practice Exercise For Loop Structures": "sampleloop1.txt",
    "Loop Statements": "loops2.txt",
    "Practice Exercise For Loop Statements": "sampleloop2.txt",
    "Challenge Exercises For Loops": "chalLoops.txt",
    "Sequence Functions Part I": "SeqFunc1.txt",
	"Sequence Functions Part II": "SeqFunc2.txt",
    "Practice Exercise For Sequence Functions": "samplesequencefunctions.txt",
    "Strings": "Strings.txt",
    "Practice Exercise for Strings": "samplestrings1.txt",
    "Indexing and Slicing": "IndexSlice.txt",
    "Practice Exercise for Indexing and Slicing": "samplestrings2.txt",
    "Check & Concatenate Strings": "CheckConcatenate.txt",
    "Escape Characters & Raw Strings": "EscapeCharac.txt",
    "Practice Exercises for Escape Characters": "samplestrings3.txt",
    "String Formatting": "StringFormatting.txt",
    "String Formatting Practice Exercise": "samplestrings4.txt",
    "String Methods": "StringMethods.txt",
    "Practice Exercises For String Methods": "samplestrings5.txt",
    "Lists Part I": "list1.txt",
    "Lists Quiz I": "samplelist1.txt",
    "List Part II": "list2.txt",
    "Lists Quiz II": "samplelist2.txt",
    "Tuples": "tuple.txt",
    "Sets": "sets.txt",
    "Dictionaries": "dictionary.txt",
    "Sample Exercises For Dictionaries": "sampledictionary.txt",
    "Challenge Exercises For Data Structures": "sequencechallenge.txt",
    "File Handling": "FileHandling.txt",
    "Challenge Exercises": "ChallengeFile.txt",
    "Functions": "functions.txt",
    "Sample Exercises For Functions": "samplefunction.txt",
    "Scope": "scope.txt",
    "Recursive Functions": "recursivefunctions.txt",
    "Lambda Functions": "lambda.txt",
    "Practice Exercises For Lambda": "samplelambda.txt",
    "Challenge Exercises For Functions": "functionchallenge.txt",
    "Try and Except": "TryandExcept.txt",
    "Try and Except quiz": "sampletryexcept.txt",
    "Try and Except challenge": "chalTryandExcept.txt",
    "NumPy I": "Numpy.txt",
    "NumPy II": "numpy2.txt",
    "Challenge Exercises Numpy": "NumPyChallenge.txt",
    "Tkinter Introduction": "tkinterintro.txt",
    "Tkinter Widgets": "widgets.txt",
    "Tkinter Color Game": "colorgame.txt"}

# --- add widgets in tableFrame ---

for name in tableContent.keys():
  try:
    bt=tk.Button(tableFrame, text=name, font="Arial 14",
                 justify="left", padx=10, wraplength=150, command=lambda name=name: update(tableContent[name]))
    bt.pack(fill="both")
    update(tableContent[name])
  except FileNotFoundError:
    print(name+"is not found")
  except:
    print(name+"is too long")

# --- add widgets in contentFrame ---
    

update("intro.txt")

# --- start program ---

root.mainloop()
