import text
from typing import Tuple

def menu() -> int:
    print(text.menu[0])
    for i, item in enumerate(text.menu[1:], 1):
        print(f"    {i}. {item}")
    while True:
        select = input(text.menu_select)
        if select.isdigit() and 0 < int(select) < len(text.menu):
            return int(select)
        print(text.input_error())

def input_contact() -> Tuple[str, str, str]:
    return tuple([input(txt) for txt in text.input_contact])

def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')

def show_contacts(book: list[tuple[str]], message: str):
    if book:
        max_len = [len(max([field[i] for field in book], key=len)) for i in range(1, 4)]
        print('\n' + '=' * (sum(max_len) + 8))
        for cnt in book:
            print(f'{cnt[0] :>3} {cnt[1]: <{max_len[0]}} {cnt[2]:<{max_len[1]}} {cnt[3]:<{max_len[2]}}')
        print('=' * (sum(max_len) + 8) + '\n')
    else:
        print_message(message)