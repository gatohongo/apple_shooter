import pygame, sys

def main():

    pygame.init()
    clock = pygame.time.Clock()

    logo = pygame.image.load("gatoironico.jpeg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("test")

    screen = pygame.display.set_mode((720,480))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
