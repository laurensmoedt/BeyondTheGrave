import pygame

class button:

    global text
    global position
    
    def __init__(self, colors, properties):
        self.backColor = colors[0]
        self.textColor = colors[1]
        self.width = properties[0]
        self.height = properties[1]

    def setupRect(self):
        rect = pygame.Rect((self.position[0], self.position[1]), (self.width, self.height))
        return rect

    def setupText(self):
        font = pygame.font.Font('Extensions/assets/fonts/KulimPark-Regular.ttf', 18)
        textToRender = font.render(str(self.text), True, self.textColor)
        textRect = textToRender.get_rect()
        textRect.center = (self.position[0] + (self.width / 2), self.position[1] + (self.height / 2))
        return [textToRender, textRect]

    def getClick(self):
        clicked = False
        mousePosition = []
        positionsX = [self.position[0], self.position[0] + self.width]
        positionsY = [self.position[1], self.position[1] + self.height]
        if pygame.mouse.get_pressed()[0]:
            mousePosition = pygame.mouse.get_pos()
            if (mousePosition[0] >= positionsX[0]) and (mousePosition[0] <= positionsX[1]):
                if (mousePosition[1] >= positionsY[0]) and (mousePosition[1] <= positionsY[1]):
                    clicked = True
        return clicked

    def draw(self, win):
         rect = pygame.draw.rect(win, self.backColor, self.setupRect())
         [text, textRect] = self.setupText()
         text = win.blit(text, textRect)
        
