menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать все контакты',
             'Создать новый контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

menu_select = 'Выберите пункт меню: '

def input_error ():
    return f'Некорректный ввод. Выберите пункт от 1 до {len(menu)-1}'

def add_successful (name: str) -> str:
    return f'Контакт {name} успешно добавлен! Сохраните файл.'

input_contact = ['Введите имя контакта: ', 'Введите телефон: ', 'Введите комментарий к контакту: ']

input_change_contact = ['Введите новое имя: ', 'Введите новый телефон: ', 'Введите новый комментарий к контакту: ']

load_successful = 'Файл успешно загружен.'

empty_file = 'Телефонная книга пуста или файл не открыт'

save_successful = 'Файл успешно сохранен'

not_found = 'Контакт не найден'

input_index_delete = 'Введите id контакта для удаления: '

delete_successful = 'Контакт успешно удален.'

search_contact = 'Введите контакт, который вы ищите: '

input_index = 'Введите id изменяемого контакта (если не хотите вносить изменения в какие-то пункты нажмите Enter): '

edit_successful = 'Контакт успешно изменен.'

invalid_index = 'Введен неверный индекс контакта'

delete_error = 'Ошибка удаления контакта. Проверьте введенный номер.'

message_exit = 'До новых встреч!'