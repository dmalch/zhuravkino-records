from verso.ru.dsl import (Gender, Month, Relationship, death, death_month, death_records, person,
                          relative)
from verso.ru.dsl.causes_of_death import SCARLATINA
from verso.ru.dsl.statuses import KAZENNYJ_PEASANT_DAUGHTER, KAZENNYJ_PEASANT_MALE

# Журавкинка въ книгѣ чужого прихода 1902 г. — ЦГАРМ 57-7-47 (Зарубкино), найдено по OCR Яндексъ.Архива,
# прочитано по скану 07.11.2026; reviewed=False.

other_deaths_1902_zarubkino = death_records(
    "ЦГАРМ", "57", "7", "47", "Зарубкино", "Христорождественская",
    1902,
    *death_month(Month.JANUARY,
        death(2, Gender.FEMALE, 17, 18,
              deceased=person("Надежда", status=KAZENNYJ_PEASANT_DAUGHTER, residence="Журавкино"),
              relatives=[relative(person("Семенъ", "Пименовъ", last_name_orig="Семакинъ", status=KAZENNYJ_PEASANT_MALE), Relationship.FATHER)],
              cause_of_death=SCARLATINA,
              comment="Яндексъ.Архивъ 57-7-47, сканъ 333; графа лѣтъ ушла въ корешокъ. Мѣсяцъ — январь: листъ "
                      "открываетъ часть 3 книги 1902 г., заголовка мѣсяца на немъ нѣтъ"),
    ),
    reviewed=False,
)
