# Memorizer
이 프로그램은 이제현의 성공적인 인디 시험을 위해 제작한 프로그램입니다.

## Environments
개발과 문서 작성은 윈도우 10 운영 체제를 기준으로 하였습니다.

## Initial Setting
1. 파이썬을 설치하세요.
1. `pip`으로 PySide6, PyInstaller 및 의존 라이브러리를 설치하세요.
1. 이곳에서 다음 명령어를 실행하세요.

```
pyinstaller -w -F src/main.py
```

## Usage
1. [resources/images](resources/images/)에 사진을 넣으세요.
1. [resources/answer.csv](resources/answer.csv)에 사진과 상응하는 답안을 양식에 맞추어 적으세요.
1. [이곳](dist/main.exe)에 있는 파일을 실행하세요.
