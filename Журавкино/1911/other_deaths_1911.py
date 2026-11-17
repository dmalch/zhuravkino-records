from verso.ru.dsl import (Gender, Month, Relationship, death, death_month, death_records, person,
                          relative)
from verso.ru.dsl.causes_of_death import WEAKNESS
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_MALE

# Журавкинка въ книгѣ чужого прихода 1911 г. — ЦГАРМ 57-4-1042 (Темниковскій у., с. Шалы), найдено по OCR
# Яндексъ.Архива, прочитано по оригиналу 07.11.2026; reviewed=False.

other_deaths_1911_shaly = death_records(
    "ЦГАРМ", "57", "4", "1042", "Шалы", "",
    1911,
    *death_month(Month.APRIL,
        death(17, Gender.FEMALE, 6, 7,
              deceased=person("Матрена", status=PEASANT_DAUGHTER, residence="Журавкино"),
              age="2 нед",
              relatives=[relative(person("Иванъ", "Егоровъ", last_name_orig="Амелькинъ", status=PEASANT_MALE), Relationship.FATHER)],
              cause_of_death=WEAKNESS,
              comment="Яндексъ.Архивъ 57-4-1042, сканъ 348; «отъ слабости»; погребалъ свящ. Василій Свѣтловъ; "
                      "лѣта «2н.» — нед. или дн.; мѣсяцъ — апрѣль по заголовку предыдущаго листа"),
    ),
    reviewed=False,
)
