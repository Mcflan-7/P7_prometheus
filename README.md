![enter image description here](https://travis-ci.com/Mcflan-7/P5_OpenFoodFacts.svg?branch=master) ![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

# ✨ Prometheus bot ✨

Prometheus is a web application using Google Maps and Media Wiki API that display specific information in AJAX following the guest question.

The name come from the book's intro **Life 3.0** from Max Tegmark where a fictional story with a superhuman AI (Prometheus) is conquering the world, it does an amazing job of outlining some of the ways a superhuman AI could impact the world in the good or bad way.

[The Tale of the Omega Team - Max Tegmark: Life 3.0 ](https://www.youtube.com/watch?v=ttZSk7rmFvc)

## Summary 📋

- [Getting started](#getting-started)
- [Installing](#installing)
- [Prerequisites](#prerequisites)
- [Built with](#built-with)
- [Authors](#authors)

## Getting Started 🚀

These instructions will guide to test the project on your own or you local machine

### Prerequisites

If you wish to test the code online : [to be completed]

Make sure to have Python 3x installed on your computer
Run the following in your command prompt

```
python
```

I used **Python 3.8.0** to built this program, Python 3.0 to 3.8 will work.

### Installing

A step by step that tell you how to get my code up and running on your local machine :

- Clone my repo

```
git clone https://github.com/Mcflan-7/P7_prometheus.git
```

- Set up your virtual environnement (using venv for this example, any will do)

```
python -m venv venv
```

- Activate your virtual environement with

  ```
  Windows: source venv/Scripts/activate
  MacOS: source venv/bin/activate
  ```

- Install the requirement with

```
pip install -r requirements.txt
```

- CD to the app directory

```
cd prometheus
```

- Export the app and run flask

```
export FLASK_APP=index.py
python -m flask run

```

## Built With 🛠

- [Python](<[https://www.python.org/](https://www.python.org/)>) - The programming language that lets you work quicklyand integrate systems more effectively
- [Flask](<[https://flask.palletsprojects.com/en/1.1.x/(https://flask.palletsprojects.com/en/1.1.x/)>) - Web development one drop at a time
- [VSCODE](<[https://code.visualstudio.com/](https://code.visualstudio.com/)>) - The code editing redefined

## Authors 💻

- **Gaëtan GROND** - _Initial work_ - [GITHUB](<[https://github.com/Mcflan-7](https://github.com/Mcflan-7)>)
