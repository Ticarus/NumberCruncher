import pygame
import random

pygame.init()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Number Cruncher')

clock = pygame.time.Clock()
fps = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

text_font = pygame.font.Font("Minecraft.ttf", 40)

button_image = pygame.image.load("Button.png")
answer_button_0 = Button(10, 200, button_image)
answer_button_1 = Button(10, 300, button_image)
answer_button_2 = Button(210, 200, button_image)
answer_button_3 = Button(210, 300, button_image)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def draw_question(operator, num1, num2, text_font, TEXT_COLOR):
    draw_text(str(operator), text_font, TEXT_COLOR, 180, 100)
    draw_text(str(num1), text_font, TEXT_COLOR, 130, 100)
    draw_text(str(num2), text_font, TEXT_COLOR, 230, 100)
def rogs():     #Random Operation Generation System
    return random.randint(0, 3)

def rngs():     #Random Number Generation System
    return random.randint(1, 99)

def rags():     #Random Answer Generation System
    return random.randint(-98, 198)

opr = rogs()
num1 = rngs()
num2 = rngs()
correct_answer = 0

ra_0 = rags() + rngs()
ra_1 = rags() + num1
ra_2 = rags() + num2

isCorrect = False

isRunning = True
while isRunning:

    draw_text("Number Cruncher", text_font, WHITE, 22, 10)
    if opr == 0:
        draw_question(str(" +"), num1, num2, text_font, WHITE)
        correct_answer = num1 + num2


    elif opr == 1:
        draw_question(str(" -"), num1, num2, text_font, WHITE)
        correct_answer = num1 - num2

    elif opr == 2:
        draw_question(str(" x"), num1, num2, text_font, WHITE)
        correct_answer = num1 * num2

    elif opr == 3:
        draw_question(str(" /"), num1, num2, text_font, WHITE)
        correct_answer = int(num1 / num2)

    draw_text(str(ra_0), text_font, WHITE, 20, 220)
    draw_text(str(ra_1), text_font, WHITE, 20, 320)
    draw_text(str(ra_2), text_font, WHITE, 220, 320)
    draw_text(str(correct_answer), text_font, WHITE, 220, 220)

    answer_button_0.draw()
    answer_button_1.draw()
    answer_button_2.draw()
    answer_button_3.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            
    clock.tick(fps)

    pygame.display.flip()

pygame.quit()