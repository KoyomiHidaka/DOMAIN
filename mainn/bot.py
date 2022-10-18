from aiogram import Dispatcher, types, Bot
from entry import bot, dp
import surrogates

# LAND_OF_MEMORIES
dance_of_steel_I = "AgACAgIAAxkBAANkY03H63zwe5FEISQyV7cyLRYtZCIAAi7AMRvOMXFKe5G4uR5ZfqUBAAMCAAN4AAMqBA"
dance_of_steel_II = "AgACAgIAAxkBAANmY03H8Z3-zMLHdjPYUGfn2whH7AIAAi_AMRvOMXFKq3ygI_EYfqQBAAMCAAN4AAMqBA"
dance_of_steel_III = "AgACAgIAAxkBAANoY03H8xDhgtCDFxjhMNLBIiPdGk4AAjDAMRvOMXFK2eoccTUIuJsBAAMCAAN4AAMqBA"
dance_of_steel_IV = "AgACAgIAAxkBAANqY03H9tJuW11n2IJYy-dmKIhPhQwAAjHAMRvOMXFKvFOj70aQeakBAAMCAAN4AAMqBA"
dance_of_steel_V = "AgACAgIAAxkBAANsY03H-W-C0fw5SsVEtGZJ0PvfLr4AAjLAMRvOMXFKkSUbRWPl2eQBAAMCAAN4AAMqBA"


async def start(message: types.Message):
    await message.answer("Ohayo!")


async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


async def send_ph(message: types.Message):
    id_01 = "AgACAgIAAxkBAAMDY02zni8AAWvcuIYN0G9o_ECilh1wAAIEwDEbzjFxSr3ljpUzeFMTAQADAgADeQADKgQ"
    await message.answer_photo(id_01)


async def domains(message: types.Message):
    inll = types.InlineKeyboardMarkup()
    inll.add(types.InlineKeyboardButton("Июльские сады", callback_data="july"))
    inll.add(types.InlineKeyboardButton("Долина Воспоминаний", callback_data="memories"))
    await message.answer("В какое подземелье на этот раз?", reply_markup=inll)


async def keyboard_july_garden(callback_query: types.CallbackQuery):
    july = types.InlineKeyboardMarkup()
    july.add(types.InlineKeyboardButton("Пламя очищения I", callback_data="Flame_of_Clean_I"))
    july.add(types.InlineKeyboardButton("Пламя очищения II", callback_data="Flame_of_Clean_II"))
    july.add(types.InlineKeyboardButton("Пламя очищения III", callback_data="Flame_of_Clean_III"))
    july.add(types.InlineKeyboardButton("Пламя очищения IV", callback_data="Flame_of_Clean_IV"))
    july.add(types.InlineKeyboardButton("Пламя очищения V", callback_data="Flame_of_Clean_V"))
    july.add(types.InlineKeyboardButton("Пламя очищения VI", callback_data="Flame_of_Clean_VI"))
    back = surrogates.decode("	\u2728")
    await bot.send_message(callback_query.from_user.id, f"Куда отправляемся? {back}", reply_markup=july)


async def keyboard_field_of_memories(callback_query: types.CallbackQuery):
    memories = types.InlineKeyboardMarkup()
    memories.add(types.InlineKeyboardButton("Танец стали I", callback_data="Dance_of_steel_I"))
    memories.add(types.InlineKeyboardButton("Танец стали II", callback_data="Dance_of_steel_II"))
    memories.add(types.InlineKeyboardButton("Танец стали II", callback_data="Dance_of_steel_II"))
    memories.add(types.InlineKeyboardButton("Танец стали IV", callback_data="Dance_of_steel_IV"))
    memories.add(types.InlineKeyboardButton("Танец стали V", callback_data="Dance_of_steel_V"))
    back = surrogates.decode("	\u2728")
    await bot.send_message(callback_query.from_user.id, f"Куда отправляемся? {back}", reply_markup=memories)


async def flame_of_clean_i(callback_query: types.CallbackQuery):
    flame_of_clean_1 = "AgACAgIAAxkBAAMJY028FSChQ1apP54_ywlzL1soMvcAAhnAMRvOMXFKK8Sc18ziKzUBAAMCAAN4AAMqBA"
    await bot.send_photo(callback_query.from_user.id, flame_of_clean_1)



async def flame_of_clean_ii(callback_query: types.CallbackQuery):
    flame_of_clean_2 = "AgACAgIAAxkBAAMLY028H2Ta3YuM24rkX5pYNKB45TcAAhrAMRvOMXFKjR5Dykn5IjgBAAMCAAN4AAMqBA"
    await bot.send_photo(callback_query.from_user.id, flame_of_clean_2)



async def flame_of_clean_iii(callback_query: types.CallbackQuery):
    flame_of_clean_3 = "AgACAgIAAxkBAAMNY028J8trEfjFMYCABF6lPDlY9hcAAhvAMRvOMXFKUj073YpC5R8BAAMCAAN4AAMqBA"
    await bot.send_photo(callback_query.from_user.id, flame_of_clean_3)


async def flame_of_clean_iv(callback_query: types.CallbackQuery):
    flame_of_clean_4 = "AgACAgIAAxkBAAMPY028K1nhuRzLRJKtOJ5DiisnduMAAhzAMRvOMXFKYzHYtQu0OH8BAAMCAAN4AAMqBA"
    await bot.send_photo(callback_query.from_user.id, flame_of_clean_4)


async def flame_of_clean_v(callback_query: types.CallbackQuery):
    flame_of_clean_5 = "AgACAgIAAxkBAAMRY028Lmg6cO64T3BNafKz_6YYUD8AAh3AMRvOMXFKlpN1CV6sjB0BAAMCAAN4AAMqBA"
    await bot.send_photo(callback_query.from_user.id, flame_of_clean_5)


async def flame_of_clean_vi(callback_query: types.CallbackQuery):
    flame_of_clean_6 = "AgACAgIAAxkBAAMTY028MZoyyOOrru4WZRTsbULmaBMAAh7AMRvOMXFK6p6k9ZaCyx0BAAMCAAN4AAMqBA"
    await bot.send_photo(callback_query.from_user.id, flame_of_clean_6)


async def dance_of_steel_i(callback_query: types.CallbackQuery):
    dance_of_steel_1 = "AgACAgIAAxkBAANkY03H63zwe5FEISQyV7cyLRYtZCIAAi7AMRvOMXFKe5G4uR5ZfqUBAAMCAAN4AAMqBA"
    await bot.send_photo(callback_query.from_user.id, dance_of_steel_1)


async def dance_of_steel_ii(callback_query: types.CallbackQuery):
    dance_of_steel_2 = "AgACAgIAAxkBAANmY03H8Z3-zMLHdjPYUGfn2whH7AIAAi_AMRvOMXFKq3ygI_EYfqQBAAMCAAN4AAMqBA"
    await bot.send_photo(callback_query.from_user.id, dance_of_steel_2)


async def dance_of_steel_iii(callback_query: types.CallbackQuery):
    dance_of_steel_3 = "AgACAgIAAxkBAANoY03H8xDhgtCDFxjhMNLBIiPdGk4AAjDAMRvOMXFK2eoccTUIuJsBAAMCAAN4AAMqBA"
    await bot.send_photo(callback_query.from_user.id, dance_of_steel_3)


async def dance_of_steel_iv(callback_query: types.CallbackQuery):
    dance_of_steel_4 = "AgACAgIAAxkBAANqY03H9tJuW11n2IJYy-dmKIhPhQwAAjHAMRvOMXFKvFOj70aQeakBAAMCAAN4AAMqBA"
    await bot.send_photo(callback_query.from_user.id, dance_of_steel_4)


async def dance_of_steel_v(callback_query: types.CallbackQuery):
    dance_of_steel_5 = "AgACAgIAAxkBAANsY03H-W-C0fw5SsVEtGZJ0PvfLr4AAjLAMRvOMXFKkSUbRWPl2eQBAAMCAAN4AAMqBA"
    await bot.send_photo(callback_query.from_user.id, dance_of_steel_5)


def reg_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands="Start")
    dp.register_message_handler(get_file_id_p, content_types=['photo'])
    dp.register_message_handler(send_ph, text="Test")
    dp.register_message_handler(domains, commands="st")
    dp.register_callback_query_handler(keyboard_july_garden, text="july")
    dp.register_callback_query_handler(keyboard_field_of_memories, text="memories")
    dp.register_callback_query_handler(flame_of_clean_i, text="Flame_of_Clean_I")
    dp.register_callback_query_handler(flame_of_clean_ii, text="Flame_of_Clean_II")
    dp.register_callback_query_handler(flame_of_clean_iii, text="Flame_of_Clean_III")
    dp.register_callback_query_handler(flame_of_clean_iv, text="Flame_of_Clean_IV")
    dp.register_callback_query_handler(flame_of_clean_v, text="Flame_of_Clean_V")
    dp.register_callback_query_handler(flame_of_clean_vi, text="Flame_of_Clean_VI")
    dp.register_callback_query_handler(dance_of_steel_i, text="Dance_of_steel_I")
    dp.register_callback_query_handler(dance_of_steel_ii, text="Dance_of_steel_II")
    dp.register_callback_query_handler(dance_of_steel_iii, text="Dance_of_steel_III")
    dp.register_callback_query_handler(dance_of_steel_iv, text="Dance_of_steel_IV")
    dp.register_callback_query_handler(dance_of_steel_v, text="Dance_of_steel_V")
