# FastAPI-Super-Blog-Site
This repository contains the files for my FastAPI Blog site which will be a simple yet holistic blog site using a micro-database called SQLITE. 


## What is the idea behing this app?
I've always loved the idea of a blog site but wanted to make a simple solution towards it, I will be using the following frameworks and libraries for this project:
  - FastAPI (for routing and back-end processing)
  - SQITE (for storing data efficiently)
  - Django (for ORM)
  - React (for front-end designs and User Interface)

## How to run this ?
Please activate a virtual environment for python by following these steps:

### For windows
```bash
python -m venv VirtualEnviron
cd VirtualEnviron/scripts/
activate

#Come back to the root of this project's repository using cd 
pip install -r requirements/dev.txt
uvicorn API.Core.asgi:application --reload
```
### For Linux
```bash
python -m venv VirtualEnviron
cd VirtualEnviron/bin/
source activate

#Come back to the root of this project's repository using cd 
pip install -r requirements/dev.txt
uvicorn API.Core.asgi:application --reload
```

