from app.components.pixel import Pixel
from app.renderers.color import Color
from app.renderers.terminal_renderer import TerminalRenderer
from app.renderers.color_terminal_renderer import ColorTerminalRenderer

if __name__ == "__main__":
    terminal_x_scale = 3
    renderer = TerminalRenderer(terminal_x_scale=terminal_x_scale)
    color_renderer = ColorTerminalRenderer(terminal_x_scale=terminal_x_scale)
    print("\033[2J", end="")

    coordinates = [
        (6, 0),
        (7, 0),
        (8, 0),
        (9, 0),
        (10, 0),
        (11, 0),
        (5, 1),
        (6, 1),
        (11, 1),
        (12, 1),
        (4, 2),
        (5, 2),
        (12, 2),
        (13, 2),
        (3, 3),
        (4, 3),
        (13, 3),
        (14, 3),
        (3, 4),
        (5, 4),
        (12, 4),
        (14, 4),
        (3, 5),
        (4, 5),
        (13, 5),
        (14, 5),
        (2, 6),
        (3, 6),
        (6, 6),
        (11, 6),
        (14, 6),
        (15, 6),
        (0, 7),
        (1, 7),
        (2, 7),
        (3, 7),
        (5, 7),
        (10, 7),
        (11, 7),
        (12, 7),
        (14, 7),
        (15, 7),
        (16, 7),
        (17, 7),
        (0, 8),
        (3, 8),
        (4, 8),
        (9, 8),
        (10, 8),
        (12, 8),
        (14, 8),
        (17, 8),
        (1, 9),
        (2, 9),
        (3, 9),
        (4, 9),
        (7, 9),
        (8, 9),
        (9, 9),
        (12, 9),
        (14, 9),
        (15, 9),
        (16, 9),
        (2, 10),
        (4, 10),
        (5, 10),
        (6, 10),
        (7, 10),
        (8, 10),
        (10, 10),
        (11, 10),
        (12, 10),
        (13, 10),
        (15, 10),
        (2, 11),
        (4, 11),
        (6, 11),
        (7, 11),
        (10, 11),
        (11, 11),
        (13, 11),
        (15, 11),
        (2, 12),
        (3, 12),
        (4, 12),
        (6, 12),
        (11, 12),
        (13, 12),
        (14, 12),
        (15, 12),
        (3, 13),
        (4, 13),
        (5, 13),
        (12, 13),
        (13, 13),
        (14, 13),
        (4, 14),
        (5, 14),
        (6, 14),
        (7, 14),
        (8, 14),
        (9, 14),
        (10, 14),
        (11, 14),
        (12, 14),
        (13, 14),
        (3, 15),
        (5, 15),
        (12, 15),
        (14, 15),
        (2, 16),
        (5, 16),
        (12, 16),
        (15, 16),
        (1, 17),
        (4, 17),
        (5, 17),
        (12, 17),
        (13, 17),
        (16, 17),
        (1, 18),
        (2, 18),
        (4, 18),
        (6, 18),
        (7, 18),
        (10, 18),
        (11, 18),
        (13, 18),
        (15, 18),
        (16, 18),
        (2, 19),
        (3, 19),
        (4, 19),
        (7, 19),
        (10, 19),
        (13, 19),
        (14, 19),
        (15, 19),
        (4, 20),
        (5, 20),
        (6, 20),
        (11, 20),
        (12, 20),
        (13, 20),
        (3, 21),
        (7, 21),
        (8, 21),
        (9, 21),
        (10, 21),
        (14, 21),
        (3, 22),
        (6, 22),
        (7, 22),
        (10, 22),
        (11, 22),
        (14, 22),
        (4, 23),
        (5, 23),
        (6, 23),
        (11, 23),
        (12, 23),
        (13, 23),
    ]
    all_coordinates = [
        (0, 0, "White"),
        (1, 0, "White"),
        (2, 0, "White"),
        (3, 0, "White"),
        (4, 0, "White"),
        (5, 0, "White"),
        (6, 0, "Black"),
        (7, 0, "Black"),
        (8, 0, "Black"),
        (9, 0, "Black"),
        (10, 0, "Black"),
        (11, 0, "Black"),
        (12, 0, "White"),
        (13, 0, "White"),
        (14, 0, "White"),
        (15, 0, "White"),
        (16, 0, "White"),
        (17, 0, "White"),
        (0, 1, "White"),
        (1, 1, "White"),
        (2, 1, "White"),
        (3, 1, "White"),
        (4, 1, "White"),
        (5, 1, "Black"),
        (6, 1, "Black"),
        (7, 1, "Green"),
        (8, 1, "Green"),
        (9, 1, "Green"),
        (10, 1, "Green"),
        (11, 1, "Black"),
        (12, 1, "Black"),
        (13, 1, "White"),
        (14, 1, "White"),
        (15, 1, "White"),
        (16, 1, "White"),
        (17, 1, "White"),
        (0, 2, "White"),
        (1, 2, "White"),
        (2, 2, "White"),
        (3, 2, "White"),
        (4, 2, "Black"),
        (5, 2, "Black"),
        (6, 2, "Green"),
        (7, 2, "Green"),
        (8, 2, "Green"),
        (9, 2, "Green"),
        (10, 2, "Green"),
        (11, 2, "Green"),
        (12, 2, "Black"),
        (13, 2, "Black"),
        (14, 2, "White"),
        (15, 2, "White"),
        (16, 2, "White"),
        (17, 2, "White"),
        (0, 3, "White"),
        (1, 3, "White"),
        (2, 3, "White"),
        (3, 3, "Black"),
        (4, 3, "Black"),
        (5, 3, "Green"),
        (6, 3, "Green"),
        (7, 3, "Green"),
        (8, 3, "Green"),
        (9, 3, "Green"),
        (10, 3, "Green"),
        (11, 3, "Green"),
        (12, 3, "Green"),
        (13, 3, "Black"),
        (14, 3, "Black"),
        (15, 3, "White"),
        (16, 3, "White"),
        (17, 3, "White"),
        (0, 4, "White"),
        (1, 4, "White"),
        (2, 4, "White"),
        (3, 4, "Black"),
        (4, 4, "Green"),
        (5, 4, "Black"),
        (6, 4, "Yellow"),
        (7, 4, "Yellow"),
        (8, 4, "Yellow"),
        (9, 4, "Yellow"),
        (10, 4, "Yellow"),
        (11, 4, "Yellow"),
        (12, 4, "Black"),
        (13, 4, "Green"),
        (14, 4, "Black"),
        (15, 4, "White"),
        (16, 4, "White"),
        (17, 4, "White"),
        (0, 5, "White"),
        (1, 5, "White"),
        (2, 5, "White"),
        (3, 5, "Black"),
        (4, 5, "Black"),
        (5, 5, "Yellow"),
        (6, 5, "Yellow"),
        (7, 5, "Yellow"),
        (8, 5, "Yellow"),
        (9, 5, "Yellow"),
        (10, 5, "Yellow"),
        (11, 5, "Yellow"),
        (12, 5, "Yellow"),
        (13, 5, "Black"),
        (14, 5, "Black"),
        (15, 5, "White"),
        (16, 5, "White"),
        (17, 5, "White"),
        (0, 6, "White"),
        (1, 6, "White"),
        (2, 6, "Black"),
        (3, 6, "Black"),
        (4, 6, "Yellow"),
        (5, 6, "Yellow"),
        (6, 6, "Black"),
        (7, 6, "Yellow"),
        (8, 6, "Yellow"),
        (9, 6, "Yellow"),
        (10, 6, "Yellow"),
        (11, 6, "Black"),
        (12, 6, "Yellow"),
        (13, 6, "Yellow"),
        (14, 6, "Black"),
        (15, 6, "Black"),
        (16, 6, "White"),
        (17, 6, "White"),
        (0, 7, "Black"),
        (1, 7, "Black"),
        (2, 7, "Black"),
        (3, 7, "Black"),
        (4, 7, "Yellow"),
        (5, 7, "Black"),
        (6, 7, "Yellow"),
        (7, 7, "Yellow"),
        (8, 7, "Yellow"),
        (9, 7, "Yellow"),
        (10, 7, "Black"),
        (11, 7, "Black"),
        (12, 7, "Black"),
        (13, 7, "Yellow"),
        (14, 7, "Black"),
        (15, 7, "Black"),
        (16, 7, "Black"),
        (17, 7, "Black"),
        (0, 8, "Black"),
        (1, 8, "Peach"),
        (2, 8, "Peach"),
        (3, 8, "Black"),
        (4, 8, "Black"),
        (5, 8, "Yellow"),
        (6, 8, "Yellow"),
        (7, 8, "Yellow"),
        (8, 8, "Yellow"),
        (9, 8, "Black"),
        (10, 8, "Black"),
        (11, 8, "Peach"),
        (12, 8, "Black"),
        (13, 8, "Yellow"),
        (14, 8, "Black"),
        (15, 8, "Peach"),
        (16, 8, "Peach"),
        (17, 8, "Black"),
        (0, 9, "White"),
        (1, 9, "Black"),
        (2, 9, "Black"),
        (3, 9, "Black"),
        (4, 9, "Black"),
        (5, 9, "Yellow"),
        (6, 9, "Yellow"),
        (7, 9, "Black"),
        (8, 9, "Black"),
        (9, 9, "Black"),
        (10, 9, "Peach"),
        (11, 9, "Peach"),
        (12, 9, "Black"),
        (13, 9, "Yellow"),
        (14, 9, "Black"),
        (15, 9, "Black"),
        (16, 9, "Black"),
        (17, 9, "White"),
        (0, 10, "White"),
        (1, 10, "White"),
        (2, 10, "Black"),
        (3, 10, "Yellow"),
        (4, 10, "Black"),
        (5, 10, "Black"),
        (6, 10, "Black"),
        (7, 10, "Black"),
        (8, 10, "Black"),
        (9, 10, "Peach"),
        (10, 10, "Black"),
        (11, 10, "Black"),
        (12, 10, "Black"),
        (13, 10, "Black"),
        (14, 10, "Yellow"),
        (15, 10, "Black"),
        (16, 10, "White"),
        (17, 10, "White"),
        (0, 11, "White"),
        (1, 11, "White"),
        (2, 11, "Black"),
        (3, 11, "Yellow"),
        (4, 11, "Black"),
        (5, 11, "White"),
        (6, 11, "Black"),
        (7, 11, "Black"),
        (8, 11, "Peach"),
        (9, 11, "Peach"),
        (10, 11, "Black"),
        (11, 11, "Black"),
        (12, 11, "White"),
        (13, 11, "Black"),
        (14, 11, "Yellow"),
        (15, 11, "Black"),
        (16, 11, "White"),
        (17, 11, "White"),
        (0, 12, "White"),
        (1, 12, "White"),
        (2, 12, "Black"),
        (3, 12, "Black"),
        (4, 12, "Black"),
        (5, 12, "Peach"),
        (6, 12, "Black"),
        (7, 12, "White"),
        (8, 12, "Peach"),
        (9, 12, "Peach"),
        (10, 12, "White"),
        (11, 12, "Black"),
        (12, 12, "Peach"),
        (13, 12, "Black"),
        (14, 12, "Black"),
        (15, 12, "Black"),
        (16, 12, "White"),
        (17, 12, "White"),
        (0, 13, "White"),
        (1, 13, "White"),
        (2, 13, "White"),
        (3, 13, "Black"),
        (4, 13, "Black"),
        (5, 13, "Black"),
        (6, 13, "Peach"),
        (7, 13, "Peach"),
        (8, 13, "Peach"),
        (9, 13, "Peach"),
        (10, 13, "Peach"),
        (11, 13, "Peach"),
        (12, 13, "Black"),
        (13, 13, "Black"),
        (14, 13, "Black"),
        (15, 13, "White"),
        (16, 13, "White"),
        (17, 13, "White"),
        (0, 14, "White"),
        (1, 14, "White"),
        (2, 14, "White"),
        (3, 14, "White"),
        (4, 14, "Black"),
        (5, 14, "Black"),
        (6, 14, "Black"),
        (7, 14, "Black"),
        (8, 14, "Black"),
        (9, 14, "Black"),
        (10, 14, "Black"),
        (11, 14, "Black"),
        (12, 14, "Black"),
        (13, 14, "Black"),
        (14, 14, "White"),
        (15, 14, "White"),
        (16, 14, "White"),
        (17, 14, "White"),
        (0, 15, "White"),
        (1, 15, "White"),
        (2, 15, "White"),
        (3, 15, "Black"),
        (4, 15, "Lime"),
        (5, 15, "Black"),
        (6, 15, "Green"),
        (7, 15, "Green"),
        (8, 15, "Green"),
        (9, 15, "Green"),
        (10, 15, "Green"),
        (11, 15, "Green"),
        (12, 15, "Black"),
        (13, 15, "Lime"),
        (14, 15, "Black"),
        (15, 15, "White"),
        (16, 15, "White"),
        (17, 15, "White"),
        (0, 16, "White"),
        (1, 16, "White"),
        (2, 16, "Black"),
        (3, 16, "Lime"),
        (4, 16, "Lime"),
        (5, 16, "Black"),
        (6, 16, "Green"),
        (7, 16, "Green"),
        (8, 16, "Green"),
        (9, 16, "Green"),
        (10, 16, "Green"),
        (11, 16, "Green"),
        (12, 16, "Black"),
        (13, 16, "Lime"),
        (14, 16, "Lime"),
        (15, 16, "Black"),
        (16, 16, "White"),
        (17, 16, "White"),
        (0, 17, "White"),
        (1, 17, "Black"),
        (2, 17, "Peach"),
        (3, 17, "Peach"),
        (4, 17, "Black"),
        (5, 17, "Black"),
        (6, 17, "Green"),
        (7, 17, "Green"),
        (8, 17, "Green"),
        (9, 17, "Green"),
        (10, 17, "Green"),
        (11, 17, "Green"),
        (12, 17, "Black"),
        (13, 17, "Black"),
        (14, 17, "Peach"),
        (15, 17, "Peach"),
        (16, 17, "Black"),
        (17, 17, "White"),
        (0, 18, "White"),
        (1, 18, "Black"),
        (2, 18, "Black"),
        (3, 18, "Peach"),
        (4, 18, "Black"),
        (5, 18, "Green"),
        (6, 18, "Black"),
        (7, 18, "Black"),
        (8, 18, "Yellow"),
        (9, 18, "Yellow"),
        (10, 18, "Black"),
        (11, 18, "Black"),
        (12, 18, "Green"),
        (13, 18, "Black"),
        (14, 18, "Peach"),
        (15, 18, "Black"),
        (16, 18, "Black"),
        (17, 18, "White"),
        (0, 19, "White"),
        (1, 19, "White"),
        (2, 19, "Black"),
        (3, 19, "Black"),
        (4, 19, "Black"),
        (5, 19, "Green"),
        (6, 19, "Green"),
        (7, 19, "Black"),
        (8, 19, "Yellow"),
        (9, 19, "Yellow"),
        (10, 19, "Black"),
        (11, 19, "Green"),
        (12, 19, "Green"),
        (13, 19, "Black"),
        (14, 19, "Black"),
        (15, 19, "Black"),
        (16, 19, "White"),
        (17, 19, "White"),
        (0, 20, "White"),
        (1, 20, "White"),
        (2, 20, "White"),
        (3, 20, "White"),
        (4, 20, "Black"),
        (5, 20, "Black"),
        (6, 20, "Black"),
        (7, 20, "Green"),
        (8, 20, "Green"),
        (9, 20, "Green"),
        (10, 20, "Green"),
        (11, 20, "Black"),
        (12, 20, "Black"),
        (13, 20, "Black"),
        (14, 20, "White"),
        (15, 20, "White"),
        (16, 20, "White"),
        (17, 20, "White"),
        (0, 21, "White"),
        (1, 21, "White"),
        (2, 21, "White"),
        (3, 21, "Black"),
        (4, 21, "Brown"),
        (5, 21, "Brown"),
        (6, 21, "Brown"),
        (7, 21, "Black"),
        (8, 21, "Black"),
        (9, 21, "Black"),
        (10, 21, "Black"),
        (11, 21, "Brown"),
        (12, 21, "Brown"),
        (13, 21, "Brown"),
        (14, 21, "Black"),
        (15, 21, "White"),
        (16, 21, "White"),
        (17, 21, "White"),
        (0, 22, "White"),
        (1, 22, "White"),
        (2, 22, "White"),
        (3, 22, "Black"),
        (4, 22, "Brown"),
        (5, 22, "Brown"),
        (6, 22, "Black"),
        (7, 22, "Black"),
        (8, 22, "White"),
        (9, 22, "White"),
        (10, 22, "Black"),
        (11, 22, "Black"),
        (12, 22, "Brown"),
        (13, 22, "Brown"),
        (14, 22, "Black"),
        (15, 22, "White"),
        (16, 22, "White"),
        (17, 22, "White"),
        (0, 23, "White"),
        (1, 23, "White"),
        (2, 23, "White"),
        (3, 23, "White"),
        (4, 23, "Black"),
        (5, 23, "Black"),
        (6, 23, "Black"),
        (7, 23, "White"),
        (8, 23, "White"),
        (9, 23, "White"),
        (10, 23, "White"),
        (11, 23, "Black"),
        (12, 23, "Black"),
        (13, 23, "Black"),
        (14, 23, "White"),
        (15, 23, "White"),
        (16, 23, "White"),
        (17, 23, "White"),
    ]
    for coordinate in coordinates:
        pixel = Pixel(coordinate[0], coordinate[1])
        pixel.render(renderer)
    for coordinate in coordinates:
        pixel = Pixel(coordinate[0], coordinate[1], color=Color.BRIGHT_YELLOW)
        pixel.render(color_renderer)
    for x, y, color in all_coordinates:
        pixel = Pixel(x, y, color=Color[color.upper()])
        pixel.render(color_renderer)
    print("\n\n")
    print("The Hero.".center(18 * terminal_x_scale))
    print("\n\n")
