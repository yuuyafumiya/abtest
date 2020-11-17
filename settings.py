DEBUG = False #Trueから変更

###
省略
###

#追加
try:
    from .local_settings import *
except ImportError:
    pass
