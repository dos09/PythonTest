class Common:
    VAR_COMMON = 'VAR_COMMON'
    NUMS = [1,2,3]
    
    def __init__(self, c):
        print(' * init Common')
        self.c = c
        
    def run(self):
        print(' * run Common')
        print('Common vars:',
              Common.VAR_COMMON, Common.NUMS)
        print('self vars:', self.c, self.VAR_COMMON, self.NUMS)

class Asset(Common):
    VAR_ASSET = 'VAR_ASSET'
    NUMS = Common.NUMS + [3, 4, 5]
    
    def __init__(self, a, c):
        print(' * init Asset')
        super(Asset, self).__init__(c)
        self.a = a
        
    def run(self):
        print(' * run Asset')
        super(Asset, self).run()
        print(Asset.VAR_ASSET, self.a)
        print('BonusC:', 
              self.c, Asset.VAR_COMMON, Common.VAR_COMMON, self.VAR_COMMON)
        print('BonusA:', Asset.VAR_ASSET, self.VAR_ASSET)
        print('NUMS:', Common.NUMS, Asset.NUMS, self.NUMS)
        
oc = Common('c')
oc.run()
oa = Asset('a', 'c')
oa.run()