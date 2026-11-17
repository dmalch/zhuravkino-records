from corpus.statuses import (ENGALYCHEV_IAL_PEASANT_MALE, SLEPTSOV_GM_PEASANT_FEMALE,
                             SLEPTSOV_TI_PEASANT_FEMALE)
from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.causes_of_death import NATURAL, NOT_IN_DOCUMENT
from verso.ru.dsl.statuses import YASAK_PEASANT_BOY, YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE

zhuravkino_deaths_1804 = death_records(
    "ЦГАРМ", "57", "1", "389а", "Журавкино", "Николаевская",
    1804,
    *page("?",
          *death_month(Month.JANUARY,
                       death(1, Gender.FEMALE, 10, None,
                             deceased=person("Настасия", "Петрова", status=SLEPTSOV_GM_PEASANT_FEMALE), age=53),
                       ),
          *death_month(Month.MARCH,
                       death(2, Gender.FEMALE, 2, None,
                             deceased=person("Мария", "Григорьева"), age=54),
                       death(3, Gender.FEMALE, 4, None,
                             deceased=person("Елена", "Петрова", residence="Авдалово", status=SLEPTSOV_TI_PEASANT_FEMALE), age=65),
                       ),
          *death_month(Month.MAY,
                       death(4, Gender.FEMALE, 26, None,
                             deceased=person("София", "Иванова", residence="Авдалово", status=SLEPTSOV_TI_PEASANT_FEMALE), age=78),
                       ),
          *death_month(Month.JUNE,
                       death(1, Gender.MALE, 10, None,
                             deceased=person("Никита", "Васильев"), age=70),
                       ),
          *death_month(Month.OCTOBER,
                       death(2, Gender.MALE, 8, None,
                             deceased=person("Семен", "Афанасьев", residence="Авдалово", status=ENGALYCHEV_IAL_PEASANT_MALE), age=60,
                             cause_of_death=NOT_IN_DOCUMENT),
                       death(3, Gender.MALE, 8, None,
                             deceased=person("Спиридон", status=YASAK_PEASANT_BOY), age=2, cause_of_death=NOT_IN_DOCUMENT),
                       death(4, Gender.MALE, 8, None,
                             deceased=person("Савва", "Савельев"), age=1),
                       death(5, Gender.MALE, 8, None,
                             deceased=person("Петр", residence="Авдалово", status="отрок из крестьян помещицы Екатерины Фирсовны Слепцовой"), age=3),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
