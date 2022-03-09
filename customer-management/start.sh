#!/bin/bash

# start api server
python /api.py & 

# start kafka consumer
python /consumer.py
