import pygame


def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        displayUpdate()

            # Separately sort elements before
            # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
        if arr[j] <= pivot:
                # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)


def displayUpdate():
    for k, n in enumerate(mainArray):
        pygame.draw.rect(screen, (255, 255, 255), (
            k * (WIDTH / len(mainArray)), HEIGHT - (mainArray[k]) * 50, (WIDTH / len(mainArray)), (n) * 50))
        for i in range(len(mainArray)):
            print(str(mainArray[i]) + " ")
        print()
        # update the display
    pygame.display.flip()
    clock.tick(5)

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
    quickSort(mainArray, 0, len(mainArray)-1)


    # increment control variables
    if j < len(mainArray) - 1:
        j += 1
    elif i < len(mainArray) - 1:
        i += 1
        j = 0



