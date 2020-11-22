from scripts.engine.core import state
from scripts.engine.internal.constants import GameState


class TestState:

    def test_set_state(self):
        """
        Test changing the state
        """
        state.set_new(GameState.GAMEMAP)
        assert state.get_current() == GameState.GAMEMAP
