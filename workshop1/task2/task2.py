from http import client

# создаем соединение
connection = client.HTTPConnection("www.google.com")
connection.request("GET", "/")

# получаем ответ
response = connection.getresponse()

print("Статус: {} и описание: {}".format(response.status, response.reason))

# закрываем соединение
connection.close()
