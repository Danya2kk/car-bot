from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

applications = []


class Register(StatesGroup):
    name = State()
    surname = State()
    car = State()
    cost = State()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, я бот который делает заявку машин и может повторять сообщения! Нажмите кнопку чтобы "
                         "сделать заявку!", reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Здесь должна была быть helpa')


@router.message(Command('show'))
@router.message(F.text == 'Показать список заявок')
async def show_applications(message: Message):
    if applications:
        i = 1
        await message.answer('Список заявок:')
        for app in applications:
            await message.answer(f'Заявка {i}:\n'
                                 f'Имя: {app["name"]}\nФамилия: {app["surname"]}\n'
                                 f'Марка машины: {app["car"]}\nСумма: {app["cost"]}')
            i += 1
    else:
        await message.answer('Заявок нет!')


@router.message(Command('register'))
@router.message(F.text == 'Добавить заявку')
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя', reply_markup=ReplyKeyboardRemove())


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.surname)
    await message.answer('Введите вашу фамилию')


@router.message(Register.surname)
async def register_surname(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await state.set_state(Register.car)
    await message.answer('Выберите желаемую марку машины', reply_markup=kb.car)


@router.message(Register.car)
async def register_car(message: Message, state: FSMContext):
    await state.update_data(car=message.text)
    await state.set_state(Register.cost)
    await message.answer('Введите стоимость(в $) за которую хотели бы приобрести машину', reply_markup=ReplyKeyboardRemove())


@router.message(Register.cost)
async def register_cost(message: Message, state: FSMContext):
    await state.update_data(cost=message.text)
    data = await state.get_data()
    await message.answer("Ваша заявку успешно создана!")
    await message.answer(f"Ваше имя: {data['name']}\nВаша фамилия: {data['surname']}\n"
                         f"Желаемая машина: {data['car']}\nСумма: {data['cost']}$", reply_markup=kb.main)
    applications.append(data)

    await state.clear()


@router.message(F.text)
async def echo(message: Message):
    await message.answer(message.text)

