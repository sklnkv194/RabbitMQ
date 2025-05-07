import pika

def send_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='user_messages')
    
    while True:
        message = input("Введите сообщение (или 'exit' для выхода): ")
        if message.lower() == 'exit':
            break
            
        channel.basic_publish(
            exchange='',
            routing_key='user_messages',
            body=message
        )
        print(f"Отправлено сообщение: '{message}'")
    
    connection.close()
    print("Программа завершена.")

if __name__ == "__main__":
    send_message()