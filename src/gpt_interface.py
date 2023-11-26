from openai import OpenAI

class Gpt():
    def __init__(self) -> None:
        self.client: OpenAI = OpenAI()

    def apiCall(self, board_state: str, board_size: int, num_in_row_to_win: int) -> tuple[int, int]:

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert TicTacToe player."},
                {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
            ]
        )

        return completion.choices[0].message
    



# client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)