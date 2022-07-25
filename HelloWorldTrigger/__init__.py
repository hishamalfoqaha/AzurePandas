import logging
import json
import azure.functions as func
import sys
import os
import pandas


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    mydataset = {'cars': ["BMW", "Volvo", "Ford"], 'passings': [3, 7, 2] }

    myvar = pandas.DataFrame(mydataset)

     #Retreive Method type, it tells us what kind of request we're receiving
    method_type = req.method

    if method_type == "GET":
        name = req.params.get('name') #getting the name argument from a get request from req "func.HttpRequest" :- we check if this request contains a 'name' argument in it
    
    elif method_type == "POST":
        try:
            req_body = req.get_json()  #check if the request contains json "if we recieve a json", if this code execute without any errors, we go to the else statement, if there is any exceptions in this line we go to except ValueError:
        except ValueError:
            name = None
        else:
            name = req_body.get('name')  #get the name value

    if name:  #we check if the name was found
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.", status_code=200)
    else:
        return func.HttpResponse(
             "Pass a name in the query string (GET request) or a JSON body (POST request)",
             status_code=400
        )