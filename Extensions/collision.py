class collision:

    _hasCollision = None
    _squarePositionsStationary = []
    _squarePositionsMoving = []
    _circlePositionsStationary = []
    _circlePositionsMoving = []

    def __init__(self, actor, colType):
        if (colType is None) or (not colType in ('square', 'circle')):
            raise NameError('Given type not valid')
        self.actor = actor
        self.type = colType
        self.width = self.actor.width
        self.height = self.actor.height

    '''
    Functionality for turning the collision on & off.
    If the objType is moving, always call '_setPositionMoving' function in the update of the class.
    '''
    def setCollision(self, col, objType):
        if col is True:
            if objType is 'stationary':
                self._setPositionStationary()
            if objType is 'moving':
                self._setPositionMoving()
        self._hasCollision = col
        return self._hasCollision

    '''
    Calculate the start X & Y and end X & Y.
    This calculation needs the X & Y positions and the width and height from a actor.
    '''
    def _calculateSquarePositions(self):
        startX, startY = self.actor.getPosition()
        endX = self.actor.getPosition()[0] + self.width
        endY = self.actor.getPosition()[1] + self.height
        name = self.actor.name
        return [startX, startY, endX, endY, name]

    def _calculateCirclePositions(self):
        dx, dy = self.actor.getPosition()
        radius = (self.width / 2)
        return [dx, dy, radius]

    '''
    Adding start X & Y and end X & Y.
    Calculation is done by @calculatePositions.
    '''
    def _setPositionStationary(self):
        if self.type is 'square':
            self._squarePositionsStationary.append(self._calculateSquarePositions())
        elif self.type is 'circle':
            self._circlePositionsStationary.append(self._calculateCirclePositions())

    def _setPositionMoving(self):
        if self.type is 'square':
            self._squarePositionsMoving.append(self._calculateSquarePositions())
        elif self.type is 'circle':
            self._circlePositionsMoving.append(self._calculateCirclePositions())

    '''
    Returns the list with active collision
    '''
    def getActiveCols(self, colType):
        if colType is 'square':
            return self._squarePositionsMoving
        elif colType is 'circle':
            return self._circlePositions

    '''
    Returns if collided or not.
    Checks currents actor position to already registered collision objects positions.
    '''
    def _checkSquareCollision(self, name = None):
        collided = False
        [startX, startY] = self.actor.getPosition()
        [endX, endY] = self.actor.getPosition() + [self.width, self.height]

        if name != None: # Checks for individual collision
            for i in range(len(self._squarePositionsMoving)):
                if name == self._squarePositionsMoving[i][4]:
                    if (startX < self._squarePositionsMoving[i][2] and endX > self._squarePositionsMoving[i][0] and startY < self._squarePositionsMoving[i][3] and endY > self._squarePositionsMoving[i][1]):
                        collided = True
                        break
            return collided

        for i in range(len(self._squarePositionsStationary)): # Checks collision with stationary objects
            if (startX < self._squarePositionsStationary[i][2] and endX > self._squarePositionsStationary[i][0] and startY < self._squarePositionsStationary[i][3] and endY > self._squarePositionsStationary[i][1]):
                collided = True
                break
        for i in range(len(self._squarePositionsMoving)): # Checks collision for all moving objects
            if self.actor.name == self._squarePositionsMoving[i][4]:
                break
            elif (startX < self._squarePositionsMoving[i][2] and endX > self._squarePositionsMoving[i][0] and startY < self._squarePositionsMoving[i][3] and endY > self._squarePositionsMoving[i][1]):
                collided = True
                break

        if not collided: # Checks for rectangle collision onto circle collision
            for i in range(len(self._circlePositionsStationary)):
                mx = max(x, min(self._circlePositionsStationary[i][0], x + self.width))
                my = max(y, min(self._circlePositionsStationary[i][1], y + self.height))
                dx = self._circlePositionsStationary[i][0] - mx
                dy = self._circlePositionsStationary[i][1] = my
                if (dx * dx + dy * dy) < (self._circlePositionsStationary[i][2] * self._circlePositionsStationary[i][2]):
                    collided = True
                    break
        return collided

    def _checkCircleCollision(self):
        collided = False
        [x, y, r] = self._calculateCirclePositions()
        for i in range(len(self._circlePositionsStationary)):
            dx = x - self._circlePositionsStationary[i][0]
            dy = y - self._circlePositionsStationary[i][1]
            radius = r - self._circlePositionsStationary[i][2]
            if (dx * dx + dy * dy) < (radius * radius):
                collided = True
                break
        if not collided:
            for i in range(len(self._squarePositionsStationary)):
                width = (self._squarePositionsStationary[i][2] - self._squarePositionsStationary[i][0])
                height = (self._squarePositionsStationary[i][3] - self._squarePositionsStationary[i][1])
                mx = max(self._squarePositionsStationary[i][0], min(x, self._squarePositionsStationary[i][0] + width))
                my = max(self._squarePositionsStationary[i][1], min(y, self._squarePositionsStationary[i][1] + height))
                dx = x - mx
                dy = y - my
                if (dx * dx + dy * dy) < (r * r):
                    collided = True
                    break
        return collided

    def clearMovingObjects(self):
        self._squarePositionsMoving.clear()
        self._circlePositionsMoving.clear()

    def checkState(self, name = None):
        if self.type is 'square':
            if name == None:
                return self._checkSquareCollision()
            else:
                return self._checkSquareCollision(name)
        elif self.type is 'circle':
            return self._checkCircleCollision()
