import pygame

class slider:

    global position
    _indicatorPosition = [] 
    _percentage = 0

    def __init__(self, colors, properties):
        self.position = [0, 0]
        self.backColor = colors[0]
        self.indiColor = colors[1]
        self.width = properties[0]
        self.height = properties[1]

    def _setupRect(self):
        rect = pygame.Rect((self.position[0], self.position[1]), (self.width, self.height))
        return rect

    def _setupIndicator(self):
        if (not self._indicatorPosition) or self._indicatorPosition is self.position:
            self._indicatorPosition = [self.position[0], self.position[1] + (self.height / 2)]
        else: pass
        radius = self.height * 1.5
        return radius

    def _getClick(self):
        clicked = False
        mousePosition = []
        positionsX = [self._indicatorPosition[0] - (self.height * 1.5), (self._indicatorPosition[0] - (self.height * 1.5)) + ((self.height * 1.5) *2)]
        positionsY = [self._indicatorPosition[1] - (self.height * 1.5), (self._indicatorPosition[1] - (self.height * 1.5)) + ((self.height * 1.5) *2)]
        if pygame.mouse.get_pressed()[0]:
            mousePosition = pygame.mouse.get_pos()
            if (mousePosition[0] >= positionsX[0]) and (mousePosition[0] <= positionsX[1]):
                if (mousePosition[1] >= positionsY[0]) and (mousePosition[1] <= positionsY[1]):
                    clicked = True
        return clicked

    def _slide(self):
        isSliding = True
        mousePosX = None
        while isSliding:
            for event in pygame.event.get():
                if pygame.mouse.get_pos()[0] >= (self.position[0] + self.width):
                    mousePosX = self.position[0] + self.width
                    isSliding = False
                elif pygame.mouse.get_pos()[0] < self.position[0]:
                    mousePosX = self.position[0]
                    isSliding = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    mousePosX = pygame.mouse.get_pos()[0]
                    isSliding = False
        return mousePosX

    def _calcPercentage(self):
        value = (self.position[0] + self.width) - self._indicatorPosition[0]
        percent = (value / self.width) * 100
        self._percentage = abs(100-percent)

    def _calcX(self):
        x = (self.width * self._percentage) / 100
        self._indicatorPosition[0] = x + self.position[0]

    def getPercentage(self):
        return round(self._percentage)

    def setPercentage(self, newPercentage):
        if (not self._indicatorPosition):
            self._indicatorPosition = [self.position[0], self.position[1] + (self.height / 2)]
        self._percentage += newPercentage
        self._calcX()

    def draw(self, win):
        radius = self._setupIndicator()
        rect = pygame.draw.rect(win, self.backColor, self._setupRect())
        circle = pygame.draw.circle(win, self.indiColor, self._indicatorPosition, radius)

    def update(self):
        while self._getClick():
            self._indicatorPosition[0] = self._slide()
            self._calcPercentage()
     
