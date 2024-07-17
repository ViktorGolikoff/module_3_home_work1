def send_email(message, recipient, sender="university.help@gmail.com"):
    if not (("@" in sender and "@" in recipient) or (".com" in sender or ".ru" in sender or ".net" in sender) or (
            ".com" in recipient or ".ru" in recipient or ".net" in recipient)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return False
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return False
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        return False
    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        return True




send_email('Это сообщение для проверки связи', 'pravgolvik@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


