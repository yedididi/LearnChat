from .generator import Generator
from .retrieval import Retrieval


class ChatBot:
    def __init__(self) -> None:
        self.retrieval = Retrieval()
        self.generator = Generator()

    def respond(self, query: str, debug: bool = False) -> str:

        retrieved = self.retrieval.retrieve(query)

        prompt: str = (
            f"<user>: {query}\n\n<assistant>: "
        )

        if retrieved:
            prompt = f"<system> Use this information: {retrieved}\n\n" + prompt

        if debug:
            print("===prompt===")
            print(prompt)
            print("============")

        answer = self.generator.generate(prompt)

        return answer

    def converse(self) -> None:
        while True:
            query = input("<< ")
            answer = self.respond(query)
            print(f">> {answer}")
