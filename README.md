# 독서 블로그

## 목차
[1. 목표와 기능](#1-목표와-기능)<br>
[2. 개발 기술 및 환경](#2-개발-기술-및-환경)<br>
[3. 프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)<br>
[4. URL 구조](#4-url-구조)<br>
[5. UI](#5-ui)<br>
[6. 데이터베이스 모델링(ERD)](#6-데이터베이스-모델링erd)<br>
[7. 기능](#7-기능)<br>
[8. 개발하며 느낀 점](#8-개발하며-느낀-점)<br>

## 1. 목표와 기능
 ### 1-1. 목표
 -
 -
 ### 1-2. 기능
 -
 -
 -
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

<img src = "https://user-images.githubusercontent.com/142385695/281078349-d9e17541-0309-4783-b5d1-83803d9fbdf2.png" width="80%">

## 4. UI

| | |
|:-:|:-:|
|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/4fabd0f0-5ddc-46be-92d0-1a15f3bdef81" width="100%">메인페이지_로그인X|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/d1777935-6742-4d0f-90dc-9d403e0844b2" width="100%"> 메인페이지_로그인O|
|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/2b25b4e6-c332-4bc7-b6b9-156a03e1224d" width="100%">회원가입|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/d64ad494-e6e2-47e5-b2ab-2e1ec8183653" width="100%">회원가입 성공|
|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/8ef5062a-8b0b-4817-a34f-d2d2dad69ff2" width="100%"> 로그인|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/b207ddc2-0585-400f-a035-1eec5b5f19d4" width="100%">글목록|
|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/04f652c3-76f1-46d9-a383-4fe41bd062f3" width="100%">글작성|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/15f4ef89-61f7-47b1-a4e6-cea064c017a2" width="100%">글삭제|

| |
|:-:|
|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/551f6e07-82d2-4521-b7c0-fe89f2bb0875" width="80%"> 
글 상세보기_댓글X 본인글O|
|<img src="https://github.com/hantang820/Django_Blog/assets/142385695/47662b9c-d3eb-4e1e-8fac-ea36a81d70bf" width="80%"> 
글 상세보기_댓글O 본인글X|

## 5. 데이터베이스 모델링(ERD)
## 6. 기능
## 7. 개발하며 느낀 점 