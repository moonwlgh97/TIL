# GIT이란?
>분산 버전 관리 시스템


## GIT의 3가지 영역
1. Working Directory
  - 
2. Staging Area
  - 
3. Repository
  - 


### git 초기화
```bash
$ git init
```


### 상태 확인 명령어

```bash
$ git status
```

### staging area에 추가
```bash
$ git add {path}<folder_name>/{file_name}
```


### repository에 저장하기
```bash
$ git commit -m "commit message"
```


### git 기초 설정

```bash
$ git config --global user.email "moonwlgh@naver.com"
$ git config --global user.name "문지호"
$ git config --global --list
```


### commit 기록 확인하기

```bash
$ git log
```

### 직전 커밋 수정하기

```bash
git commit --amend
#vim에서 커밋 내용 수정ㅏ하기
#1. insert를 눌러서 - 삽입 상태로 만든다
#2. 커밋 메세지를 수정한다
#3. esc를 눌러서 -삽입 상태를 종료한다
#4. :wq를 입력해서 저장하고 종료한다
```


### git 설정 초기화
```bash
#vim 을 활용해서 설정 제거하기
#vim git  설정파일 열기
$ vim ~/.gitconfig
#insert 키: 수정상태 만들기
#--insert--인 상태에서 모든 내용 삭제
#esc:수정상태 종료
#wq

$ code ~/.gitconfig
```


### 원격 저장소 git에 등록

```bash 
$ git remote add {remote _nickname} {remote_url}
```

### 원격 저장소에 업로드
```bash
$ git push origin master
$ git pull origin master

```


### 원격저장소에 다운로드

``` bash


```