try:
    from settings_local import *
except ImportError as e:
    from settings_prod import *
