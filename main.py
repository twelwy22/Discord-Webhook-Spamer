import requests

def discord_webhook_spammer():
    message = input("Введите текст сообщения для спама: ")
    webhook_url = input("Введите URL Webhook: ")
    num_messages = int(input("Введите количество сообщений для отправки: "))
    
    for i in range(num_messages):
        response = requests.post(webhook_url, json={"content": message})
        if response.status_code == 204:
            print(f"Сообщение {i+1} успешно отправлено.")
        else:
            print(f"Ошибка при отправке сообщения {i+1}: {response.status_code}")

if __name__ == "__main__":
    discord_webhook_spammer()
