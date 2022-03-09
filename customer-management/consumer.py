import kafka
import json
import pymongo

def insertDB(json_data):
    myclient = pymongo.MongoClient("mongodb://root:example@mongo:27017/")

    mydb = myclient["webstore"]
    mycol = mydb["orders"]

    x = mycol.insert_one(json_data)


consumer = kafka.KafkaConsumer("topic1",
                               group_id=None,
                               auto_offset_reset='earliest',
                               bootstrap_servers=['kafka:9092'],
                               value_deserializer=lambda m: json.loads(m.decode('ascii')))
for msg in consumer:
  insertDB(msg.value)
  print(msg.value)
