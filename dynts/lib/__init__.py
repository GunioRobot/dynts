try:
    from cts import *
    hasextensions = True
except:
    hasextensions = False
    from .fallback import *
else:
    import fallback
    