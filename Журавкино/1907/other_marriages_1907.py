from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import PEASANT_GIRL, PEASANT_MALE

# Журавкинка въ книгѣ чужого прихода 1907 г. — ЦГАРМ 57-7-51а (Анаево, 1904–1909), найдено по OCR
# Яндексъ.Архива, прочитано по оригиналу 07.11.2026; reviewed=False.
# Поручители: первые двое — со стороны жениха, вторые — невѣсты.

other_marriages_1907_anaevo = marriage_records(
    "ЦГАРМ", "57", "7", "51а", "Анаево", "Покровская",
    1907,
    *marriage_month(Month.APRIL,
        marriage(11, 30,
                 groom=person("Иванъ", "Сергѣевъ", last_name_orig="Ѳединъ", status=PEASANT_MALE, residence="Анаево"),
                 groom_marriage_num=1, groom_age=19,
                 bride=person("Пелагія", "Прокопьева", last_name_orig="Ѳедулова", status=PEASANT_GIRL, residence="Журавкино"),
                 bride_marriage_num=1, bride_age=26,
                 witness1=person("Василій", "Тимоѳеевъ", last_name_orig="Ѳединъ", status=PEASANT_MALE, residence="Анаево"),
                 witness2=person("Сергѣй", "Ивановъ", last_name_orig="Илларіоновъ", status=PEASANT_MALE, residence="Анаево"),
                 witness3=person("Адріанъ", "Васильевъ", last_name_orig="Ѳединъ", status=PEASANT_MALE, residence="Анаево"),
                 witness4=person("Иванъ", "Петровъ", last_name_orig="Зуйкинъ", status=PEASANT_MALE, residence="Анаево"),
                 comment="Яндексъ.Архивъ 57-7-51а, сканъ 183; «невѣста … села Журавкина» (въ OCR — «приказали»)"),
    ),
    reviewed=False,
)
