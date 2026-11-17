from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import PEASANT_GIRL, PEASANT_MALE

# Журавкинка въ книгѣ чужого прихода — ЦГАРМ 57-9-229 (Саранскій у., с. Кажлодка), найдено по OCR Яндексъ.Архива,
# прочитано по оригиналу 07.11.2026; reviewed=False. Годъ въ шапкѣ листа не вписанъ; 1912 — по сосѣднимъ
# листамъ части 2 («1912-й»), въ отчетѣ по Яндексу дѣло значится 1911 г. Провѣрить.

other_marriages_1912_kazhlodka = marriage_records(
    "ЦГАРМ", "57", "9", "229", "Кажлодка", "",
    1912,
    *marriage_month(Month.NOVEMBER,
        marriage(9, 13,
                 groom=person("Яковъ", "Алексѣевъ", last_name_orig="Скопиновъ", status=PEASANT_MALE, residence="Кажлодка"),
                 groom_marriage_num=1, groom_age=26,
                 bride=person("Васса", last_name_orig="Каргина", status=PEASANT_GIRL, residence="Журавкино", comment="отчество не записано"),
                 bride_marriage_num=1, bride_age=15,
                 witness1=person("Ѳедоръ", last_name_orig="Резянкинъ", status=PEASANT_MALE, residence="Кажлодка"),
                 witness2=person("Никифоръ", last_name_orig="Скопиновъ", status=PEASANT_MALE, residence="Кажлодка"),
                 witness3=person("Василій", last_name_orig="Ошкинъ", status=PEASANT_MALE, residence="Кажлодка"),
                 witness4=person("Максимъ", last_name_orig="Ошкинъ", status=PEASANT_MALE, residence="Кажлодка"),
                 comment="Яндексъ.Архивъ 57-9-229, сканъ 238; лѣта невѣсты «15-1…» (16?); поручители записаны "
                         "общимъ спискомъ; вѣнчалъ свящ. Михаилъ Морозовъ"),
    ),
    reviewed=False,
)
