from verso.ru.dsl import (Gender, Month, Relationship, death, death_month, death_records, person,
                          relative)
from verso.ru.dsl.causes_of_death import PNEUMONIA
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_MALE, PEASANT_SON

# Журавкинка въ книгѣ чужого прихода 1908 г. — ЦГАРМ 57-7-52 (Вадовскіе Селищи), найдено по OCR
# Яндексъ.Архива, прочитано по скану 07.11.2026; reviewed=False.

other_deaths_1908_vadovskie_selishchi = death_records(
    "ЦГАРМ", "57", "7", "52", "Вадовские Селищи", "Покровская",
    1908,
    *death_month(Month.JANUARY,
        death(2, Gender.FEMALE, 27, 28,
              deceased=person("Анна", status=PEASANT_DAUGHTER, residence="Журавкино"),
              relatives=[relative(person("Иванъ", "Васильевъ", last_name_orig="Чичайковъ", status=PEASANT_MALE, comment="фамилія читается неувѣренно; въ 1905 г. «Чинничковъ», въ 1909 г. «Чинчиковъ»"),
                                  Relationship.FATHER)],
              cause_of_death="слаборожденная",
              comment="Яндексъ.Архивъ 57-7-52, сканъ 377; въ графѣ лѣтъ «1» безъ единицы (не внесено) — при «слаборожд.» "
                      "скорѣе дни или недѣли, чѣмъ годъ"),
    ),
    reviewed=False,
)

# Журавкинцы въ московскихъ книгахъ 1908 г. — ЦГА Москвы 203-782-308 (Василіе-Кесарійская ц. Никитскаго сорока;
# второй экземпляръ — 2124-2-36, сканъ 690) и 203-782-541 (Петропавловская ц. Сретенскаго сорока), прочитано
# по оригиналамъ 07.11.2026. Іоаннъ и Евдокія — близнецы, рожденные 18 февраля (other_births_1908).
other_deaths_1908_moscow_vasilie_kesariyskaya = death_records(
    "ЦГА Москвы", "203", "782", "308", "Москва", "Василие-Кесарийская",
    1908,
    *death_month(Month.MARCH,
        death(98, Gender.MALE, 7, 9,
              deceased=person("Іоаннъ", status=PEASANT_SON, residence="Журавкино"),
              age="3 нед",
              relatives=[relative(person("Иванъ", "Ивановъ", last_name_orig="Игнатовъ", status=PEASANT_MALE), Relationship.FATHER)],
              cause_of_death="отъ врожденной слабости",
              comment="Яндексъ.Архивъ 203-782-308, сканъ 674; Ваганьковское кладбище"),
    ),
    reviewed=False,
)

other_deaths_1908_moscow_petropavlovskaya = death_records(
    "ЦГА Москвы", "203", "782", "541", "Москва", "Петропавловская",
    1908,
    *death_month(Month.JUNE,
        death(39, Gender.FEMALE, 25, 27,
              deceased=person("Евдокія", status=PEASANT_DAUGHTER, residence="Журавкино"),
              age="4 мес",
              relatives=[relative(person("Іоаннъ", "Іоанновъ", last_name_orig="Игнатовъ", status=PEASANT_MALE), Relationship.FATHER)],
              cause_of_death=PNEUMONIA,
              comment="Яндексъ.Архивъ 203-782-541, сканъ 680; «въ домѣ Лебова»; Ваганьковское кладбище; "
                      "мѣсяцъ — по № 38 выше («21/VI»?), читается неувѣренно"),
    ),
    reviewed=False,
)
