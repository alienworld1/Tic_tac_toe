import basegame
import pygame
import os

pygame.init()
WIDTH, HEIGHT = 500, 500
pygame.display.set_icon(pygame.image.load(os.path.join('Assets', 'icon.png')))
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-tac-toe')
FPS = 60
backColor = (51, 51, 51)
xColor = (204, 153, 255)
oColor = (0, 204, 204)

blankSquare = pygame.image.load(os.path.join('Assets', 'blanksquaretemplate.png'))
xSquare = pygame.image.load(os.path.join('Assets', 'xsquare.png'))
oSquare = pygame.image.load(os.path.join('Assets', 'osquare.png'))

openSans = pygame.font.Font(os.path.join('Assets', 'OpenSans-Medium.ttf'), 32)
textColor = (255, 248, 220)
newGameText = openSans.render('Press N to play a new game', True, textColor)
newGameRect = newGameText.get_rect()
newGameRect.center = (250, 450)

gameBoard = basegame.board()


def convert_board(tBoard):
    """Output the board displayed on the screen for a given board."""
    l = [[], [], []]
    for i in range(3):
        for j in range(3):
            if tBoard[i][j] == ' ':
                p = blankSquare
            elif tBoard[i][j] == 'X':
                p = xSquare
            else:
                p = oSquare
            l[i].append(p)
    return l


def draw_window(tBoard, moveText, moveRect):
    window.fill(backColor)
    for i in range(3):
        for j in range(3):
            window.blit(tBoard[i][j], ((j + 1) * 100, (i + 1) * 100))
    window.blit(newGameText, newGameRect)
    window.blit(moveText, moveRect)
    pygame.display.update()


def main():
    rectList = [[], [], []]
    for i in range(3):
        for j in range(3):
            rectList[i].append(pygame.Rect((i + 1) * 100, (j + 1) * 100, 100, 100))

    clock = pygame.time.Clock()
    run = True
    while run:

        i = 0
        clock.tick(FPS)
        curMove = gameBoard.CheckTurn()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(3):
                    for j in range(3):
                        if rectList[i][j].collidepoint(event.pos):
                            try:
                                if result == -1:
                                    gameBoard.set(curMove, j, i)
                            except:
                                pass

        curMove = gameBoard.CheckTurn()
        if curMove == 'X':
            color = xColor
        else:
            color = oColor
        moveText = openSans.render(curMove + ' to Move', True, color)
        moveRect = moveText.get_rect()
        moveRect.center = 250, 50

        # To check the win conditions
        result = gameBoard.CheckBoard()
        if result == 0:
            moveText = openSans.render('X wins!', True, xColor)
            moveRect = moveText.get_rect()
            moveRect.center = 250, 50
        elif result == 1:
            moveText = openSans.render('O wins!', True, oColor)
            moveRect = moveText.get_rect()
            moveRect.center = 250, 50
        elif result == 2:
            moveText = openSans.render('Draw', True, textColor)
            moveRect = moveText.get_rect()
            moveRect.center = 250, 50

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_n]:
            gameBoard.clearBoard()

        displayBoard = convert_board(gameBoard.board)
        draw_window(displayBoard, moveText, moveRect)

        i += 1

    pygame.quit()


if __name__ == "__main__":
    main()
