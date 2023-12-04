from openai import OpenAI
from board import Mark
import re

class Gpt():
    def __init__(self) -> None:
        self.client: OpenAI = OpenAI()

    def apiCall(self, board_state: str, board_size: int, num_in_row_to_win: int,
                playerMark: Mark, gptMark: Mark) -> tuple[int, int] | None:

        content_system: str = f"""You are playing TicTacToe against a user.
        You shal try to play as perfectly as possible and always make a move within the board.
        Try to win by getting {num_in_row_to_win}. If not possibel, stop the user from winning.
        You can only answer in the following format "(X,Y)", where the X and Y are the coordinates of the board placement.
        The X and Y shal be integers.
        """
        content_user: str = f"""
        I am {playerMark}, you are {gptMark}. It is your move. The board is {board_size}x{board_size} in size.
        One needs {num_in_row_to_win} in row to win. This is the current game/board state: \n {board_state} \n
        What is your move? Answer in nothing else than the following format: (row, column). Examaple of this top left is: (0,0)
        """

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": content_system},
                {"role": "user", "content": content_user}
            ]
        )

        def parseCoordinates(text: str) -> list:
            pattern = r"\(([^,]+),([^)]+)\)"
            matches = re.findall(pattern, text)
            coordinates = []
            for match in matches:
                x, y = match
                coordinates.append((x.strip(), y.strip()))  # Stripping to remove any extra whitespace
            return coordinates

        if completion.choices[0].message.content == None:
            return None

        gpt_str = str(parseCoordinates(completion.choices[0].message.content)[0])

        # Removing parentheses and spaces
        cleaned_str = gpt_str.strip("() ").split(", ")

        # Converting each value to an integer
        values = [int(val.strip("'")) for val in cleaned_str]

        output: tuple[int, int] = (int(values[0]), int(values[1]))

        # Literal['stop', 'length', 'tool_calls', 'content_filter', 'function_call']
        if completion.choices[0].finish_reason == "stop":
            return output # Ok
        elif completion.choices[0].finish_reason == "length":
            print("Error model response: 'length'")
            return None
        elif completion.choices[0].finish_reason == "content_filter":
            print("Error model response: 'content_filter'")
            return None
        elif completion.choices[0].finish_reason == "function_call":
            print("Error model response: 'function_call'")
            return None
        elif completion.choices[0].finish_reason == "tool_calls":
            print("Error model response: 'tool_calls'")
            return None
        return None





# client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)

#
# 0 1 2 3 4
# 0|X| | | | |
# 1| | | | | |
# 2| | | | | |
# 3| | | | | |
# 4| | | | | |