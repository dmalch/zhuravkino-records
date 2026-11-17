from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Журавкинка въ книгѣ чужого прихода 1909 г. — ЦГАРМ 57-7-52 (Вадовскіе Селищи), найдено по OCR
# Яндексъ.Архива, прочитано по скану 07.11.2026; reviewed=False.
# Поручители: первые двое — со стороны жениха, вторые — невѣсты.

other_marriages_1909_vadovskie_selishchi = marriage_records(
    "ЦГАРМ", "57", "7", "52", "Вадовские Селищи", "Покровская",
    1909,
    *marriage_month(Month.NOVEMBER,
        marriage(16, 1,
                 groom=person("Осипъ", "Максимовъ", last_name_orig="Кичигинъ", status=PEASANT_MALE, residence="Вадовские Селищи"),
                 groom_marriage_num=2, groom_age=28,
                 bride=person("Агрипина", "Васильева", last_name_orig="Наумкина", status=PEASANT_FEMALE, residence="Журавкино"),
                 bride_marriage_num=2, bride_age=26,
                 witness1=person("Ефимъ", "Васильевъ", last_name_orig="Зинкинъ", status=PEASANT_MALE),
                 witness2=person("Емельянъ", "Михаиловъ", last_name_orig="Соколовъ", status=PEASANT_MALE),
                 witness3=person("Игнатій", "Ивановъ"),
                 witness4=person("Осипъ", "Васильевъ"),
                 comment="Яндексъ.Архивъ 57-7-52, сканъ 403"),
    ),
    reviewed=False,
)

# Журавкинка въ книгѣ Анаева 1909 г. — ЦГАРМ 57-7-51а (1904–1909), прочитано по оригиналу 07.11.2026.
other_marriages_1909_anaevo = marriage_records(
    "ЦГАРМ", "57", "7", "51а", "Анаево", "Покровская",
    1909,
    *marriage_month(Month.NOVEMBER,
        marriage(36, 11,
                 groom=person("Аѳанасій", "Степановъ", last_name_orig="Волковъ", status=PEASANT_MALE, residence="Анаево"),
                 groom_marriage_num=2, groom_age=20,
                 bride=person("Анна", "Флорова", last_name_orig="Лобачева", status=PEASANT_FEMALE, residence="Журавкино"),
                 bride_marriage_num=2, bride_age=21,
                 witness1=person("Ѳеодоръ", "Ивановъ", last_name_orig="Таракинъ", status=PEASANT_MALE, residence="Анаево"),
                 witness2=person("Григорій", "Петровъ", last_name_orig="Глуховъ", status=PEASANT_MALE, residence="Анаево"),
                 witness3=person("Иванъ", "Васильевъ", last_name_orig="Волковъ", status=PEASANT_MALE, residence="Анаево"),
                 witness4=person("Сергѣй", "Ивановъ", last_name_orig="Илларіоновъ", status=PEASANT_MALE, residence="Анаево"),
                 comment="Яндексъ.Архивъ 57-7-51а, сканъ 189; годъ — по шапкѣ листа (въ OCR «1909»), мѣсяцъ — «Ноябрь» "
                         "сосѣдняго листа; день «11» читается неувѣренно; вѣнчалъ свящ. Михаилъ Курганскій"),
    ),
    reviewed=False,
)
