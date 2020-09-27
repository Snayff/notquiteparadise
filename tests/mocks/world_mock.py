import sys



def mock_methods(methods):
    module = sys.modules['scripts.engine.world']
    for name, value in methods.items():
        setattr(module, name, value)
