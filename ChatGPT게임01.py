import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
screen_width = 800
screen_height = 600
block_width = 60
block_height = 20
paddle_width = 100
paddle_height = 10
ball_radius = 10
block_rows = 5
block_cols = 10
block_spacing = 5
block_color = (0, 128, 255)
paddle_color = (255, 0, 0)
ball_color = (0, 255, 0)
background_color = (0, 0, 0)
font = pygame.font.Font(None, 36)

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block Breaker")

# Create the paddle
paddle = pygame.Rect((screen_width - paddle_width) // 2, screen_height - paddle_height - 20, paddle_width, paddle_height)

# Create the ball
ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_radius * 2, ball_radius * 2)
ball_speed = [random.choice([-5, 5]), -5]

# Create the blocks
blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(
            col * (block_width + block_spacing) + block_spacing,
            row * (block_height + block_spacing) + block_spacing,
            block_width, block_height
        )
        blocks.append(block)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        paddle.move_ip(5, 0)

    # Move the ball
    ball.move_ip(ball_speed[0], ball_speed[1])

    # Collision detection with walls
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # Collision detection with paddle
    if ball.colliderect(paddle) and ball_speed[1] > 0:
        ball_speed[1] = -ball_speed[1]

    # Collision detection with blocks
    for block in blocks:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed[1] = -ball_speed[1]
            break

    # Clear the screen
    screen.fill(background_color)

    # Draw the blocks
    for block in blocks:
        pygame.draw.rect(screen, block_color, block)

    # Draw the paddle
    pygame.draw.rect(screen, paddle_color, paddle)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball.center, ball_radius)

    # Update the display
    pygame.display.flip()

    # Delay to control frame rate
    pygame.time.delay(30)

# Clean up
pygame.quit()
