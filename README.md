# Memorizer
이 프로그램은 이제현의 성공적인 인디 시험을 위해 제작한 프로그램입니다.

## Environments
개발과 문서 작성은 윈도우 10 운영 체제를 기준으로 하였습니다.

## Initial Setting

> **필독**: 이미 이 디렉토리에 Main.exe가 존재합니다. 그걸 사용하세요. 아래 내용은 스스로 빌드해보고자 하는 분들을 위한 설명입니다.

1. 파이썬을 설치하세요.
2. `pip`으로 PySide6, PyInstaller 및 의존 라이브러리를 설치하세요.
3. 이곳에서 다음 명령어를 실행하세요. (명령 프롬프트)

    ```
    pyinstaller -w -F src\Main.py
    ```
4. dist 폴더의 Main.exe를 복사하여 이 폴더로 붙여넣으세요.

## Usage
1. [resources/images](resources/images/)에 사진을 넣으세요.
    - 이때 사진의 이름은 #. chapter_name이어야 합니다.
    - (예) 1. 심장의 구조
1. [resources/answer.csv](resources/answer.csv)에 사진과 상응하는 답안을 양식에 맞추어 적으세요.
    - 첫째 줄은 헤더입니다. 남겨 주세요.
    - 둘째 줄부터 각 항목을 쉼표로 구분하여 한 줄에 답을 한 개씩 적으세요.
1. 복사한 .exe 파일을 실행하세요.
