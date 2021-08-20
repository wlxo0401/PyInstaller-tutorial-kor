![pyinstaller 설치](https://github.com/wlxo0401/PyInstaller/blob/main/image/pyinstaller_logo.png)

# 개요 
파이썬으로 코딩을 완료하고 배포하는 방법을 정리

배포하는데 도움 주는 친구들
1. PyInstaller
2. cx_freeze

이 글에서는 PyInstaller를 다룬다.
자세하게는 다루지 않고 사용하는 범위 안에서 간단하게 정리한다.

# PyInstaller

[공식 사이트](http://www.pyinstaller.org/)   
PyInstaller는 파이썬 응용 프로그램과 모든 종속성을 단일 패키지로 번들로 묶는다.

프로젝트 작업을 하면서 사용하는 ui, 이미지, 아이콘 등 다같이 배포하기 쉽게 묶어준다.

[도큐멘트](https://pyinstaller.readthedocs.io/en/stable/)
[라이센스](https://pyinstaller.readthedocs.io/en/stable/license.html)


# 설치

![pyinstaller 설치](https://github.com/wlxo0401/PyInstaller/blob/main/image/1.gif)
```python
pip install pyinstaller
```

설치는 간단하게 이루어진다. 


# 사용방법
사용방법으로는 spec파일을 생성해서 하는 것과 명령어를 이용하는 방법이 있다.

간단한 프로그램은 커맨드 방법으로도 충분한데 spec을 다루면 옵션을 지정하고 편하게 사용 가능하다.

둘다 최종적으로 명령어를 입력해서 실행하기 때문에 콘솔 위치는 python파일 혹은 spec파일이 위치한 곳으로 이동해야한다.

테스트 예시 프로그램은 2가지로 ui프로그램과 커맨드 프로그램으로 나뉜다.   
[코드 보러가기](https://github.com/wlxo0401/PyInstaller)


![테스프 프로그램 예시](https://github.com/wlxo0401/PyInstaller/blob/main/image/2.gif)

1번 테스트 프로그램은 basic_test.py 파일 하나로 이루어진 단순 덧셈 프로그램이다.



![테스프 프로그램 예시](https://github.com/wlxo0401/PyInstaller/blob/main/image/3.gif)

2번 테스트 프로그램은 UI폴더 image폴더가있고 그 안에 각각 사진과 py파일이 들어있다.

## 기본 방법
```
pyinstaller basic_test.py
```
제일 기본적인 방법이다. 모든 값이 기본 값으로 설정되며 
exe파일 구성 요소는 폴더 안에 다 들어있다.

이렇게 실행하면 build, dist 폴더와 spec파일이 생성되는데 dist폴더 안에 exe파일이 준비된다. 

![기본 방법](https://github.com/wlxo0401/PyInstaller/blob/main/image/4.gif)

> 기본적인 실행 방법 예시

## 명령어 방식

명령어 방식은 해당 옵션들을 기억하고 입력해주어야한다.   
옵션은 기본 명령어와 축약 명령어로 두가지 방법이 있으니 편하게 사용하면된다.

1. 프로그램을 하나의 폴더로 구성한다.
```
pyinstaller --onedir basic_test.py
pyinstaller --D basic_test.py
```
이 옵션은 입력을 안해도 기본적으로 적용되는 옵션이라 기본 방법과 같다.   
프로그램을 설치하면 "내 컴퓨터 - 프로그램 파일"에 깔리는 것 처럼 폴더가 생성된다.

2. 프로그램을 하나의 파일로 구성한다.
```
pyinstaller --onefile basic_test.py
pyinstaller --F basic_test.py
```


[아이콘](https://www.nicepng.com/ourpic/u2w7e6y3y3a9w7w7_registration-for-portuguese-and-spanish-classes-learn-free/)


[맥라렌](https://www.pngitem.com/middle/hhxwiwx_mclaren-png-transparent-png/)