def send_email (message, recipient, *, sender = "university.help@gmail.com"):
    valid_domains = (".com", ".ru", ".net")
    if "@" not in recipient or "@" not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif not (sender.endswith(valid_domains) and recipient.endswith(valid_domains)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
