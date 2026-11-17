from verso.ru.dsl import (Gender, Month, Relationship, death, death_month, death_records, person,
                          relative)
from verso.ru.dsl.statuses import PEASANT_MALE, PEASANT_SON

# Журавкинецъ въ книгѣ чужого прихода 1915 г. — ЦГАРМ 57-7-54 (Подлясово), найдено по OCR Яндексъ.Архива,
# прочитано по скану 07.11.2026; reviewed=False.

other_deaths_1915_podlyasovo = death_records(
    "ЦГАРМ", "57", "7", "54", "Подлясово", "",
    1915,
    *death_month(Month.JULY,
        death(10, Gender.MALE, 7, 8,
              deceased=person("Георгій", status=PEASANT_SON, residence="Журавкино"),
              relatives=[relative(person("Иванъ", "Егоровъ", last_name_orig="Амелькинъ", status=PEASANT_MALE),
                                  Relationship.FATHER)],
              cause_of_death="отъ слаборожденности",
              comment="Яндексъ.Архивъ 57-7-54, сканъ 394; лѣта «1½ нед.»; родился 27 іюня того же года (other_births_1915)"),
    ),
    reviewed=False,
)
