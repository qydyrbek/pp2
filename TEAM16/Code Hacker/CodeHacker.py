import pygame
import sys
import time
import imageio

def play_video(video_path):
    video = imageio.get_reader(video_path, 'ffmpeg')
    fps = video.get_meta_data()['fps']
    return video, fps

def main_menu(screen):
    menu_background = pygame.image.load('menu_background.jpeg')
    menu_background = pygame.transform.scale(menu_background, (800, 400))

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 204, 0)

    start_button = pygame.Rect(350, 250, 100, 50)
    start_font = pygame.font.Font('font1.ttf', 24)

    running = True
    while running:
        screen.blit(menu_background, (0, 0))
        pygame.draw.rect(screen, GREEN, start_button)
        start_text = start_font.render("START", True, BLACK)
        screen.blit(start_text, (start_button.x + 20, start_button.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    running = False

        pygame.display.flip()

def play_level(screen, video, fps):
    WIDTH, HEIGHT = 800, 400

    bg_sound = pygame.mixer.Sound('materials\ibg.mp3')
    bg_sound.play()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (204, 0, 0)
    GREEN = (0, 204, 0)

    FONT = pygame.font.Font('font1.ttf', 36)

    def display_text(text, x, y, color=GREEN, outline_color=BLACK, outline_thickness=2):
        text_surface = FONT.render(text, True, outline_color)
    
    # Render outline
        for dx in range(-outline_thickness, outline_thickness + 1):
            for dy in range(-outline_thickness, outline_thickness + 1):
                screen.blit(text_surface, (x + dx, y + dy))

    # Render main text
        text_surface = FONT.render(text, True, color)
        screen.blit(text_surface, (x, y))

    def input_box(x, y, w, h, color=GREEN):
        pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h), 1)
        return pygame.Rect(x, y, w, h)

    def game_over():
        display_text("Game Over", 300, 150, RED)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    clock = pygame.time.Clock()
    input_rect = input_box(100, 300, 600, 50)
    input_text = ""
    active = False
    level = 1
    score = 0
    levels = [
        ("prnt('Hello, world!')", "print('Hello, world!')"),
        ("/this is a comment", "#this is a comment"),
        ("for i in range(10)\n print(i)", "for i in range(10):\n    print(i)")
    ]

    frame_iterator = iter(video)

    while True:
        try:
            frame = next(frame_iterator)
        except StopIteration:
            frame_iterator = iter(video)
            frame = next(frame_iterator)

        frame_image = pygame.image.frombuffer(
            frame.tostring(), frame.shape[1::-1], 'RGB'
        )
        screen.blit(frame_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if input_text == levels[level-1][1]:
                            score += 1
                            level += 1
                            if level > len(levels):
                                level = 1
                        else:
                            game_over()
                        input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        if active:
            color = WHITE
        else:
            color = (127, 127, 127)
        input_rect = input_box(100, 300, 600, 50, color)

        display_text(f"Level {level}: Fix the following Python code:", 50, 100)
        display_text(levels[level-1][0], 175, 200)
        display_text(input_text, 110, 310)
        display_text(f"Score: {score}", 0, 0)

        pygame.display.flip
        pygame.display.flip()
        clock.tick(fps)



def main():
    pygame.init()
    pygame.mixer.init()

    size = (800, 400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Code Hacker")

    icon = pygame.image.load('icon.png').convert_alpha()
    pygame.display.set_icon(icon)

    video_path = "code.mp4"
    video, fps = play_video(video_path)

    main_menu(screen)
    play_level(screen, video, fps)

    pygame.quit()


if __name__ == "__main__":
    main()