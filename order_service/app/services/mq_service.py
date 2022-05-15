import pika
import json


def exchange_services(order):

    credentials = pika.PlainCredentials('admin', 'admin')
    parameters = pika.ConnectionParameters('rabbitmq',
                                           5672,
                                           '/',
                                           credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(
        queue='orders', durable=True)

    body = json.dumps(order, indent=4,
                      sort_keys=True, default=str)

    channel.basic_publish(exchange='', routing_key='orders', body=body,
                          properties=pika.BasicProperties(
                              delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                          ))
    # print(f" [x] Sent {body}")
    connection.close()
