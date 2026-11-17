from corpus.statuses import ENGALYCHEV_IAL_PEASANT_MALE, MOISEEVA_PB_PEASANT_MALE
from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL, YASAK_PEASANT_MALE

avdalovo_marriages_1774 = marriage_records(
    "ГАРО", "627", "255", "18", "Авдалово", "Николая Чудотворца",
    1774,
    *page("27об",
          *marriage_month(Month.FEBRUARY,
                          marriage(1, 2,
                                   groom=person("Савва", "Лонгинов", status=MOISEEVA_PB_PEASANT_MALE), groom_age=17, groom_marriage_num=1,
                                   bride=person("Васса", "Акимова", status="крестьянка помещицы Прасковьи Богдановны Моисеевой"), bride_age=15, bride_marriage_num=1),
                          marriage(2, 2,
                                   groom=person("Александр", "Аввакумов", status=ENGALYCHEV_IAL_PEASANT_MALE), groom_age=16, groom_marriage_num=1,
                                   bride=person("Ульяна", "Алексеева", status="крестьянка помещика Ивана Александровича Енгалычева"), bride_age=14, bride_marriage_num=1),
                          ),
          *marriage_month(Month.SEPTEMBER,
                          marriage(3, 4,
                                   groom=person("Иван", "Федоров", residence="Журавкино"), groom_age=15, groom_marriage_num=1,
                                   bride=person("Федосья", "Кузмина", residence="Журавкино"), bride_age=15, bride_marriage_num=1),
                          ),
          *marriage_month(Month.OCTOBER,
                          marriage(4, 19,
                                   groom=person("Николай", "Иванов", residence="Журавкино"), groom_age=20, groom_marriage_num=1,
                                   bride=person("Дарья", "Моисеева", residence="Журавкино"), bride_age=18, bride_marriage_num=1),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
