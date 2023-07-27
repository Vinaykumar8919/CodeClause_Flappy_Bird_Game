import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 500, 600
GRAVITY = 0.25
BIRD_JUMP = -4
PIPE_GAP = 150
PIPE_VELOCITY = -1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BIRD_COLOR = (255,255, 0)  # Red

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Font setup
pygame.font.init()
font = pygame.font.SysFont(None, 40)

# Function to display the start screen
def show_start_screen():
    screen.fill(BLACK)
    start_text = font.render("Press SPACE to Start", True, WHITE)
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0
        self.gravity = GRAVITY

    def jump(self):
        self.velocity = BIRD_JUMP

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self):
        pygame.draw.circle(screen, BIRD_COLOR, (self.x, int(self.y)), 15)

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(150, 400)
        self.passed = False

    def update(self):
        self.x += PIPE_VELOCITY

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, 0, 50, HEIGHT - self.height))
        pygame.draw.rect(screen, WHITE, (self.x, HEIGHT - self.height + PIPE_GAP, 50, self.height))

def check_collision(bird, pipes):
    if bird.y < 0 or bird.y > HEIGHT:
        return True

    for pipe in pipes:
        if pipe.x <= bird.x <= pipe.x + 50:
            if bird.y < HEIGHT - pipe.height or bird.y > HEIGHT - pipe.height + PIPE_GAP:
                return True

    return False
def display_score():
    text = font.render("Score: " + str(current_score), True, WHITE)
    screen.blit(text, (10, 10))
    text = font.render("High Score: " + str(high_score), True, WHITE)
    screen.blit(text, (10, 50))

def main():
    global current_score, high_score
    bird = Bird()
    pipes = [Pipe(WIDTH + i * 200) for i in range(3)]
    clock = pygame.time.Clock()

    while True:
        show_start_screen()  # Show the start screen before entering the game loop
        current_score = 0  # Reset the current score at the start of each game
        bird = Bird()  # Create a new bird at the start of each game
        pipes = [Pipe(WIDTH + i * 200) for i in range(3)]  # Reset pipes at the start of each game

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.jump()

            screen.fill(BLACK)

            bird.update()
            bird.draw()

            for pipe in pipes:
                pipe.update()
                pipe.draw()

            if pipes[0].x < -50:
                pipes.pop(0)
                pipes.append(Pipe(WIDTH))

            if check_collision(bird, pipes):
                con = ""
                if current_score > high_score:
                    high_score = current_score
                    con="your are the top"
                print("----------------------------------------")
                print("Game Over")
                print(con)
                print("Your Score is", current_score)
                break  # Break the game loop on collision to return to the start screen

            # Check for scoring
            if not pipes[0].passed and bird.x > pipes[0].x + 50:
                current_score += 1
                pipes[0].passed = True

            display_score()

            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    current_score = 0
    high_score = 0
    main()

