# Import library
import pygame

# Game option
WINDOW_HEIGHT = 360
WINDOW_WIDTH = 360

# Color
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
CORAL = pygame.Color(255, 127, 80)
DODGERBLUE = pygame.Color(30, 144, 255)
GRAY = pygame.Color(128, 128, 128)
SILVER = pygame.Color(192, 192, 192)
SANDYBROWN = pygame.Color(244, 164, 96)
CHOCOLATE = pygame.Color(210, 105, 30)
SADDLEBROWN = pygame.Color(139, 69, 19)
SIENNA = pygame.Color(160, 82, 45)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption("TicTacToe Game")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Game
running = True

# Function
def drawBoardCell(surf, colo_back, color, y, x):
    pygame.draw.rect(surf, colo_back, [x * 120, y * 120, 120, 120])
    pygame.draw.rect(surf, color, [x * 120 + 5, y * 120 + 5, 120 - 10, 120 - 10])


def drawCircleMark(surf, color_back, color, y, x):
    pygame.draw.circle(surf, color_back, [x * 120 + 60, y * 120 + 60], 60 - 8, 14)
    pygame.draw.circle(surf, color, [x * 120 + 60, y * 120 + 60], 60 - 10, 14 - 4)


def drawXMark(surf, color_back, color, y, x):
    pygame.draw.line(surf, color_back, [x * 120 + 20, y * 120 + 10],
                     [x * 120 + 120 - 20, y * 120 + 120 - 10], 20)
    pygame.draw.line(surf, color_back, [x * 120 + 120 - 20, y * 120 + 10],
                     [x * 120 + 20, y * 120 + 120 - 10], 20)
    pygame.draw.line(surf, color, [x * 120 + 22, y * 120 + 12],
                     [x * 120 + 120 - 22, y * 120 + 120 - 12], 20 - 6)
    pygame.draw.line(surf, color, [x * 120 + 120 - 22, y * 120 + 12],
                     [x * 120 + 22, y * 120 + 120 - 12], 20 - 6)


# Main loop
while running:
    # Key event
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Refresh game screen
    window.fill(BLACK)
    drawBoardCell(window, SADDLEBROWN, SIENNA, 0, 0)
    drawBoardCell(window, CHOCOLATE, SANDYBROWN, 2, 2)
    drawCircleMark(window, GRAY, SILVER, 0, 1)
    drawXMark(window, GRAY, SILVER, 1, 1)
    drawCircleMark(window, BLACK, CORAL, 0, 2)
    drawXMark(window, BLACK, DODGERBLUE, 1, 2)
    pygame.display.update()

# Quit
pygame.quit()
quit()