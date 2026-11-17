from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import PEASANT_GIRL, PEASANT_MALE, PEASANT_WIFE

# Журавкинцы въ книгѣ чужого прихода 1909 г. — ЦГАРМ 57-7-52 (Вадовскіе Селищи), найдено по OCR
# Яндексъ.Архива, прочитано по скану 07.11.2026; reviewed=False.

other_births_1909_vadovskie_selishchi = birth_records(
    "ЦГАРМ", "57", "7", "52", "Вадовские Селищи", "Покровская",
    1909,
    *birth_month(Month.JANUARY,
        birth(6, Gender.MALE, 27, 28,
              child=person("Василій"),
              father=person("Иванъ", "Васильевъ", last_name_orig="Чинчиковъ", status=PEASANT_MALE, residence="Журавкино", comment="въ 1905 г. «Чинничковъ», въ 1908 г. «Чичайковъ»"),
              mother=person("Параскева", "Иванова", status=PEASANT_WIFE),
              god_parent1=person("Гавріилъ", "Ѳедотовъ", last_name_orig="Никуличкинъ", status=PEASANT_MALE, comment="села Димитріева Усада"),
              god_parent2=person("Екатерина", "Иванова", status=PEASANT_GIRL),
              comment="Яндексъ.Архивъ 57-7-52, сканъ 387"),
    ),
    reviewed=False,
)

# Журавкинцы въ книгѣ с. Малино 1909 г. — ЦГА Москвы 203-780-3954 (Коломенскій у.), прочитано по оригиналу 07.11.2026.
other_births_1909_malino = birth_records(
    "ЦГА Москвы", "203", "780", "3954", "Малино", "",
    1909,
    *birth_month(Month.OCTOBER,
        birth(55, Gender.FEMALE, 8, 9,
              child=person("Александра"),
              father=person("Иванъ", "Трофимовъ", last_name_orig="Булаевъ", status=PEASANT_MALE, residence="Журавкино", comment="= Иванъ Трофимовъ Ѳедотовъ, онъ же Булаевъ (бракъ 1908 г., other_marriages_1908)"),
              mother=person("Параскева", "Григорьева", status=PEASANT_WIFE),
              god_parent1=person("Николай", "Николаевъ", last_name_orig="Ольшинъ", status=PEASANT_MALE, residence="Малино", comment="фамилія читается неувѣренно"),
              god_parent2=person("Анастасія", "Михайлова", last_name_orig="Рыбакова", status=PEASANT_GIRL, comment="деревни Хариной"),
              comment="Яндексъ.Архивъ 203-780-3954, сканъ 254; крестилъ свящ. А. Величкинъ"),
    ),
    reviewed=False,
)
