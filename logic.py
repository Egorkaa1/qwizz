# Задание 2 - Импортируй нужные классы
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    # Задание 1 - Создай геттер для получения текста вопроса
    @property
    def get_text(self):
        return self.__text


    
        # Задание 3 - Создай метод для генерации Inline клавиатуры
    def gen_markup(self):
        markup = InlineKeyboardMarkup
        markup.row_width = len(self.options)

        for i, option in enumerate(markup.row_width):
            if i[answer_id]=answer_id: 
                markup.add(InlineKeyboardButton(option, callback_data='correct'))
            else:
                markup.add(InlineKeyboardButton(option, callback_data='wrong'))
        return markup

# Задание 4 - заполни список своими вопросами
quiz_questions = [
    Question("Что котики делают, когда никто их не видит?", 1, "Спят", "Пишут мемы"),
    Question("Как котики выражают свою любовь?", 0, "Громким мурлыканием", "Отправляют фото на Instagram", "Гавкают"),
    Question("Какие книги котики любят читать?", 3, "Обретение вашего внутреннего урр-мирения", "Тайм-менеджмент или как выделить 18 часов в день для сна", "101 способ уснуть на 5 минут раньше, чем хозяин", "Пособие по управлению людьми")
]
