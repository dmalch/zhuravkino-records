from verso.ru.dsl import (Gender, Month, Relationship, death, death_month, death_records, person,
                          relative)
from verso.ru.dsl.causes_of_death import DIARRHEA
from verso.ru.dsl.statuses import KAZENNYJ_PEASANT_DAUGHTER, KAZENNYJ_PEASANT_MALE

# Журавкинка въ книгѣ чужого прихода 1900 г. — ЦГАРМ 57-7-51 (Анаево), найдено по OCR Яндексъ.Архива,
# прочитано по скану 07.11.2026; reviewed=False.

other_deaths_1900_anaevo = death_records(
    "ЦГАРМ", "57", "7", "51", "Анаево", "Покровская",
    1900,
    *death_month(Month.AUGUST,
        death(27, Gender.FEMALE, 28, 30,
              deceased=person("Екатерина", status=KAZENNYJ_PEASANT_DAUGHTER, residence="Журавкино"),
              age=2.5,
              relatives=[relative(person("Тимоѳей", "Мануиловъ", last_name_orig="Юткинъ", status=KAZENNYJ_PEASANT_MALE), Relationship.FATHER)],
              cause_of_death=DIARRHEA,
              comment="Яндексъ.Архивъ 57-7-51, сканъ 46. Въ счетѣ женскаго пола «27», по порядку должно быть 22 "
                      "(предыдущій листъ кончается № 22 3 августа, слѣдующая запись — № 23). Мѣсяцъ — августъ по "
                      "заголовку предыдущаго листа; дальше на листѣ безъ заголовка идетъ сентябрь"),
    ),
    reviewed=False,
)
