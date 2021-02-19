import pygame,sys
pygame.init()

w=800
h=600
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("Associates Version 1.0.1")

people=[]

class Person:
    def __init__(self,name,number,pied,order,clicked=False):
        self.name=name
        self.number=number
        self.pied=pied
        self.order=order
        self.clicked=clicked
        self.back=None
        self.pier=None
        self.pie=pygame.image.load('pie.png')
        self.pie=pygame.transform.scale(self.pie,(30,30))
        if len(self.name)>=30 and len(self.name)<40:
            self.text=smallFont.render(name,True,(255,0,204))
        elif len(name)>=40:
            self.text=tinyFont.render(name,True,(255,0,204))
        elif len(name)<30:
            self.text=BigFont.render(name,True,(255,0,204))
        self.textRect=self.text.get_rect(topleft=(20,(len(people)+1)*50))
        
        self.pieRect=self.pie.get_rect(center=(self.textRect.right+30,(len(people)+1)*50+27))
    
    def draw(self):
        screen.blit(self.text,self.textRect)
        
    def viewed(self):
        self.viewRect=self.text.get_rect(center=(w//2,35))
        screen.blit(self.text,self.viewRect)
        self.pieRectClick=self.pie.get_rect(center=(w//2,h//2))
        if self.pied:
            screen.blit(self.pie,self.pieRectClick)
        
        self.numtext=smallFont.render(self.number,True,(255,0,204))
        self.numRect=self.numtext.get_rect(center=(w//2,80))
        screen.blit(self.numtext,self.numRect)
        
        self.back=BigFont.render('<=',True,(255,0,204))
        self.backRect=self.back.get_rect(topleft=(10,10))
        screen.blit(self.back,self.backRect)
        
        self.pier=BigFont.render('Pie?',True,(255,0,204))
        self.pierRect=self.pier.get_rect(center=(w//2,h//2))
        if not self.pied:
            screen.blit(self.pier,self.pierRect)

BiggerFont=pygame.font.SysFont('comicsansms',64)
BigFont=pygame.font.SysFont('comicsansms',40)
smallFont=pygame.font.SysFont('comicsansms',30)
tinyFont=pygame.font.SysFont('comicsansms',21)

people=[Person('Grandma Pumkin Pierson Leader of Pies','+0 (666) 666-1313',True,1)]
people.append(Person('Grandpa Mete Pierson Leader of Weird spelling and apple references','+0 (111) 222-9009',False,90))
people.append(Person("Banana Bonbon Leader of the BONBONs",'+0 (000) 000-0000',False,123))
people.append(Person("Weird Colour Guy Leader of the COLOURs",'+0 (999) 777-3355',False,123))

def new():
    name=input("Write their name: ")
    phoneNum=input("Write their number: ")
    
    while True:
        if len(phoneNum) == 10:
            phoneNum="(" + phoneNum[0:3] + ") " + phoneNum[3:6] + '-' + phoneNum[6:]
            break
        elif len(phoneNum) == 11:
            phoneNum='+'+phoneNum[0]+" (" + phoneNum[1:4] + ") " + phoneNum[4:7] + '-' + phoneNum[7:]
            break
        elif phoneNum == '411':
            break
        elif phoneNum== '911':
            break
        phoneNum=input("Write their number: ")
        
    people.append(Person(name,phoneNum,False,1))

NewBttn=BiggerFont.render('+',True,(255,0,204))
NewBttnRect=NewBttn.get_rect(topright=(w-20,5))

#main loop
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if NewBttnRect.collidepoint(event.pos):
                new()
            for x in range(len(people)):
                i=people[x]
                if i.textRect.collidepoint(event.pos):
                    print(i.number)
                    i.clicked=True
                
                if i.back!=None:
                    if i.backRect.collidepoint(event.pos):
                        i.back=None
                        i.clicked=False
                if i.pier!=None:
                    if i.pierRect.collidepoint(event.pos):
                        i.pied=True
                     
    screen.fill((198, 195, 244))
    
    if len(people)==0:
        screen.blit(NewBttn,NewBttnRect)
    
    for i in people:
       if not i.clicked:
           i.draw()
           screen.blit(NewBttn,NewBttnRect)
           if i.pied:
               screen.blit(i.pie,i.pieRect)
       else:
            screen.fill((198, 195, 244))
            i.viewed()
            break       
    
    pygame.display.update()
    
