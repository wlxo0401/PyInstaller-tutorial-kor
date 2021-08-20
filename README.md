![pyinstaller 설치](https://github.com/wlxo0401/PyInstaller/blob/main/image/pyinstaller_logo.png)

# 개요 

Python으로 작업한 프로그램을 배포하기 위해서는 실행 파일로 만들어야한다.

다른 사용자에게 주는 것이 아닌 나 혼자 어디서든 사용하기 위해서도 실행 파일로 바꾸는게 좋다.

Python 배포파일을 생성하기 위한 방법은 아래 두가지 방법이있다.   

1. PyInstaller   
2. cx_freeze

이 글에서는 PyInstaller를 다룬다.


※ 읽기 전에 주의   
개인적으로 기억하려고 남긴 것.   
가독성이 많이 떨어진다.   
더 좋은 글들이 많다.


# PyInstaller

[공식 사이트](http://www.pyinstaller.org/)   

***"PyInstaller는 파이썬 응용 프로그램과 모든 종속성을 단일 패키지로 번들로 묶는다."***
공식 사이트 내용을 번역한 것이다.

쉽게 생각해서 프로젝트 작업을 하면서 사용하는 ui, 이미지, 아이콘 등 다같이 배포하기 쉽게 묶어준다.

Windows와 Linux 호환은 안되며, 32bit와 64bit 환경에서 각각 배포파일을 생성해야한다.


[도큐멘트](https://pyinstaller.readthedocs.io/en/stable/)
[라이센스](https://pyinstaller.readthedocs.io/en/stable/license.html)

# 설치

![pyinstaller 설치](https://github.com/wlxo0401/PyInstaller/blob/main/image/1.gif)
```python
pip install pyinstaller
```

파이썬을 사용한 사람들은 누구나 쉽게 설치 가능하다.

# 사용할 파이썬 예제 코드

## [예제 코드 보러가기](https://github.com/wlxo0401/PyInstaller)


![테스프 프로그램 예시](https://github.com/wlxo0401/PyInstaller/blob/main/image/2.gif)

> **1번 테스트 프로그램은 basic_test.py 파일 하나로 이루어진 단순 덧셈 프로그램이다.**



![테스프 프로그램 예시](https://github.com/wlxo0401/PyInstaller/blob/main/image/3.gif)

> **2번 테스트 프로그램은 UI폴더 image폴더가있고 그 안에 각각 사진과 py파일이 들어있다.**


# 사용방법

1. **명령어**만 입력해서 콘솔창에서 실행하는 방법 [바로보기](#명령어-방식)
2. **옵션파일**을 만들어서 <U>명령어로 그 **옵션**을 실행하는 방법</U>이 있다. [바로보기](#spec(옵션파일)-방식)

간단한 프로그램은 명령어 방법으로도 충분한데 **옵션파일**을 다루면 <U>옵션을 저장하고 편하게 사용</U> 가능하다.

※둘다 최종적으로 명령어를 입력해서 실행하기 때문에 콘솔 위치는 python파일 혹은 spec파일이 위치한 곳으로 이동해야한다.

## 명령어 방식

명령어 방식은 해당 옵션들을 기억하고 입력해주어야한다.   
옵션은 **기본 명령어**와 **축약 명령어**로 두가지 방법이 있으니 편하게 사용하면된다.

**0. 제일 기본 방법**
```
pyinstaller basic_test.py
```
제일 **기본적인** 방법이다. 모든 값이 default값으로 설정되며    
이렇게 실행하면 **build폴더, dist폴더, spec(옵션파일)파일**이 생성되는데 **dist폴더**는 최종 결과물 폴더가 생성된다.

![기본 방법](https://github.com/wlxo0401/PyInstaller/blob/main/image/4.gif)

> **기본적인 실행 방법 예시**

<br>

**1. 프로그램을 하나의 폴더로 배포하기**
```
pyinstaller --onedir basic_test.py
pyinstaller -D basic_test.py
```
> 이 옵션은 입력을 안해도 default로 적용된다. 결과는 위에 <U>제일 기본 방법</U>과 같다.

**"내 컴퓨터 - 프로그램 파일"**에 설치된 파일들 처럼 폴더 안에 프로그램 실행에 필요한 구성 요소들이 생성된다.

<br>

**2. 프로그램을 하나의 파일로 배포하기**
```
pyinstaller --onefile basic_test.py
pyinstaller -F basic_test.py
```
> 이 옵션은 하나의 파일로 모두 압축하는 방법으로 포터블 프로그램이 공유되듯이 파일 하나로 생성된다.

<br>

**3. 콘솔 표시하지 않기**
```
pyinstaller --noconsole basic_test.py
pyinstaller -w basic_test.py
```
> 표준 i/o에 대 한 콘솔 창을 제공 하지 않습니다. 설정하지 않으면 콘솔창 표시되는게 기본 값이다.

GUI가 없는 프로그램이라면 콘솔창으로 입/출력하기 때문에 적용하면 안된다. (완료해도 실행하면 에러 발생)   
※ 나만 나는 것인지 아닌지 지금은 모르겠다. 콘솔 창을 제공 하지 않아 cmd로 실행 시켜도 에러가 발생한다.

반대로 GUI가 있는 프로그램은 입/출력을 대신하는 화면이 있기 때문에 콘솔 창이 필요 없다면 꼭 설정하기! 

> - 옵션을 적용하지 말아야 할 떄   
콘솔 창이 출력되면 에러와 print가 모두 출력되니 최종 배포하기 전 까지는 콘솔창을 출력하는게 좋다.

![콘솔 옵션을 끈 CUI프로그램](https://github.com/wlxo0401/PyInstaller/blob/main/image/6.gif)
> 옵션을 적용한 콘솔 창 프로그램 (에러는 모두가 나는지 모름)

![콘솔이 표시된 GUI프로그램](https://github.com/wlxo0401/PyInstaller/blob/main/image/5.gif)
> 옵션을 적용하지 않은 GUI 프로그램

<br>

**4. 예시**

예시는 정답이 아닙니다. 이렇게도 사용하는구나 하면서 봐주세요.

```
pyinstaller --onefile basic_test.py
```
> - GUI가 없는 콘솔 프로그램인데 폴더가 아닌 하나의 파일로 배포 or 테스트하고 싶은 경우   
> - GUI가 있는데 하나의 파일로 만들어서 콘솔로 만들어서 테스트하고 싶은 경우  

<br>

```
pyinstaller --onedir basic_test.py
```
> - GUI가 없이 콘솔 프로그램인데 폴더로 생성해서 배포하고 싶은 경우
> - GUI가 있는데 폴더로 만들어서 테스트하고 싶은 경우

<br>

```
pyinstaller -w --onefile basic_test.py
```
> - GUI가 있으면서 하나의 파일로 배포하고 싶은 경우

<br>

```
pyinstaller -w --onedir basic_test.py
```
> - GUI가 있으면서 하나의 폴더로 배포하고 싶은 경우

<br>

**5. 명령어 방법 주의**

> 1. 프로그램 코드에 상대주소를 사용한다면 최종 배포물 폴더 안에 파일들을 이동해야한다.
> 2. 처음 배포파일 만들 때 콘솔창 끄는 옵션은 주지 말고 콘솔 창을 확인하면서 에러를 잡아가는게 좋다.
> 3. 가끔 뭔가 안되는 것 같다.

<hr>

## SPEC(옵션파일) 방식

**1. 준비**

![폴더 구조](https://github.com/wlxo0401/PyInstaller/blob/main/image/1.PNG)   

icon, image, ui 폴더가 있고 ```My_Program.py```으로 실행하는 프로그램이 있다면

```My_Program.py```과 같은 자리에 ```My_Program.spec``` 파일을 하나 만들고 아래 설정들을 붙여 넣어 준다.

```
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [함께 가지고 가야하는 파일들]
a = Analysis([실행하는 코드 파일],
            pathex=[실행하는 코드 파일 경로],
            binaries=[],
            datas=added_files,
            hiddenimports=[강제로 가지고가는 라이브러리],
            hookspath=[],
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)
exe = EXE(pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name=프로그램 이름,
        debug=True,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,
        uac_admin=True,
        icon=아이콘 경로)
coll = COLLECT(exe,
            a.binaries,
            a.zipfiles,
            a.datas,
            strip=False,
            upx=True,
            upx_exclude=[],
            name=dist안 폴더이름)
```

**2. 배포파일 생성 예시**

*2번 테스트 프로그램으로 작성*

- **added_files**   
![added_files](https://github.com/wlxo0401/PyInstaller/blob/main/image/2.PNG) 
> 프로그램 상대경로에 필요한 파일들을 한 폴더에 넣어기 위해서 작성. image폴더 및 아이콘을 가지고 온다.
```
added_files = [ ("./test.ico", '.'),
                ("./image/*", './image')]
```
소괄호 안에 옮길 파일or폴더와 배포 폴더 안에 어디로 갈지 정해줍니다.

아이콘은 상위폴더에, 이미지 폴더 속 사진들은 배포 폴더 속에서도 그대로 위치해주기 위해서 저렇게 설정합니다.

<br>

- **Analysis**   
![Analysis](https://github.com/wlxo0401/PyInstaller/blob/main/image/3.PNG) 
> 실행 코드 파일입니다. 프로그램 실행할 때 제일 먼저 실행하는 파일을 적어주세요.
```
['My_Program.py']
```

<br>

- **Analysis -> "pathex"**   
![pathex](https://github.com/wlxo0401/PyInstaller/blob/main/image/4.PNG) 
> 실행 파일이 있는 경로입니다.
```
pathex=['C:\\Users\\wlxo0\\Documents\\Python\\PyInstaller\\example\\002']
```

<br>

- **Analysis -> "hiddenimports"**   
[설명](https://stackoverflow.com/questions/27947639/how-to-properly-create-a-pyinstaller-hook-or-maybe-hidden-import)
> 자동으로 배포에 포함되지 않는 라이브러리들을 작성해줍니다. 지금 프로그램에서는 문제가 없습니다. 공백으로 둡니다.
```
만약에 작성한다면
hiddenimports=["PyQt5.QtMultimediaWidgets"]
```

<br>

- **Analysis -> "datas"**    
![datas](https://github.com/wlxo0401/PyInstaller/blob/main/image/5.PNG) 
> 위에 ```added_files```을 작성한 여부로 설정되도록 미리 작성해둔 겁니다.
```
datas=added_files
```

<br>

- **EXE -> "name"**    
![name](https://github.com/wlxo0401/PyInstaller/blob/main/image/6.PNG) 
> 프로그램 exe 실행 파일 이름과 프로세서 이름을 결정
```
name='My_Test_Program'
```

<br>

- **EXE -> "debug"**   
![debug](https://github.com/wlxo0401/PyInstaller/blob/main/image/7.PNG) 
> 콘솔창을 활성화해서 배포한다면 프로그램 실행하기 전 모습이 출력됨
```
debug=False
```

<br>

- **EXE -> "console"**   
![console](https://github.com/wlxo0401/PyInstaller/blob/main/image/8.PNG)
> 콘솔창 출력 여부 테스트하는 상황이라면 콘솔창도 뜨게 하는게 좋다.
```
console=True
```

<br>

- **EXE -> "uac_admin"**
> 프로그램으로 파일을 읽고 쓴다면 관리자 권한 부여를 키고 배포해야한다. 그냥 설정하는게 좋다고 생각됨
```
uac_admin=True
```

<br>

- **EXE -> "icon"**   
![name](https://github.com/wlxo0401/PyInstaller/blob/main/image/6.PNG) 
> 배포하는 프로그램 아이콘을 설정해준다.
```
icon='./test.ico'
```

<br>

- **COLLECT -> "name"은 생성되는 폴더 이름**   
![name](https://github.com/wlxo0401/PyInstaller/blob/main/image/9.PNG) 
> dist 폴더 속에 생성된 배포용 폴더 이름
```
name='Public_Program'
```

<br>
<br>

**3. 최종 결과**
```
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [ ("./test.ico", '.'),
                ("./image/*", './image')]
a = Analysis(['My_Program.py'],
            pathex=['C:\\Users\\wlxo0\\Documents\\Python\\PyInstaller\\example\\002'],
            binaries=[],
            datas=added_files,
            hiddenimports=[],
            hookspath=[],
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)
exe = EXE(pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='My_Test_Program',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=True,
        uac_admin=True,
        icon='./test.ico')
coll = COLLECT(exe,
            a.binaries,
            a.zipfiles,
            a.datas,
            strip=False,
            upx=True,
            upx_exclude=[],
            name='Public_Program')
```
![콘솔이 표시된 GUI프로그램](https://github.com/wlxo0401/PyInstaller/blob/main/image/7.gif)

# 정리

1. SPEC 파일을 잘 활용하자
2. 안켜지면 상대경로 파일들을 배포파일 위치로 잘 옮겨주자
3. 한번만에 되는 경우가 없다.
4. 라이브러리 에러가 발생하면 스택오버플로우로 달려가자
5. 자기가 어떤 프로그램을 만들지 생각하고 옵션을 적용하자
6. 모르면 검색하고 댓글 달기



<hr>
사진 출처      

[맥라렌](https://www.pngitem.com/middle/hhxwiwx_mclaren-png-transparent-png/)

[아이콘](https://www.nicepng.com/ourpic/u2w7e6y3y3a9w7w7_registration-for-portuguese-and-spanish-classes-learn-free/)