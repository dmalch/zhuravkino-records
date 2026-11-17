from verso.ru.dsl import (Gender, Month, Relationship, death, death_month, death_records, person,
                          relative)
from verso.ru.dsl.causes_of_death import PLEURISY
from verso.ru.dsl.statuses import KAZENNYJ_PEASANT_DAUGHTER, KAZENNYJ_PEASANT_MALE

# Журавкинцы въ книгахъ чужихъ приходовъ 1866 г. — ЦГАРМ 57-6-498а, прочитано по сканамъ 07.11.2026;
# reviewed=False. Внесены только записи, гдѣ журавкинецъ — умершій.

other_deaths_1866_korgoshino = death_records(
    "ЦГАРМ", "57", "6", "498а", "Коргошино", "Троицкая",
    1866,
    *death_month(Month.SEPTEMBER,
        death(20, Gender.FEMALE, 21, 23,
              deceased=person("Марія", status=KAZENNYJ_PEASANT_DAUGHTER, residence="Журавкино"),
              age="2 мес",
              relatives=[relative(person("Иванъ", "Игнатовъ", status=KAZENNYJ_PEASANT_MALE), Relationship.FATHER)],
              cause_of_death=PLEURISY,
              comment="Яндексъ.Архивъ, сканъ 119; родилась 16 іюля того же года (other_births_1866, отецъ тамъ «Игнатіевъ»)"),
    ),
    reviewed=False,
)
