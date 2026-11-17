from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import DEACON, PEASANT_MALE, PEASANT_WIFE

# Журавкинцы въ книгѣ чужого прихода 1905 г. — ЦГАРМ 57-7-52 (Вадовскіе Селищи), найдено по OCR
# Яндексъ.Архива, прочитано по скану 07.11.2026; reviewed=False.
# Отецъ записанъ въ 1905 г. «Чинничковъ», въ 1908 г. «Чичайковъ», въ 1909 г. «Чинчиковъ» — одна семья
# (Иванъ Васильевъ и жена его Параскева Иванова).

other_births_1905_vadovskie_selishchi = birth_records(
    "ЦГАРМ", "57", "7", "52", "Вадовские Селищи", "Покровская",
    1905,
    *birth_month(Month.JANUARY,
        birth(8, Gender.FEMALE, 21, 22,
              child=person("Ксенія"),
              father=person("Иванъ", "Васильевъ", last_name_orig="Чинничковъ", status=PEASANT_MALE, residence="Журавкино", comment="фамилія читается неувѣренно"),
              mother=person("Параскева", "Иванова", status=PEASANT_WIFE),
              god_parent1=person("Димитрій", last_name_orig="Носинскій", status=DEACON, residence="Журавкино"),
              god_parent2=person("Александра", "Николаева", comment="«…щина» передъ именемъ — такъ въ записи"),
              comment="Яндексъ.Архивъ 57-7-52, сканъ 250"),
    ),
    reviewed=False,
)
