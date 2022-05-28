# Simple pygame program

# Import and initialize the pygame library
import pygame
import random

class Game_Gui():
    def __init__(self):
        self.globalColors = []
        self.generate_colours()

    def generate_colours(self):
        for i in range(50):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            if r == g and g == b:  # execlude dark colours
                pass
            elif (r, g, b) not in self.globalColors:  # prevent repeating numbers
                self.globalColors.append((r, g, b))

    def writeText(self, screen, word, position, font):
        font = pygame.font.SysFont("Arial", font)
        text = font.render(word, True, (0, 0, 0))
        screen.blit(text, position)

    def drawGrid(self, screen, size):
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
                rectangle = pygame.Rect(xPosition, yPosition, 80, 80)
                # LEFT,TOP,RIGHT,BOTTOM
                pygame.draw.rect(screen, (255, 255, 255), rectangle, 2)
                inner_list.append([rectangle])
                #writeText(screen, "3*", rectangle.midtop)
                # draw_text("hi",rect.topleft)
                xPosition += 80
                y += 1
            rectangle_list.append(inner_list)
            x += 1
            y = 1
            xPosition = 10  # initial x-position
            yPosition += 80
        #print(rectangle_list, "rectangle list")
        return rectangle_list

    def applyGrid(self, screen, grid, rectangle_list):
        cage_number = []
        cage_color = []
        globalidex = -1
        for rows, recRows in zip(grid, rectangle_list):
            for cell, recCell in zip(rows, recRows):
                #print(cell, recCell)
                if cell[0] not in cage_number:
                    globalidex += 1
                    cage_number.append(cell[0])
                    cage_color.append([cell[0], self.globalColors[globalidex]])
                    pygame.draw.rect(
                        screen, self.globalColors[globalidex], recCell[0])
                    pygame.draw.rect(screen, (255, 255, 255), recCell[0], 2)
                    if (cell[2] == "="):
                        self.writeText(screen, str(
                            cell[1]), recCell[0].topleft, 30)
                    else:
                        self.writeText(screen, str(cell[1]) +
                                       cell[2], recCell[0].topleft, 30)

                else:
                    for index in cage_color:
                        #print(index)
                        if index[0] == cell[0]:
                            pygame.draw.rect(screen, index[1], recCell[0])
                            pygame.draw.rect(
                                screen, (255, 255, 255), recCell[0], 2)
                #print(index, cell)
                # r = rectangle_list[index][3]
                # for x, y, r in rectangle_list[index]:
        #print(cage_color)

    def applySoution(self, screen, solution, rectangle_list):
        for rows, solRows in zip(rectangle_list, solution):
            i = 0
            #print(rows, solRows, "rows1")
            for cell in rows:
                self.writeText(screen, str(solRows[i]), cell[0].center, 20)
                #print(cell, solRows[i], "rows")
                i += 1

    def GamePlaying(self, size, grid, solution):
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
            rectangle_list = self.drawGrid(screen, size)
            self.applyGrid(screen, grid, rectangle_list)
            self.applySoution(screen, solution, rectangle_list)

            # Flip the display to run any changes
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()


# GamePlaying(3, [[[1, 12, '*'], [2, 18, '*'], [2, 18, '*']], [[1, 12, '*'],
#             [3, 1, '='], [2, 18, '*']], [[1, 12, '*'], [1, 12, '*'], [2, 18, '*']]])
