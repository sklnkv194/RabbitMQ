import pika

def receive_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='user_messages')
    
    def callback(ch, method, properties, body):
        print(f"Получено сообщение: '{body.decode()}'")
    
    channel.basic_consume(
        queue='user_messages',
        on_message_callback=callback,
        auto_ack=True
    )
    
    print('Ожидание сообщений. Для выхода нажмите CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    try:
        receive_message()
    except KeyboardInterrupt:
        print("\nПолучатель остановлен.")