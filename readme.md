# Парсер регионов России


Этот проект представляет собой простой парсер для извлечения информации о регионах России. Парсер способен собирать данные, такие как название региона, его административный центр, население и другие важные характеристики.

## Предварительные требования

- [Git](https://git-scm.com)
- [Python 3.6 или выше](https://www.python.org/downloads/)

### Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/zoDLer1/region-parser
   cd region-parser
2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
### Использование

1. Запустите приложение:

    ```bash
    python main.py
    ```
2. Подождите выполнение скрипта
3. В директории проекта появятся 2 файла с информацией `flags.docx` и `info.docx` *(по умолчанию)*

### Конфигурация
- В файле configuration.py вы можете настроить параметры парсера, такие как, путь к файлу для сохранения данных, стили отображения данных и другие настройки.
### Сторонние ресурсы
- Данные берустся из - https://geo.koltyrin.ru/

