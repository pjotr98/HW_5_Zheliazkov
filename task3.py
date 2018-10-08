import requests

url = "https://dummyimage.com/600x400/000/fff"
response = requests.get(url)
if response.status_code == 200:
    with open("/Users/oles/PycharmProjects/HW_5_Zheliazkov/saved_file_for_task3.jpg", 'wb') as f:
        f.write(response.content)