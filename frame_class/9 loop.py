while True:
    key_control(snake_head)

    if snake_head.head.row == food_obj.pos.row and snake_head.head.col == food_obj.pos.col:
        snake_body.body_add()
        pass

        snake_body.move()
        snake_head.head_move()

        if failure_check(snake_head, snake_body):
            exit()
            pass

        draw.rect(scrn, white, (0, 0, weight, height))
        rect(snake_head.head, head_color, scrn)
        for i in snake_body.body:
            rect(i, body_color, scrn)
            pass
        rect(fruit_obj.pos, food_color, scrn)

        display.update()

        clock.tick(snake_speed)
        pass

    pass