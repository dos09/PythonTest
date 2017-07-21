class SwitchFruit:    
    # if not using a method preffix, someone can call
    # any method on this object
    
    @staticmethod
    def fruit_banana():
        print('banana')
    
    @staticmethod
    def fruit_orange():
        print('orange')
    
    @staticmethod
    def default_fruit():
        print('default fruit')
    
    @staticmethod
    def switch(fruit):
        chosen = getattr(SwitchFruit, 
                         'fruit_'+fruit, 
                         SwitchFruit.default_fruit)
        chosen()

SwitchFruit.switch('banana')        
SwitchFruit.switch('mango')