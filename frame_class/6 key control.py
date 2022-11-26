import pygame


def key_control(snake_obj):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake_obj.direct == 'left' or snake_obj.direct == 'right':
                    snake_obj.direct == 'up'
            elif event.key == pygame.K_DOWN:
                if snake_obj.direct == 'left' or snake_obj.direct == 'right':
                    snake_obj.direct == 'down'
            elif event.key == pygame.K_LEFT:
                if snake_obj.direct == 'up' or snake_obj.direct == 'down':
                    snake_obj.direct == 'left'
            elif event.key == pygame.K_RIGHT:
                if snake_obj.direct == 'up' or snake_obj.direct == 'down':
                    snake_obj.direct == 'right'
            pass
