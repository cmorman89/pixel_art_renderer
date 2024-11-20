import random
import os
import sys
import time
from collections import deque
from app.components.pixel import Pixel
from app.components.layer import Layer
from app.data.pixel_matrix import PixelMatrix
from app.data.pixel_matrix_manager import PixelMatrixManager
from app.renderers.terminal.color_terminal_renderer import ColorTerminalRenderer
from app.renderers.utils.color import Color


class Star:
    def __init__(self, x, speed, color):
        self.x = x
        self.y = 0
        self.speed = speed
        self.color = color
        self.position_offset = 0.0

    def move(self):
        self.position_offset += self.speed
        if self.position_offset >= 1.0:
            self.y += int(self.position_offset)
            self.position_offset %= 1.0

    def get_position(self):
        return self.x, self.y

    def get_color(self):
        return self.color

    def get_tail_length(self):
        if self.speed < 1.0:
            return 0
        elif self.speed < 4.0:
            return 1
        elif self.speed < 7.0:
            return 2
        elif self.speed < 9.0:
            return 3
        else:
            return 4

    def is_off_screen(self, height):
        return self.y >= height


def generate_stars(num_columns, star_probability=0.005):
    stars = []
    for x in range(num_columns):
        if random.random() < star_probability:
            speed = random.uniform(0.25, 10)
            color = random.choices(
                [Color.WHITE, Color.PINK, Color.CYAN, Color.GRAY],
                weights=[0.5, 0.05, 0.05, 0.4],
                k=1,
            )[0]
            stars.append(Star(x, speed, color))
    return stars


def initialize_pixel_matrix(width, height, pixel_matrix_manager):
    pixel_matrix = PixelMatrix(pixel_matrix_manager)
    for y in range(height):
        for x in range(width):
            black_pixel = Pixel(x, y, color=Color.BLACK)
            pixel_matrix_manager.add_pixel(pixel_matrix, black_pixel)
    return pixel_matrix


def draw_frame(stars, pixel_matrix, pixel_matrix_manager, previous_positions):
    # Remove previous star positions by replacing them with black pixels
    for x, y in previous_positions:
        if 0 <= y < pixel_matrix.height and 0 <= x < pixel_matrix.width:
            black_pixel = Pixel(x, y, color=Color.BLACK)
            pixel_matrix_manager.add_pixel(pixel_matrix, black_pixel)

    # Update the stars' positions in the matrix
    new_positions = []
    for star in stars:
        x, y = star.get_position()
        tail_length = star.get_tail_length()
        for i in range(tail_length + 1):
            if y - i >= 0:
                star_pixel = Pixel(x, y - i, color=star.get_color())
                pixel_matrix_manager.add_pixel(pixel_matrix, star_pixel)
                new_positions.append((x, y - i))

    return new_positions


def calculate_fps(frame_times, current_time):
    frame_times.append(current_time)
    if len(frame_times) > 30:
        frame_times.popleft()

    frame_times_list = list(frame_times)
    if len(frame_times_list) > 1:
        instantaneous_fps = 1.0 / (frame_times_list[-1] - frame_times_list[-2])
        if len(frame_times_list) >= 5:
            time_diff_5 = frame_times_list[-1] - frame_times_list[-5]
            last_5_avg_fps = 4 / time_diff_5 / 2 if time_diff_5 > 0 else 0.0
        else:
            last_5_avg_fps = instantaneous_fps

        time_diff_30 = frame_times_list[-1] - frame_times_list[0]
        last_30_avg_fps = (
            (len(frame_times_list) - 1) / time_diff_30 / 2 if time_diff_30 > 0 else 0.0
        )
    else:
        instantaneous_fps = 0.0
        last_5_avg_fps = 0.0
        last_30_avg_fps = 0.0

    return instantaneous_fps, last_5_avg_fps, last_30_avg_fps


def calculate_fps_over_time(frame_times, current_time, time_window):
    frame_times = [t for t in frame_times if current_time - t <= time_window]
    if len(frame_times) > 1:
        valid_intervals = [
            (frame_times[i] - frame_times[i - 1])
            for i in range(1, len(frame_times))
            if (frame_times[i] - frame_times[i - 1])
            > 0.001  # Filter out very small intervals
        ]
        if valid_intervals:
            avg_fps = len(valid_intervals) / sum(valid_intervals)
            min_fps = min(1.0 / interval for interval in valid_intervals)
            max_fps = max(1.0 / interval for interval in valid_intervals)
            return avg_fps, min_fps, max_fps
    return 0.0, 0.0, 0.0


def main():
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines - 10
    pixel_matrix_manager = PixelMatrixManager()
    terminal_renderer = ColorTerminalRenderer(terminal_x_scale=1)

    stars = []
    frame_times = deque()
    pixel_matrix = initialize_pixel_matrix(width, height, pixel_matrix_manager)
    previous_positions = []
    fps_target = 30
    target_frame_time = 1.0 / fps_target
    infinite = True

    try:
        while infinite:
            start_time = time.time()

            new_stars = generate_stars(width)
            stars.extend(new_stars)

            for star in stars:
                star.move()

            stars = [star for star in stars if not star.is_off_screen(height)]

            previous_positions = draw_frame(
                stars, pixel_matrix, pixel_matrix_manager, previous_positions
            )
            layer = Layer(pixel_matrix=pixel_matrix)
            layer.render(terminal_renderer)

            # Metrics:
            terminal_renderer._cursor_locator((0, height + 1))
            terminal_renderer._set_ansi_color_code(Color.RESET)

            current_time = time.time()
            instantaneous_fps, last_5_avg_fps, last_30_avg_fps = calculate_fps(
                frame_times, current_time
            )

            avg_fps_1_sec, min_fps_1_sec, max_fps_1_sec = calculate_fps_over_time(
                list(frame_times), current_time, 1
            )
            avg_fps_5_sec, min_fps_5_sec, max_fps_5_sec = calculate_fps_over_time(
                list(frame_times), current_time, 5
            )
            avg_fps_30_sec, min_fps_30_sec, max_fps_30_sec = calculate_fps_over_time(
                list(frame_times), current_time, 30
            )
            print()
            sys.stdout.write(
                f"Terminal:			{width} x {height} characters ({fps_target} FPS target)           \n"
            )
            sys.stdout.write(f"Instantaneous FPS:		{instantaneous_fps:.2f}          \n")
            sys.stdout.write(
                f"Average FPS (5 frames):		{last_5_avg_fps:.2f}          \n"
            )
            sys.stdout.write(
                f"Average FPS (30 frames):	{last_30_avg_fps:.2f}          \n"
            )
            sys.stdout.write(
                f"Average FPS (1 sec):		Avg: {avg_fps_1_sec:.2f}	Min: {min_fps_1_sec:.2f}	Max: {max_fps_1_sec:.2f}          \n"
            )
            sys.stdout.write(
                f"Average FPS (5 sec):		Avg: {avg_fps_5_sec:.2f}	Min: {min_fps_5_sec:.2f}	Max: {max_fps_5_sec:.2f}          \n"
            )
            sys.stdout.write(
                f"Average FPS (30 sec):		Avg: {avg_fps_30_sec:.2f}	Min: {min_fps_30_sec:.2f}	Max: {max_fps_30_sec:.2f}          \n"
            )
            sys.stdout.flush()

            end_time = time.time()
            frame_duration = end_time - start_time
            frame_times.append(end_time)

            # fps_target +=0.1
            target_frame_time = 1.0 / fps_target
            sleep_duration = target_frame_time - frame_duration
            if sleep_duration > 0:
                time.sleep(sleep_duration)

    except KeyboardInterrupt:
        # Clear screen and print final metrics
        os.system("cls" if os.name == "nt" else "clear")
        print("Starfield animation terminated.")
        print(f"Terminal:			{width} x {height} characters")
        print(f"Instantaneous FPS:		{instantaneous_fps:.2f}")
        print(f"Average FPS (5 frames):		{last_5_avg_fps:.2f}")
        print(f"Average FPS (30 frames):	{last_30_avg_fps:.2f}")
        print(
            f"Average FPS (1 sec):		Avg: {avg_fps_1_sec:.2f}	Min: {min_fps_1_sec:.2f}	Max: {max_fps_1_sec:.2f}"
        )
        print(
            f"Average FPS (5 sec):		Avg: {avg_fps_5_sec:.2f}	Min: {min_fps_5_sec:.2f}	Max: {max_fps_5_sec:.2f}"
        )
        print(
            f"Average FPS (30 sec):		Avg: {avg_fps_30_sec:.2f}	Min: {min_fps_30_sec:.2f}	Max: {max_fps_30_sec:.2f}"
        )


if __name__ == "__main__":
    main()
