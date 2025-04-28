import pygame
import random
import time
from sorting import *

pygame.init()


class DrawInformation:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GREY = (128, 128, 128)
    BLUE = (0, 0, 255)
    BACKGROUND_COLOR = WHITE
    SIDE_PAD = 100
    TOP_PAD = 150
    GRADIENTS = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]
    FONT = pygame.font.SysFont('comicsans', 20)

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithms")
        self.set_list(lst)
        self.current_sorting_algorithm = None
        self.sorting_completed = False
        self.sorting_time = 0

    def set_list(self, lst):
        self.lst = lst
        self.max_value = max(lst)
        self.min_value = min(lst)
        self.visible_blocks = min(len(lst), self.width - self.SIDE_PAD)
        self.block_width = max(1, round((self.width - self.SIDE_PAD) / self.visible_blocks))
        self.block_height = max(1, round((self.height - self.TOP_PAD) / (self.max_value - self.min_value + 1)))
        total_width = self.block_width * self.visible_blocks
        self.start_x = (self.width - total_width) // 2

def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.FONT.render(f"Visualisering av {len(draw_info.lst)} tall mellom 0 og 10000", 1, draw_info.BLACK)
    draw_info.window.blit(title, (draw_info.width // 2 - title.get_width() // 2, 5))

    if draw_info.sorting_completed and draw_info.sorting_time > 0:
        time_text = draw_info.FONT.render(f"Tidsforbruk: {draw_info.sorting_time:.4f} sekunder", 1, draw_info.BLUE)
        draw_info.window.blit(time_text, (draw_info.width // 2 - time_text.get_width() // 2, 30))

    sorting_algorithms = {
        "0": ("Bubblesort", bubble_sort),
        "1": ("Selectionsort", selection_sort),
        "2": ("Insertionsort", insertion_sort),
        "3": ("Countingsort", counting_sort),
        "4": ("Mergesort", merge_sort),
        "5": ("Quicksort", quick_sort),
        "6": ("Heapsort", heap_sort)
    }

    menu_title = draw_info.FONT.render("Sorteringsalgoritmer:", 1, draw_info.BLACK)
    left_margin = 50
    draw_info.window.blit(menu_title, (left_margin, 35))

    for i, (key, (name, _)) in enumerate(sorting_algorithms.items()):
        algo_text = draw_info.FONT.render(f"'{key}' {name}", 1, draw_info.BLACK)
        draw_info.window.blit(algo_text, (left_margin, 65 + i * 25))

    controls_title = draw_info.FONT.render("Kontroller:", 1, draw_info.BLACK)
    right_margin = draw_info.width - 250
    draw_info.window.blit(controls_title, (right_margin, 35))

    controls = [
        "'SPACE' Start sortering",
        "'R' Reset",
        "'ESC' Avbryt sortering"
    ]

    for i, control in enumerate(controls):
        control_text = draw_info.FONT.render(control, 1, draw_info.BLACK)
        draw_info.window.blit(control_text, (right_margin, 65 + i * 25))

    algo_name = "Ingen algoritme valgt"

    if draw_info.current_sorting_algorithm:
        for key, (name, func) in sorting_algorithms.items():
            if func == draw_info.current_sorting_algorithm:
                algo_name = name
                break

    status_text = draw_info.FONT.render(f"Valgt algoritme: {algo_name}", 1, draw_info.BLACK)
    draw_info.window.blit(status_text, (draw_info.width // 2 - status_text.get_width() // 2, 120))
    draw_list(draw_info)

    return sorting_algorithms


def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst
    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD,draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    group_size = max(1, len(lst) // draw_info.visible_blocks)
    scaling_factor = 18

    for i in range(0, draw_info.visible_blocks):
        start_idx = i * group_size
        end_idx = min(start_idx + group_size, len(lst))
        group_values = lst[start_idx:end_idx]

        if not group_values:
            continue

        avg_value = sum(group_values) / len(group_values)
        x = draw_info.start_x + i * draw_info.block_width
        scaled_value = avg_value / scaling_factor
        height = max(1, (scaled_value - draw_info.min_value / scaling_factor) * draw_info.block_height)
        y = draw_info.height - height
        color = draw_info.GRADIENTS[i % 3]
        for idx in range(start_idx, end_idx):
            if idx in color_positions:
                color = color_positions[idx]
                break

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, height))
    pygame.display.update()

def generate_starting_list(size):
    lst = [random.randint(0, 10000) for _ in range(size)]
    return lst

def main():
    run = True
    clock = pygame.time.Clock()
    list_size = 1000
    original_lst = generate_starting_list(list_size)
    current_lst = original_lst.copy()
    draw_info = DrawInformation(1200, 800, current_lst)
    sorting = False

    while run:
        clock.tick(60)
        sorting_algorithms = draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    original_lst = generate_starting_list(list_size)
                    current_lst = original_lst.copy()
                    draw_info.set_list(current_lst)
                    sorting = False
                    draw_info.current_sorting_algorithm = None
                    draw_info.sorting_completed = False
                    draw_info.sorting_time = 0
                elif event.key == pygame.K_ESCAPE and sorting:
                    sorting = False
                elif event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    if draw_info.current_sorting_algorithm:
                        sort_function = draw_info.current_sorting_algorithm
                        start_time = time.time()
                        try:
                            sorting_generator = sort_function(draw_info.lst, draw_info)
                            if hasattr(sorting_generator, '__iter__'):
                                for _ in sorting_generator:
                                    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
                                    sorting_algorithms = draw(draw_info)

                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            run = False
                                            sorting = False
                                            break
                                        elif event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_ESCAPE:
                                                sorting = False
                                                break

                                    if not sorting:
                                        break

                                draw_info.window.fill(draw_info.BACKGROUND_COLOR)
                                sorting_algorithms = draw(draw_info)
                            else:
                                sorted_list = sorting_generator
                                if sorted_list is not None:
                                    draw_info.set_list(sorted_list)
                                draw_info.window.fill(draw_info.BACKGROUND_COLOR)
                                sorting_algorithms = draw(draw_info)
                        except Exception as e:
                            print(f"Feil under sortering: {e}")
                        end_time = time.time()
                        final_sorting_time = end_time - start_time
                        sorting = False
                        draw_info.current_sorting_algorithm = None
                        draw_info.sorting_time = final_sorting_time
                        draw_info.sorting_completed = True

                elif event.unicode in sorting_algorithms and not sorting:
                    draw_info.current_sorting_algorithm = sorting_algorithms[event.unicode][1]
                    current_lst = original_lst.copy()
                    draw_info.set_list(current_lst)
                    draw_info.sorting_completed = False

    pygame.quit()


if __name__ == "__main__":
    main()