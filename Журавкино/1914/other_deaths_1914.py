from verso.ru.dsl import (Gender, Month, Relationship, death, death_month, death_records, person,
                          relative)
from verso.ru.dsl.statuses import PEASANT_MALE, PEASANT_SON

# Авдаловецъ въ московской книгѣ 1914 г. — ЦГА Москвы 2126-2-119 (Крестовоздвиженская ц.), прочитано по
# оригиналу 07.11.2026; reviewed=False.

other_deaths_1914_moscow_krestovozdvizhenskaya = death_records(
    "ЦГА Москвы", "2126", "2", "119", "Москва", "Крестовоздвиженская",
    1914,
    *death_month(Month.JULY,
        death(111, Gender.MALE, 20, 21,
              deceased=person("Николай", status=PEASANT_SON, residence="Авдалово"),
              age="2 мес",
              relatives=[relative(person("Прокопій", "Михайловъ", last_name_orig="Шеровъ", status=PEASANT_MALE, comment="«Шеровъ, онъ же Шеринъ»"), Relationship.FATHER)],
              cause_of_death="отъ катарра желудка и кишекъ",
              comment="Яндексъ.Архивъ 2126-2-119, сканъ 279; лѣта «2½ м.»; Семеновское кладбище; та же запись "
                      "повторена на сканѣ 280 подъ № 112 съ помѣтой «не числить»; родился 2 мая (other_births_1914)"),
    ),
    reviewed=False,
)
