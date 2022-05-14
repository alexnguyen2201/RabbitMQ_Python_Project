import pika
import json

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       '/',
                                       credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='orders', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='orders', queue=queue_name)

print(' [*] Waiting for orders. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % json.loads(body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
