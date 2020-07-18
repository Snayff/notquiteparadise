import sys
from tests.mocks import ui_mock

def mock_methods(methods):
    module = sys.modules['scripts.engine.world']
    for name, value in methods.items():
        setattr(module, name, value)
