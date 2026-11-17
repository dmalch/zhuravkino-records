from verso.ru.dsl import (Gender, Month, Relationship, death, death_month, death_records, person,
                          relative)
from verso.ru.dsl.causes_of_death import COLD
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_MALE

# Журавкинка въ книгѣ чужого прихода 1904 г. — ЦГА Москвы 203-780-3461 (г. Руза, Воскресенскій соборъ),
# найдено по OCR Яндексъ.Архива, прочитано по оригиналу 07.11.2026; reviewed=False.

other_deaths_1904_ruza = death_records(
    "ЦГА Москвы", "203", "780", "3461", "Руза", "Воскресенская",
    1904,
    *death_month(Month.DECEMBER,
        death(36, Gender.FEMALE, 24, 26,
              deceased=person("Анастасія", status=PEASANT_DAUGHTER, residence="Журавкино"),
              age=2,
              relatives=[relative(person("Иванъ", "Ивановъ", status=PEASANT_MALE), Relationship.FATHER)],
              cause_of_death=COLD,
              comment="Яндексъ.Архивъ 203-780-3461, сканъ 70; «Майданской волости села Журавкина»"),
    ),
    reviewed=False,
)
