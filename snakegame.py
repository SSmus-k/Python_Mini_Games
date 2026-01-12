import pygame
import random
import sys

class SnakeGame:
    scale = 20
    width = 50
    height = 30

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.width * self.scale, self.height * self.scale)
        )
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25)
        self.reset()

    def reset(self):
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = (0, -1)
        self.spawn_food()
        self.score = 0
        self.game_over = False

    def spawn_food(self):
        while True:
            food = (
                random.randint(0, self.width - 1),
                random.randint(0, self.height - 1),
            )
            if food not in self.snake:
                self.food = food
                return

    def change_direction(self, new_dir):
        opposite = {
            (0, 1): (0, -1),
            (0, -1): (0, 1),
            (1, 0): (-1, 0),
            (-1, 0): (1, 0),
        }
        if new_dir != opposite.get(self.direction):
            self.direction = new_dir

    def update(self):
        if self.game_over:
            return

        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        if (
            new_head in self.snake
            or new_head[0] < 0
            or new_head[0] >= self.width
            or new_head[1] < 0
            or new_head[1] >= self.height
        ):
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.spawn_food()
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill((0, 0, 0))

        for x, y in self.snake:
            pygame.draw.rect(
                self.screen,
                (0, 255, 0),
                (x * self.scale, y * self.scale, self.scale, self.scale),
            )

        fx, fy = self.food
        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            (fx * self.scale, fy * self.scale, self.scale, self.scale),
        )

        score = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score, (10, 10))

        if self.game_over:
            text = self.font.render("Game Over! Press R", True, (255, 255, 255))
            self.screen.blit(
                text,
                (
                    self.screen.get_width() // 2 - text.get_width() // 2,
                    self.screen.get_height() // 2,
                ),
            )

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        self.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        self.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.change_direction((1, 0))
                    elif event.key == pygame.K_r and self.game_over:
                        self.reset()

            self.update()
            self.draw()
            self.clock.tick(10)
