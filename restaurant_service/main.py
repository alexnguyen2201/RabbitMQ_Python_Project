from app.services import mq_service


if __name__ == '__main__':
    mq_service.amqp_connect_and_consume()
