# from typing import Iterator
# from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch


# class Generator:
#     def __init__(self) -> None:
#         # 모델 및 토크나이저 로딩 (GPT2)#
#         self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
#         self.model = AutoModelForCausalLM.from_pretrained("gpt2")
#         self.model.eval()  # 추론 모드

#         # pad_token 설정 (gpt2는 원래 없음)
#         if self.tokenizer.pad_token is None:
#             self.tokenizer.pad_token = self.tokenizer.eos_token

#         self.device = "cuda" if torch.cuda.is_available() else "cpu"
#         self.model.to(self.device)

#     def generate(self, prompt: str) -> Iterator[str]:
#         # 텍스트 토크나이즈
#         input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)

#         # 생성
#         output = self.model.generate(
#             input_ids=input_ids,
#             max_new_tokens=50,
#             do_sample=True,
#             top_k=50,
#             top_p=0.95,
#             temperature=0.8,
#             pad_token_id=self.tokenizer.pad_token_id
#         )

#         # 생성된 텍스트 디코딩 (prompt 제외 부분)
#         generated_ids = output[0][input_ids.size(1):]
#         generated_text = self.tokenizer.decode(generated_ids, skip_special_tokens=True)

#         # 한 단어씩 stream 출력
#         from time import sleep
#         for word in generated_text.split():
#             sleep(0.1)
#             yield word
#             yield " "

from typing import Iterator
from llama_cpp import Llama


class Generator:
    def __init__(self) -> None:
        # DeepSeek 모델 로드
        self.model = Llama.from_pretrained(
            repo_id="bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF",
            filename="DeepSeek-R1-Distill-Qwen-1.5B-IQ2_M.gguf",
        )

    def generate(self, prompt: str) -> Iterator[str]:
        # 모델 호출 (스트리밍 모드)
        stream = self.model(prompt, max_tokens=80, stream=True)

        # 스트리밍 응답 생성
        for chunk in stream:
            yield chunk["choices"][0]["text"]

