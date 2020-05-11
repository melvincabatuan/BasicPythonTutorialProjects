import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


# Function for parsing content and challenge exercise text files
def basicHtmlParse(file, frame):
  #open file
  with open(file, "r", encoding="utf8") as html:
    html=html.read()
  
  global hintStr
  headerTags={key:('arial', value, 'bold') for key, value in zip(["<h%d>"%i for i in range(1,7)], [32, 28, 24, 20, 18, 16])}
  startExample, endExample=0, 0
  startHint=index=0
  hintStr=[]
  
  def hint(index):
    messagebox.showinfo("Hint", hintStr[index])
  
  for count, i in enumerate(html.splitlines()):
    i=i.strip()

  #|------<p> tag ----------|
    if i.startswith("<p>") and i.endswith("</p>"):
      style="Arial 14"
      i=i.replace("<p>", "").replace("</p>", "")
      text=tk.Label(frame, text=i, font=style)

  #|------<br> tag ----------|
    elif i=="<br>":
      style="Arial 14"
      i=" "
      text=tk.Label(frame, text=i, font=style)
      
    #|------<h1-6> tags ----------|
    elif i[0:4] in headerTags.keys():
      style=headerTags[i[0:4]]
      i=i.replace("</", "<").replace(i[0:4], '')
      text=tk.Label(frame, text=i, font=style)

    #|------<img> tags----------|     
    elif i.startswith("<") and i.endswith(">") and i[1:].startswith("img"):
      global photo       
      #|--------------- Get the Source ---------------|
      startSrc=i.find("\"", i.find("=", i.find("src")+1)+1)+1
      if startSrc!=-1:
        endSrc=i.find("\"", startSrc)
        img = i[startSrc:endSrc].replace("\"", "")
        photo = Image.open(img)        
        #|--------------- Get the width ---------------|
        startWidth=i.find("\"", i.find("=", i.find("width", endSrc)+1)+1)+1
        if startWidth!=-1 and "width" in i:
          endWidth=i.find("\"", startWidth)
          
          imageWidth, imageHeight = photo.size
          aspectRatio=imageHeight/imageWidth
          
          adjustedWidth = int(i[startWidth:endWidth])
          adjustedHeight = int(adjustedWidth*aspectRatio)
          #|--------------- Resize the Photo ---------------|
          photo=photo.resize((adjustedWidth, adjustedHeight), Image.ANTIALIAS)
        #|--------------- Display the Photo ---------------|      
        photo = ImageTk.PhotoImage(photo)        
        text=tk.Label(frame, image=photo)
        text.image=photo
    
    #|------<example> tags----------|    
    elif i.startswith("<example>"):
      style=("Consolas", 14)
      startExample=html.find("<example>", startExample)+9
      endExample=html.find("</example>", startExample)-1

      string="".join(html[startExample+1: endExample])
      text=tk.Label(frame, text=string, font=style, bd=10, relief="groove")

    #|------<hint> tags----------|
    elif i.startswith("<hint>"):
      style="Arial 14"
      startHint=html.find("<hint>", startHint)+5
      endHint=html.find("</hint>", startHint)-1
      
      hintStr.append("".join(html[startHint+2: endHint]))
      tk.Label(frame, text=" ", font=style, bg="white").pack()
      tk.Button(frame, text="Hint", font=style, command=lambda index=index: hint(index)).pack()
      index+=1

    #|------Pack the Contents----------| 
    text.configure(anchor="w", justify="left", wraplength=800, bg="white")
    text.pack(fill="x")        
 

# Function for parsing quiz text files   
def quizHtmlParse(file, frame, canvas):
  #open file
  with open(file, "r", encoding="utf8") as html:
    html=html.read()

  index = 0  # question number
  score = 0
  questions = {}
  startCode = endCode = 0

  # Check answer function
  def check(correct, answer, frame, canvas):
    nonlocal score
    style = "Helvetica 16 bold"
    
    if correct == answer:
      score += 1
      msg = tk.Label(frame, text="\nCongratulations! You got it right!", font=style)
    else:
      msg = tk.Label(frame, text="\nWrong! Try again next time.", font=style)
    
    # Put msg Label on screen
    msg.configure(anchor="w", justify="left", bg="white")
    msg.pack(fill="x")
    
    tk.Button(frame, text="NEXT", font="Helvetica 14", command=lambda: next(frame, canvas)).pack()


  # Next question function (clears screen and updates flag)
  def next(frame, canvas):
    nonlocal index
    index += 1
    style = "Helvetica 20 bold"

    # Clear frame of widgets
    frame.destroy()
    frame = tk.Frame(canvas, padx=50, pady=20, bg="white")
    canvas.create_window((0,0), window=frame, anchor="nw", width=1035)
    frame.bind("<Configure>", canvas.configure(scrollregion=canvas.bbox('all')))

    if index != len(questions):
      ask(frame, canvas)
    else:
      msg1 = tk.Label(frame, text="Quiz finished! You got a score of " + str(score) + " over " + str(index) + ".")
      msg1.configure(font=style, anchor="w", justify="left", wraplength=800, bg="white")
      msg1.pack(fill="x")
	  
	  # assessment test scores evaluation and recommendation of lessons
      if file == "assess.txt":
          if score>=0 and score<=4:
              msg2 = tk.Label(frame, text="\nLevel: Beginner \nRecommended Lesson: Print and Comment")
          elif score>=5 and score<=7:
              msg2 = tk.Label(frame, text="\nLevel: Intermediate \nRecommended Lesson: Sequence Functions Part I")
          else:
              msg2 = tk.Label(frame, text="\nLevel: Advanced \nRecommended Lesson: File Handling")

          msg2.configure(font=style, anchor="w", justify="left", wraplength=800, bg="white")
          msg2.pack(fill="x")


  # Ask questions function
  def ask(frame, canvas):
    nonlocal startCode, endCode
    answer = tk.StringVar()
    answer.set("0")
    

    # Loop through each line in question
    for i in questions[index].splitlines():
      i=i.strip()
      
      #|-------- <h> tag (for quiz name) ----------|
      if i.startswith("<h>") and i.endswith("</h>"):
        style = "Helvetica 20 bold"
        i = i.replace("<h>", "").replace("</h>", "")
        tk.Label(frame, text=i, font=style, wraplength=800, anchor="w", justify="left", bg="white").pack(fill="x")
      
      #|-------- <p> tag (for question) ----------|
      elif i.startswith("<p>") and i.endswith("</p>"):
        style = "Helvetica 14"
        i = i.replace("<p>", "").replace("</p>", "")
        tk.Label(frame, text="\n" + i + "\n", font=style, wraplength=800, anchor="w", justify="left", bg="white").pack(fill="x")

       #|------<code> tag (for codes) ----------|    
      elif i.startswith("<code>"):
        style=("Consolas", 14)
        startCode=html.find("<code>", startCode)+6
        endCode=html.find("</code>", startCode)-1

        string="".join(html[startCode+1: endCode])
        tk.Label(frame, text=string, font=style, wraplength=800, anchor="w", justify="left", bg="white smoke").pack(fill="x")
        tk.Label(frame, text="", bg="white").pack()

      #|-------- <rb> tag (for choices) ----------|
      elif i.startswith("<rb>"):
        style = "Helvetica 14"
        i = i.replace("<rb>", "")
        tk.Radiobutton(frame, text=i[3:], variable=answer, value=i[0], font=style, wraplength=800, anchor="w", justify="left", bg="white").pack(fill="x")

      #|-------- <enter> tag (for user-input for fill in the blanks) ----------|
      elif i.startswith("<enter>"):
        style = "Helvetica 14"
        i = i.replace("<enter>", "")
        tk.Entry(frame, width=700, textvariable=answer, font=style, justify="left", bg="white").pack(fill="x")
        answer.set("Enter answer here")

      #|-------- <c> tag (for correct answer) ----------|
      elif i.startswith("<c>"):
        i = i.replace("<c>", "")
        correct = i

    tk.Button(frame, text="SUBMIT", font="Helvetica 14", command=lambda: check(correct, answer.get(), frame, canvas)).pack()

  # Loop through each set of question (question, choices, and correct answer) and save it in the dictionary questions
  # <br> tag act as a divider for each set of question
  for count, question in enumerate(html.split("<br>")):
    questions[count] = question

  ask(frame, canvas)