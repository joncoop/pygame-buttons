import pygame

class Button:

    def __init__(self, label, left, top, width, height, bg_color, hover_color, text_color, font):
        self.rect = pygame.Rect(left, top, width, height)
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
        
        self.label = font.render(label, True, text_color)
        self.label_rect = self.label.get_rect()
        self.label_rect.center = self.rect.center
        
    def mouse_is_over(self):
        mx, my = pygame.mouse.get_pos()

        return (self.rect.left <= mx < self.rect.right and
                self.rect.top <= my < self.rect.bottom)
    
    def is_clicked(self):
        pressed = pygame.mouse.get_pressed()
        left_button_down = pressed[0]
        
        return self.mouse_is_over() and left_button_down
        
    def draw(self, surface):
        if self.mouse_is_over():
            color = self.hover_color
        else:
            color = self.bg_color
        
        pygame.draw.rect(surface, color, self.rect)
        surface.blit(self.label, self.label_rect)    
