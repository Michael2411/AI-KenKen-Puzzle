# Simple pygame program

# Import and initialize the pygame library
import pygame
def writeText(screen,word,position):
    font=pygame.font.SysFont("Arial",30)
    text=font.render(word,True,(0,0,255))
    screen.blit(text,position)
    
pygame.init()

# Set up the drawing window
screenWidth=800
screenHeight=800
screen = pygame.display.set_mode([screenWidth, screenHeight])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 0, 0))
    xPosition=20 #left
    yPosition=20 #top
    
    #make an array of tuples for each rectangle with an index
    #(xindex,yindex,xposition,ypositio)
    rectangle_list=[]
    #draw the table board
    x=1
    y=1
    for i in range (4):
        for i in range(4):
            rectangle=pygame.Rect(xPosition,yPosition,60,60)
            pygame.draw.rect(screen,(255,255,255),rectangle,2) #LEFT,TOP,RIGHT,BOTTOM
            rectangle_list.append((x,y,rectangle))
            writeText(screen,"3*",rectangle.midtop)
            #draw_text("hi",rect.topleft)
            xPosition+=60
            y+=1
        x+=1
        y=1    
        xPosition=20 #initial x-position
        yPosition+=60    
    
    union_list_y = []
    union_list_x=[]
    for x,y,r in rectangle_list:
        if(x==1 and y==2):
            union_list_y.append(r)
            pygame.draw.rect(screen,(255,0,0),r)
            pygame.draw.rect(screen,(255,255,255),r,2) #LEFT,TOP,RIGHT,BOTTOM
            writeText(screen,"new",r.topleft)
            pygame.draw.rect(screen,(255,0,0),r)
            # LEFT,TOP,RIGHT,BOTTOM
            pygame.draw.rect(screen, (255, 255, 255), r, 2)
            writeText(screen,"mizo",r.topleft)
        elif (x==2 and y==2):
            union_list_y.append(r)
            union_list_x.append(r)
        elif(x==2 and y==3):
            union_list_x.append(r)    
            
    print(union_list_y,"y")        
    rect_union_y=union_list_y[0].unionall(union_list_y)
    pygame.draw.rect(screen, (255, 255, 255), rect_union_y)

    pygame.draw.rect(screen,(0,255,0),rect_union_y,2)

    print(union_list_x,"x")
    rect_union_x=union_list_x[0].unionall(union_list_x)
    pygame.draw.rect(screen, (255, 255, 255), rect_union_x, 2)

    pygame.draw.rect(screen,(0,255,0),rect_union_x,2)
    #make horizonatal squares of size n
    # for i in range(4):
    #     surf=pygame.Surface((50,50)) #create surface with length and width
    #     surf.fill((255,255,255))
    #     rect=surf.get_rect()
    #     screen.blit(surf,(width/2  ,height/2),)#center
    #     width=width+50 
    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)


    # Flip the display to run any changes
    pygame.display.flip()



# Done! Time to quit.
pygame.quit()
