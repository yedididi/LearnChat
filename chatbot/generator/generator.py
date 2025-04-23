from typing import Iterator
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class Generator:
    def __init__(self) -> None:
        # ###
        self.tokenizer = AutoTokenizer.from_pretrained("skt/kogpt2-base-v2")
        self.model = AutoModelForCausalLM.from_pretrained("skt/kogpt2-base-v2")
        self.model.eval()  # 추론 모드
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        # ###
        


    def generate(self, prompt: str) -> Iterator[str]:
        # #
        # 주석을 지우고 다음 기능을 완성하자.
        # generate 는 단순 prompt 뒤에 이어질 "자연스러운" 말을 리턴하면 된다.
        # 단, 토큰을 하나하나 출력하기 위해서는 Iterator 로 리턴해야한다. 
        # yield 개념을 모른다면 공부해보자!
        # 
        # 예시 1:
        # prompt: I want
        # @return: " to be a doctor"
        # 
        # 예시 2:
        # prompt: Pizza is 
        # @return: " so delicious"
        # ###
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)

        output = self.model.generate(
            input_ids,
            max_new_tokens=50,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.8,
            pad_token_id=self.tokenizer.eos_token_id
        )

        # 새로 생성된 부분만 추출
        generated_ids = output[0][input_ids.size(1):]
        generated_text = self.tokenizer.decode(generated_ids, skip_special_tokens=True)

        # 한 단어씩 stream 출력
        from time import sleep
        for word in generated_text.split():
            sleep(0.1)  # 애니메이션처럼 출력
            yield word
            yield " "
