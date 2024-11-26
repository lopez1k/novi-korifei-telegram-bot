from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from utils.requestsbd import exists_user, create_user, create_ticket, insert_feedback, insert_suggestion
from utils.keyboards.inline_builder import spectacls, soc_merezhi
from utils.keyboards.reply_kb import main_kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime
from utils.otherfunc import greet
from data.config import LOG_CHAT




uohandle = Router()


class Suggestion(StatesGroup):
    namevistava = State()

class Feedback(StatesGroup):
    feedback = State()

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
    await msg.answer_photo(photo = "https://telegra.ph/file/71f02301ec9deaf902106.jpg", caption= f"<i>Найближчі вистави станом на </i><b>{now_time}</b>", reply_markup = kb)


@uohandle.message(F.text.lower() == "запропонувати виставу") 
async def suggest_vistavu(msg: Message, state: FSMContext):
    await state.set_state(Suggestion.namevistava)
    await msg.reply("Введіть назву вистави, яку хотіли б бачити у нашому виконанні.")



@uohandle.message(Suggestion.namevistava)
async def state_suggestion(msg: Message, state: FSMContext, bot: Bot): 
    await state.clear()
    await insert_suggestion(msg.from_user.id, msg.text)
    await msg.answer(f"Ваша пропозиція буде врахована. <b>{greet()}</b>")
    await bot.send_message(chat_id=LOG_CHAT, text = f"Надійшла нова пропозиція щодо вистави:\n<code>{msg.text}</code>", message_thread_id=1291)



@uohandle.message(F.text.lower() == "залишити запитання")
async def profile(msg: Message, state: FSMContext):
    await msg.reply("Введіть опис проблеми")
    await state.set_state(RegForm.title)
    



@uohandle.message(RegForm.title)
async def reg_ticket(msg: Message, state: FSMContext):
    await create_ticket(msg.from_user.id, msg.text)
    await state.clear()
    await msg.reply(f"Ви успішно створили запитання. Очікуйте відповіді❤️. {greet()}", reply_markup = main_kb)



@uohandle.callback_query(F.data.startswith("feedback_"))
async def feedback_callback(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer("Відправте відгук:")
    await state.set_state(Feedback.feedback)
    await state.update_data(name = call.data[9:])

@uohandle.message(Feedback.feedback)
async def state_handler_feedback(msg: Message, state: FSMContext):
    data = await state.get_data()
    name_spect = data['name']
    await state.clear()
    await insert_feedback(msg.from_user.id, msg.text, name_spect)
    await msg.answer_sticker(sticker = "CAACAgQAAxUAAWY0zUlxc_wAAenM72RFn662X3hehQACIh0AAlF9AAFQbzZh3VBYo6U0BA")
    await msg.reply("Дякуємо вам за відгук. Завдяки вам ми стаємо кращими.❤️", reply_markup = main_kb)
    print(name_spect, msg.text)

    