try:
    text = input('Введите что-нибудь --> ')
except EOFError:
    print('Ну зачем вы сделали мне EOF?') # Нажмите ctrl-d
except KeyboardInterrupt:
    print('Вы отменили операцию.') # Нажмите ctrl-c
else:
    print('Вы ввели {0}'.format(text))
