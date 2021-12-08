<h1 align="center">
	<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/110px-Python-logo-notext.svg.png"  alt="Logo"  width="150"><br><br>
    TOPAZ - Simulador de Cloud
</h1>

<div>
    <p align="center">
    <a href="https://www.linkedin.com/in/christian-d-oliveira/" target="_blank">
        <img src="https://img.shields.io/static/v1?label=Author&message=Christian&color=blue&style=for-the-badge&logo=LinkedIn" alt="Author: Christian">
    </a>
    <a href="#">
        <img src="https://img.shields.io/static/v1?label=Language&message=Python&color=yellow&style=for-the-badge&logo=Python" alt="Language: Python">
    </a>
    </p>
</div>

## Table of Contents

<p align="center">
 <a href="#about">About</a> •
 <a href="#features">Features</a> •
 <a href="#installation">Installation</a> • 
 <a href="#tests">Tests</a> •
 <a href="#technologies">Technologies</a>
</p>

## 📌About

<div>
    <p align="center">
    <em>
        Construction of a aplication using Python, a project to simulation cloud enviroment (load balance).
    </em>
    </p>
</div>

## 🚀Features

- Creation and Deletion of Servers.
- Connect and Disconnect Users in Servers.
- Read and Write files.

## 📕Installation

**You must have already installed**
- [Python](https://www.python.org/) >= 3.9

**Recommendations**
-   I recommend using VSCode as development IDE

**Let's divide it into 3 steps.**
1. Clone this repository
2. Install dependencies
3. Initializing the BackEnd
  ---
### 1. Clone this repository
```
git clone https://github.com/Christian-Oliveira/topaz-simulador-cloud.git
```
---
### 2. Create and Active Virtual Environment (VENV)
```
python -m venv .venv
```
### 2.1. Active VENV in Windows Enviroment
```
.venv/Scripts/activate
```
or
```
source .venv/Scripts/activate
```
### 2.2. Active VENV in Linux Enviroment
```
source .venv/bin/activate
```

### 3. Install the dependencies
```
pip install -r requirements.txt
```

*Make sure your internet is stable, as this may take a while* 

### 4. Initializing the Application
First check if it is inside the *src* folder.

```
python app.py
```
When processing is finished, the *output.txt* file will be in the *src/temp* folder.

## ✅Tests
To run the tests just run the following command in the *src* folder.
```
pytest
```
## 🌐Technologies

- [Python](https://www.python.org/)
- [Pytest](https://docs.pytest.org/en/6.2.x/)
- [Git](https://git-scm.com/)
