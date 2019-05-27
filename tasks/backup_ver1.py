import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список
source = ['"C:\\My Documents"', 'C:\\Code']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'С:\\Backup'  # Подставьте тот путь, который вы будете использовать
# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
# Запускаем создание резервной копии

print(zip_command)
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')

#todo doesn't work for now:
# Пользователи Windows могут установить её
# со страницы проекта GnuWin32 и добавить “C:\Program Files\GnuWin32\bin” к си-
# стемной переменной окружения PATH, аналогично тому, как мы это делали для са-
# мой команды “python”. Обратите внимание, что для этого подойдёт любая команда
# архивации, если у неё есть интерфейс командной строки, чтобы ей можно было
# передавать аргументы из нашего сценария.