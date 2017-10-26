class Common:
    VAR_COMMON = 'VAR_COMMON'
    
    def __init__(self, c):
        print(' * init Common')
        self.c = c
        
    def run(self):
        print(' * run Common')
        print(Common.VAR_COMMON, self.c)

class Asset(Common):
    VAR_ASSET = 'VAR_ASSET'
    
    def __init__(self, a, c):
        print(' * init Asset')
        super(Asset, self).__init__(c)
        self.a = a
        
    def run(self):
        print(' * run Asset')
        super(Asset, self).run()
        print(Asset.VAR_ASSET, self.a)
        print('BonusC:', self.c, Asset.VAR_COMMON, Common.VAR_COMMON, self.VAR_COMMON)
        print('BonusA:', Asset.VAR_ASSET, self.VAR_ASSET)
        
oc = Common('c')
oc.run()
oa = Asset('a', 'c')
oa.run()