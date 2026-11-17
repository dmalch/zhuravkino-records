from corpus.statuses import SLEPTSOV_GM_PEASANT_GIRL, SLEPTSOV_GM_PEASANT_MALE
from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL, YASAK_PEASANT_MALE

zhuravkino_marriages_1794 = marriage_records(
    "ГАРО", "627", "298", "30", "Журавкино", "Николая Чудотворца",
    1794,
    *page("16об",
          *marriage_month(Month.JANUARY,
                          marriage(1, 15,
                                   groom=person("Афанасий", "Филатов", status=SLEPTSOV_GM_PEASANT_MALE), groom_age=17, groom_marriage_num=1,
                                   bride=person("Татьяна", "Спиридонова", status=SLEPTSOV_GM_PEASANT_GIRL), bride_age=15, bride_marriage_num=1),
                          ),
          *marriage_month(Month.FEBRUARY,
                          marriage(2, 5,
                                   groom=person("Фока", "Иванов"), groom_age=17, groom_marriage_num=1,
                                   bride=person("Анисья", "Васильева", residence="Тихоновка"), bride_age=16, bride_marriage_num=1,
                                   comment="В РС 1795 указано что она из деревни Тихоновки"),
                          marriage(3, 5,
                                   groom=person("Тимофей", "Леонтиев"), groom_age=19, groom_marriage_num=1,
                                   bride=person("Варвара", "Максимова", residence="Пичевка"), bride_age=17, bride_marriage_num=1,
                                   comment="В РС 1795 указано что она из деревни Пичевки"),
                          ),
          *marriage_month(Month.APRIL,
                          marriage(4, 23,
                                   groom=person("Костантин", "Никифоров"), groom_age=18, groom_marriage_num=1,
                                   bride=person("Анна", "Семенова"), bride_age=16, bride_marriage_num=1),
                          ),
          *marriage_month(Month.MAY,
                          marriage(5, 14,
                                   groom=person("Флор", "Никитин"), groom_age=18, groom_marriage_num=1,
                                   bride=person("Прасковья", "Антонова", residence="Промзино"), bride_age=19, bride_marriage_num=1,
                                   comment="В РС 1795 указано что она из деревни Промзино"),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
