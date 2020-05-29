# Data Engineering

Data Engineering is the connection between the data behind a program and the frontend/backend. In this situation, the data engineering code connected the machine learning model to the frontend/backend to allow user input to run through the model and output the prediction in a format that can be used for front end output.

## Contents
*__init__.py* - Contains the file that creates the app and ties in all the modules found within the data_engineering directory.

*routes* - Contains the routes that connect the machine learning model to the frontend/backend:

    *home_routes.py* : Sets home page and ensures app is working    correctly.

    *predict_routes.py* : Takes in user input front front end, converts it to a useable form, runs it through a pretrained prediction model, and outputs the prediction in json format using a /predict endpoint. 


**Contributors:**
Daniel Benson