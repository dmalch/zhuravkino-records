from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (YASAK_PEASANT_BOY, YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL,
                                   YASAK_PEASANT_MALE)

zhuravkino_marriages_1809 = marriage_records(
    "ЦГАРМ", "57", "6", "68", "Журавкино", "Николаевская",
    1809,
    *page("?",
          *marriage_month(Month.JANUARY,
                          marriage(1, 17,
                                   groom=person("Никифор", "Иванов", status=YASAK_PEASANT_BOY),
                                   bride=person("Наталья", "Осипова", residence="Крюковка")),
                          marriage(2, 24,
                                   groom=person("Иван", "Федосеев", status=YASAK_PEASANT_BOY),
                                   bride=person("Акилина", "Иванова")),
                          ),
          *marriage_month(Month.APRIL,
                          marriage(3, 4,
                                   groom=person("Марк", "Александров", status=YASAK_PEASANT_BOY),
                                   bride=person("Настасья", "Кузмина")),
                          marriage(4, 4,
                                   groom=person("Порфирий", "Федоров", status=YASAK_PEASANT_BOY),
                                   bride=person("Федосья", "Сергеева", residence="Анаево")),
                          marriage(5, 25,
                                   groom=person("Никита", "Нестеров", status=YASAK_PEASANT_BOY),
                                   bride=person("Матрона", "Егорова", residence="Пичевка")),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
