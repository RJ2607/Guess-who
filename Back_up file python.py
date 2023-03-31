import pygame, random, sys ,os,time
from pygame.locals import *
import time
pygame.init()

#Defining characters charteristics
import mysql.connector as msql
mydb=msql.connect(
    host="localhost",
    user="root",
    database="guesswho",
    password="rj@2607"
    )
mycursor=mydb.cursor()

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
"""
cursor = mydb.cursor(dictionary=True)
mycursor.execute("SELECT * FROM GS")
myresult=mycursor.fetchall()
mydb.commit()
sql_list=[]
sql_list_score=[]
for X in myresult:
    sql_list.append(X[0])
    sql_list_score.append(X[1])

"""


character_list=[["andy","large eyebrows","black hair",'male','brown eyeballs','black','big lips'],
['ashley','female','wears cap/hat','white','small lips','brown eyeballs','reddish-brown hair'],
["brandon","blonde hair","wears cap/hat",'male','white','without beard','small lips','brown eyeballs'],
['chris','male','wears cap/hat','white','small lips','brown eyeballs','without beard','small lips'], 
['connor','male','moustache','black','small lips','brown eyeballs','brown hair'],
['daniel','male','wears cap/hat','black','small lips','large eyebrows'],
['david','male','bald','white','beard','large eyebrows','brown eyeballs','small lips'],
['emily','female','spectacles','white','white hair','small lips','blue eyeballs'],
['jake','male','moustache','white','blonde hair','brown eyeballs','small lips'],
['james','brown eyeballs','bald','male','small lips','beard','black'],
['jon','white hair','small lips','white','male','beard'],
['joseph','blue eyeballs','spectacles','reddish-brown hair','white','male','small lips'],
['justin','moustache','white','small lips','brown eyeballs','male'],
['kyle','blonde hair','big lips','blue eyeballs','white','male'],
['matt','white','male','small lips','white hair'],
['megan','blonde hair','female','blue eyeballs','small lips','white'],
['nick','spectacles','white','male','small lips','blue eyeballs','bald'],
['rachael','wears cap/hat','small lips','white','female','brown hair'],
['sarah','black','black hair','big lips','wears spectacles','female','brown eyeballs'],
['tyler','moustache','big lips','brown eyeballs','black hair','large eyebrows','white','male'],
['william','white','male','blonde hair','small lips','brown eyeballs'],
['zachary','large eyebrows','brown eyeballs','small lips','white','male','bald'],
]

win=pygame.display.set_mode((1300,650))
win.fill((255,255,255))

#win.fill((0,0,0))

#All functions

class button():
    def __init__(self, color, x,y,width,height, text=''):
        global w
        w=width
        global h
        h=height
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            #pygame.draw.rect(win, outline, (self.x,self.y,self.width,self.height),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsansms', 20)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
           
        return False
#Text box functions

import pygame 

pygame.init()
#screen = pygame.display.set_mode((1300,900))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 38)
#screen.fill((255,255,255))

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    #print(self.text)
                    global text_ans
                    text_ans=self.text
                    if(self.text!=""):
                        print(self.text)
                        return
                    
                    self.text = ''
                    
                    #print (a)
                    #pygame.quit()
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)



def redrawWindow():
    win.fill((255,255,255))
    greenButton.draw(win,(0,0,0))

"""for i in range(0,22):
    if character_list[i][0]==ans:
        character_list.remove(character_list[i])
        character_list.append([ans,""])"""
def blackout(c_req,ans,character_list,size_list,t_x,t_y):
    
    #pygame.display.update()
    adnum=0
    for i in character_list:
        if i[0]==ans:
            c_number=adnum
            break
        adnum+=1
    #print(c_number)
    #print(c_req)
    #print(character_list)
    #print(character_list[c_number])
    #print("Size list: ",size_list)
    if(c_req in character_list[c_number]):
        #print("1")
        
        for i in range(0,22):
            if(character_list[i][0]==ans):
                continue
            elif c_req not in character_list[i]:
        
                namei=character_list[i][0]
                #print("going")
                for k in size_list:
                    if ((k[0]==namei) and (k[0] not in check_list)) :
                        check_list.append(k[0])
                        wimage = pygame.image.load(r'C:\Users\user\Desktop\guess who\WR.png')
                        wimage = pygame.transform.scale(wimage, (80,70))
                        #pygame.display.update()
                        #print("This:",k[1],k[2])
                        win.blit(wimage, (k[1]+20,k[2]+30))
                        pygame.display.update()
        textwrite(c_req+' : YES',(0, 0, 128),30,t_x,t_y)
        
    elif(c_req not in character_list[c_number]):
        #print("2")
        
        for i in range(0,22):
            if(character_list[i][0]==ans):
                continue
            elif c_req in character_list[i]:
        
                namei=character_list[i][0]
                #print("going")
                for k in size_list:
                    if ((k[0]==namei) and (k[0] not in check_list)) :
                        check_list.append(k[0])
                        wimage = pygame.image.load(r'C:\Users\user\Desktop\guess who\WR.png')
                        wimage = pygame.transform.scale(wimage, (80,70))
                        #pygame.display.update()
                        #print("This:",k[1],k[2])
                        win.blit(wimage, (k[1]+20,k[2]+30))
                        pygame.display.update()
        textwrite(c_req+' : NO',(0, 0, 128),30,t_x,t_y)
    
#First page
#done=False

input_box1 = InputBox(500, 400, 250, 40)

def textwrite(you_said,cl,f_size,x_co,y_co):
    font = pygame.font.Font('freesansbold.ttf', f_size) 
    #greeni = (0, 255, 0) 
    #bluei = (0, 0, 128) 
    texti = font.render(you_said, True, cl) 
    textRect = texti.get_rect()  
    textRect.center = (x_co,y_co) 
    win.blit(texti, textRect) 
    
#def notin_button(first,second):

def up_score(n,s):
    cursor = mydb.cursor
    #mycursor.execute("SELECT * FROM GS")
    # sql="""INSERT INTO gs VALUES(%s,%s)"""
    sql = f"INSERT INTO gs VALUES({n},{s})"
    val=[(n,s)]


    mycursor.executemany(sql,val)
    mydb.commit()
    cursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM GS")
    myresult=mycursor.fetchall()
    
    for X in myresult:
        print(X)
    return
    
def down_score():
    cursor = mydb.cursor
    cursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM GS")
    myresult=mycursor.fetchall()
    cp=[]
    cp_max5=[]
    cpd=[]
    cpr=[]
    not_again=1
    for X in myresult:
        print(X)
        d1=X[0]
        d2=X[1]
        cp.append(d1)
        d2=d2+not_again
        cpd.append(d2)
        cp_max5.append(d2)
        
        cpr.append([d2,not_again])
        not_again+=1
    print(cpr)
    cp_max5.sort()
    cp_max5=cp_max5[::-1]
    #cpr.sort()
    print(cpr)
    print(cpd)
    print(cp_max5)
    x1=250
    x2=620
    y1=375
    y2=375
    for i in range(0,5):
        g=cp_max5[i]
        for i in range(0,len(cpr)):
            if(cpr[i][0]==g):
                j=cpr[i][1]
                
                break
        print(g)
        ind=cpd.index(g)
        h=cp[ind]
        g=g-j
        textwrite(h,(0,0,0),20,x1,y1)
        textwrite(str(g),(0,0,0),20,x2,y2)
        y1+=65
        y2+=65
        pygame.display.update()
        
        
    
    
    


running=True

wimage = pygame.image.load(r'C:\Users\User\Desktop\guess who\WR.png')


play_again=1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #redrawWindow()
    #pygame.display.update()
    if(play_again==1):
        cursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM GS")
        myresult=mycursor.fetchall()
        mydb.commit()
        sql_list=[]
        sql_list_score=[]
        for X in myresult:
            sql_list.append(X[0])
            sql_list_score.append(X[1])

        name_list=[]
        for i in character_list:
            name_list.append(i[0])
        Not_needed_in_button=[['male','female'],['big lips','small lips'],['white','black']]
        
        ans_no=random.randint(0,len(character_list)-1)
        ans=character_list[ans_no][0]
        Possible_Qlist=["black","blonde hair","male","female","large eyebrows","wears cap/hat",
                        'small lips','spectacles','blue eyeballs','moustache','bald','big lips','white']
        up_Qlist=Possible_Qlist
        print(ans)
        score=0
        text_ans=""
        stpage=False
        win.fill((255,255,255))
        stp1 = pygame.image.load(r'C:\Users\user\Desktop\guess who\bk.png')
        stp1 = pygame.transform.scale(stp1, (1300,850))           
        win.blit(stp1, (0,0))
        pygame.display.update()
        #time.sleep(5)
        stp1Button=button((0,255,0),1100,700,100,50,'Skip')
        stp1Button.draw(win,(0,0,0))
        pygame.display.update()
        dis=True
    
        while(dis==True):
            for event in pygame.event.get():
                pos=pygame.mouse.get_pos()
                if 1100+100 > pos[0] > 1100 and 700+50 > pos[1] > 700:
                    if event.type==pygame.MOUSEBUTTONDOWN:  
                        dis=False
                        stpage=True
                        break

        win.fill((255,255,255))   
        stp = pygame.image.load(r'C:\Users\user\Desktop\hwt.jpg')
        stp = pygame.transform.scale(stp, (800,700))
                        
        win.blit(stp, (100,100))
        stpButton=button((0,255,0),1100,700,100,50,'Skip')
        
        stpButton.draw(win,(0,0,0))
        pygame.display.update()
        
        while(stpage==True):
            for event in pygame.event.get():
                pos=pygame.mouse.get_pos()
                if 1100+100 > pos[0] > 1100 and 700+50 > pos[1] > 700:
                    if event.type==pygame.MOUSEBUTTONDOWN:  
                        done=False
                        stpage=False
                        break
        
        
        
        
        while not done:
            for event in pygame.event.get():
                
                input_box1.handle_event(event)
                
            win.fill((255,255,51))
            textwrite("Hey,what's your Username ??",(0, 0, 128),40,600,200)
            
            input_box1.draw(win)
            
            pygame.display.flip()
            if(text_ans==""):
                
                done=False
                
            else:
                username_sql=text_ans
                pygame.display.update()
                break
                    #print(text_ans)
                    
                #win.fill((255,255,255))
        sql_ask=0
        sql_sc=0
        if(username_sql in sql_list):
            sql_ask=1
            keep=sql_list.index(username_sql)
            sql_sc=sql_list_score[keep]
            cursor = mydb.cursor(dictionary=True)
            sql="""delete from gs where Username='%s'"""%(username_sql)
            mycursor.execute(sql)
            mydb.commit()
            win.fill((255,255,255))
            textwrite("Welcome Back !!",(0,0,0),70,450,400)
            pygame.display.update()
            time.sleep(4)
        else:
            win.fill((255,255,255))
            textwrite("Welcome New user!!",(0,0,0),70,450,400)
            pygame.display.update()
            time.sleep(4)
        win.fill((156,102,31)) 
        greenButton=button((0,255,0),1100,680,100,50,'Start')
    
        greenButton.draw(win,(0,0,0))
        pygame.display.update()
    play_again=0
    print("Out")
    for event in pygame.event.get():
        pos=pygame.mouse.get_pos()
        if 1100+w > pos[0] > 1100 and 680+h > pos[1] > 680 and play_again==0:
            if event.type==pygame.MOUSEBUTTONDOWN:
                print("CLicked the button")
                # All initialization
                #win.fill((156,102,31))    
                blackout_list=[]    
                life=3
                print(ans)
                fun=""
                crip=0
                y=0
                to_sc1=0
                size_list=[]
                check_list=[] #for function so no character gets wrong sign 2 times
                #check_list.append(ans)
                to_sc1=1
                
                xc=50
                yc=50
                win.fill((156,102,31))
               # print("CLicked the button")
                for i in character_list:
                    if(xc>900):
                       xc=50
                       yc+=200
                    carImg = pygame.image.load(r'C:\Users\user\Desktop\Guess who\Pics\c_'+i[0]+'.jpg')
                    carImg = pygame.transform.scale(carImg, (120,140))
                    pik=[i[0],xc,yc]
                    size_list.append(pik)
                    
                    win.blit(carImg, (xc,yc))
                    xc+=150
                    
                k=[]
                #Working
                nlist=Possible_Qlist
                #print("hi")
               # a1=0
               # a2=1
               # a3=2
                pygame.display.update()
                
# Not_needed_in_button=[['male','female'],['big lips','small lips'],['white','black']]     
                textwrite("Does he/she (HAVE/IS)",(0, 0, 128),20,1100,50)
                Not_needed_in_button_recover=[]
                print("C")
                if(to_sc1==1):
                    print("Ci")
                    currentlength_list=len(nlist)-1
                    a1=random.randint(0,currentlength_list)
                    question_a1=nlist[a1]
                    k.append(nlist[a1])
                    nlist.remove(nlist[a1])
                    QButton=button((0,255,0),1100,100,140,50,question_a1)
                    QButton.draw(win,(0,0,0))
                    
                    for i in Not_needed_in_button:
                        if (question_a1==i[0]):
                            print(i[1])
                            nlist.remove(i[1])
                            Not_needed_in_button_recover.append(i[1])
                        elif(question_a1==i[1]):
                            print(i[0])
                            nlist.remove(i[0])
                            Not_needed_in_button_recover.append(i[0])
                    currentlength_list=len(nlist)-1
                    a2=random.randint(0,currentlength_list)
                    question_a2=nlist[a2]
                    k.append(nlist[a2])
                    nlist.remove(nlist[a2])
                    QButton=button((0,255,0),1100,200,140,50,question_a2)
                    QButton.draw(win,(0,0,0))
                    for i in Not_needed_in_button:
                        if (question_a2==i[0]):
                            print(i[1])
                            nlist.remove(i[1])
                            Not_needed_in_button_recover.append(i[1])
                        elif(question_a2==i[1]):
                            print(i[0])
                            nlist.remove(i[0])
                            Not_needed_in_button_recover.append(i[0])
                    currentlength_list=len(nlist)-1
                    a3=random.randint(0,currentlength_list)
                    question_a3=nlist[a3]
                    k.append(nlist[a3])
                    nlist.remove(nlist[a3])
                    QButton=button((0,255,0),1100,300,140,50,question_a3)
                    QButton.draw(win,(0,0,0))
                    for i in Not_needed_in_button:
                        if (question_a3==i[0]):
                            print(i[1])
                            nlist.remove(i[1])
                            Not_needed_in_button_recover.append(i[1])
                        elif(question_a3==i[1]):
                            print(i[0])
                            nlist.remove(i[0])
                            Not_needed_in_button_recover.append(i[0])
                    prun=True
                    print("Cthr")
                    print(k)
                    pygame.display.update()
                    
                    #nlist=nlist
                    nor=[]
                    nor=k
                    
                    
                
                    while prun==True:
                        #print("Cthrough")
                        
                        for event in pygame.event.get():
                            
                            
                            posi=pygame.mouse.get_pos()
                            #if event.type==pygame.MOUSEBUTTONDOWN:
                            
                            if 1100+100 > posi[0] > 1100 and 100+50 > posi[1] > 100:
                                
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    us_ans=0
                                    prun=False
                                    
                            #pos=pygame.mouse.get_pos()
                            elif 1100+200 > posi[0] > 1100 and 200+50 > posi[1] > 200:
                                
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    us_ans=1
                                    prun=False
                            #pos=pygame.mouse.get_pos()
                            elif 1100+300 > posi[0] > 1100 and 300+50 > posi[1] > 300:
                                
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    us_ans=2
                                    prun=False
                                  
                    print(nlist)
                    
                    #nlist=["black","blonde hair","male","female","large eyebrows","wears cap/hat",
                          # 'small lips','spectacles','blue eyeballs','moustache','bald','big lips']
                          
                    
                    
                    
                    print(nlist)   
                    #nlist.remove()
                    fun=nor[us_ans]
                    print(fun)
                    for i in Not_needed_in_button:
                        if((fun in k)):
                            print("i")
                                
                            k.remove(fun)
                                
                        if((i[0] in k) and i[0]!=fun):
                            
                            print("i")
                            nlist.append(i[0])
                            nlist.append(i[1])
                            k.remove(i[0])
                        if((i[1] in k) and i[1]!=fun):
                            
                            print("i")
                            nlist.append(i[0])
                            nlist.append(i[1])
                            k.remove(i[1])
                        
                    for i in k:
                        nlist.append(i)
                        k.remove(i)
                            
                                
                    #crip=nlist.index(fun)
                    #print(crip)
                    #pen=nlist.pop(crip)
                    #print(pen)
                    c_req=fun
                    print(nlist)
                    print("DOing..")
                    temp_list=nlist
                    blackout(c_req,ans,character_list,size_list,1100,370)
                    
                    print("DOne")
                   # Second time
                   
                   
                    Not_needed_in_button_recover=[]
                    Not_needed_in_button=[['male','female'],['big lips','small lips'],['white','black']]

                    pin=[]
                    for i in nlist:
                        pin.append(i)
                    
                    #print(nlist)
                    print(temp_list)
                    #temp_list=nlist
                    k=[]
                    nor=[]
                    pygame.display.update()
                    currentlength_list=len(temp_list)-1
                    a1=random.randint(0,currentlength_list)
                    question_a1=temp_list[a1]
                    k.append(temp_list[a1])
                    temp_list.remove(temp_list[a1])
                    QButton=button((0,255,0),1100,100,150,50,question_a1)
                    QButton.draw(win,(0,0,0))
                    print(temp_list)
                    for i in Not_needed_in_button:
                        if (question_a1==i[0]):
                            print(i[1])
                            temp_list.remove(i[1])
                            Not_needed_in_button_recover.append(i[1])
                        elif(question_a1==i[1]):
                            print(i[0])
                            temp_list.remove(i[0])
                            Not_needed_in_button_recover.append(i[0])
                    
                    currentlength_list=len(temp_list)-1
                    a2=random.randint(0,currentlength_list)
                    question_a2=temp_list[a2]
                    k.append(temp_list[a2])
                    temp_list.remove(temp_list[a2])
                    QButton=button((0,255,0),1100,200,150,50,question_a2)
                    QButton.draw(win,(0,0,0))
                    print(temp_list)
                    for i in Not_needed_in_button:
                        if (question_a2==i[0]):
                            print(i[1])
                            temp_list.remove(i[1])
                            Not_needed_in_button_recover.append(i[1])
                        elif(question_a2==i[1]):
                            print(i[0])
                            temp_list.remove(i[0])
                            Not_needed_in_button_recover.append(i[0])
                    
                    currentlength_list=len(temp_list)-1
                    a3=random.randint(0,currentlength_list)
                    question_a3=temp_list[a3]
                    k.append(temp_list[a3])
                    temp_list.remove(temp_list[a3])
                    QButton=button((0,255,0),1100,300,150,50,question_a3)
                    QButton.draw(win,(0,0,0))
                    pygame.display.update()
                    print(temp_list)
                    for i in Not_needed_in_button:
                        if (question_a3==i[0]):
                            print(i[1])
                            temp_list.remove(i[1])
                            Not_needed_in_button_recover.append(i[1])
                        elif(question_a3==i[1]):
                            print(i[0])
                            temp_list.remove(i[0])
                            Not_needed_in_button_recover.append(i[0])
                    prun=True
                    nor=k
                    
                    while prun==True:
                            #print("Cthrough")
                        for event in pygame.event.get():
                            pygame.display.update()
                            
                            posi=pygame.mouse.get_pos()
                            #if event.type==pygame.MOUSEBUTTONDOWN:
                            
                            if 1100+100 > posi[0] > 1100 and 100+50 > posi[1] > 100:
                                
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    us_ans2=0
                                    prun=False
                                    
                            #pos=pygame.mouse.get_pos()
                            elif 1100+200 > posi[0] > 1100 and 200+50 > posi[1] > 200:
                                
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    us_ans2=1
                                    prun=False
                            #pos=pygame.mouse.get_pos()
                            elif 1100+300 > posi[0] > 1100 and 300+50 > posi[1] > 300:
                                
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    us_ans2=2
                                    prun=False
                                    
                    #nlist.remove()
                    
                    #nlist=temp_list
                    print(k)
                    #temp_list=nlist
                    print(temp_list)
                    print(pin)
                    funs=nor[us_ans2]
                    print(funs)
                    for i in Not_needed_in_button:
                        if((funs in k)):
                            
                            k.remove(funs)
                            
                        if((i[0] in k) and i[0]!=funs):
                            
                            temp_list.append(i[0])
                            temp_list.append(i[1])
                            k.remove(i[0])
                        if((i[1] in k) and i[1]!=funs):
                            
                            temp_list.append(i[0])
                            temp_list.append(i[1])
                            k.remove(i[1])
                        
                    for i in k:
                        
                        print("Yes")
                        temp_list.append(i)
                        k.remove(i)
                    #crips=pin.index(funs)
                    #print(crips)
                    #pen=pin.pop(crips)
                    #print(pen)
                    c_req=funs
                    #print(pin)
                    print("DOing..")
                    blackout(c_req,ans,character_list,size_list,1100,410)
                    print("DOne")
                    print(temp_list)
                    
                    # Third Time
                    Not_needed_in_button=[['male','female'],['big lips','small lips'],['white','black']]
                    pin1=[]
                    for i in pin:
                        pin1.append(i)
                    
                    Not_needed_in_button_recover=[]
                    k=[]
                    nor=[]
                    pygame.display.update()
                    currentlength_list=len(temp_list)-1
                    a1=random.randint(0,currentlength_list)
                    question_a1=temp_list[a1]
                    k.append(temp_list[a1])
                    temp_list.remove(temp_list[a1])
                    QButton=button((0,255,0),1100,100,150,50,question_a1)
                    QButton.draw(win,(0,0,0))
                    print(temp_list)
                    for i in Not_needed_in_button:
                        if (question_a1==i[0]):
                            print(i[1])
                            temp_list.remove(i[1])
                            Not_needed_in_button_recover.append(i[1])
                        elif(question_a1==i[1]):
                            print(i[0])
                            temp_list.remove(i[0])
                            Not_needed_in_button_recover.append(i[0])
                    
                    currentlength_list=len(temp_list)-1
                    a2=random.randint(0,currentlength_list)
                    question_a2=temp_list[a2]
                    k.append(temp_list[a2])
                    temp_list.remove(temp_list[a2])
                    QButton=button((0,255,0),1100,200,150,50,question_a2)
                    QButton.draw(win,(0,0,0))
                    print(temp_list)
                    for i in Not_needed_in_button:
                        if (question_a2==i[0]):
                            print(i[1])
                            temp_list.remove(i[1])
                            Not_needed_in_button_recover.append(i[1])
                        elif(question_a2==i[1]):
                            print(i[0])
                            temp_list.remove(i[0])
                            Not_needed_in_button_recover.append(i[0])
                    
                    currentlength_list=len(temp_list)-1
                    a3=random.randint(0,currentlength_list)
                    question_a3=temp_list[a3]
                    k.append(temp_list[a3])
                    temp_list.remove(temp_list[a3])
                    QButton=button((0,255,0),1100,300,150,50,question_a3)
                    QButton.draw(win,(0,0,0))
                    print(temp_list)
                    for i in Not_needed_in_button:
                        if (question_a3==i[0]):
                            print(i[1])
                            temp_list.remove(i[1])
                            Not_needed_in_button_recover.append(i[1])
                        elif(question_a3==i[1]):
                            print(i[0])
                            temp_list.remove(i[0])
                            Not_needed_in_button_recover.append(i[0])
                                                
                    pygame.display.update()
                    prun=True
                    nor=k
                    
                    while prun==True:
                        #print("Cthrough")
                        pygame.display.update()
                        for event in pygame.event.get():
                            posi=pygame.mouse.get_pos()
                            #if event.type==pygame.MOUSEBUTTONDOWN:
                            
                            if 1100+100 > posi[0] > 1100 and 100+50 > posi[1] > 100:
                                
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    us_ans3=0
                                    prun=False
                                    
                            #pos=pygame.mouse.get_pos()
                            elif 1100+200 > posi[0] > 1100 and 200+50 > posi[1] > 200:
                                
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    us_ans3=1
                                    prun=False
                            #pos=pygame.mouse.get_pos()
                            elif 1100+300 > posi[0] > 1100 and 300+50 > posi[1] > 300:
                                
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    us_ans3=2
                                    prun=False
                                    
                   
                    print(k)
                    #temp_list=nlist
                    print(temp_list)
                    print(pin1)
                    funs=nor[us_ans3]
                    print(funs)
                    for i in Not_needed_in_button:
                        if((funs in k)):
                            if((i[0]==funs or i[1]==funs)):
                                k.remove(funs)
                            
                        if((i[0] in k) and i[0]!=funs):
                            
                            temp_list.append(i[0])
                            temp_list.remove(i[0])
                        if((i[1] in k) and i[1]!=funs):
                            
                            temp_list.append(i[0])
                            temp_list.append(i[1])
                            k.remove(i[1])
                    print(k)    
                    for i in k:
                        
                        print("Yes")
                        temp_list.append(i)
                        k.remove(i)
                    
                    c_req=funs
                    
                    print("DOing..")
                    blackout(c_req,ans,character_list,size_list,1100,450)
                    print("DOne")
                    
                    
                    # Now making a guess
                    guessButton=button((0,255,0),1100,570,100,50,'Guess')
                    guessButton.draw(win,(0,0,0))
                    pygame.display.update()
                    
                    print(check_list)
                    if(sql_ask==1):
                        print("jaks")
                        score=sql_sc
                    else:
                        score=0
                    
                        
                    again=False     
                    #check_list.remove(ans)
                    while again==False:
                                        
                        for event in pygame.event.get():
                            pos=pygame.mouse.get_pos()
                            if 1100+100 > pos[0] > 1100 and 570+50 > pos[1] > 570:
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    print("CLicked the button")
                        
                                    print("Time to guess")
                                    remaining_c=21-len(check_list)
                                    alt=remaining_c

                                    
                                    win.fill((255,255,255))
                                    print(check_list)
                                    #king=False
                                    if(alt==0):
                                        time.sleep(4)
                                        win.fill((255,255,255))
                                        score+=100
                                        want="Score: "+str(score)
                                        print("You Win")
                                        sButton=button((255,0,0),1050,100,200,50,want)
                                        sButton.draw(win,(0,0,0))
                                        up_score(username_sql,score)
                                          
                                        #pygame.display.update()
                                        leader_board = pygame.image.load(r'C:\Users\user\Desktop\Guess who\LB1.png')
                                        leader_board = pygame.transform.scale(leader_board, (900,700))
                                        win.blit(leader_board, (50,50))
                                        textwrite("You Won",(0, 0, 128),30,1150,60)
                                        
                                        pygame.display.update()
                                        down_score()
                                        print("Gaya")
                                                    
                                        time.sleep(7) 
                                        again=True
                                        king=True
                                        print("You Win")
                                        #break
                                        
                                                    
                                                    
                                                    
                                    else:
                                        king=False   
                                    while king==False:
                                        for i in range(0,alt):
                                            input_box2 = InputBox(1050, 400, 200, 40)
                                            stay=0
                                            text_ans=""
                                            done=False
                                            
                                            while done==False:
                                                for event in pygame.event.get():
                                                    
                                                    input_box2.handle_event(event)
                                                
                                                win.fill((0,255,0))
                                                textwrite("Your Guess:",(0, 0, 0),30,1050,350)    
                                                #stay+=1
                                                input_box2.draw(win)
                                                
                                                pygame.display.update()
                                                
                                                if(text_ans!=""):
                                                    done=True
                                                
                                            else:
                                                
                                                nameis=text_ans
                                                    #print("going")
                                                for k in size_list:
                                                    if ((k[0]==nameis) and (k[0] not in check_list)) :
                                                        
                                                        check_list.append(k[0])
                                                        wimage = pygame.image.load(r'C:\Users\user\Desktop\Guess who\WR.png')
                                                        wimage = pygame.transform.scale(wimage, (80,70))
                                                       
                                                        win.blit(wimage, (k[1]+20,k[2]+30))
                                                    
                                                xc=50
                                                yc=50
                                                for i in character_list:
                                                    if(xc>900):
                                                        xc=50
                                                        yc+=200
                                                    carImg = pygame.image.load(r'C:\Users\user\Desktop\Guess who\Pics\c_'+i[0]+'.jpg')
                                                    carImg = pygame.transform.scale(carImg, (120,140))
                                                    win.blit(carImg, (xc,yc))
                                                    xc+=150
                                                    
                                                for k in size_list:
                                                    if(k[0] in check_list):
                                                        wimage = pygame.image.load(r'C:\Users\user\Desktop\Guess who\WR.png')
                                                        wimage = pygame.transform.scale(wimage, (80,70))
                                                        win.blit(wimage, (k[1]+20,k[2]+30))
                                                        if(nameis not in name_list):
                                                            print("Fooled")
                                                            #done=True
                                                #time.sleep(2)
                                                pygame.display.update()
                                                        
                                                        
                                                if(nameis==ans):
                                                    
                                                    score+=100
                                                    want="Score: "+str(score)
                                                    print("You Win")
                                                    sButton=button((255,0,0),1050,100,200,50,want)
                                                    sButton.draw(win,(0,0,0))
                                                    up_score(username_sql,score)
                                                    pygame.display.update()
                                                    time.sleep(4)  
                                                    win.fill((255,255,255))
                                                    #pygame.display.update()
                                                    leader_board = pygame.image.load(r'C:\Users\user\Desktop\Guess who\LB1.png')
                                                    leader_board = pygame.transform.scale(leader_board, (900,700))
                                                    win.blit(leader_board, (50,50))
                                                    textwrite("You Won",(0, 0, 128),30,1150,60)
                                                    down_score()
                                                    pygame.display.update()
                                                    print("Gaya")

                                                    time.sleep(7) 

                                                    
                                                        
                                                    print("KK")
                                                    king=True
                                                    again=True
                                                        
                                                    break
                                                else:
                                                    score-=20
                                                    want="Score: "+str(score)
                                                    print(want)
                                                    sButton=button((255,0,0),1050,100,200,50,want)
                                                    sButton.draw(win,(0,0,0))
                                                    textwrite("Wrong Guess!",(0, 0, 0),30,1100,600)
                                                    pygame.display.update()
                                                    print("yes")
                                        
                                                    time.sleep(4)  
                                                   
                                        else:
                                            up_score(username_sql,score)
                                            win.fill((255,255,255))  

                                            leader_board = pygame.image.load(r'C:\Users\user\Desktop\Guess who\LB1.png')
                                            leader_board = pygame.transform.scale(leader_board, (900,700))
                                            print("Gaya")
                                            win.blit(leader_board, (50,50))
                                            textwrite("Sorry,You lose!!",(0, 0, 128),30,1150,60)
                                            down_score()
                                            pygame.display.update()
                                            time.sleep(8)
                                            king=True
                                            again=True
                                            
                    
                   #funct algorithm 
                    pygame.display.update()
                    win.fill((255,255,255))
                    textwrite("DO YOU WANT TO save the username??",(0, 0, 128),30,550,400)
                    fButton=button((255,0,0),1050,100,200,50,"Yes")
                    fButton.draw(win,(0,0,0))
                    fButton=button((255,0,0),1050,400,200,50,"No")
                    fButton.draw(win,(0,0,0))
                    pygame.display.update()
                    pri=True
                    while pri==True:
                        print("inw")
                        pygame.display.update()
                        for event in pygame.event.get():
                            pos=pygame.mouse.get_pos()
                            if 1050+200 > pos[0] > 1050 and 100+50 > pos[1] > 100:
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    bon=1
                                    pri=False
                                    
                            elif 1050+200 > pos[0] > 1050 and 400+50 > pos[1] > 400:
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    bon=0
                                    pri=False
                    else:
                        if(bon==1):
                            #prik=True
                            break
                        elif(bon==0):
                            cursor = mydb.cursor()
                            sql="""delete from gs where Username='%s'"""%(username_sql)
                            mycursor.execute(sql)
                            mydb.commit()
                            #prik=True
                    pygame.display.update()        
                    win.fill((255,255,255))
                    textwrite("DO YOU WANT TO CONTINUE",(0, 0, 128),30,550,400)
                    fButton=button((255,0,0),1050,100,200,50,"Yes")
                    fButton.draw(win,(0,0,0))
                    fButton=button((255,0,0),1050,400,200,50,"No")
                    fButton.draw(win,(0,0,0))
                    pygame.display.update()
                    #prik=True
                    prik=True
                    while prik==True:
                        print("inw")
                        pygame.display.update()
                        for event in pygame.event.get():
                            pos=pygame.mouse.get_pos()
                            if 1050+200 > pos[0] > 1050 and 100+50 > pos[1] > 100:
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    bond=1
                                    prik=False
                                    
                            elif 1050+200 > pos[0] > 1050 and 400+50 > pos[1] > 400:
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    bond=0
                                    prik=False
                    else:
                        if(bond==1):
                            play_again=1
                            
                            pygame.display.update()
                            time.sleep(1)
                            run=True
                        elif(bond==0):
                            print("Bye")
                            pygame.quit()
                            quit()
                    
                    print("abhi")
                    
           
        if event.type == KEYDOWN:
                if event.key == K_s:
                    
                    pygame.quit()
                    quit()
        pygame.display.update()





