import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Add Sprites Example")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

sprite_size = 50
sprite1_pos = [100, 100]  
sprite2_pos = [300, 300]  
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        sprite1_pos[1] -= speed
    if keys[pygame.K_DOWN]:
        sprite1_pos[1] += speed
    if keys[pygame.K_LEFT]:
        sprite1_pos[0] -= speed
    if keys[pygame.K_RIGHT]:
        sprite1_pos[0] += speed

    sprite1_pos[0] = max(0, min(WIDTH - sprite_size, sprite1_pos[0]))
    sprite1_pos[1] = max(0, min(HEIGHT - sprite_size, sprite1_pos[1]))

    screen.fill(WHITE)  
    pygame.draw.rect(screen, RED, (*sprite1_pos, sprite_size, sprite_size))
    pygame.draw.rect(screen, BLUE, (*sprite2_pos, sprite_size, sprite_size))

    pygame.display.flip()

pygame.quit()