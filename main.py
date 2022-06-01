import os
import database
import requests
import json
import sys
import random

if __name__ == '__main__':
    print("Program started!")
    database_name = os.environ['database']
    username = os.environ['username']
    if username == 'expli':
        username = os.environ['database']
    password = os.environ['password']
    address = os.environ['address']
    print("Env finished!")
    # pixiv_name = os.environ['pixiv_username']
    # pixiv_pass = os.environ['pixiv_password']
    # refresh = os.environ['pixiv_refresh']
    db = database.Database(database_name, username, address, password)
    print("Db connected!")
