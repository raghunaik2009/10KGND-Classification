# Description
This project, is a Machine Learning based flask application aims to predict the classes of a german language by inputing the text. 
# project files
preprocess : Class contains the contains the functions (utils) used to preprocess and clean the text
mlmodel: Class for Machine learning model loading and prediction 
Notebook: NLP Assignment 10KGNAD contains all training and data wrangling, visulization details
# How to use it!
use python 3.xx
i'm using python 3.8.8 version
# Running from app.py file
Start flask application by running app.py file from VS code or any other tool or command line
# Open below link in browser
using http://127.0.0.1:5000/


# Running using docker (Must install docker desktop https://docs.docker.com/desktop/)
 # 1. Building docker image
    docker build -t <image_name>:tag .
    E.g. docker build -t germantext-classification:v1 .
 # 2. running docker image
    docker run -p 5000:5000 -it <image_name>:tag
    E.g. docker run -p 5000:5000 -it germantext-classification:v11
 # Open below link in browser
    using http://localhost:5000/

http://127.0.0.1:5000/
## Perspectives
1. Train deep learning models (BERT, LSTM) and enhance model performance
2. add language detector to the pipeline to only accept german language
