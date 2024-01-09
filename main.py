import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #Here, we say the pixel size of the game window with variables
pygame.display.set_caption('Number Cruncher')  #This is for naming the game window

clock = pygame.time.Clock()
fps = 60

TEXT_COLOR = (255, 255, 255)

title_font = pygame.font.Font("Minecraft.ttf", 40)
text_font = pygame.font.Font("Minecraft.ttf", 40)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def draw_question(operator, num1, num2, text_font, TEXT_COLOR):
    draw_text(str(operator), text_font, TEXT_COLOR, 150, 100)
    draw_text(str(num1), text_font, TEXT_COLOR, 100, 100)
    draw_text(str(num2), text_font, TEXT_COLOR, 200, 100)
def rogs():     #Random Operation Generation System
    return random.randint(0, 3)

def rngs():     #Random Number Generation System
    return random.randint(1, 99)

opr = rogs()
num1 = rngs()
num2 = rngs()

isRunning = True
while isRunning:

    draw_text("Number Cruncher", title_font, TEXT_COLOR, 22, 10)
    if opr == 0:
        draw_question(str(" +"), num1, num2, text_font, TEXT_COLOR)
    elif opr == 1:
        draw_question(str(" -"), num1, num2, text_font, TEXT_COLOR)
    elif opr == 2:
        draw_question(str(" x"), num1, num2, text_font, TEXT_COLOR)
    elif opr == 3:
        draw_question(str(" /"), num1, num2, text_font, TEXT_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    clock.tick(fps)  #Limiting fps to 60, so everything in code can work according to 60fps

    pygame.display.flip()

pygame.quit()