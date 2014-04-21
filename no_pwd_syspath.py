class NoPathHook(object):
    def __init__(self, syspath):
        if syspath == '':
            pass
        else:
            raise ImportError

    @staticmethod
    def find_module(dummy_module):
        return None

def register():
    import sys
    sys.path_hooks.append(NoPathHook)
    sys.path_importer_cache.clear()
