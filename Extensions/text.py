import pygame

class text:

    global bColor
    global text
    global position
    _font = None

    def __init__(self, tColor, fontSize, properties):
        self.bColor = None
        self.tColor = tColor
        self.position = [0, 0]
        self.text = 'template'
        self.fontSize = fontSize
        self.width = properties[0]
        self.height = properties[1]

    def _setupText(self):
        self._font = pygame.font.Font('Extensions/assets/fonts/KulimPark-Regular.ttf', self.fontSize)
        textToRender = self._font.render(str(self.text), True, self.tColor)
        textRect = textToRender.get_rect()
        textRect.center = (self.position[0] + (self.width / 2), self.position[1] + (self.height / 2))
        return [textToRender, textRect]

    def _setBackground(self, win, render):
        tmpSurface = pygame.Surface((self.width, self.height))
        tmpSurface.fill(self.bColor)
        tmpSurface.blit(render, (self.position[0], self.position[1]))
        win.blit(tmpSurface, (self.position[0], self.position[1]))

    def setFont(self, path):
        self._font = pygame.font.Font(path, self.fontSize)

    def draw(self, win):
        [text, textRect] = self._setupText()
        if not self.bColor is None: self._setBackground(win, text)
        text = win.blit(text, textRect)

