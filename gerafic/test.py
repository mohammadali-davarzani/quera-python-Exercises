import pygame
img = pygame.image.load('sq.png')
size = tuple(img.get_rect())
print(size)
pic_string = pygame.image.tostring(img, 'RGB')
print(size)
img2 = pygame.image.fromstring(pic_string, size, 'RGB')
print(size)
pygame.image.save(img2, 'out.png')
print(size)