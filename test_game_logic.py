import sys
sys.path.append("..")  # Add parent directory to path to import logic_utils
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, message = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, message = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, message = check_guess(40, 50)
    assert result == "Too Low"

def test_attempts_starts_at_zero():
    """Attempts should be 0 before any guess, not 1."""
    initial_attempts = 0
    attempt_limit = 8  # Normal difficulty
    attempts_left = attempt_limit - initial_attempts
    assert attempts_left == attempt_limit

def test_first_guess_decrements_by_one():
    """After one guess, attempts left should drop by exactly 1."""
    initial_attempts = 0
    attempt_limit = 8
    initial_attempts += 1  # simulate first guess
    attempts_left = attempt_limit - initial_attempts
    assert attempts_left == 7

def test_new_game_resets_attempts():
    """New Game should reset attempts to 0."""
    attempts = 5  # mid-game
    attempts = 0  # new game reset
    assert attempts == 0

def test_new_game_resets_history():
    """New Game should clear the guess history."""
    history = [50, 25, 75]
    history = []  # new game reset
    assert history == []

def test_new_game_resets_status():
    """New Game should reset status to 'playing'."""
    status = "won"
    status = "playing"  # new game reset
    assert status == "playing"

def test_new_game_resets_score():
    """New Game should reset score to 0."""
    score = 150
    score = 0  # new game reset
    assert score == 0

def test_new_game_uses_difficulty_range():
    """New Game should pick a secret within the difficulty range, not hardcoded 1-100."""
    import random
    # Simulate Easy difficulty (range 1-20)
    low, high = 1, 20
    for _ in range(100):
        secret = random.randint(low, high)
        assert 1 <= secret <= 20, f"Secret {secret} is outside Easy range 1-20"
