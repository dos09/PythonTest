class Banana:
    def __init__(self, color = 'yellow'):
        self.color = color and color.strip().lower()
        
    def run(self):
        return 'I am {0:s} banana'.format(self.color)