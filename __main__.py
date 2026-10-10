import pygame
from map_generator import *

def render_map():
    """
    This function will be deleted on the final version on NumWorks website, it is only used to debug the map generation algorithm.
    """
    pygame.init()

    SCALE = 3
    WIDTH = MAP_SIZE * SCALE
    HEIGHT = MAP_SIZE * SCALE

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Heightmap Debug")

    surface = pygame.Surface((MAP_SIZE, MAP_SIZE))

    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            h = get_map(x, y)
            surface.set_at((x, y), (h, h, h))

    scaled = pygame.transform.scale(
        surface, (WIDTH, HEIGHT)
    )

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_r:
                    generate_map()

                    for y in range(MAP_SIZE):
                        for x in range(MAP_SIZE):
                            h = get_map(x, y)
                            surface.set_at(
                                (x, y), (h, h, h)
                            )

                    scaled = pygame.transform.scale(
                        surface, (WIDTH, HEIGHT)
                    )

        screen.blit(scaled, (0, 0))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__=="__main__":
    generate_map()
    render_map()