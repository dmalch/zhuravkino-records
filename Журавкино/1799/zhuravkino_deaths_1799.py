from corpus.statuses import SLEPTSOV_GM_PEASANT_MALE
from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE

zhuravkino_deaths_1799 = death_records(
    "ГАТО", "1049", "10", "85", "Журавкино", "Николая Чудотворца",
    1799,
    *page("34об",
          *death_month(Month.FEBRUARY,
                       death(1, Gender.FEMALE, 1, None,
                             deceased=person("Елена", "Михайлова"), age=65),
                       ),
          *death_month(Month.MARCH,
                       death(2, Gender.MALE, 11, None,
                             deceased=person("Никифор", "Леонтьев"), age=82),
                       death(3, Gender.MALE, 4, None,
                             deceased=person("Тит", "Казмин"), age=52),
                       death(4, Gender.MALE, 4, None,
                             deceased=person("Макар", "Дементьев", status=SLEPTSOV_GM_PEASANT_MALE), age=27),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
    ),
)
