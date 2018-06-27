
import tkinter as tk

exp=''
def printno(val):
    global label2
    global exp
    exp=(exp+val)
    label2.config(text=exp)

def clear():
    global exp
    exp=''

#calculating the expression
try:
    def equals():
        j=0
        varlist = []
        oplist = []

        for k in range(0,len(exp)):
            if exp[k]=='+' or exp[k]=='-' or exp[k]=='*' or exp[k]=='/':
                i=exp[j:k]
                varlist.append(int(i))
                j=k+1
                oplist.append(exp[k])
        p=exp[j:]
        varlist.append(int(p))
        if (len(oplist)>len(varlist)):
            raise ValueError
        else:
            var2=varlist[0]
            for l in range(0,len(oplist)):
                if(oplist[l]=='+'):
                    var2=var2+varlist[l+1]
                if (oplist[l] == '-'):
                    var2 = var2 - varlist[l + 1]
                if (oplist[l] == '*'):
                    var2 = var2 * varlist[l + 1]
                if (oplist[l] == '/'):
                    var2 = var2 / varlist[l + 1]

            label2.config(text=str(var2))
        clear()

except ValueError:
    label2.config(text='Enetr correct epression')
    clear()

mainwindow=tk.Tk()
mainwindow.geometry('380x350')
label1=tk.Label(mainwindow,text='Calculator')
label1.config(bg='red',font=('times',40,'bold'),fg='blue')
label1.grid(row=1,columnspan=4,padx=50,pady=10,ipadx=10,ipady=10)


label2=tk.Label(mainwindow,relief='sunken')
label2.config(bg='white',height=1,width=35)
label2.grid(row=2,columnspan=4,padx=50,pady=10,ipadx=10,ipady=10)

button1=tk.Button(mainwindow,text='1',relief='raised',command=lambda:printno('1'))
button1.config(bg='white',height=1,width=5)
button1.grid(row=3,column=0,padx=1,pady=1,ipadx=1,ipady=3)


button2=tk.Button(mainwindow,text='2',relief='raised',command=lambda:printno('2'))
button2.config(bg='white',height=1,width=5)
button2.grid(row=3,column=1,padx=1,pady=1,ipadx=1,ipady=3)


button3=tk.Button(mainwindow,text='3',relief='raised',command=lambda:printno('3'))
button3.config(bg='white',height=1,width=5)
button3.grid(row=3,column=2,padx=1,pady=1,ipadx=1,ipady=3)


buttona=tk.Button(mainwindow,text='+',relief='raised',command=lambda:printno('+'))
buttona.config(bg='white',height=1,width=5)
buttona.grid(row=3,column=3,padx=1,pady=1,ipadx=1,ipady=3)


button4=tk.Button(mainwindow,text='4',relief='raised',command=lambda:printno('4'))
button4.config(bg='white',height=1,width=5)
button4.grid(row=4,column=0,padx=1,pady=1,ipadx=1,ipady=3)


button5=tk.Button(mainwindow,text='5',relief='raised',command=lambda:printno('5'))
button5.config(bg='white',height=1,width=5)
button5.grid(row=4,column=1,padx=1,pady=1,ipadx=1,ipady=3)


button6=tk.Button(mainwindow,text='6',relief='raised',command=lambda:printno('6'))
button6.config(bg='white',height=1,width=5)
button6.grid(row=4,column=2,padx=1,pady=1,ipadx=1,ipady=3)

buttons=tk.Button(mainwindow,text='-',relief='raised',command=lambda:printno('-'))
buttons.config(bg='white',height=1,width=5)
buttons.grid(row=4,column=3,padx=1,pady=1,ipadx=1,ipady=3)


button7=tk.Button(mainwindow,text='7',relief='raised',command=lambda:printno('7'))
button7.config(bg='white',height=1,width=5)
button7.grid(row=5,column=0,padx=1,pady=1,ipadx=1,ipady=3)


button8=tk.Button(mainwindow,text='8',relief='raised',command=lambda:printno('8'))
button8.config(bg='white',height=1,width=5)
button8.grid(row=5,column=1,padx=1,pady=1,ipadx=1,ipady=3)


button9=tk.Button(mainwindow,text='9',relief='raised',command=lambda:printno('9'))
button9.config(bg='white',height=1,width=5)
button9.grid(row=5,column=2,padx=1,pady=1,ipadx=1,ipady=3)

buttonm=tk.Button(mainwindow,text='*',relief='raised',command=lambda:printno('*'))
buttonm.config(bg='white',height=1,width=5)
buttonm.grid(row=5,column=3,padx=1,pady=1,ipadx=1,ipady=3)

button0=tk.Button(mainwindow,text='0',relief='raised',command=lambda:printno('0'))
button0.config(bg='white',height=1,width=5)
button0.grid(row=6,column=0,padx=1,pady=1,ipadx=1,ipady=3)


buttone=tk.Button(mainwindow,text='=',relief='raised',command=lambda:equals())
buttone.config(bg='white',height=1,width=20)
buttone.grid(row=6,column=1,padx=1,pady=1,ipadx=1,ipady=3)

buttond=tk.Button(mainwindow,text='/',relief='raised',command=lambda:printno('/'))
buttond.config(bg='white',height=1,width=5)
buttond.grid(row=6,column=3,padx=1,pady=1,ipadx=1,ipady=3)


mainwindow.mainloop()
