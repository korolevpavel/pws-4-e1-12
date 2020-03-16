import pytest
import game

@pytest.fixture()
def word_test():
    game.WORD = 'skillfactory'
