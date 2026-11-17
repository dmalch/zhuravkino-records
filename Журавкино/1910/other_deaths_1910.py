from verso.ru.dsl import (Gender, Month, Relationship, death, death_month, death_records, person,
                          relative)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_MALE

# Авдаловка въ московской книгѣ 1910 г. — ЦГА Москвы 203-782-563 (Крестовоздвиженская ц.; второй экземпляръ —
# 2126-2-115, сканъ 291), прочитано по оригиналу 07.11.2026; reviewed=False.

other_deaths_1910_moscow_krestovozdvizhenskaya = death_records(
    "ЦГА Москвы", "203", "782", "563", "Москва", "Крестовоздвиженская",
    1910,
    *death_month(Month.FEBRUARY,
        death(20, Gender.FEMALE, 13, 14,
              deceased=person("Анастасія", status=PEASANT_DAUGHTER, residence="Авдалово"),
              relatives=[relative(person("Прокопій", "Михайловъ", last_name_orig="Шеринъ", status=PEASANT_MALE),
                                  Relationship.FATHER)],
              cause_of_death="отъ воспаленія почекъ",
              comment="Яндексъ.Архивъ 203-782-563, сканъ 268; «въ домѣ Миронова»; Семеновское кладбище; лѣта ушли въ "
                      "корешокъ; годъ въ шапкѣ у корешка (по описи 1910). Не та Анастасія, что родилась 10 октября "
                      "1910 г., — вѣроятно, рожденная 23 декабря 1907 г. (other_births_1907)"),
    ),
    reviewed=False,
)
