import pygame


pygame.init()

Vector_len = 0
x = 0
IsRunning = True
WIDTH = 1000
HEIGHT = 500
mainArray = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
i = 0
j = 0
IsRunning = True
# main loop
clock = pygame.time.Clock()
while IsRunning:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IsRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            IsRunning = False

    # clear screen
    screen.fill(0)

    # draw the entire range
    for k, n in enumerate(mainArray):
        pygame.draw.rect(screen, (255, 255, 255), (
            k * (WIDTH / len(mainArray)), HEIGHT - (mainArray[k]) * 50, (WIDTH / len(mainArray)), (n) * 50))

    # update the display
    pygame.display.flip()
    clock.tick(5)

    # bubblesort (1 step)
    print((j * (WIDTH / len(mainArray)), (mainArray[j]) * 50))
    try:
        if mainArray[j] > mainArray[j + 1]:
            x = mainArray[j]
            mainArray[j] = mainArray[j + 1]
            mainArray[j + 1] = x
    except(IndexError):
        pass

    # increment control variables
    if j < len(mainArray) - 1:
        j += 1
    elif i < len(mainArray) - 1:
        i += 1
        j = 0
