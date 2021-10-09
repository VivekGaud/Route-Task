from celery import Celery
import pika,json,sqlite3
from time import sleep

# celery -A celeryTask worker -l info -P eventlet  

# broker_url = 'amqp://vivek:vivek101@localhost:5672/myvhost'
# app = Celery('tasks', backend='rpc://', broker=broker_url)

app = Celery('tasks', backend='rpc://', broker='pyamqp://')
# app = Celery('tasks', broker='pyamqp://guest@localhost//')



# Celery which access rabbitMQ queue 
@app.task
def celeryConsumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='queueName')


    channel.basic_consume(queue='queueName', on_message_callback=callback, auto_ack=True)
    print("Started Consuming...")
    channel.start_consuming()

# Callback function which checks the queue and change status of item
def callback(ch, method, properties, body):
    print("Message Received ...")
    data = json.loads(body)
    print('Processing Data: {0}'.format(data['item']))
    sleep(10)
    conn = sqlite3.connect('../route_task/routeTask/db.sqlite3')
    conn.execute('''Update rm55_items SET status = "completed" where item='{0}';'''.format(data['item']))
    conn.commit()
    conn.close()
    print('{0} Status Changed To Completed'.format(data['item']))


