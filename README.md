# 독서 블로그
책을 읽고 책에 대한 감상을 나눌 수 있는 블로그입니다.

## 목차
[1. 목표와 기능](#1-목표와-기능)<br>
[2. 개발 기술 및 환경](#2-개발-기술-및-환경)<br>
[3. 프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)<br>
[4.UI](#4-ui)<br>
[5. 데이터베이스 모델링(ERD)](#5-데이터베이스-모델링erd)<br>
[6. 기능](#6-기능)<br>
[7. 개발하며 느낀 점](#7-개발하며-느낀-점)<br>

## 1. 목표와 기능
 ### 1-1. 목표
 - 읽은 책에 대한 감상을 나눌 수 있는 블로그
 ### 1-2. 기능
 - 원하는 장르의 책을 찾아볼 수 있도록 태그 기능 추가
 - 다양한 의견을 나눌 수 있도록 댓글 기능 추가
## 2. 개발 기술 및 환경
 ### 2-1. 개발 기술

<div>
    <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white"> 
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white"> 
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"> 
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"> 
</div>

 <div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> 
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
</div>

 ### 2-2. 개발 환경
 <div>
    <img src="https://img.shields.io/badge/VisualStudioCode-007ACC?style=for-the-badge&logo=VisualStudioCode&logoColor=white"> 
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
</div>

## 3. 프로젝트 구조와 개발 일정
 ### 3-1. 프로젝트 구조

 ```
 📦Django_Blog
 ┣ 📂accounts
 ┃ ┣ 📂migrations 
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂main
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂reading_blog
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂templates
 ┃ ┣ 📂accounts
 ┃ ┃ ┣ 📜login.html
 ┃ ┃ ┣ 📜signup.html
 ┃ ┃ ┗ 📜signup_success.html
 ┃ ┣ 📂main
 ┃ ┃ ┗ 📜index.html
 ┃ ┣ 📂reading_blog
 ┃ ┃ ┣ 📜form.html
 ┃ ┃ ┣ 📜post_confirm_delete.html
 ┃ ┃ ┣ 📜post_detail.html
 ┃ ┃ ┗ 📜post_list.html
 ┃ ┗ 📜base.html
 ┣ 📂tutorialdjango
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂media
 ┃ ┗ 📂blog
 ┣ 📂static
 ┃ ┣ 📂asset
 ┃ ┗ 📜bootstrap.min.css
 ┣ 📂venv
 ┣ 📜.gitignore
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
 ```

 ### 3-2. URL 구조

- main

|App: main    |views 함수     |html 파일     |
|:------------|:--------------|:-------------|
|'/'          |index          |index.html    |

- accounts

|App: accounts      |views 함수      |html 파일             |
|:-----------------|:---------------|:---------------------|
|'signup/'         |signup          |signup.html           |
|'signup_success/' |signup_success  |signup_success .html  |
|'login/'          |login           |login.html            |
|'logout/'         |logout          |                      |

- reading_blog

|App: reading_blog      |views 함수         |html 파일                       |
|:----------------------|:------------------|:-------------------------------|
|'/'                    |post_list          |post_list.html                  |
|'new/'                 |post_new           |post_write.html                 |
|'<int:pk>/'            |post_detail        |post_detail.html                |
|'<int:pk>/edit/'       |post_edit          |post_write.html                 |
|'<int:pk>/delete/'     |post_delete        |post_confirm_delete.html        |
|'<int:pk>/comment/new/'|views.comment_new  |                                |
|'posttag/<str:tag>/'   |posttag            |                                |
 
 ### 3-3. 개발 일정(WBS)

<img src="https://user-images.githubusercontent.com/142385695/281078349-d9e17541-0309-4783-b5d1-83803d9fbdf2.png" width="80%">

## 4. UI

| | |
|:-:|:-:|
|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/4fabd0f0-5ddc-46be-92d0-1a15f3bdef81" width="100%">메인페이지|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/2b25b4e6-c332-4bc7-b6b9-156a03e1224d" width="100%">회원가입|
|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/d64ad494-e6e2-47e5-b2ab-2e1ec8183653" width="100%">회원가입 성공|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/8ef5062a-8b0b-4817-a34f-d2d2dad69ff2" width="100%">로그인|
|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/b207ddc2-0585-400f-a035-1eec5b5f19d4" width="100%">글목록|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/04f652c3-76f1-46d9-a383-4fe41bd062f3" width="100%">글작성|
|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/15f4ef89-61f7-47b1-a4e6-cea064c017a2" width="100%">글삭제|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/551f6e07-82d2-4521-b7c0-fe89f2bb0875" width="100%"> 글 상세보기|

## 5. 데이터베이스 모델링(ERD)

<img src="https://github.com/hantang820/Django_Blog/assets/142385695/e15bf8fb-bf55-43b7-b44c-fea9a2927248" width="80%">

## 6. 기능
 ### 6-1. 블로그 CRUD 기능
#### 메인페이지
- 로그인 전
<img src="https://github.com/hantang820/Django_Blog/assets/142385695/42438640-bee9-497e-8860-f0de6c36562e" width="100%">

- 로그인 후 
<img src="https://github.com/hantang820/Django_Blog/assets/142385695/03742dc9-36aa-4308-9365-44a90cbf6a09" width="100%">

#### 회원가입
![회원가입](https://github.com/hantang820/Django_Blog/assets/142385695/103ca953-851e-4ff0-9bf5-dd15231cff43)

#### 로그인
![gif](https://github.com/hantang820/Django_Blog/assets/142385695/02d24062-6727-4c8f-812c-d48336fdc502)

#### 게시글 작성
![gif](https://github.com/hantang820/Django_Blog/assets/142385695/ab95da1f-0bb0-49ee-aff1-cf3b9eeebe14)


#### 게시글 목록
<img src="https://github.com/hantang820/Django_Blog/assets/142385695/468cca70-4d3e-46ca-8f18-89ac480a5d95" width="100%">

- 글 목록에서 제목, 작성자, 작성일, 조회수 확인
- 글에 댓글이 작성되었을 경우엔 제목 옆에 댓글의 수가 표시됨

#### 게시글 상세보기
![gif](https://github.com/hantang820/Django_Blog/assets/142385695/63aada23-1649-4b84-82c0-fc977fea2244)

#### 게시글 수정
![gif](https://github.com/hantang820/Django_Blog/assets/142385695/fcfd28b7-48d8-42d4-8cc1-e27485930c2d)

#### 게시글 삭제
![gif](https://github.com/hantang820/Django_Blog/assets/142385695/1784cac5-30bd-4ed6-89b5-527fc3eb644e)
- 게시글 삭제 확인을 위한 페이지에서 아니요를 누르면 글목록으로 돌아감

#### 게시글 검색
![gif](https://github.com/hantang820/Django_Blog/assets/142385695/d02d3afc-3c18-40d0-8d3c-4bad53d790e3)

#### 같은 태그의 게시글 모아보기
![gif](https://github.com/hantang820/Django_Blog/assets/142385695/64b22b75-c322-4229-b16c-a3e4b51b7278)

- 글에 있는 태그를 눌러서 같은 태그를 가진 글들을 모아볼 수 있음

### 6-2. 로그인/회원가입 기능을 이용하기

#### 로그인을 한 사용자만 게시글 작성 가능
![gif](https://github.com/hantang820/Django_Blog/assets/142385695/b0b03116-7071-4723-af61-6155ee3ef2ba)

- 로그인 상태로 블로그에 접속해야 글 작성 버튼 활성화

#### 본인이 작성한 게시글일 때만 수정/삭제 가능
<img src="https://github.com/hantang820/Django_Blog/assets/142385695/1371a50c-8351-4beb-8dc5-82a72423c16e" width="100%">
<img src="https://github.com/hantang820/Django_Blog/assets/142385695/36bf64ab-a929-496c-97b8-36ff564704cf" width="100%">

- 본인이 작성한 글일 때만 수정/삭제 버튼 활성화

## 7. 개발하며 느낀 점 
- Django를 사용해서 페이지를 개발하는 게 얼마나 편리한지 느낄 수 있었습니다. 또, 모르는 부분이 많아 그 편리함을 제대로 이용하지 못한다는 것이 답답하게 느껴질 때도 많았습니다. 좋은 기능을 잘 활용하기 위해서 더 많이 공부해야겠다는 생각을 하게 된 프로젝트였습니다. 