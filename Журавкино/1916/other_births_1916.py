from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIFE

# Журавкинцы въ книгѣ чужого прихода 1916 г. — ЦГАРМ 57-4-1266 (Инсарскій у., с. Ускляй), найдено по OCR
# Яндексъ.Архива, прочитано по оригиналу 07.11.2026; reviewed=False.

other_births_1916_usklyai = birth_records(
    "ЦГАРМ", "57", "4", "1266", "Ускляй", "",
    1916,
    *birth_month(Month.OCTOBER,
        birth(16, Gender.FEMALE, 14, 15,
              child=person("Елизавета"),
              father=person("Ѳеодоръ", "Захаровъ", last_name_orig="Чудакинъ", status=PEASANT_MALE, residence="Журавкино", comment="въ другихъ книгахъ — «Чудайкинъ»"),
              mother=person("Варвара", "Иванова", status=PEASANT_WIFE),
              god_parent1=person("Михаилъ", "Михайловъ", last_name_orig="Сандинъ", status=PEASANT_MALE, residence="Журавкино"),
              god_parent2=person("Евдокія", "Филиппова", last_name_orig="Чепкаева", status=PEASANT_FEMALE, comment="села Архангельско-Голицына"),
              comment="Яндексъ.Архивъ 57-4-1266, сканъ 121; годъ въ шапкѣ не вписанъ (по описи 1916); мѣсяцъ — по "
                      "сосѣднему листу («Октябрь»); крестилъ свящ. В. Многомировъ"),
    ),
    reviewed=False,
)
