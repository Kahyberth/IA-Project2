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

# Cargar imágenes
IMAGE_MAP = {
    '🟥': pygame.image.load('../Assets/Red.png'),
    '🟦': pygame.image.load('../Assets/Blue.png'),
    '⬜': pygame.image.load('../Assets/Empty.png'),
}

# Cargar imagen de fondo
BACKGROUND_IMAGE = pygame.image.load('../Assets/Grass.png')
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SQUARE_SIZE, SQUARE_SIZE))  # Ajustar el tamaño de la imagen de fondo
# Ajustar el tamaño de la imagen de fondo
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SQUARE_SIZE//2, SQUARE_SIZE//2))
# Cargar imagen de la muralla
WALL_IMAGE = pygame.image.load('../Assets/Wall.png')
WALL_IMAGE = pygame.transform.scale(WALL_IMAGE, (SQUARE_SIZE, SQUARE_SIZE * ROWS))  # Ajustar el tamaño de la imagen de la muralla

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

dragging = None  # Variable para rastrear qué ficha se está arrastrando


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
            if board[row][col] in ['🟥', '🟦']:  # Si el usuario hizo clic en una ficha
                dragging = (row, col)

        if event.type == pygame.MOUSEBUTTONUP:
            if dragging is not None:  # Si el usuario está arrastrando una ficha
                pos = pygame.mouse.get_pos()
                col = pos[0] // SQUARE_SIZE
                row = pos[1] // SQUARE_SIZE
                # Solo mover la ficha si la celda de destino está vacía
                if board[row][col] == '⬜':
                    board[row][col] = board[dragging[0]][dragging[1]]  # Mover la ficha a la nueva posición
                    board[dragging[0]][dragging[1]] = '⬜'  # Marcar la celda original como vacía
                    print(board)  # Imprimir la representación de la matriz en la consola
            dragging = None  # El usuario ha soltado la ficha

    # Dibujar cuadrícula
    WIN.fill(WHITE)
    for i in range(ROWS):
        for j in range(COLS):
            # Dibujar imagen de fondo
            for x in range(j*SQUARE_SIZE, (j+1)*SQUARE_SIZE, BACKGROUND_IMAGE.get_width()):
                for y in range(i*SQUARE_SIZE, (i+1)*SQUARE_SIZE, BACKGROUND_IMAGE.get_height()):
                    WIN.blit(BACKGROUND_IMAGE, (x, y))

            # Dibujar borde si el cuadro es '⬛'
            if board[i][j] == '⬛':
                pygame.draw.rect(WIN, BORDER_COLOR, (j*SQUARE_SIZE, i*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)  # Dibujar borde

            # Dibujar imagen de la muralla si el cuadro es '⬛'
            if board[i][j] == '⬛':
                WIN.blit(WALL_IMAGE, (j*SQUARE_SIZE, 0))

            # Dibujar imagen del cuadro si no es 'empty' ni '⬛' y no se está arrastrando
            elif board[i][j] != '⬜' and (dragging is None or (i, j) != dragging):
                image = IMAGE_MAP[board[i][j]]
                image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))  # Ajustar el tamaño de la imagen
                WIN.blit(image, (j*SQUARE_SIZE, i*SQUARE_SIZE))

            # Dibujar borde si el cuadro no es '⬛'
            if board[i][j] != '⬛':
                pygame.draw.rect(WIN, BORDER_COLOR, (j*SQUARE_SIZE, i*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)  # Dibujar borde

    # Dibujar la ficha que se está arrastrando en la posición del ratón
    if dragging is not None:
        pos = pygame.mouse.get_pos()
        image = IMAGE_MAP[board[dragging[0]][dragging[1]]]
        image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))  # Ajustar el tamaño de la imagen
        WIN.blit(image, (pos[0] - SQUARE_SIZE // 2, pos[1] - SQUARE_SIZE // 2))  # Dibujar la imagen centrada en el ratón

    pygame.display.update()

pygame.quit()