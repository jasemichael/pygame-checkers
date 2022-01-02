import pygame

class Menu(pygame.Surface):
    
    def __init__(self, width, height):
        super().__init__((width, height))
        self.fill((240, 240, 240)) # background color
        # Checkers title
        font = pygame.font.Font(None, 42)
        text = font.render("Checkers", 1, (10, 10, 10))
        text_pos = text.get_rect()
        text_pos.centerx = self.get_rect().centerx
        text_pos.y = height * .05
        self.blit(text, text_pos)
        # Play AI option
        ai_button = self.create_button("Play with AI")
        ai_button_pos = ai_button.get_rect()
        ai_button_pos.centerx = self.get_rect().centerx
        ai_button_pos.y = height * .15
        self.blit(ai_button, ai_button_pos)
        self.ai_button_pos = ai_button_pos
        # Play as Host
        host_button = self.create_button("Play game as Host")
        host_button_pos = host_button.get_rect()
        host_button_pos.centerx = self.get_rect().centerx
        host_button_pos.y = height * .27
        self.blit(host_button, host_button_pos)
        self.host_button_pos = host_button_pos
        # Play as Joiner
        joiner_button = self.create_button("Play game as Joiner")
        joiner_button_pos = joiner_button.get_rect()
        joiner_button_pos.centerx = self.get_rect().centerx
        joiner_button_pos.y = height * .39
        self.blit(joiner_button, joiner_button_pos)
        self.joiner_button_pos = joiner_button_pos

    def create_button(self, text):
        button = pygame.Surface((self.get_width()*.5, self.get_height()*.1))
        button.fill((255, 255, 255))
        button_pos = button.get_rect()
        button_pos.centerx = self.get_rect().centerx
        font = pygame.font.Font(None, 24)
        text = font.render(text, 1, (10, 10, 10))
        text_pos = text.get_rect()
        text_pos.centerx = button.get_rect().centerx
        text_pos.centery = button.get_rect().centery
        button.blit(text, text_pos)
        return button

    def get_ai_button_pos(self):
        return self.ai_button_pos

    def get_host_button_pos(self):
        return self.host_button_pos

    def get_joiner_button_pos(self):
        return self.joiner_button_pos