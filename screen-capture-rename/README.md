# Screen capture rename

스크린 캡쳐하고 저장되는 파일 이름에 관한 스크립트입니다.


## Using

터미널에서 다음과 같이 사용합니다.

```
python3 index.py
> Please input filename:
Rename screen capture
> Using dates in filename (Y/n): 
Update useDate
> Using shadow window (Y/n): 
Update useShadow
Good bye
```

다음과 같이 질문이 있으며 입력하면 그대로 적용됩니다.

- `Please input filename`: 저장되는 파일이름을 입력합니다.
- `Using dates in filename`: 저장되는 파일이름에서 날짜를 사용합니다.
- `Using shadow window`: 창 캡쳐를 할때 그림자를 사용할지에 대한 여부


## 참고할만한 내용들..

- 스크린 캡쳐 튜토리얼  
  https://support.apple.com/ko-kr/HT201361
- 캡쳐할때 썸네일 이미지가 잠시 나오는 기능 끄기  
  https://apple.stackexchange.com/questions/338066/how-to-disable-mojaves-floating-thumbnail-screenshot-preview
- 파일이름의 날짜에서 `오전|오후`를 `AM|PM`으로 변경하기  
  https://happygom.com/2018/10/24/한글-mac-os-스크린샷-파일명-영문으로-변경하기/
