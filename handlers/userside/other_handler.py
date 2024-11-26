from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from utils.requestsbd import exists_user, create_user, create_ticket
from utils.keyboards.inline_builder import spectacls, soc_merezhi
from utils.keyboards.reply_kb import main_kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime


uohandle = Router()

class RegForm(StatesGroup):
    title = State()


@uohandle.message(F.contact)
async def start_cmd_user(msg: Message):
    if await exists_user(msg.from_user.id) is None:
        await create_user(msg.from_user.id, msg.from_user.full_name, msg.contact.phone_number)
        await msg.reply("Ви успішно зареєструвались", reply_markup = main_kb)


@uohandle.message(F.text.lower() == "про нас")
async def aboutus(msg: Message):
    await msg.reply('''<b>Наша команда має чітку місію — <u>популяризувати театр та українську культуру серед молоді</u>. Ми віримо, що культурні події, такі як театральні вистави, мають бути доступними для кожного, незалежно від їхнього статусу чи можливостей.

Ми відчуваємо відповідальність перед людьми з обмеженими можливостями, включаючи тих, хто зіткнувся з фінансовими труднощами. Для нас важливо, щоб кожен міг насолоджуватися мистецтвом без перешкод.

Також, ми звертаємо увагу на <u>дітей-сиріт.</u> Наше серце просто розривається, думаючи про те, що ці діти можуть пропустити шанс відчути красу та натхнення, яке може дати театральна вистава. Ми віримо, що мистецтво може стати важливою складовою виховання та розвитку кожної дитини, незалежно від її життєвої ситуації.

Ці напрямки в нашій роботі відображають наше прагнення зробити світ кращим місцем для всіх. <i>Ми горді тим, що можемо допомагати іншим та сприяти культурному збагаченню нашого суспільства через театральне мистецтво.</i>
</b>''', reply_markup = soc_merezhi)
    

@uohandle.message(F.text.lower() == "найближчі вистави")
async def closest_spectacls(msg: Message):
    kb = await spectacls()
    time = datetime.now()
    now_time = time.strftime("%d-%m-%y %H:%M:%S")
    await msg.reply(f"<i>Найближчі вистави станом на </i><b>{now_time}</b>", reply_markup = kb)

@uohandle.message(F.text.lower() == "залишити запитання")
async def profile(msg: Message, state: FSMContext):
    await msg.reply("Введіть опис проблеми")
    await state.set_state(RegForm.title)




@uohandle.message(RegForm.title)
async def reg_ticket(msg: Message, state: FSMContext):
    await create_ticket(msg.from_user.id, msg.text)
    await state.clear()
    await msg.reply("Ви успішно створили запитання. Очікуйте відповіді❤️", reply_markup = main_kb)
