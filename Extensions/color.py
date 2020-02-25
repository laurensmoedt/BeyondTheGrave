class color:
    
    '''
    Inialization for the premade colors.
    Values are being set in the constructor
    '''
    global black, white # Non colors
    global red, green, blue # Primary colors
    global yellow, violet, orange # secondary colors
    global pink, brown, cyan, gray # The rest of the colors
    
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)
        self.violet = (238, 130, 238)
        self.pink = (255, 105, 180)
        self.brown = (102, 51 , 0)
        self.orange = (255, 140, 0)
        self.cyan = (0, 255, 255)
        self.gray = (128, 128, 128)

    '''
    Function for using custom colors with hexcodes
    Converting hexcodes to a rgb tuple
    '''
    def custom(self, hexcode):
        hexC = hexcode.lstrip('#')
        rgb = tuple(int(hexC[i:i+2], 16) for i in (0, 2, 4))
        return rgb
