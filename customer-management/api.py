from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
import json

def getItemsDB():
    json_data = requests.get('http://mongo-express:8081/db/webstore/expArr/orders?key=&value=&type=S&query=&projection=%20&sort[userid]=1')
    return json_data.content

app = Flask(__name__)
api = Api(app)

class AllBuys (Resource):
   
    def get (self):
        data = getItemsDB()
        return {"data": json.loads(data)}

    pass

api.add_resource(AllBuys, '/allBuys')

app.run(host='0.0.0.0', port=5001)


