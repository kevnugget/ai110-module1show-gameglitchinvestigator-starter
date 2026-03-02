# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

Phase 1: Four bugs I found in the program are:
- When a game ends, the "New Game" button does not work. It changes the secret number, but the user is unable to actually enter their guesses.
   - The button fails to actually reset the game because it only resets attempts and secret. It does not reset the st.session_state.history, st.session_state.status, and st.session_state.score. It also hardcodes the difficulty range as it is strictly 1-100, but low-high determined by the difficulty range. Since it doesn't reset those variables, it means that the player carries over their previous's games history, win/status, and score into the new game.
- The hint is telling the user the incorrect range to find the secret number. The logic is flipped, where a higher guess is told to "Go HIGHER" whereas a lower guess is told to "Go LOWER"
   - The logic in the "Check Guess" function is flipped. When a user enters a guess that is too high, we want the game to print "GO LOWER" to get the user to lower their guess and vice versa. This will allow them to actually get closer to the secret, rather than farther away.
- The "Attempts Left" does not count the first attempt that user inputs. The second input and successive ones do count towards the "Attempts Left."
   - The st.info display uses attempt_limit - st.session_state.attempts, and attempts starts at 1.When the user submits, attempts increments by 1, but the st.info line runs before the if submit: block in the page. So on that rerun, the display still reads incorrect attempts - 1 because the increment hasn't happened yet in that pass. The increment happens lower on the page, and its effect only shows on the next rerun.
      - Simply put, load → shows wrong attempts by 1, first guess rerun → shows same wrong attempts by 1 (increment happens after display), second guess rerun → shows correct attempts 
- The game shows an incorrect range in display
   - st.info always says "between 1 and 100" instead of using low and high variables to determine the range for guessing.

Phase 2: 
