import pygame



pygame.init()

winHeight = 700
winWidth = 1000


sample_surface = pygame.display.set_mode((winWidth, winHeight))
color = (0,255,0)
color2 = (255,0,0)

#drawing
#player 1
s1 = pygame.Rect(40,155,120,20)
s2 = pygame.Rect(165,22,10,120)
s5 = pygame.Rect(895,155,25,25)
s6 = pygame.Rect(850,155,120,20)
"""
s2 = pygame.Rect(85,155,25,25)
s3 = pygame.Rect(130,155,25,25)
abilities = []
pygame.draw.rect(sample_surface,color,s1)
pygame.draw.rect(sample_surface,color,s2)
pygame.draw.rect(sample_surface,color,s3)
"""
#player 2
"""
s4 = pygame.Rect(940,155,25,25)
s5 = pygame.Rect(895,155,25,25)
s6 = pygame.Rect(850,155,25,25)
abilities = []
pygame.draw.rect(sample_surface,color,s4)
pygame.draw.rect(sample_surface,color,s5)
pygame.draw.rect(sample_surface,color,s6)
"""
#imaging 

image1 = pygame.image.load('./game/images/tictac.jpg')
imgage2 = pygame.image.load('./game/images/cat.jpg')
imgage3 = pygame.image.load('./game/images/chad.jpg')

bg_image = pygame.transform.scale(image1,(winWidth, winHeight)).convert()
player_img1 = pygame.transform.scale(imgage2, (120, 120))
player_img2 = pygame.transform.scale(imgage3, (120,120))

x, y = 200, 200
speed = 5

#sample_surface.blit(image,(x,y)) 














running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
     running = False
 
  sample_surface.blit(bg_image, (0,0))  # background first
  sample_surface.blit(player_img1, (36,22))
  sample_surface.blit(player_img2, (850,22))


  pygame.draw.rect(sample_surface, color, s1)
  pygame.draw.rect(sample_surface, color2, s2)
  pygame.draw.rect(sample_surface, color, s5)
  pygame.draw.rect(sample_surface, color, s6)

  """
  pygame.draw.rect(sample_surface, color, s3)
  pygame.draw.rect(sample_surface, color, s4)
  pygame.draw.rect(sample_surface, color, s5)
  pygame.draw.rect(sample_surface, color, s6)
  """
  pygame.display.flip()


