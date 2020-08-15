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


        key = mainArray[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while (j >= 0) and (mainArray[j] > key):
            mainArray[j + 1] = mainArray[j]
            j -= 1
            screen.fill(0)
        mainArray[j+1] = key
            # draw the entire range
        for k, n in enumerate(mainArray):
            pygame.draw.rect(screen, (255, 255, 255), (
                k * (WIDTH / len(mainArray)), HEIGHT - (mainArray[k]) * 50, (WIDTH / len(mainArray)), (n) * 50))
            pygame.display.flip()
            clock.tick(5)
        # Everything's been moved out of the way, insert
        # the key into the correct location
        if i < len(mainArray) - 1:
            i += 1
            j = 0
