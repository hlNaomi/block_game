import pygame
import asyncio

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

BLUE = (0, 120, 255)
WHITE = (255, 255, 255)

x = 350
y = 250

speed = 5

async def main():

    global x
    global y

    running = True

    while running:

        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= speed

        if keys[pygame.K_RIGHT]:
            x += speed

        if keys[pygame.K_UP]:
            y -= speed

        if keys[pygame.K_DOWN]:
            y += speed

        screen.fill(BLUE)

        pygame.draw.rect(
            screen,
            WHITE,
            (x, y, 100, 100)
        )

        pygame.display.flip()

        await asyncio.sleep(0)

asyncio.run(main())