# Import library
import pygame

# Game option
WINDOW_HEIGHT = 360
WINDOW_WIDTH = 360
WINDOW_FPS = 60

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

# FPS
fps = pygame.time.Clock()

# Game
running = True
time = 0
player = {"a": -1, "b": 1}

# Cursor
cursor = [1, 1]
cursor_type = player["a"]

# Board
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Main loop
while running:
    # Frame Per Second / Refresh Rate
    delta_time = fps.tick(WINDOW_FPS)
    time += delta_time

    # Key event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cursor[0] += -1 if cursor[0] > 0 else 0
            if event.key == pygame.K_DOWN:
                cursor[0] += 1 if cursor[0] < 2 else 0
            if event.key == pygame.K_LEFT:
                cursor[1] += -1 if cursor[1] > 0 else 0
            if event.key == pygame.K_RIGHT:
                cursor[1] += 1 if cursor[1] < 2 else 0
            if event.key == pygame.K_RETURN:
                board[cursor[0]][cursor[1]] = cursor_type
                cursor_type = player["b"] if cursor_type == player["a"] else player["a"]
            if event.key == pygame.K_ESCAPE:
                running = False
            print(board)

    # Game over

    # Refresh game screen
    window.fill(BLACK)
    for i in range(3): # Board
        for j in range(3):
            if (i + j) % 2 == 0:
                pygame.draw.rect(window, SADDLEBROWN, [j * 120, i * 120, 120, 120])
                pygame.draw.rect(window, SIENNA, [j * 120 + 5, i * 120 + 5, 120 - 10, 120 - 10])
            else:
                pygame.draw.rect(window, CHOCOLATE, [j * 120, i * 120, 120, 120])
                pygame.draw.rect(window, SANDYBROWN, [j * 120 + 5, i * 120 + 5, 120 - 10, 120 - 10])
            if board[i][j] == player["a"]:
                pygame.draw.circle(window, BLACK, [j * 120 + 60, i * 120 + 60], 60 - 8, 14)
                pygame.draw.circle(window, CORAL, [j * 120 + 60, i * 120 + 60], 60 - 10, 10)
            elif board[i][j] == player["b"]:
                pygame.draw.line(window, BLACK, [j * 120 + 20, i * 120 + 20],
                                 [j * 120 + 120 - 20, i * 120 + 120 - 20], 20)
                pygame.draw.line(window, BLACK, [j * 120 + 120 - 20, i * 120 + 20],
                                 [j * 120 + 20, i * 120 + 120 - 20], 20)
                pygame.draw.line(window, DODGERBLUE, [j * 120 + 22, i * 120 + 22],
                                 [j * 120 + 120 - 22, i * 120 + 120 - 22], 14)
                pygame.draw.line(window, DODGERBLUE, [j * 120 + 120 - 22, i * 120 + 22],
                                 [j * 120 + 22, i * 120 + 120 - 22], 14)

    if cursor_type == player["a"]: # Cursor
        pygame.draw.circle(window, GRAY, [cursor[1] * 120 + 60, cursor[0] * 120 + 60], 60 - 8, 14)
        pygame.draw.circle(window, SILVER, [cursor[1] * 120 + 60, cursor[0] * 120 + 60], 60 - 10, 10)
    else:
        pygame.draw.line(window, GRAY, [cursor[1] * 120 + 20, cursor[0] * 120 + 20],
                         [cursor[1] * 120 + 120 - 20, cursor[0] * 120 + 120 - 20], 20)
        pygame.draw.line(window, GRAY, [cursor[1] * 120 + 120 - 20, cursor[0] * 120 + 20],
                         [cursor[1] * 120 + 20, cursor[0] * 120 + 120 - 20], 20)
        pygame.draw.line(window, SILVER, [cursor[1] * 120 + 22, cursor[0] * 120 + 22],
                         [cursor[1] * 120 + 120 - 22, cursor[0] * 120 + 120 - 22], 14)
        pygame.draw.line(window, SILVER, [cursor[1] * 120 + 120 - 22, cursor[0] * 120 + 22],
                         [cursor[1] * 120 + 22, cursor[0] * 120 + 120 - 22], 14)
    pygame.display.update()

# Quit
print("Winner is player : ")
pygame.quit()
quit()
