from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import MESHCHANIN, PEASANT_GIRL, PEASANT_MALE

# Авдаловка въ московской книгѣ 1916 г. — ЦГА Москвы 2126-2-93 (Знаменская ц. въ Переяславской слободѣ),
# найдено по OCR Яндексъ.Архива, прочитано по оригиналу 07.11.2026; reviewed=False.
# Поручители: первые двое — со стороны жениха, третій — невѣсты.

other_marriages_1916_moscow_znamenskaya = marriage_records(
    "ЦГА Москвы", "2126", "2", "93", "Москва", "Знаменская",
    1916,
    *marriage_month(Month.OCTOBER,
        marriage(83, 9,
                 groom=person("Ѳеодоръ", "Андреевъ", last_name_orig="Шумаковъ", status=MESHCHANIN, comment="мѣщанинъ г. Торжка"),
                 groom_marriage_num=1, groom_age=25,
                 bride=person("Евгенія", "Михайлова", last_name_orig="Калинкина", status=PEASANT_GIRL, residence="Авдалово"),
                 bride_age=25,
                 witness1=person("Василій", "Егоровъ", last_name_orig="Мельниковъ", status=PEASANT_MALE, comment="Рязанской губ., Михайловскаго у., дер. Верхней Турловки"),
                 witness2=person("Алексѣй", "Арсеньевъ", last_name_orig="Деменскій", status=PEASANT_MALE, comment="Старицкаго у., дер. Демина; фамилія читается неувѣренно"),
                 witness3=person("Иванъ", "Евѳимовъ", last_name_orig="Желтовъ", status=PEASANT_MALE, comment="Владимірской губ., Гороховецкаго у., дер. Черненкова"),
                 comment="Яндексъ.Архивъ 2126-2-93, сканъ 167; вѣнчалъ свящ. Сергій Глаголевскій. Невѣста — та Евгенія "
                         "Михайловна Калинкина, что въ 1906 г. родила дочь Анну (other_births_1906)?"),
    ),
    reviewed=False,
)
