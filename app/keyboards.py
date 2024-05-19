from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить заявку')],
        [KeyboardButton(text='Показать список заявок')]
    ],
    resize_keyboard=True
)


car = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='BMW'),
            KeyboardButton(text='Mercedes'),
            KeyboardButton(text='Audi')
        ],

        [
            KeyboardButton(text='Toyota'),
            KeyboardButton(text='Kia'),
            KeyboardButton(text='Renault')
        ]



    ],
    resize_keyboard=True
)

