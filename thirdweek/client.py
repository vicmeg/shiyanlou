#!/usr/bin/env python3

import requests

user_info = {'name': 'shixiaolou','password': 'abc123','hobbies': ['code','swim']}
r = requests.post("http://127.0.0.1:5000/register",data=user_info)
print(r.txt)
