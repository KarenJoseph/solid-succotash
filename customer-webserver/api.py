from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests
import json
import kafka
import bson

app = Flask(__name__)
api = Api(app)

class AllBuys (Resource):
   
    def get (self):
        data = requests.get('http://customer-management:5001/allBuys')
        return json.loads(data.content)

    pass

class BuyItem (Resource):

    def post (self):
        json_data = request.get_json(force=True)
        #json_data = { "username": "John", "userid": "83_njxcs", "price": "25.4", "timestamp": "17821078927389" }
        producer = kafka.KafkaProducer(bootstrap_servers=['kafka:9092'],
                                   api_version=(0, 10, 1),
                                   value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        
        producer.send("topic1",json_data)
    
        return 200
   
    pass

api.add_resource(AllBuys, '/allBuys')
api.add_resource(BuyItem, '/buy')

app.run(host='0.0.0.0')
