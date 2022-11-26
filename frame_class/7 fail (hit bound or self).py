def failure_check(snake_h, snake_b):
    fail = False
    # hit the bound
    if snake_h.head.col < 0 or snake_h.head.row < 0 or snake_h.head.col >= COL or snake_h.head.row >= ROW:
        fail = True
        pass
    # hit itself
    for i in snake_b.body:
        if snake_h.head.col == i.col and snake_h.head.row == i.row:
            fail = True
            break
        pass
    return fail