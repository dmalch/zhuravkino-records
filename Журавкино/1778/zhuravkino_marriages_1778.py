from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_GIRL, YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE

avdalovo_marriages_1778 = marriage_records(
    "ГАРО", "627", "255", "24", "Авдалово", "Николая Чудотворца",
    1778,
    *page("111",
          *marriage_month(Month.FEBRUARY,
                          marriage(1, 5,
                                   groom=person("Павел", "Григорьев", status="отрок из крестьян помещицы Прасковьи Богдановны Моисеевой"), groom_age=17,
                                   bride=person("Васса", "Петрова", status="девка из крестьян помещицы Прасковьи Богдановны Моисеевой"), bride_age=16),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=ECON_PEASANT_GIRL
    ),
)
