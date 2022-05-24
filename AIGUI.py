# Simple pygame program

# Import and initialize the pygame library
import pygame
import random


globalColors = []

for i in range(50):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    globalColors.append((r, g, b))


def writeText(screen, word, position):
    font = pygame.font.SysFont("Arial", 30)
    text = font.render(word, True, (0, 0, 0))
    screen.blit(text, position)


def drawGrid(screen, size):
    xPosition = 10  # left
    yPosition = 10  # top

    # make an array of tuples for each rectangle with an index
    # (xindex,yindex,xposition,ypositio)
    rectangle_list = []
    # draw the table board
    x = 1
    y = 1
    for i in range(size):
        inner_list = []
        for j in range(size):
            rectangle = pygame.Rect(xPosition, yPosition, 60, 60)
            # LEFT,TOP,RIGHT,BOTTOM
            pygame.draw.rect(screen, (255, 255, 255), rectangle, 2)
            inner_list.append([rectangle])
            #writeText(screen, "3*", rectangle.midtop)
            # draw_text("hi",rect.topleft)
            xPosition += 60
            y += 1
        rectangle_list.append(inner_list)
        x += 1
        y = 1
        xPosition = 10  # initial x-position
        yPosition += 60
    #print(rectangle_list, "rectangle list")
    return rectangle_list


def applyGrid(screen, grid, rectangle_list):
    cage_number = []
    cage_color = []
    globalidex = -1
    for rows, recRows in zip(grid, rectangle_list):
        for cell, recCell in zip(rows, recRows):
            #print(cell, recCell)
            if cell[0] not in cage_number:
                globalidex += 1
                cage_number.append(cell[0])
                cage_color.append([cell[0], globalColors[globalidex]])
                pygame.draw.rect(screen, globalColors[globalidex], recCell[0])
                pygame.draw.rect(screen, (255, 255, 255), recCell[0], 2)
                if (cell[2] == "="):
                    writeText(screen, str(cell[1]), recCell[0].topleft)
                else:
                    writeText(screen, str(cell[1])+cell[2], recCell[0].topleft)

            else:
                for index in cage_color:
                    print(index)
                    if index[0] == cell[0]:
                        pygame.draw.rect(screen, index[1], recCell[0])
                        pygame.draw.rect(
                            screen, (255, 255, 255), recCell[0], 2)

            #print(index, cell)
            # r = rectangle_list[index][3]
            # for x, y, r in rectangle_list[index]:
    print(cage_color)


def GamePlaying(size, grid):
    pygame.init()

    # Set up the drawing window
    screenWidth = 800
    screenHeight = 800
    screen = pygame.display.set_mode([screenWidth, screenHeight])

    #title and icon
    pygame.display.set_caption("KenKen Puzzle")
    icon = pygame.image.load('number-puzzle.png')
    pygame.display.set_icon(icon)
    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Fill the background with white
        screen.fill((0, 0, 0))
        rectangle_list = drawGrid(screen, size)
        applyGrid(screen, grid, rectangle_list)

        # union_list_y = []
        # union_list_x = []
        # for x, y, r in rectangle_list:
        #     if(x == 1 and y == 2):
        #         union_list_y.append(r)
        #         pygame.draw.rect(screen, (255, 0, 0), r)
        #         pygame.draw.rect(screen, (255, 255, 255), r,
        #                      2)  # LEFT,TOP,RIGHT,BOTTOM
        #         writeText(screen, "new", r.topleft)
        #         pygame.draw.rect(screen, (255, 0, 0), r)
        #         # LEFT,TOP,RIGHT,BOTTOM
        #         pygame.draw.rect(screen, (255, 255, 255), r, 2)
        #         writeText(screen, "mizo", r.topleft)
        #     elif (x == 2 and y == 2):
        #         union_list_y.append(r)
        #         union_list_x.append(r)
        #     elif(x == 2 and y == 3):
        #         union_list_x.append(r)

        # print(union_list_y, "y")
        # rect_union_y = union_list_y[0].unionall(union_list_y)
        # pygame.draw.rect(screen, (255, 255, 255), rect_union_y)

        # pygame.draw.rect(screen, (0, 255, 0), rect_union_y, 2)

        # print(union_list_x, "x")
        # rect_union_x = union_list_x[0].unionall(union_list_x)
        # pygame.draw.rect(screen, (255, 255, 255), rect_union_x, 2)

        # pygame.draw.rect(screen, (0, 255, 0), rect_union_x, 2)

        # make horizonatal squares of size n
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


# GamePlaying(3, [[[1, 12, '*'], [2, 18, '*'], [2, 18, '*']], [[1, 12, '*'],
#             [3, 1, '='], [2, 18, '*']], [[1, 12, '*'], [1, 12, '*'], [2, 18, '*']]])
