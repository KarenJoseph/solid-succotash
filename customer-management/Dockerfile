FROM python

RUN pip install flask flask_restful pymongo requests kafka-python

COPY api.py /api.py
COPY consumer.py /consumer.py
COPY start.sh /start.sh

EXPOSE 5001

ENTRYPOINT bash start.sh
