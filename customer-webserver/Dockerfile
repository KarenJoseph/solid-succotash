FROM python

RUN pip install flask flask_restful kafka-python bson requests

COPY api.py /api.py

EXPOSE 5000

ENTRYPOINT python /api.py
