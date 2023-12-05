# Tictactoe

Hello there!

This is a TicTacToe game. It can be scaled to any size wanted (see Configuration).

## Setup
To play the game, install first some packages

- I have used python `3.11.3` but older ones should work fine.
- `pip install -r requirements.txt` will dowload and install the required packages

#### OpenAI API key
To be able to play against the AI model (which you you must), you will need to setup a `API key` in your `PATH` variables. This `API key` must look like this:
```
OPENAI_API_KEY: sk-Abcdefg....
```

#### Configuration

To change any settings of the game, go to `main.py` and locate `# Config`

Here change any of the lines to alter the game function:

```python
# Config
display_size = (900, 900)
board_size = 5
in_row_to_win = 4
```

## Gameplay
To run the game, open a terminal and navigate to to the main project folder and run:
```
python main.py
```
When playing, have the terminal open beside the window that will popup. The window that pops up will be the board of the game. There you can make move by clicking on any square/cell. After you have made your move, the model will make its move.

# Note

The AI model is not good at all....
It does not seem to understand the logic of TicTacToe at all and has no sense of awareness.

I have tried to promt it in a better way, but the result is the same. If you want to try changing the promt, see file `src/gpt_interface.py`. Both variables `content_system` and `content_user` can be changed to alter its functionality. Just make sure to not remove any text that tell the model to answer in the specific format, or the code might break.

