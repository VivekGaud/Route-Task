from celeryTask import celeryConsumer
import requests,sqlite3
import pika,json

result = celeryConsumer.delay()
# print(result.get())
