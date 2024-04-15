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
player = {"a": 1, "b": -1}
turn = 0
winner = None

# Cursor
cursor = [1, 1]
cursor_type = player["a"]
cursor_visible = True
cursor_time = 0
cursor_tick = 500

# Board
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

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
                if board[cursor[0]][cursor[1]] == 0:
                    board[cursor[0]][cursor[1]] = cursor_type
                    cursor_type = player["b"] if cursor_type == player["a"] else player["a"]
                    turn += 1
            if event.key == pygame.K_ESCAPE:
                running = False

    # Cursor
    if time - cursor_time >= cursor_tick:
        cursor_visible = False if cursor_visible else True
        cursor_time = time

    # Game over
    for i in range(3):
        if abs(sum(board[i])) == 3:
            winner = board[i][0]
            running = False
        elif abs(sum(board[j][i] for j in range(3))) == 3:
            winner = board[0][i]
            running = False
    if abs(sum(board[i][i] for i in range(3))) == 3 or abs(sum(board[i][2-i] for i in range(3))) == 3:
        winner = board[1][1]
        running = False
    if turn >= 9:
        running = False

    # Refresh game screen
    window.fill(BLACK)
    for i in range(3):
        for j in range(3):
            if (i + j) % 2 == 0:
                drawBoardCell(window, SADDLEBROWN, SIENNA, i, j)
            else:
                drawBoardCell(window, CHOCOLATE, SANDYBROWN, i, j)
            if board[i][j] == player["a"]:
                drawCircleMark(window, BLACK, CORAL, i, j)
            elif board[i][j] == player["b"]:
                drawXMark(window, BLACK, DODGERBLUE, i, j)
    if cursor_visible:
        if cursor_type == player["a"]:
            drawCircleMark(window, GRAY, SILVER, cursor[0], cursor[1])
        else:
            drawXMark(window, GRAY, SILVER, cursor[0], cursor[1])
    pygame.display.update()

# Quit
if winner:
    print("Player " + ("A[O]" if winner == player["a"] else "B[X]") + " is winner!", end="")
else:
    print("Draw!", end="")
pygame.quit()
quit()
