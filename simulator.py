from tkinter import *
import tkinter.font as tkFont
import turtle as t
from operator import itemgetter

mode = "None"
n = 5

def draw_template():
    try:
        t.reset()
        screen = t.Screen()
        screen.setup(500,500)
        t.title("Process Scheduling Simulator")
        t.speed(0)
        t.hideturtle()
        t.bgcolor("Light grey")
        t.pu()
        t.goto(-200,20)
        t.pd()
        t.goto(200,20)
        t.goto(200,-20)
        t.goto(-200,-20)
        t.goto(-200,20)
        t.pu()
        t.goto(-200,-45)
        t.write("0",False,"center",("Arial",8,"normal"))
        t.goto(200,-45)
        t.write("100",False,"center",("Arial",8,"normal"))
        t.goto(100,200)
        t.color("red")
        t.write("Process 1: Red",False,"left",("Arial",8,"normal"))
        t.goto(100,180)
        t.color("green")
        t.write("Process 2: Green",False,"left",("Arial",8,"normal"))
        t.goto(100,160)
        t.color("blue")
        t.write("Process 3: Blue",False,"left",("Arial",8,"normal"))
        t.goto(100,140)
        t.color("Yellow")
        t.write("Process 4: Yellow",False,"left",("Arial",8,"normal"))
        t.goto(100,120)
        t.color("Purple")
        t.write("Process 5: Purple",False,"left",("Arial",8,"normal"))
    except:
        pass

def Special(list):
    global ArrayAns
    list.append(0)
  
    count2 = 0
    for i in range(0,len(list)):  
        if(i+1==len(list)):pass   
        elif(i != len(list)):
            if(list[i] != list[i+1] ): count2 += 1
            
    ArrayAns=[]

    
    for i in range(0,count2):
        ArrayAns+=[0]
    for i in range(0,count2):

        ArrayAns[i] = [0]*3
    for i in range(0,count2):   
        ArrayAns[i][0] = i

 
    start = 0
    i=0
    count = 0
 
    
    for i in range(0,len(list)):
        current = i

        if list[current] != list[start]:

          
            
            ArrayAns[count][0] = list[i-1] #indicate number of process
            ArrayAns[count][1] = start #Set the starting time of that process
            ArrayAns[count][2] = current #The stop time of that process
            
            count+=1
            start = current

    #print(ArrayAns)
    
    return ArrayAns # ArrayAns[ #number process, starting time, stop time]

def Respond(list):

    Res  = []

    AvgR = 0

    check=[]
    
    num =len(list)

    for i in range(0,num):
        if(list[i][0] in check):pass

        else:
            check.append(list[i][0])
            Res.append((list[i][0],list[i][1]))


    for i in range(0,len(Res)):

        AvgR += float(Res[i][1])

    #print(AvgR)
    #print(float(len(Res)))

    AvgR = AvgR/float(len(Res))

    #print(AvgR)

    return AvgR

def Waiting(list,list2):

    #list   = list ที่่ return จาก Special
    #list2  = list input เริ่มต้น (ที่เป็น process,burst,arrival) / (สร้าง duplicate มาใส่เพราะว่า algorithm ผมมัน pop ออก list ไปแล้ว)
    check = []
    check2 = []
    Wait = []
    AvgW = 0

    for i in range(len(list)-1,-1,-1):

        if(list[i][0] not in check2):
            check.append(list[i])
            check2.append(list[i][0])

            
          
    check.sort(key=lambda x: x[0])
    
    for i in range(len(check)):

        Wait.append(int(check[i][2])-int(list2[i][2])-int(list2[i][1]))

    for i in range(0,len(Wait)):

        AvgW += int(Wait[i])

    AvgW = AvgW/float(len(Wait))

    return AvgW

def Turn(list,list2):

    #list   = list ที่่ return จาก Special
    #list2  = list input เริ่มต้น (ที่เป็น process,burst,arrival) / (สร้าง duplicate มาใส่เพราะว่า algorithm ผมมัน pop ออก list ไปแล้ว)

    print(list)
    
    TotalFinish = 0
    TotalArrival = 0

    check=[]
    check2=[]
    
    for i in range(0,len(list2)):

        TotalArrival += list2[i][1]

    
        check = []
    
    for i in range(len(list)-1,-1,-1):

        if(list[i][0] not in check2):
            check.append(list[i])
            check2.append(list[i][0])

            
          
    check.sort(key=lambda x: x[0])



    for i in range(0,len(check)):

        TotalFinish += check[i][2]


    TotalTurn = (TotalFinish - TotalArrival)/float(len(check))


    #print(TotalTurn)

    return TotalTurn

def SJF_NON2( list ):

    timepast = 0
    r=0
    lista = []
    listb = []

    seq=[]
    
    while(len(list) != 0):

        #print('')
        list.sort(key=lambda x: x[1])

 
    
        for i in range(0,len(list)):

            if(int(list[0][1]) <= timepast):lista.append(list.pop(0))
            elif(int(list[0][1]) > timepast):listb.append(list.pop(0))

        for i in range(0,len(listb)):list.append(listb.pop(0))


        if(len(lista) != 0):

            lista.sort(key=lambda x: x[2])

            

            while(int(lista[0][2]) != 0):
    

                #print('Time : '+str(timepast)+' -> ',end='')
                #print(lista[0][0])
                seq.append(int(lista[0][0]))
                lista[0][2] = int(lista[0][2])-1
                timepast+=1
                


            lista.pop(0)
            
            while(len(lista) != 0):
                list.append(lista.pop(0))


            
                

        elif(len(lista) == 0):
            #print('Time : '+str(timepast)+' -> ',end='')
            #print('-')
            timepast+=1
            seq.append(0)
    Special(seq)
            
def RR( list ):

    ts = quantum

    seq = []
    timepast = 0
    queue = []
    queue2 = []
    r = 0
    tq = list
    tq.sort(key=lambda x: x[1])
    st = int(tq[0][1])
    
    
    while(len(list) != 0):
        

      
        
        for i in range(0,len(list)):
            
                if(int(list[0][1]) <= timepast ):
                    queue.append(list.pop(0))

                elif(int(list[0][1]) > timepast):
                    queue2.append(list.pop(0))


        for i in range(0,len(queue2)):
            list.append(queue2.pop(0))
            
        

        if(len(queue) == 0):
            #print('Time : '+str(timepast)+' -> ',end='')
            #print(' - ')
            timepast += 1
            seq.append(0)

        
        while(len(queue) != 0 ):
            for i in range(0,ts):
                

                if(len(queue) == 0):
                    #print('Time : '+str(timepast)+' -> ',end='')
                    #print(' - ')
                    timepast+=1
                    seq.append(0)
                elif(int(queue[0][2]) != 0):
                    #print('Time : '+str(timepast)+' -> ',end='')
                    #print(queue[0][0])
                    seq.append(int(queue[0][0]))
                    queue[0][2] = str(int(queue[0][2])-1)
                    if(int(queue[0][2]) == 0):
                        #print('')
                        #print(str(queue[0][0])+'Finished')
                        #print('')
                        queue.pop(0)
                    timepast+=1
                   
                
                    
            if(len(queue) != 0 ):list.append(queue.pop(0))



    #print('end')
            
    Special(seq)

def SJF( list ):


        lista = []
        listb = []
        timepast = 0
        r=0
        tl = list
        tl.sort(key=lambda x: x[1])
        st = int(tl[0][1])
        seq = []
        
        
        while(len(list) != 0):
            
      
                 
             for i in range(0,len(list)):
                 if(int(list[0][1]) <= timepast): lista.append(list.pop(0))
                 elif(int(list[0][1]) > timepast):listb.append(list.pop(0))

             for i in range(0,len(listb)):list.append(listb.pop(0))

      
   
             lista.sort(key=lambda x: x[2])



            # print('Time : '+str(timepast)+' -> ',end='')
             if(len(lista) != 0):
                 if(int(lista[0][2]) != 0):
                    #print('Time : '+str(timepast)+' -> ',end='')
                    #print(lista[0][0])
                    seq.append(int(lista[0][0]))
                    
                 elif(int(lista[0][2]) == 0 ):
                     if(len(lista) != 1):
                         #print('Time : '+str(timepast)+' -> ',end='')
                         seq.append(int(lista[1][0]))
                        # print(lista[1][0])
                         
                    
                     elif(len(lista) == 1):
                         #print('-')
                         seq.append(0)
                    
            
                 if(int(lista[0][2])==1):
                    #print(lista[0][0]+' Finished')
                    pass
                 if(int(lista[0][2])==0):lista.pop(0)
                     
                    
                 
                 if(len(lista) != 0):
                     if(int(lista[0][2]) > 0):
                         lista[0][2] = int(lista[0][2])-1
                         list.append(lista.pop(0))
                         

                 


                 for i in range(0,len(lista)):list.append(lista.pop(0))

             elif(len(lista) == 0):
               # print('Time : '+str(timepast)+' -> ',end='')
                #print(' - ')
                seq.append(0)
             timepast += 1


  
        Special(seq)

            
def animate_FCFS():
    global  proc1, proc2, proc3, proc4, proc5, at1, at2, at3, at4, at5, bt1, bt2, bt3, bt4,bt5
    if(n<=3):
        procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
        temp2 = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
    if(n==4):
        procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
        temp2 = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
    if(n>=5):
        procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]
        temp2 = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]
    procList.sort(key=itemgetter(1))
    s1 = procList[0][1]
    f1 = s1 + procList[0][2]
    if(procList[1][1]<f1):
        s2 = f1
    else:
        s2 = procList[1][1]
    f2 = s2 + procList[1][2]
    if(procList[2][1]<f2):
        s3 = f2    
    else:
        s3 = procList[2][1]
    f3 = s3 + procList[2][2]
    if(n>=4):
        if(procList[3][1]<f3):
            s4 = f3
        else:
            s4 = procList[3][1]
        f4 = s4 + procList[3][2]
        if(n==5):
            if(procList[4][1]<f4):
                s5 = f4
            else:
                s5 = procList[4][1]
            f5 = s5 + procList[4][2]
    draw_template()
    if(procList[0][0] == 1):
         t.color("Red")
    elif(procList[0][0]== 2):
        t.color("Green")
    elif(procList[0][0]==3):
        t.color("Blue")
    elif(procList[0][0]==4):
        t.color("Yellow")
    elif(procList[0][0]==5):
        t.color("Purple")
    t.begin_fill()
    t.goto(4*s1-200,-20)
    t.goto(4*f1-200,-20)
    t.goto(4*f1-200,20)
    t.goto(4*s1-200,20)
    t.goto(4*s1-200,-20)
    t.end_fill()
    if(procList[1][0] == 1):
         t.color("Red")
    elif(procList[1][0]== 2):
        t.color("Green")
    elif(procList[1][0]==3):
        t.color("Blue")
    elif(procList[1][0]==4):
        t.color("Yellow")
    elif(procList[1][0]==5):
        t.color("Purple")
    t.begin_fill()
    t.goto(4*s2-200,-20)
    t.goto(4*f2-200,-20)
    t.goto(4*f2-200,20)
    t.goto(4*s2-200,20)
    t.goto(4*s2-200,-20)
    t.end_fill()
    if(procList[2][0] == 1):
         t.color("Red")
    elif(procList[2][0]== 2):
        t.color("Green")
    elif(procList[2][0]==3):
        t.color("Blue")
    elif(procList[2][0]==4):
        t.color("Yellow")
    elif(procList[2][0]==5):
        t.color("Purple")
    t.begin_fill()
    t.goto(4*s3-200,-20)
    t.goto(4*f3-200,-20)
    t.goto(4*f3-200,20)
    t.goto(4*s3-200,20)
    t.goto(4*s3-200,-20)
    t.end_fill()
    if(n>=4):
        if(procList[3][0] == 1):
            t.color("Red")
        elif(procList[3][0]== 2):
            t.color("Green")
        elif(procList[3][0]==3):
            t.color("Blue")
        elif(procList[3][0]==4):
            t.color("Yellow")
        elif(procList[3][0]==5):
            t.color("Purple")
        t.begin_fill()
        t.goto(4*s4-200,-20)
        t.goto(4*f4-200,-20)
        t.goto(4*f4-200,20)
        t.goto(4*s4-200,20)
        t.goto(4*s4-200,-20)
        t.end_fill()
        if(n==5):
            if(procList[4][0] == 1):
                t.color("Red")
            elif(procList[4][0]== 2):
                t.color("Green")
            elif(procList[4][0]==3):
                t.color("Blue")
            elif(procList[4][0]==4):
                t.color("Yellow")
            elif(procList[4][0]==5):
                t.color("Purple")
            t.begin_fill()
            t.goto(4*s5-200,-20)
            t.goto(4*f5-200,-20)
            t.goto(4*f5-200,20)
            t.goto(4*s5-200,20)
            t.goto(4*s5-200,-20)
            t.end_fill()
    t.color("black")
    t.goto(s1*4-200,-45)
    t.write("%d"%s1,False,"center",("Arial",8,"normal"))
    t.goto(f1*4-200,-45)
    t.write("%d"%f1,False,"center",("Arial",8,"normal"))
    t.goto(s2*4-200,-45)
    t.write("%d"%s2,False,"center",("Arial",8,"normal"))
    t.goto(f2*4-200,-45)
    t.write("%d"%f2,False,"center",("Arial",8,"normal"))
    t.goto(s3*4-200,-45)
    t.write("%d"%s3,False,"center",("Arial",8,"normal"))
    t.goto(f3*4-200,-45)
    t.write("%d"%f3,False,"center",("Arial",8,"normal"))
    if(n>=4):
        t.goto(s4*4-200,-45)
        t.write("%d"%s4,False,"center",("Arial",8,"normal"))
        t.goto(f4*4-200,-45)
        t.write("%d"%f4,False,"center",("Arial",8,"normal"))
        if(n==5):
            t.goto(s5*4-200,-45)
            t.write("%d"%s5,False,"center",("Arial",8,"normal"))
            t.goto(f5*4-200,-45)
            t.write("%d"%f5,False,"center",("Arial",8,"normal"))
    if(n == 3):
        ArrayAns = [[procList[0][0],s1,f1],[procList[1][0],s2,f2],[procList[2][0],s3,f3]]
        temp = [[procList[0][0],s1,f1],[procList[1][0],s2,f2],[procList[2][0],s3,f3]]
    if(n >= 4):
        ArrayAns = [[procList[0][0],s1,f1],[procList[1][0],s2,f2],[procList[2][0],s3,f3],[procList[3][0],s4,f4]]
        temp = [[procList[0][0],s1,f1],[procList[1][0],s2,f2],[procList[2][0],s3,f3],[procList[3][0],s4,f4]]
        if(n == 5):
            ArrayAns = [[procList[0][0],s1,f1],[procList[1][0],s2,f2],[procList[2][0],s3,f3],[procList[3][0],s4,f4],[procList[4][0],s5,f5]]
            temp = [[procList[0][0],s1,f1],[procList[1][0],s2,f2],[procList[2][0],s3,f3],[procList[3][0],s4,f4],[procList[4][0],s5,f5]]
    rt = Respond(ArrayAns)
    wt = Waiting(ArrayAns,procList)
    tat = Turn(temp,temp2)
    t.goto(0,-175)
    t.write("Average Waiting Time : %.2f"%wt,False,"center",("Arial",14,"normal"))
    t.goto(0,-200)
    t.write("Average Turnaround Time : %.2f"%tat,False,"center",("Arial",14,"normal"))
    t.goto(0,-225)
    t.write("Average Respond Time : %.2f"%rt,False,"center",("Arial",14,"normal"))
    t.goto(-150,200)
    t.write("FCFS scheduling",False,"center",("Arial",14,"bold","underline"))

    

def animate_SJFN():
    global  proc1, proc2, proc3, proc4, proc5, at1, at2, at3, at4, at5, bt1, bt2, bt3, bt4,bt5
    if(n<=3):
         procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
         temp = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
         tempt = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
    if(n==4):
        procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
        temp = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
        tempt = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
    if(n>=5):
        procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]
        temp = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]
        tempt = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]
    draw_template()
    SJF_NON2(procList)
    for i in ArrayAns:
        if(i[0]==0):
            ArrayAns.remove(i)
    temp2 = ArrayAns
    temp2t = ArrayAns
    for i in range(len(ArrayAns)):
        s = ArrayAns[i][1]
        f = ArrayAns[i][2]
        if(ArrayAns[i][0] == 1):
            t.color("Red")
        elif(ArrayAns[i][0]== 2):
            t.color("Green")
        elif(ArrayAns[i][0]==3):
            t.color("Blue")
        elif(ArrayAns[i][0]==4):
            t.color("Yellow")
        elif(ArrayAns[i][0]==5):
            t.color("Purple")
        t.begin_fill()
        t.goto(4*s-200,-20)
        t.goto(4*f-200,-20)
        t.goto(4*f-200,20)
        t.goto(4*s-200,20)
        t.goto(4*s-200,-20)
        t.end_fill()
        t.color("black")
        t.goto(s*4-200,-45)
        t.write("%d"%s,False,"center",("Arial",8,"normal"))
        t.goto(f*4-200,-45)
        t.write("%d"%f,False,"center",("Arial",8,"normal"))
    rt = Respond(ArrayAns)
    wt = Waiting(temp2,temp)
    tat = Turn(temp2t,tempt)
    t.goto(0,-175)
    t.write("Average Waiting Time : %.2f"%wt,False,"center",("Arial",14,"normal"))
    t.goto(0,-200)
    t.write("Average Turnaround Time : %.2f"%tat,False,"center",("Arial",14,"normal"))
    t.goto(0,-225)
    t.write("Average Respond Time : %.2f"%rt,False,"center",("Arial",14,"normal"))
    t.goto(-100,200)
    t.write("SJF (Non-preemptive)",False,"center",("Arial",14,"bold","underline"))
    t.goto(-100,180)
    t.write("Scheduling",False,"center",("Arial",14,"bold","underline"))



def animate_SJF():
    global  proc1, proc2, proc3, proc4, proc5, at1, at2, at3, at4, at5, bt1, bt2, bt3, bt4,bt5
    if(n<=3):
         procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
         temp = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
         tempt = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
    if(n==4):
        procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
        temp = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
        tempt = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
    if(n>=5):
        procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]
        temp = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]
        tempt = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]
    draw_template()
    SJF(procList)
    for i in ArrayAns:
        if(i[0]==0):
            ArrayAns.remove(i)
    temp2 = ArrayAns
    temp2t =ArrayAns
    for i in range(len(ArrayAns)):
        s = ArrayAns[i][1]
        f = ArrayAns[i][2]
        if(ArrayAns[i][0] == 1):
            t.color("Red")
        elif(ArrayAns[i][0]== 2):
            t.color("Green")
        elif(ArrayAns[i][0]==3):
            t.color("Blue")
        elif(ArrayAns[i][0]==4):
            t.color("Yellow")
        elif(ArrayAns[i][0]==5):
            t.color("Purple")
        t.begin_fill()
        t.goto(4*s-200,-20)
        t.goto(4*f-200,-20)
        t.goto(4*f-200,20)
        t.goto(4*s-200,20)
        t.goto(4*s-200,-20)
        t.end_fill()
        t.color("black")
        t.goto(s*4-200,-45)
        t.write("%d"%s,False,"center",("Arial",8,"normal"))
        t.goto(f*4-200,-45)
        t.write("%d"%f,False,"center",("Arial",8,"normal"))
        rt = Respond(ArrayAns)
        wt = Waiting(temp2,temp)
        tat = Turn(temp2t,tempt)
        t.goto(0,-175)
        t.write("Average Waiting Time : %.2f"%wt,False,"center",("Arial",14,"normal"))
        t.goto(0,-200)
        t.write("Average Turnaround Time : %.2f"%tat,False,"center",("Arial",14,"normal"))
        t.goto(0,-225)
        t.write("Average Respond Time : %.2f"%rt,False,"center",("Arial",14,"normal"))
        t.goto(-100,200)
        t.write("SJF (Preemptive)",False,"center",("Arial",14,"bold","underline"))
        t.goto(-100,180)
        t.write("Scheduling",False,"center",("Arial",14,"bold","underline"))



def animate_RR():
    global  proc1, proc2, proc3, proc4, proc5, at1, at2, at3, at4, at5, bt1, bt2, bt3, bt4,bt5
    if(n<=3):
         procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
         temp = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
         tempt = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
    if(n==4):
        procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
        temp = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
        tempt = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
    if(n>=5):
        procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]
        temp = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]
        tempt = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]
    RR(procList)
    for i in ArrayAns:
        if(i[0]==0):
            ArrayAns.remove(i)
    temp2 = ArrayAns
    temp2t =ArrayAns
    draw_template()
    for i in range(len(ArrayAns)):
        s = ArrayAns[i][1]
        f = ArrayAns[i][2]
        if(ArrayAns[i][0] == 1):
            t.color("Red")
        elif(ArrayAns[i][0]== 2):
            t.color("Green")
        elif(ArrayAns[i][0]==3):
            t.color("Blue")
        elif(ArrayAns[i][0]==4):
            t.color("Yellow")
        elif(ArrayAns[i][0]==5):
            t.color("Purple")
        t.begin_fill()
        t.goto(4*s-200,-20)
        t.goto(4*f-200,-20)
        t.goto(4*f-200,20)
        t.goto(4*s-200,20)
        t.goto(4*s-200,-20)
        t.end_fill()
        t.color("black")
        t.goto(s*4-200,-45)
        t.write("%d"%s,False,"center",("Arial",8,"normal"))
        t.goto(f*4-200,-45)
        t.write("%d"%f,False,"center",("Arial",8,"normal"))
        rt = Respond(ArrayAns)
        print(temp)
        print(temp2)
        wt = Waiting(temp2,temp)
        tat = Turn(temp2t,tempt)
        t.goto(0,-175)
        t.write("Average Waiting Time : %.2f"%wt,False,"center",("Arial",14,"normal"))
        t.goto(0,-200)
        t.write("Average Turnaround Time : %.2f"%tat,False,"center",("Arial",14,"normal"))
        t.goto(0,-225)
        t.write("Average Respond Time : %.2f"%rt,False,"center",("Arial",14,"normal"))
        t.goto(-100,200)
        t.write("Round Robin Scheduling",False,"center",("Arial",14,"bold","underline"))


def Simulate_Click():
    global proc1, proc2, proc3, proc4, proc5, at1, at2, at3, at4, at5, bt1, bt2, bt3, bt4,bt5, quantum, mode
    try:
        t.reset()
        proc1 = int(proc1En.get())
        proc2 = int(proc2En.get())
        proc3 =int(proc3En.get())
        if(n>=4):
            proc4 = int(proc4En.get())
            at4 = int(proc4Arriv.get())
            bt4 = int(proc4Burs.get())
            if(n==5):
                proc5 = int(proc5En.get())
                at5 = int(proc5Arriv.get())
                bt5 = int(proc5Burs.get())
        at1 = int(proc1Arriv.get())
        at2 = int(proc2Arriv.get())
        at3 = int(proc3Arriv.get())
        bt1 = int(proc1Burs.get())
        bt2 = int(proc2Burs.get())
        bt3 = int(proc3Burs.get())
        if(mode == "RR"):
            quantum = int(QuanEn.get())

        if(mode == "FCFS"):
            animate_FCFS()
        if(mode == "SJFN"):
            animate_SJFN()
        if(mode == "SJF"):
            animate_SJF()
        if(mode == "RR"):
            animate_RR()
        else:
            pass
    except :
        pass

def FCFS_Click():
    global mode,TimeQuan, QuanEn
    mode = "FCFS"
    try:
        TimeQuan.destroy()
        QuanEn.destroy()
    except:
        pass
    

def SJFN_Click():
    global mode ,TimeQuan, QuanEn
    mode = "SJFN"
    try:
        TimeQuan.destroy()
        QuanEn.destroy()
    except:
        pass

def SJF_Click():
    global mode,TimeQuan, QuanEn
    mode = "SJF"
    try:
        TimeQuan.destroy()
        QuanEn.destroy()
    except:
        pass

def RR_Click():
    global mode, QuanEn, TimeQuan
    mode = "RR"
    TimeQuan=Label(root)
    ft = tkFont.Font(family='Times',size=10)
    TimeQuan["font"] = ft
    TimeQuan["fg"] = "#333333"
    TimeQuan["justify"] = "center"
    TimeQuan["text"] = "Time quantum"
    TimeQuan.place(x=100,y=190,width=95,height=25)

    QuanEn=Entry(root)
    QuanEn["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    QuanEn["font"] = ft
    QuanEn["fg"] = "#333333"
    QuanEn["justify"] = "center"
    QuanEn.place(x=110,y=210,width=70,height=25)
    QuanEn.insert(END,"5")


def Add_Proc():
    global n
    if(n<=3):
        n = 3
    if(n>=5):
        n = 5
    n += 1
    root.after(10,addProc)

def Sub_Proc():
    global n
    if(n<=3):
        n = 3
    if(n>=5):
        n = 5
    n -= 1
    root.after(10,subProc)

def subProc():
    if(n==3):
        proc4En.destroy()
        proc4Arriv.destroy()
        proc4Burs.destroy()
    if(n==4):
        proc5En.destroy()
        proc5Arriv.destroy()
        proc5Burs.destroy()

root = Tk()
root.geometry('600x500')
root.title("Process Scheduling Simulator")
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

LabelHead = Label(root)
ft = tkFont.Font(family='Times',size=15)
LabelHead["font"] = ft
LabelHead["fg"] = "#333333"
LabelHead["justify"] = "center"
LabelHead["text"] = "Process Scheduling Simulator"
LabelHead.place(x=190,y=20,width=250,height=39)

SimulateBtn = Button(root)
SimulateBtn["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
SimulateBtn["font"] = ft
SimulateBtn["fg"] = "#000000"
SimulateBtn["justify"] = "center"
SimulateBtn["text"] = "Simulate"
SimulateBtn.place(x=250,y=350,width=70,height=25)
SimulateBtn["command"] = Simulate_Click

AddBtn = Button(root)
AddBtn["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
AddBtn["font"] = ft
AddBtn["fg"] = "#000000"
AddBtn["justify"] = "center"
AddBtn["text"] = "+"
AddBtn.place(x=280,y=180,width=30,height=30)
AddBtn["command"] = Add_Proc

SubBtn = Button(root)
SubBtn["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
SubBtn["font"] = ft
SubBtn["fg"] = "#000000"
SubBtn["justify"] = "center"
SubBtn["text"] = "-"
SubBtn.place(x=280,y=140,width=30,height=30)
SubBtn["command"] = Sub_Proc

FCFSRadio=Radiobutton(root,value=1)
ft = tkFont.Font(family='Times',size=10)
FCFSRadio["font"] = ft
FCFSRadio["fg"] = "#333333"
FCFSRadio["justify"] = "center"
FCFSRadio["text"] = "FCFS"
FCFSRadio.place(x=50,y=70,width=85,height=25)
FCFSRadio["command"] = FCFS_Click

SJFNRadio= Radiobutton(root,value=2)
ft = tkFont.Font(family='Times',size=10)
SJFNRadio["font"] = ft
SJFNRadio["fg"] = "#333333"
SJFNRadio["justify"] = "center"
SJFNRadio["text"] = "SJF (Non-preemptive)"
SJFNRadio.place(x=35,y=100,width=200,height=32)
SJFNRadio["command"] = SJFN_Click

SJFRadio=Radiobutton(root,value=3)
ft = tkFont.Font(family='Times',size=10)
SJFRadio["font"] = ft
SJFRadio["fg"] = "#333333"
SJFRadio["justify"] = "center"
SJFRadio["text"] = "SJF (Preemptive)"
SJFRadio.place(x=32,y=130,width=180,height=30)
SJFRadio["command"] = SJF_Click

RRRadio=Radiobutton(root,value=4)
ft = tkFont.Font(family='Times',size=10)
RRRadio["font"] = ft
RRRadio["fg"] = "#333333"
RRRadio["justify"] = "center"
RRRadio["text"] = "Round Robin"
RRRadio.place(x=25,y=160,width=180,height=30)
RRRadio["command"] = RR_Click

proc1En=Entry(root)
proc1En["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc1En["font"] = ft
proc1En["fg"] = "#333333"
proc1En["justify"] = "center"
proc1En.place(x=320,y=100,width=70,height=25)
proc1En.insert(END,"1")

proc1Arriv=Entry(root)
proc1Arriv["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc1Arriv["font"] = ft
proc1Arriv["fg"] = "#333333"
proc1Arriv["justify"] = "center"
proc1Arriv.place(x=400,y=100,width=70,height=25)

proc1Burs=Entry(root)
proc1Burs["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc1Burs["font"] = ft
proc1Burs["fg"] = "#333333"
proc1Burs["justify"] = "center"
proc1Burs.place(x=480,y=100,width=70,height=25)

ArriveTime=Label(root)
ft = tkFont.Font(family='Times',size=10)
ArriveTime["font"] = ft
ArriveTime["fg"] = "#333333"
ArriveTime["justify"] = "center"
ArriveTime["text"] = "ArriveTime"
ArriveTime.place(x=390,y=70,width=100,height=25)

ProcNum=Label(root)
ft = tkFont.Font(family='Times',size=10)
ProcNum["font"] = ft
ProcNum["fg"] = "#333333"
ProcNum["justify"] = "center"
ProcNum["text"] = "Process#"
ProcNum.place(x=300,y=70,width=95,height=25)

BurstTime=Label(root)
ft = tkFont.Font(family='Times',size=10)
BurstTime["font"] = ft
BurstTime["fg"] = "#333333"
BurstTime["justify"] = "center"
BurstTime["text"] = "BurstTime"
BurstTime.place(x=480,y=70,width=100,height=25)

proc2En=Entry(root)
proc2En["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc2En["font"] = ft
proc2En["fg"] = "#333333"
proc2En["justify"] = "center"
proc2En.place(x=320,y=140,width=70,height=25)
proc2En.insert(END,"2")

proc2Arriv=Entry(root)
proc2Arriv["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc2Arriv["font"] = ft
proc2Arriv["fg"] = "#333333"
proc2Arriv["justify"] = "center"
proc2Arriv.place(x=400,y=140,width=70,height=25)

proc2Burs=Entry(root)
proc2Burs["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc2Burs["font"] = ft
proc2Burs["fg"] = "#333333"
proc2Burs["justify"] = "center"
proc2Burs.place(x=480,y=140,width=70,height=25)

proc3En=Entry(root)
proc3En["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc3En["font"] = ft
proc3En["fg"] = "#333333"
proc3En["justify"] = "center"
proc3En.place(x=320,y=180,width=70,height=25)
proc3En.insert(END,"3")

proc3Arriv=Entry(root)
proc3Arriv["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc3Arriv["font"] = ft
proc3Arriv["fg"] = "#333333"
proc3Arriv["justify"] = "center"
proc3Arriv.place(x=400,y=180,width=70,height=25)

proc3Burs=Entry(root)
proc3Burs["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc3Burs["font"] = ft
proc3Burs["fg"] = "#333333"
proc3Burs["justify"] = "center"
proc3Burs.place(x=480,y=180,width=70,height=25)

proc4En=Entry(root)
proc4En["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc4En["font"] = ft
proc4En["fg"] = "#333333"
proc4En["justify"] = "center"
proc4En.place(x=320,y=220,width=70,height=25)
proc4En.insert(END,"4")

proc4Arriv=Entry(root)
proc4Arriv["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc4Arriv["font"] = ft
proc4Arriv["fg"] = "#333333"
proc4Arriv["justify"] = "center"
proc4Arriv.place(x=400,y=220,width=70,height=25)

proc4Burs=Entry(root)
proc4Burs["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc4Burs["font"] = ft
proc4Burs["fg"] = "#333333"
proc4Burs["justify"] = "center"
proc4Burs.place(x=480,y=220,width=70,height=25)

proc5En=Entry(root)
proc5En["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc5En["font"] = ft
proc5En["fg"] = "#333333"
proc5En["justify"] = "center"
proc5En.place(x=320,y=260,width=70,height=25)
proc5En.insert(END,"5")

proc5Arriv=Entry(root)
proc5Arriv["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc5Arriv["font"] = ft
proc5Arriv["fg"] = "#333333"
proc5Arriv["justify"] = "center"
proc5Arriv.place(x=400,y=260,width=70,height=25)

proc5Burs=Entry(root)
proc5Burs["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
proc5Burs["font"] = ft
proc5Burs["fg"] = "#333333"
proc5Burs["justify"] = "center"
proc5Burs.place(x=480,y=260,width=70,height=25)

def addProc():
    global proc4En, proc4Arriv, proc4Burs, proc5En,proc5Arriv,proc5Burs
    if(n == 4):
        proc4En=Entry(root)
        proc4En["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        proc4En["font"] = ft
        proc4En["fg"] = "#333333"
        proc4En["justify"] = "center"
        proc4En.place(x=320,y=220,width=70,height=25)
        proc4En.insert(END,"4")

        proc4Arriv=Entry(root)
        proc4Arriv["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        proc4Arriv["font"] = ft
        proc4Arriv["fg"] = "#333333"
        proc4Arriv["justify"] = "center"
        proc4Arriv.place(x=400,y=220,width=70,height=25)

        proc4Burs=Entry(root)
        proc4Burs["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        proc4Burs["font"] = ft
        proc4Burs["fg"] = "#333333"
        proc4Burs["justify"] = "center"
        proc4Burs.place(x=480,y=220,width=70,height=25)
    if(n == 5):
        proc5En=Entry(root)
        proc5En["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        proc5En["font"] = ft
        proc5En["fg"] = "#333333"
        proc5En["justify"] = "center"
        proc5En.place(x=320,y=260,width=70,height=25)
        proc5En.insert(END,"5")

        proc5Arriv=Entry(root)
        proc5Arriv["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        proc5Arriv["font"] = ft
        proc5Arriv["fg"] = "#333333"
        proc5Arriv["justify"] = "center"
        proc5Arriv.place(x=400,y=260,width=70,height=25)

        proc5Burs=Entry(root)
        proc5Burs["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        proc5Burs["font"] = ft
        proc5Burs["fg"] = "#333333"
        proc5Burs["justify"] = "center"
        proc5Burs.place(x=480,y=260,width=70,height=25)

root.mainloop()
