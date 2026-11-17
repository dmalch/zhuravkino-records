from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (ECON_PEASANT_GIRL, GIRL, SOLDIER, YASAK_PEASANT_FEMALE,
                                   YASAK_PEASANT_MALE)

avdalovo_marriages_1769 = marriage_records(
    "ГАРО", "627", "255", "10", "Авдалово", "Николая Чудотворца",
    1769,
    *page("?",
          *marriage_month(Month.OCTOBER,
                          marriage(1, 10,
                                   groom=person("Климонт", "Артемов", residence="Журавкино", status=SOLDIER), groom_marriage_num=2,
                                   bride=person("Настасья", "Петрова", residence="Журавкино", status=GIRL), bride_marriage_num=1),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=ECON_PEASANT_GIRL
    ),
)
