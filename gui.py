import pygame
import sys
import random
import subprocess
from pygame import mixer 



pygame.init()



SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
FPS = 60

mixer.music.load("background-music-upbeat-2-374859.mp3")  
mixer.music.play(-1) 


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Quiz Quest")
clock = pygame.time.Clock()



DARK_BLUE = (20, 15, 60)
PURPLE_BG = (35, 20, 80)
YELLOW = (255, 230, 80)
ORANGE = (255, 160, 50)
PINK = (255, 80, 150)
CYAN = (100, 220, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()



background_image = pygame.image.load("pixelated earth that show people making pyramids playing cricket writing novels and performing in theater.jpg").convert()
background_image = pygame.transform.smoothscale(
    background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)
)  



bob_offset = 0
bob_direction = 1
bob_speed = 0.5



game_state = "START_SCREEN"  


# Star class for animated background
class Star:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.size = random.randint(1, 3)
        self.brightness = random.randint(100, 255)
        self.twinkle_speed = random.uniform(0.5, 2.0)
        self.twinkle_direction = random.choice([-1, 1])

    def update(self):
        # Twinkle effect
        self.brightness += self.twinkle_speed * self.twinkle_direction
        if self.brightness > 255:
            self.brightness = 255
            self.twinkle_direction = -1
        elif self.brightness < 100:
            self.brightness = 100
            self.twinkle_direction = 1

    def draw(self, surface):
        color = (int(self.brightness), int(self.brightness), int(self.brightness * 0.9))
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), self.size)

        # Add a glow effect for larger stars
        if self.size >= 2:
            glow_alpha = int(self.brightness * 0.3)
            glow_surface = pygame.Surface((self.size * 4, self.size * 4), pygame.SRCALPHA)
            pygame.draw.circle(
                glow_surface,
                (*color, glow_alpha),
                (self.size * 2, self.size * 2),
                self.size * 2,
            )
            surface.blit(glow_surface, (int(self.x) - self.size * 2, int(self.y) - self.size * 2))


# Create stars
stars = [Star() for _ in range(150)]


def draw_gradient_rect(surface, rect, color1, color2):
    """Draw a vertical gradient rectangle"""
    for y in range(rect.height):
        ratio = y / rect.height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        pygame.draw.line(surface, (r, g, b), (rect.x, rect.y + y), (rect.x + rect.width, rect.y + y))


def draw_outlined_text(surface, text, font, x, y, text_color, outline_color, outline_width=3):
    """Draw text with outline centered at position"""
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x, y))

    outline_surface = font.render(text, True, outline_color)
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0:
                outline_rect = outline_surface.get_rect(center=(x + dx, y + dy))
                surface.blit(outline_surface, outline_rect)

    surface.blit(text_surface, text_rect)


def draw_start_button(surface, x, y, offset=0):
    """Draw the START button with glow effect centered at position"""
    button_width = 400
    button_height = 120

    button_x = x - button_width // 2
    button_y = y - button_height // 2 + offset

    glow_rect = pygame.Rect(button_x - 10, button_y - 10, button_width + 20, button_height + 20)
    pygame.draw.rect(surface, YELLOW, glow_rect, border_radius=60)

    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(surface, BLACK, button_rect, border_radius=50)

    pygame.draw.rect(surface, YELLOW, button_rect, width=5, border_radius=50)

    font_start = pygame.font.Font(None, 100)
    draw_outlined_text(surface, "START", font_start, x, y + offset, YELLOW, BLACK, 2)

    return button_rect


def draw_title(surface, center_x, top_y):
    """Draw the QUIZ QUEST title centered"""
    font_title = pygame.font.Font(None, 200)

    quiz_y = top_y + 100
    draw_outlined_text(surface, "QUIZ", font_title, center_x, quiz_y, ORANGE, CYAN, 5)
    draw_outlined_text(surface, "QUIZ", font_title, center_x, quiz_y, ORANGE, (50, 40, 100), 3)

    quest_y = top_y + 280
    draw_outlined_text(surface, "QUEST", font_title, center_x, quest_y, PINK, CYAN, 5)
    draw_outlined_text(surface, "QUEST", font_title, center_x, quest_y, PINK, (50, 40, 100), 3)


def draw_background_icons(surface):
    """Draw decorative background icons"""
    font_icons = pygame.font.Font(None, 40)

    icons = ["?", "!", "+", "×", "=", "π", "∑", "∆"]
    positions = [
        (100, 100), (200, 150), (1000, 120), (1100, 200),
        (80, 400), (150, 600), (1050, 450), (1100, 650),
        (300, 700), (900, 720), (500, 80), (700, 90)
    ]

    for i, pos in enumerate(positions):
        icon = icons[i % len(icons)]
        alpha = 40
        text = font_icons.render(icon, True, (100, 100, 150))
        text.set_alpha(alpha)
        surface.blit(text, pos)


def draw_start_screen(screen, bob_offset, stars):
    """Draw the start screen"""
    # Draw background image
    screen.blit(background_image, (0, 0))  # [web:1][web:3]

    # Optional: stars and icons on top of image
    for star in stars:
        star.draw(screen)

    draw_background_icons(screen)

    center_x = SCREEN_WIDTH // 2
    draw_title(screen, center_x, 50)

    button_y = SCREEN_HEIGHT - 200
    draw_start_button(screen, center_x, button_y, int(bob_offset))


def run_gui2():
    """Execute gui2.py file and close the start screen"""
    try:
        pygame.quit()
        subprocess.run([sys.executable, 'gui2.py'])
        print("gui2.py executed successfully")
        sys.exit()
    except FileNotFoundError:
        print("Error: gui2.py file not found in the current directory")
        sys.exit()
    except Exception as e:
        print(f"Error executing gui2.py: {e}")
        sys.exit()


# Game loop
running = True

while running:
    if game_state == "START_SCREEN":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                center_x = SCREEN_WIDTH // 2
                button_y = SCREEN_HEIGHT - 200
                button_rect = pygame.Rect(
                    center_x - 200,
                    button_y - 60 + int(bob_offset),
                    400,
                    120
                )
                if button_rect.collidepoint(mouse_pos):
                    run_gui2()

        # Update bobbing animation
        bob_offset += bob_speed * bob_direction
        if bob_offset > 15:
            bob_direction = -1
        elif bob_offset < -15:
            bob_direction = 1

        # Update stars
        for star in stars:
            star.update()

        # Draw start screen
        draw_start_screen(screen, bob_offset, stars)

        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()
sys.exit()
