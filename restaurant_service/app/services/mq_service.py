import pika
from app.controllers import order_controller
import json


def amqp_connect_and_consume():
    credentials = pika.PlainCredentials('admin', 'admin')
    parameters = pika.ConnectionParameters('rabbitmq',
                                           5672,
                                           '/',
                                           credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(
        queue='orders', durable=True)

    channel.basic_qos(prefetch_count=1)

    print(' [*] Waiting for orders. To exit press CTRL+C')

    def callback(ch, method, properties, body):

        order = json.loads(body)

        print(order)

        print(f" [x] Received {order}")
        order_controller.accept_order(order)
        print(" [x] Accepted!")
        order_controller.process_order(order)
        print(" [x] Delivered!")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue='orders', on_message_callback=callback)

    channel.start_consuming()
