from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import KAZENNYJ_PEASANT_GIRL, PEASANT_MALE, SOLDIER_WIFE

# Журавкинки въ книгахъ чужихъ приходовъ 1900 г. — ЦГАРМ 57-7-45 (Аксёновка) и 57-7-51 (Анаево), найдено
# по OCR Яндексъ.Архива, прочитано по сканамъ 07.11.2026; reviewed=False.
# Поручители: первые двое — со стороны жениха, вторые — невѣсты.

other_marriages_1900_aksyonovka = marriage_records(
    "ЦГАРМ", "57", "7", "45", "Аксёновка", "",
    1900,
    *marriage_month(Month.JANUARY,
        marriage(6, 24,
                 groom=person("Ефимъ", "Прокопіевъ", last_name_orig="Учайкинъ", status=PEASANT_MALE, residence="Лопатино"),
                 groom_marriage_num=3, groom_age=35,
                 bride=person("Варвара", "Кирилова", last_name_orig="Шлепина", status=KAZENNYJ_PEASANT_GIRL, residence="Журавкино"),
                 bride_marriage_num=1,
                 witness1=person("Николай", last_name_orig="Анашкинъ", status=PEASANT_MALE, residence="Лопатино"),
                 witness2=person("Иванъ", last_name_orig="Почковъ", status=PEASANT_MALE, residence="Лопатино"),
                 witness3=person("Яковъ", "Семеновъ", last_name_orig="Князевъ"),
                 witness4=person("Сергій", "Максимовъ", last_name_orig="Журавлевъ"),
                 comment="Яндексъ.Архивъ 57-7-45, сканъ 59; лѣта невѣсты ушли въ корешокъ"),
    ),
    reviewed=False,
)

other_marriages_1900_anaevo = marriage_records(
    "ЦГАРМ", "57", "7", "51", "Анаево", "Покровская",
    1900,
    *marriage_month(Month.SEPTEMBER,
        marriage(13, 27,
                 groom=person("Захаръ", "Степановъ", last_name_orig="Бѣлкинъ", status=PEASANT_MALE, residence="Анаево"),
                 groom_marriage_num=2, groom_age=31,
                 bride=person("Екатерина", "Васильева", last_name_orig="Сураева", status=SOLDIER_WIFE, residence="Журавкино"),
                 bride_marriage_num=2, bride_age=24,
                 witness1=person("Павелъ", "Константиновъ", last_name_orig="Ѳединъ", status=PEASANT_MALE, residence="Анаево"),
                 witness2=person("Сергѣй", "Игнатовъ", last_name_orig="Климкинъ", status=PEASANT_MALE, residence="Анаево"),
                 witness3=person("Павелъ", "Матвѣевъ", last_name_orig="Жаворонкинъ", status=PEASANT_MALE, residence="Анаево"),
                 witness4=person("Михаилъ", "Андреевъ", last_name_orig="Петряевъ", status=PEASANT_MALE, residence="Анаево"),
                 comment="Яндексъ.Архивъ 57-7-51, сканъ 33; вѣнчалъ священникъ Алексѣй Молчановъ"),
    ),
    reviewed=False,
)
