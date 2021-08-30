# Modules
import  random,sys
from tkinter import *
from tkinter.ttk import Separator,Progressbar
from tkinter.messagebox import showinfo
from time import time, strftime
# Interface Designing
root = Tk()
root.geometry("700x500")
root.resizable(0,0)
root.title("Quiz App For Entrance Exams")
#img = ('wn', 'iconphoto',root._w,PhotoImage(file = 'Quiz app icon.jpg'))
#root.tk.call(img)
root.config(bg='black')
i=0
timeLeft = {'min':5,'sec':30}

intro = '''\t\t : : Instruction: :
...........................................................................
1. Total Quiz Time is : 05:00 Min
2. Total Questions : 05
3  Total score : 05 x 100 = 500
4. Please select appropriate option at once as you have only one chance to select.
\t\t Good Luck!'''

print(intro)

def timeshow(self):
    global  i, timeLeft,note
    if timeLeft['min']==5 and timeLeft['sec']>0:
        note.config(text='You can start Quiz after {} seconds.'.format(timeLeft['sec']))
        timeLeft['sec']-=1
    elif timeLeft['sec']>0:
        submit.config(state = NORMAL)
        instruction.config(text='')
        timeLeft['sec']-=1
        note.config(text = 'Time left: {}min:{}sec'.format(timeLeft['min'],timeLeft['sec']))
    elif timeLeft['min']!=0 and timeLeft['sec']==0:
        timeLeft['min']-=1
        timeLeft['sec']=59
        note.config(text='Time Left:{}min:{}sec'.format(timeLeft['min'],timeLeft['sec']))
    elif timeLeft['min']==0 and timeLeft['sec']==0:
        print('Time up!')
        result()
    showtime.config(text=strftime('%H:%M:%S'))
    showtime.after(1000,timeshow)
#=====Student Attendence====
def getDetails():
    global  name,roll, root, Name,Roll
    Name = name.get()
    Roll = roll.get()
    root.deiconify()
    timeshow()
    root.destroy()

def attendance():
    global name, roll, root
    root = Toplevel(root)
    root.geometry('700x500')
    root.resizable(0, 0)
    root.title('Quiz App For Entrance Exam')
    root.config(bg ='red')
#====App Nmae =====
appName = Label(root, text = 'Quiz App', font=('impact', 20, 'italic'), justify = CENTER, bg ='goldenrod2', fg ='white')
appName.pack(side =TOP, fill = BOTH)
# ====== Show current Time====
showtime1 = Label(root, text='', font=20, fg='red', bg='goldenrod2')
showtime1.place(x=600,y=50)
#===Label to show info of attendence===
info = Label(root, text='Enter your Name and Roll Number', bg ='black', fg='goldenrod2', font=('arial', 15))
info.place(x =210, y=200)
name = Entry(root, width=30)
name.place(x=250,y=235)
roll = Entry(root, width=30)
roll.place(x=250,y=260)
name.insert(END,'Name')
roll.insert(END,'roll')
submit = Button(root, text='Confirm &Start', width=20, bg='goldenrod1', fg='green', command = getDetails)
submit.place(x= 265,y=300)
root.mainloop()
#====Toplevel Finished=====

#====Quit Game===
def quit_function():
    answer = showinfo(title="Good Luch",message="good Lick for your Future")
    if answer=='ok':
        sys.exit(root.destroy())

#========Disable all Buttons===
def desableAllButton():
    option1.config(state=DISABLED)
    option2.config(state=DISABLED)
    option3.config(state=DISABLED)
    option4.config(state=DISABLED)

#====Enable All Buttons===
def enableAllButton():
    option1.config(state=NORMAL)
    option2.config(state=NORMAL)
    option3.config(state=NORMAL)
    option4.config(state=NORMAL)

#==== show  final result=====
def result():
    global score,Name,Roll
    root.withdraw()
    top  = Toplevel(root)
    top.geometry('200x100')
    top.resizable(0,0)
    top.title('Quit Result')
    top.config(bg='blue')
    top.protocol('WM_DELETE_WINDOW',quit_function)
    filename = Name+'_'+Roll+'.txt'
    data = '\nStudent: '+Name+'\nRoll: '+Roll+'\nScore: '+str(score)+'\ncompleted quit at: '+strftime('%d%m%Y---%H%M%S')
    with open(filename,'a') as file:
        file.write(data)

    lable = Label(top,text ='Quiz Over....\n Score: '+str(score),font=30,fg='white',bg='blue').place(x=50,y=25)
    exitBtn = Button(top,text='Exit',width=10,bg='black',fg='red',command=quit_function).place(x=50,y=70)
    top.mainloop()
#==== Question and Answer===
questions = { 'Who is Python Developer?':'Guido van Rossum',
              'What is the output of 12/4 ?':'3',
              'Officially Python Lunched ?':'1991',
              'Developer of C Language ?':'Denis Ritchee',
              'Standard Query Language related to ?':'SQL'

}
#===Seperate Question and Answer from question variavble
que = []
ans = []
for key,value in questions.items():
    que.append(key)
    ans.append(value)
#=====Corresponding answer with answer including at random==
options = [
    ['van nesum',ans[0],'james Gosling','gudo van rosom'],
    [ans[1],'4','0','Error',]
    ['1990','1994',ans[2],'1996',]
    [ans[0],'James','Guido van Rosom','Error',]
    ['Standard','Query','Language',ans[4]]
    ]

#==========
currentQ = ' '
queNo = None
currentA = ' '
score = 0
qn = 1
var = StringVar()
def _next():
    global currentQ,currentA,queNo,score,i,qn
    i = 0
    if len(que)>0:
        currentQ = random.choice(que)
        print(currentQ)
        q = Label(root,text='Que.'+str(qn),font=('arial',10)).place(x=20,y=80)
        qn+=1
        #======total Question=====
        queNo = que.index(currentQ)
        print(options[queNo])
        currentA = questions[currentQ]
        #-===Change in caption of button
        submit.config(text='Next')
        #Print current questions===
        queLabel.config(text=currentQ,fg='green',height=6)
        #print options from list which are asked
        enableAllButton()
        option1.config(text=options[queNo][0],bg='sky Blue',value = options[queNo][0],bd = 1,command=answer)
        option2.config(text=options[queNo][1], bg='sky Blue', value=options[queNo][1], bd=1, command=answer)
        option3.config(text=options[queNo][2], bg='sky Blue', value=options[queNo][2], bd=1, command=answer)
        option4.config(text=options[queNo][3], bg='sky Blue', value=options[queNo][3], bd=1, command=answer)
        #=== remove questions from list which are asked
        que.remove(currentQ)
        que.remove(options[queNo])
    elif len(que)==0:
        result()
def answer():
    global currentQ,currentA,score
    #==== print selected radiobutton===
    a = var.get()
    if currentA == str(a):
        score+=100
        desableAllButton()
    else:
        desableAllButton()

title = '''Entrance Exam quiz Application App'''
appName = Label(root,text = title,font=('impact',20,'italic'),justify=CENTER,bg='goldenrod2',fg='white')
appName.pack(side=TOP,fill=BOTH)
#=======Label to show current questions====
queLabel = Label(root,text='',justify=LEFT,font=25)
queLabel.pack(side=TOP,fill=BOTH)
s = separator(root).place(x=0,y=195,relwidth=1)
#=====options labels====
options1 = Radiobutton(root,text='',bg='black',font=20,width=20,relif=FLAT,indicator=0,value=1,variable=var,bd=0)
options1.place(x=150,y=250)
options2 = Radiobutton(root,text='',bg='black',font=20,width=20,relif=FLAT,indicator=0,value=2,variable=var,bd=0)
options2.place(x=400,y=250)
options3 = Radiobutton(root,text='',bg='black',font=20,width=20,relif=FLAT,indicator=0,value=3,variable=var,bd=0)
options3.place(x=150,y=300)
options4 = Radiobutton(root,text='',bg='black',font=20,width=20,relif=FLAT,indicator=0,value=4,variable=var,bd=0)
options4.place(x=400,y=300)

# Instruction of Quiz
instruction = Label(root,text=intro,bg='red',fg='white',font=('calbri',15),justify=LEFT)
instruction.place(x=150,y=200)

# note to Quiz
note = Label(root,text='',font=('impact',10),bg='black',fg='red')
note.pack(side=BOTTOM)
#=====submit Button====
submit = Button(root,text='Start Quiz',bg='blue',fg='white',width=15,font=('impact',15),state=DISABLED,command=_next)
submit.pack(side=BOTTOM)
#====Show current time===
showtime = Label(root,text='',font=20,fg='black',bg='goldenrod2')
showtime.place(x=620,y=50)
#=====Progress bar for time left====
copyri8 = Label(root,text="By:Prabhat",font=('mistrila',12,'bold'),fg='blue',bg='powder blue',width=25,justify=LEFT).place(x=0,y=480)

if __name__=="__main__":
    root.withdraw()
    attendance()
    root.mainloop()


