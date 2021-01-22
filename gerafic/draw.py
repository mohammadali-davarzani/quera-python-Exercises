import pygame

#colors
white = (255,255,255)


#start 
pygame.init()

screen = pygame.display.set_mode((300,300))

screen.fill(white)


pen_size = 1

pen_color = [0,0,0]

order = input().split()
x = True
while x == True:
    pygame.event.pump()

    if order[0] == "end":

        pygame.image.save(screen, 'draw.png')

        x = False

    if order[0] == "change":

        if order[1] == "size":

            pen_size = int(order[2])

            order = input().split()

        elif order[1] == "color":

            pen_color[0] = int(order[2])
  
            pen_color[1] = int(order[3])

            pen_color[2] = int(order[4])

            order = input().split()

    elif order[0] == "draw":

        if order[1] == "line":

            pygame.draw.line(screen, tuple(pen_color), (int(order[2]), int(order[3])), (int(order[4]), int(order[5])), pen_size)
        
            pygame.display.update()

            order = input().split()

        elif order[1] == "circle":

            pygame.draw.circle(screen, tuple(pen_color), (int(order[2]), int(order[3])), int(order[4]), pen_size)

            pygame.display.update()

            order = input().split()

        elif order[1] == "polygon":

            Dimensions = list()

            for i in range(2, len(order)):

                try :
                    if i % 2 == 0:

                        Dimensions.append((int(order[i]), int(order[i+1])))
                    
                except IndexError:

                    Dimensions.append((int(order[i])))
            
            pygame.draw.polygon(screen, tuple(pen_color), Dimensions, pen_size)

            pygame.display.update()

            order = input().split()


