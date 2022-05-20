import requests

TOKEN = '5301819648:AAECf_zuuugWd0I_6GlDrjimxVv4Yt2ZqN0'
CHAT_ID = -658723714

URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text='


def send_message(massiv: dict) -> None:
    keys = list(massiv.keys())
    d = {'porter': 'Портер: Нет',
         'movers': "Грузчики: Нет",
         'furniture_assembly': 'Разборка/сборка: Нет',
         'garbage_removal': 'Вызоз мусора: Нет'}
    text = f'Имя: {massiv["name"]}\n\nНомер: {massiv["phone_number"]}\n\n'
    for i in d.keys():
        if i in keys:
            text += f"{d[i].replace('Нет', 'Да')}\n\n"
        else:
            text += f'{d[i]}\n\n'
    text += f'Описание: {massiv["description"]}'
    requests.post(URL + text)
