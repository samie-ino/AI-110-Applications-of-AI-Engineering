from logic_utils import check_guess, get_attempts_for_difficulty
import pytest

# Section 1: Guessing the Logic Tests
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

# Section 2: Difficulty Attempts Tests
def test_attempts_for_easy_difficulty():
    # Easy difficulty should have 8 attempts
    attempts = get_attempts_for_difficulty("Easy")
    assert attempts == 8

def test_attempts_for_normal_difficulty():
    # Normal difficulty should have 6 attempts
    attempts = get_attempts_for_difficulty("Normal")
    assert attempts == 6

def test_attempts_for_hard_difficulty():
    # Hard difficulty should have 5 attempts
    attempts = get_attempts_for_difficulty("Hard")
    assert attempts == 5

# Section 3: Run the pytest
if __name__ == "__main__":
    pytest.main(["-v",__file__])