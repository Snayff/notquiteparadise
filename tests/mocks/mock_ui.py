import sys
import types

module_name = 'scripts.engine.ui.manager'
mock_module_name = f'{module_name}_mock'
mock_module = types.ModuleType(mock_module_name)

sys.modules['scripts.engine.ui.manager'] = mock_module
sys.modules['scripts.engine.ui.manager'].ui = {}  # type: ignore
