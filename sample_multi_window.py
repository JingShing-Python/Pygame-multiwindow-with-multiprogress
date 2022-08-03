import pygame
import multiprocessing

pygame.init()
SIZE = WIDTH, HEIGHT = 400, 300
window_num = 3

def main():
    fps = 60
    surface = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    img = pygame.image.load('image.png')
    surface.blit(img, (0, 0))

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        pygame.display.update()
        pygame.display.set_caption(f"FPS: {clock.get_fps():.0f}")

if __name__ == '__main__':
    for _ in range(window_num):
        multiprocessing.Process(target=main).start()