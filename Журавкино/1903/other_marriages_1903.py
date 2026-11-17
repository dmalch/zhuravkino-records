from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import PEASANT_GIRL, PEASANT_MALE

# Журавкинка въ книгѣ чужого прихода 1903 г. — ЦГАРМ 57-7-45 (Аксёновка), найдено по OCR Яндексъ.Архива,
# прочитано по скану 07.11.2026; reviewed=False.
# Поручители: первые двое — со стороны жениха, вторые — невѣсты.

other_marriages_1903_aksyonovka = marriage_records(
    "ЦГАРМ", "57", "7", "45", "Аксёновка", "",
    1903,
    *marriage_month(Month.MAY,
        marriage(15, 21,
                 groom=person("Онисимъ", "Леонтіевъ", last_name_orig="Агишевъ", status=PEASANT_MALE, residence="Сургодь"),
                 groom_marriage_num=1, groom_age=20,
                 bride=person("Дарья", "Данилова", last_name_orig="Лескина", status=PEASANT_GIRL, residence="Журавкино"),
                 bride_marriage_num=1,
                 witness1=person("Андрей", "Ѳедоровъ", last_name_orig="Агишевъ", status=PEASANT_MALE),
                 witness2=person("Семенъ", "Ѳедоровъ", last_name_orig="Галкановъ", status=PEASANT_MALE),
                 witness3=person("Данилъ", "Андреевъ", last_name_orig="Максаковъ"),
                 witness4=person("Леонтій", "Антоновъ", last_name_orig="Максаковъ"),
                 comment="Яндексъ.Архивъ 57-7-45, сканъ 201; лѣта невѣсты ушли въ корешокъ"),
    ),
    reviewed=False,
)
