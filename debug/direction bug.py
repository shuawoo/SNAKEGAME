for event in pygame.event.get():
    if event.type == pygame.QUIT:
        game_over = True
    if event.type == pygame.KEYDOWN:  # ！！left&right
        if event.key == pygame.K_LEFT:
            run_direction = 'left'
        elif event.key == pygame.K_RIGHT:
            run_direction = 'right'
        elif event.key == pygame.K_UP:
            run_direction = 'up'
        elif event.key == pygame.K_DOWN:
            run_direction = 'down'

if run == 'up' and not run_direction == 'down':
    run = run_direction
elif run == 'down' and not run_direction == 'up':
    run = run_direction
elif run == 'left' and not run_direction == 'right':
    run = run_direction
elif run == 'right' and not run_direction == 'left':
    run = run_direction

if run == 'up':
    head.y -= 20
elif run == 'down':
    head.y += 20
elif run == 'left':
    head.x -= 20
elif run == 'right':
    head.x += 20
