import game
import pytest

def test_replace_letter_found():
    assert game.replace_letter(game.WORD, 's')


def test_replace_letter_not_found():
    assert game.replace_letter(game.WORD, 'b') == []