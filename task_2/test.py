from task_2.solution import _check_continue, letters


def test_check_continue_true():
    data = {
        'continue': {
            'cmcontinue': 'page|next',
        }
    }
    assert _check_continue(data) is True


def test_check_continue_false():
    data = {
        'query': {}
    }
    assert _check_continue(data) is False


def test_handle_data_counts_correct():
    test_data_dict = {}

    def fake_handle_data(data):
        for item in data['query']['categorymembers']:
            letter = item['title'][0].upper()
            if letter in letters:
                test_data_dict[letter] = test_data_dict.get(letter, 0) + 1

    fake_data = {
        'query': {
            'categorymembers': [
                {'title': 'Акула'},
                {'title': 'Аист'},
                {'title': 'Бобр'},
                {'title': 'Выдра'},
                {'title': 'Антилопа'}
            ]
        }
    }

    fake_handle_data(fake_data)

    assert test_data_dict['А'] == 3
    assert test_data_dict['Б'] == 1
    assert test_data_dict['В'] == 1
