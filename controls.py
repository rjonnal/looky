key_triples = [
    (pygame.K_ESCAPE,Modstate('any'),sys.exit),
    (pygame.K_LEFT,Modstate(''),tar.left),
    (pygame.K_RIGHT,Modstate(''),tar.right),
    (pygame.K_UP,Modstate(''),tar.up),
    (pygame.K_DOWN,Modstate(''),tar.down),
    (pygame.K_LEFT,Modstate('ctrl'),tar.c_left),
    (pygame.K_RIGHT,Modstate('ctrl'),tar.c_right),
    (pygame.K_UP,Modstate('ctrl'),tar.c_up),
    (pygame.K_DOWN,Modstate('ctrl'),tar.c_down),
    ]

