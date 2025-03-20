import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

white = (255, 255, 255)
rectangle_color = (0, 128, 255)

rectangle = pygame.Rect(270, 215, 100, 50)

font = pygame.font.Font(None, 36)
text = font.render("Hello World!", True, (0, 0, 0))
text_rect = text.get_rect(center=(320, 180))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
    screen.fill(white)
    pygame.draw.rect(screen, rectangle_color, rectangle)
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()