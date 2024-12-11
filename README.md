# LearnChat

## RAG 기반 챗봇 디자인

RAG 기반 챗봇을 기반으로 LLM 프로젝트 구조 설계를 진행해보자.

## Setup
먼저 다음 명령어로 가상환경을 만들고 활성화 시켜주자.
```sh
python3 -m venv venv
source venvbin/activate
```

이후 필요한 패키지들을 설치해준다.
```sh
pip install -r requirements.txt
```

(optional) 만약 서비스 코드가 아니고 개발 코드라면 dev dependency 도 설치해준다.
```sh
pip install -r requirements.dev.txt
```
## Run
다음 script 를 돌려서 코드를 실행할 수 있다.
```sh
python main.py
```

<br>
<br>

## (Optional) Test
test 코드가 작성되어 있을 때는 다음 명령어로 테스트를 진행할 수 있다.
```sh
pytest
```

특정 test code 만 돌리고 싶다면 다음과 같이 쳐주자.
```sh
pytest test_[your_test].py
```

## (Optional) Development

코드를 format 하고 싶으면 다음 명령어를 쳐보자.
```sh
black .
```

import 문의 순서를 보장하고 싶으면 다음 명령어를 치자.
```sh
isort .
```

코드의 typing 을 체크하고 싶으면 다음 명령어를 쳐보자.
```sh
mypy .
```

코드의 quality 를 보고 싶으면 다음 명령어를 쳐보자.
```sh
flake8 chatbot
```

