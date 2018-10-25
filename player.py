import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,player_carX,player_carY, player):
        super().__init__()
        self.image = pygame.image.load(player +'.png')
        self.rect = self.image.get_rect()
        self.rect.x = player_carX
        self.rect.y = player_carY

    def update(self, player_carX, player_carY):
        self.rect.x = player_carX
        self.rect.y = player_carY
