from corpus.statuses import SLEPTSOV_GM_PEASANT_MALE, SLEPTSOV_TI_PEASANT_MALE
from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import GIRL, YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL, YASAK_PEASANT_MALE

zhuravkino_marriages_1802 = marriage_records(
    "ЦГАРМ", "57", "6", "40а", "Журавкино", "Николаевская",
    1802,
    *page("40об",
          *marriage_month(Month.FEBRUARY,
                          marriage(2, 9,
                                   groom=person("Гаврил", "Семенов"), groom_age=16,
                                   bride=person("Евгения", "Максимова"), bride_age=17),
                          marriage(3, 9,
                                   groom=person("Фока", "Иванов"), groom_age=15,
                                   bride=person("Праскевия", "Маркова", status=GIRL), bride_age=14),
                          marriage(4, 12,
                                   groom=person("Степан", "Моисеев"), groom_age=25,
                                   bride=person("Ирина", "Петрова", status=GIRL), bride_age=20),
                          marriage(5, 12,
                                   groom=person("Моисей", "Павлов", status=SLEPTSOV_GM_PEASANT_MALE, comment="отчество неразборчиво написано"), groom_age=15,
                                   bride=person("Праскевия", "Григорьева", status=GIRL), bride_age=14),
                          marriage(6, 12,
                                   groom=person("Иван", "Климов", residence="Авдалово", status=SLEPTSOV_TI_PEASANT_MALE), groom_age=16,
                                   bride=person("Ирина", "Петрова", residence="Авдалово", status=GIRL), bride_age=15),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
