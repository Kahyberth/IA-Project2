import pygame


board = [
    ['🟥', '⬛', '🟦', '⬛', '🟦', '⬛', '🟦', '⬛', '🟦', '⬛', '🟦', '⬛', '🟦', '⬛', '🟦'],
    ['🟥', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '🟦'],
    ['🟥', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '🟦'],
    ['🟥', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '🟦'],
    ['🟥', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '🟦'],
    ['🟥', '⬛', '🟥', '⬛', '🟥', '⬛', '🟥', '⬛', '🟥', '⬛', '🟥', '⬛', '🟥', '⬛', '🟦'],
]


# Constantes
WIDTH, HEIGHT = 800, 400
ROWS, COLS = 6, 15
SQUARE_SIZE = WIDTH // COLS

# Colores
WHITE = (255, 255, 255)
BORDER_COLOR = (0, 0, 0)  # Color del borde, en este caso es verde

IMAGE_MAP = {
    '🟥': pygame.image.load('Assets/Red.png'),
    '🟦': pygame.image.load('Assets/Blue.png'),
    '⬜': pygame.image.load('Assets/Empty.png'),
    '⬛': pygame.image.load('Assets/Bamboo.png')
}

# Cargar imagen de fondo
BACKGROUND_IMAGE = pygame.image.load('Assets/Grass.png')
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE,
                                          (SQUARE_SIZE, SQUARE_SIZE))  # Ajustar el tamaño de la imagen de fondo
# Ajustar el tamaño de la imagen de fondo
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SQUARE_SIZE // 2, SQUARE_SIZE // 2))
# Cargar imagen de la muralla
WALL_IMAGE = pygame.image.load('Assets/Wall.png')
WALL_IMAGE = pygame.transform.scale(WALL_IMAGE,
                                    (SQUARE_SIZE, SQUARE_SIZE * ROWS))  # Ajustar el tamaño de la imagen de la muralla

# Inicializar pygame y crear ventana
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Crear cuadrícula
grid = []
for i in range(ROWS):
    row = []
    for j in range(COLS):
        row.append('⬜')
    grid.append(row)

# Bucle principal
run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // SQUARE_SIZE
            row = pos[1] // SQUARE_SIZE
            print('Info: ', grid[row][col], row, col)

    # Dibujar cuadrícula
    WIN.fill(WHITE)
    PADDING = 5  # Espacio entre cuadros
    SQUARE_SIZE_WITH_PADDING = SQUARE_SIZE - PADDING

    for i in range(ROWS):
        for j in range(COLS):
            # Dibujar imagen de fondo
            for x in range(j * SQUARE_SIZE, (j + 1) * SQUARE_SIZE, BACKGROUND_IMAGE.get_width()):
                for y in range(i * SQUARE_SIZE, (i + 1) * SQUARE_SIZE, BACKGROUND_IMAGE.get_height()):
                    WIN.blit(BACKGROUND_IMAGE, (x, y))

            # Dibujar borde si el cuadro es '⬛'
            if board[i][j] == '⬛':
                pygame.draw.rect(WIN, BORDER_COLOR, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                                 1)  # Dibujar borde

            # Dibujar imagen de la muralla si el cuadro es '⬛'
            if board[i][j] == '⬛':
                WIN.blit(WALL_IMAGE, (j * SQUARE_SIZE, 0))

            # Dibujar imagen del cuadro si no es 'empty' ni '⬛'
            elif board[i][j] != '⬜':
                image = IMAGE_MAP[board[i][j]]
                image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))  # Ajustar el tamaño de la imagen
                WIN.blit(image, (j * SQUARE_SIZE, i * SQUARE_SIZE))

            # Dibujar borde si el cuadro no es '⬛'
            if board[i][j] != '⬛':
                pygame.draw.rect(WIN, BORDER_COLOR, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                                 1)  # Dibujar borde

    pygame.display.update()

pygame.quit()
