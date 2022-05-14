import pika
import json


def exchange_services(order):

    credentials = pika.PlainCredentials('admin', 'admin')
    parameters = pika.ConnectionParameters('localhost',
                                           5672,
                                           '/',
                                           credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.exchange_declare(exchange='orders', exchange_type='fanout')

    body = json.dumps(order, indent=4,
                      sort_keys=True, default=str)

    channel.basic_publish(exchange='orders', routing_key='', body=body)
    print(f" [x] Sent {body}")
    connection.close()
