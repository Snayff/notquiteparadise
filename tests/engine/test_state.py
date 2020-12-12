from scripts.engine.core import state
from scripts.engine.internal.constant import GameState


class TestState:

    def test_set_state(self):
        """
        Test changing the state
        """
        state.set_new(GameState.GAME_MAP)
        assert state.get_current() == GameState.GAME_MAP
