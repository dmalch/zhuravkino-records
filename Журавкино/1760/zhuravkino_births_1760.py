from corpus.statuses import SLEPTSOV_IT_PEASANT_MALE
from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE

avdalovo_births_1760 = birth_records(
    "ГАРО", "627", "255", "2", "Авдалово", "Николая Чудотворца",
    1760,
    *page("?",
          *birth_month(Month.APRIL,
                       birth(1, Gender.FEMALE, 1, None,
                             child=person("Марья"),
                             father=person("Леонтий", "Андреев", residence="Журавкино")),
                       ),
          *birth_month(Month.AUGUST,
                       birth(2, Gender.MALE, 21, None,
                             child=person("Аврам"),
                             father=person("Егор", "Максимов", residence="Журавкино")),
                       birth(3, Gender.MALE, 22, None,
                             child=person("Агафоник"),
                             father=person("Василий", "Олександров", status=SLEPTSOV_IT_PEASANT_MALE)),
                       ),
          *birth_month(Month.NOVEMBER,
                       birth(4, Gender.MALE, 30, None,
                             child=person("Ондрей"),
                             father=person("Олександр", "Антонов", status=SLEPTSOV_IT_PEASANT_MALE)),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE
    ),
)
