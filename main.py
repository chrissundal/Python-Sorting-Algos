import pygame
import random
pygame.init()

class DrawInformation:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GREY = (128, 128, 128)
    BACKGROUND_COLOR = WHITE
    SIDE_PAD = 100
    TOP_PAD = 150
    GRADIENTS = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithms")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.max_value = max(lst)
        self.min_value = min(lst)
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_value - self.min_value))
        self.start_x = self.SIDE_PAD // 2

def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    pygame.display.update()

def draw_list(draw_info):
    lst = draw_info.lst

    for i, value in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (value - draw_info.min_value) * draw_info.block_height
def generate_starting_list(size):
    lst = [random.randint(0, size) for _ in range(size)]
    return lst

def main():
    run = True
    clock = pygame.time.Clock()

    draw_info = DrawInformation(800, 600, generate_starting_list(100))

    while run:
        clock.tick(60)
        draw(draw_info)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


    pygame.quit()

if __name__ == "__main__":
    main()