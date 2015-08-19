# -*- coding: utf8 -*-
def qrcode_transform(code):
        import qrcode
        import os
        if code:
            img=qrcode.make(code)
            img.save(os.getcwd()+r'\testdj\static\img\test.png')
            return True
        else:
            return False
        
if  __name__ == '__main__':
    qrcode_transform('1')
