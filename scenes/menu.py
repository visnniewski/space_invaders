import pygame

class menu(object):
    def __init__(self, window, window_size):
        self.window = window
        self.window_size = window_size

        self.scene = "menu"
        self.clicked = False

        self.buttons = [button(self.window, [self.window_size[0] / 2 - 150, 100], (300, 60), "Start", (142, 68, 173)),
                        button(self.window, [self.window_size[0] / 2 - 150, 220], (300, 60), "Change controls", (142, 68, 173)),
                        button(self.window, [self.window_size[0] / 2 - 150, 400], (300, 60), "Exit", (142, 68, 173))]

    def update(self):
        m_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        for button in self.buttons:
            button.hover(m_pos)
            if self.clicked and button.text == "Start":
                self.scene = "game"

    def draw(self):
        for button in self.buttons:
            button.draw()

class button(object):
    def __init__(self, winodw, position, size, text, color):
        self.window = winodw
        self.position = position
        self.size = size
        self.text = text
        self.default_color = color
        self.color = self.default_color
        self.hover_color = (155, 89, 182)
        self.hovered = False

        self.font = pygame.font.SysFont('roboto', int(self.size[0] * 0.15))
        self.btn_text = self.font.render(self.text, True, (236, 240, 241))
        self.btn_text_rect = self.btn_text.get_rect()
        self.btn_text_rect.center = (self.size[0] // 2 + self.position[0], self.size[1] // 2 + self.position[1])

        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        
        self.shadow = pygame.Rect(self.rect.x + 4, self.rect.y + 3, self.rect.width, self.rect.height)

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.window, (127, 140, 141), self.shadow)
        pygame.draw.rect(self.window, self.color, self.rect)
        self.window.blit(self.btn_text, self.btn_text_rect)
    
    @property
    def get_x(self):
        return self.rect.x
    
    @property
    def get_y(self):
        return self.rect.y
    
    @property
    def get_width(self):
        return self.rect.width
    
    @property
    def get_height(self):
        return self.rect.height
    
    def hover(self, m_pos):
        if m_pos[0] >= self.get_x and m_pos[0] <= self.get_x + self.get_width and m_pos[1] >= self.get_y and m_pos[1] <= self.get_y + self.get_height:
            self.color = self.hover_color
            self.shadow.x = self.rect.x
            self.shadow.y = self.rect.y
            self.hovered = True
        else:
            if self.color == self.hover_color:
                self.color = self.default_color
                self.shadow.x = self.rect.x + 4
                self.shadow.y = self.rect.y + 3
                self.hovered = False