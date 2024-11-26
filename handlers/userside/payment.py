from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, LabeledPrice, PreCheckoutQuery, Message, FSInputFile, ReactionTypeEmoji
from utils.requestsbd import get_cur_spect_name, get_cur_spect_price, getiser, create_ticketss
from utils.keyboards.inline_builder import buy_kb, aceppt_kb
import os
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class DonateCheck(StatesGroup):
    screenshoot = State()
    accept = State()


payment_rt = Router()


@payment_rt.callback_query(F.data.startswith("buy_"))
async def buy_handleer(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.answer()
    spect = await get_cur_spect_name(call.data[4:])
    price = LabeledPrice(label= f"{spect[1]}", amount= spect[5]*100)
    await call.message.answer("Відправте ваш донат на цю банку: https://send.monobank.ua/jar/5Z4VqdvCio або 5375 4112 1868 7924 (номер карти банки). Після успішно переказу зробіть скріншот операції та відправте його мені😊")
    #await bot.send_invoice(call.from_user.id, 
    #                      title = "Квиток",
    #                      description = f'Покупка квитка на виставу {spect[1]}',
    #                      provider_token=PAYMENT_TOKEN,
    #                        currency="USD",
    #                       prices=[price],
    #                       start_parameter=f'buy_ticket_spect_{spect[0]}',
    #                       payload="test-invoice-payload",
    #                       reply_to_message_id=call.message.message_id
    #                       )
    await state.set_state(DonateCheck.screenshoot)
    await state.update_data(spect = spect[1], spectid = spect[0])

@payment_rt.message(DonateCheck.screenshoot, F.photo)
async def photos(msg: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    kb = await aceppt_kb(data['spectid'], msg.from_user.id)
    await bot.send_photo(chat_id = -1001952618666, photo = msg.photo[-1].file_id, caption = f"{msg.from_user.full_name} зробив запит на підтвердження квитка. Вистава: {data['spect']}", message_thread_id=1291, reply_markup = kb)
    await state.set_state(DonateCheck.accept)
    await msg.answer("Ви успішно створили заявку. Почекайте 5 хвилин, поки заявка обробиться модераторами...")

@payment_rt.callback_query(F.data.startswith("acct_"))
async def check_ticket_moder(call: CallbackQuery, state: FSMContext, bot: Bot):
    user = await getiser(call.data[5:])
    await create_ticketss(call.data[5:], user[1], call.from_user.id)
    await bot.send_photo(chat_id=user[1], photo=FSInputFile(path=f"{user[1]}.png"), caption="Чекаємо вас на виставі!🎭🎟Ваш е-квиток. Не загубіть його.😆")
    os.remove(f"./{user[1]}.png")
    await call.message.edit_reply_markup(reply_markup=None)
    react = ReactionTypeEmoji(emoji="👍")
    await call.message.react([react])

@payment_rt.callback_query(F.data.startswith("dect_"))
async def check_ticket_moder(call: CallbackQuery, state: FSMContext, bot: Bot):
    user = await getiser(call.data[5:])
    await bot.send_message(chat_id=user[1], text =  "Ваш запит на покупку квитка відхилено.")
    await call.message.edit_reply_markup(reply_markup=None)
    react = ReactionTypeEmoji(emoji="👎")
    await call.message.react([react])

@payment_rt.pre_checkout_query()
async def pre_checkout_query(pre_checkout_q: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@payment_rt.message(F.successful_payment)
async def yes(msg: Message):
    await msg.answer("✅Оплата пройшла успішно!✅")
    await get_cur_spect_price(msg.successful_payment.total_amount // 100, msg.from_user.id)
    await msg.answer_photo(photo=FSInputFile(path=f"{msg.from_user.id}.png"), caption="Чекаємо вас на виставі!🎭🎟Ваш е-квиток. Не загубіть його.😆")
    os.remove(f"E:/lssp_bot/{msg.from_user.id}.png")