from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import PEASANT_GIRL, PEASANT_MALE, PEASANT_WIDOW, PRIVATE_SOLDIER

# Журавкинецъ и авдаловецъ въ книгахъ чужихъ приходовъ 1908 г. — ЦГА Москвы 203-780-3839 (Коломенскій у.,
# с. Малино) и 203-782-307 (Москва, Богородице-Рождественская ц. на Бутыркахъ), найдено по OCR Яндексъ.Архива,
# прочитано по оригиналамъ 07.11.2026; reviewed=False.
# Поручители: первые двое — со стороны жениха, остальные — невѣсты.

other_marriages_1908_malino = marriage_records(
    "ЦГА Москвы", "203", "780", "3839", "Малино", "",
    1908,
    *marriage_month(Month.FEBRUARY,
        marriage(8, 15,
                 groom=person("Иванъ", "Трофимовъ", last_name_orig="Ѳедотовъ", status=PEASANT_MALE, residence="Журавкино", comment="«Ѳедотовъ, онъ же Булаевъ»"),
                 groom_marriage_num=1, groom_age=22,
                 bride=person("Параскева", "Григорьева", last_name_orig="Рыбакова", status=PEASANT_GIRL, comment="деревни Харина"),
                 bride_marriage_num=1, bride_age=20,
                 witness1=person("Александръ", "Іосифовъ", last_name_orig="Мошковъ", status=PEASANT_MALE, residence="Малино", comment="фамилія читается неувѣренно"),
                 witness2=person("Николай", "Николаевъ", last_name_orig="Ольшинъ", status=PEASANT_MALE, residence="Малино", comment="фамилія читается неувѣренно"),
                 witness3=person("Владиміръ", "Ивановъ", last_name_orig="Смирновъ", status=PEASANT_MALE, residence="Малино"),
                 comment="Яндексъ.Архивъ 203-780-3839, сканъ 262; годъ въ шапкѣ «190?» (вписанъ блѣдно) — 1908 по описи; "
                         "вѣнчалъ свящ. Александръ Величкинъ"),
    ),
    reviewed=False,
)

other_marriages_1908_moscow_butyrki = marriage_records(
    "ЦГА Москвы", "203", "782", "307", "Москва", "Богородице-Рождественская",
    1908,
    *marriage_month(Month.FEBRUARY,
        marriage(49, 15,
                 groom=person("Иванъ", "Антоновъ", last_name_orig="Евлановъ", status=PRIVATE_SOLDIER, residence="Авдалово", comment="«запасный рядовой, объѣздчикъ Вержболовской бригады пограничной стражи»"),
                 groom_marriage_num=1, groom_age=29,
                 bride=person("Марія", "Арсеньева", last_name_orig="Шейкина", status=PEASANT_WIDOW, comment="Тульской губ., Богородицкаго у., Солодиловской вол., дер. Зарѣчной слободы"),
                 bride_marriage_num=2, bride_age=32,
                 witness1=person("Михаилъ", "Климовъ", last_name_orig="Тереховъ", status=PEASANT_MALE, comment="Калужской губ., Тарусскаго у., д. Шемякина"),
                 witness2=person("Гавріилъ", "Львовъ", last_name_orig="Фроловъ", status=PEASANT_MALE, comment="той же деревни"),
                 witness3=person("Иванъ", "Львовъ", last_name_orig="Фроловъ", status=PEASANT_MALE, comment="той же деревни"),
                 witness4=person("Харитонъ", "Семеновъ", last_name_orig="Чувиковъ", status=PEASANT_MALE, comment="Рязанской губ., с. Болошнева"),
                 comment="Яндексъ.Архивъ 203-782-307, сканъ 262; вѣнчалъ протоіерей Христофоръ Максимовъ"),
    ),
    reviewed=False,
)
