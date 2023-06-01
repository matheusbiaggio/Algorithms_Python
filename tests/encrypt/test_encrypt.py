from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("hello", "key")

    with pytest.raises(TypeError):
        encrypt_message(123, 5)

    assert encrypt_message("hello world", 4) == "dlrow o_lleh"

    assert encrypt_message("hello world", 5) == "olleh_dlrow "

    assert encrypt_message("hello", 1) == "h_olle"

    assert encrypt_message("hello", 5) == "olleh"

    assert encrypt_message("", 3) == ""

    assert encrypt_message("", 0) == ""

    assert encrypt_message("", 1) == ""

    assert encrypt_message("", 2) == ""

    assert encrypt_message("", -3) == ""

    assert encrypt_message("hello world", 7) == "w olleh_dlro"

    assert encrypt_message("hello!@#$%^world", 5) == "olleh_dlrow^%$#@!"
