from verso.ru.dsl import (Gender, Month, Relationship, death, death_month, death_records, person,
                          relative)
from verso.ru.dsl.statuses import PEASANT_MALE, PEASANT_SON

# Журавкинцы и авдаловцы въ книгахъ чужихъ приходовъ 1913 г. — ЦГАРМ 57-4-1141 (г. Темниковъ, Спасо-Преображенская
# ц.) и ЦГА Москвы 203-782-594 (Сретенскій сорокъ), найдено по OCR Яндексъ.Архива, прочитано по оригиналамъ
# 07.11.2026; reviewed=False.

other_deaths_1913_temnikov = death_records(
    "ЦГАРМ", "57", "4", "1141", "Темников", "Спасо-Преображенская",
    1913,
    *death_month(Month.OCTOBER,
        death(34, Gender.FEMALE, 23, 25,
              deceased=person("Анастасія", "Михайлова", last_name_orig="Козлова", status="вдова псаломщика", residence="Журавкино"),
              age=40,
              cause_of_death="отъ воспаленія почекъ",
              comment="Яндексъ.Архивъ 57-4-1141, сканъ 47; погребена на городскомъ кладбищѣ; исповѣдывалъ свящ. "
                      "Ал. Тихонравовъ"),
    ),
    reviewed=False,
)

other_deaths_1913_moscow = death_records(
    "ЦГА Москвы", "203", "782", "594", "Москва", "",
    1913,
    *death_month(Month.JANUARY,
        death(7, Gender.MALE, 10, 12,
              deceased=person("Іоаннъ", status=PEASANT_SON, residence="Авдалово"),
              age="2 нед",
              relatives=[relative(person("Прокопій", "Михайловъ", last_name_orig="Шеровъ", status=PEASANT_MALE, comment="«Шеровъ, онъ же Шеринъ»"), Relationship.FATHER)],
              cause_of_death="слаборожденный",
              comment="Яндексъ.Архивъ 203-782-594, сканъ 725; «въ домѣ Ведихина»; Семеновское кладбище; родился "
                      "28 декабря 1912 г. (other_births_1912)"),
    ),
    reviewed=False,
)
