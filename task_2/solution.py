import requests
import csv


url = 'https://ru.wikipedia.org/w/api.php'

params = {
    'action': 'query',
    'format': 'json',
    'list': 'categorymembers',
    'cmtitle': 'Категория:Животные_по_алфавиту',
    'cmlimit': 500
}

letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
current_letter = letters[0]
data_dict = {}


def _check_continue(data):
    if 'continue' in data:
        params['cmcontinue'] = data['continue']['cmcontinue']
        return True
    return False


def _handle_data(data):
    for item in data['query']['categorymembers']:
        letter = item['title'][0].upper()
        if letter in letters:
            data_dict[letter] = data_dict.get(letter, 0) + 1


def _create_csv():
    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows([[k, v] for k, v in data_dict.items()])


def _start_search():
    while True:
        response = requests.get(url, params=params)
        data = response.json()
        _handle_data(data)
        if not _check_continue(data):
            break
    _create_csv()


if __name__ == '__main__':
    _start_search()
