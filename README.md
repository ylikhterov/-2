# Программа "my-todo" занимается хранением списка дел.

# Требования:
# - Команда my-todo add 'title' 'description' добавляет одно "дело" в список дел
# - Команда my-todo show 5 показывает нужно количество самых свежих дел
# - Команда my-todo done 1 отмечает какое-то дело как сделанное и удаляет его из списка
# - Команда my-todo find 'text' ищет дела по заголовку или описанию

# Технические требования:
# - Хранение дел мы организуем в файле todo.json в текущей директории
# - Парсинг команд и аргументов командой строки реализуем через argparse

# Пример:

# Можно запускать с помощью poetry run из директории my-todo:
cd poetry/
poetry run my-todo todo.py add 'Buy milk' 'Go to the store and buy some milk'
poetry run my-todo todo.py add 'Do laundry' 'Wash the clothes and hang them to dry'
poetry run my-todo todo.py show
poetry run my-todo todo.py done 1
poetry run my-todo todo.py find 'laundry'

# Можно установить пакет в систему и использовать программу в консоли
# Для этого переходим в директорию "my-todo", создаём новое вирт. окружение и активируем его:
cd my-todo/
python3 -m venv env
. env/bin/activate

# Запускаем установку пакета в вирт. окружение
python3 setup.py install

# Можем использовать программу в консоли
my-todo todo.py add 'Buy milk' 'Go to the store and buy some milk'
my-todo todo.py add 'Do laundry' 'Wash the clothes and hang them to dry'
my-todo todo.py show
my-todo todo.py done 1
my-todo todo.py find 'laundry'
