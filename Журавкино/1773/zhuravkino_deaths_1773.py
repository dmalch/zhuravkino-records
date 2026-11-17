from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.statuses import WIDOW, YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE

avdalovo_deaths_1773 = death_records(
    "ГАРО", "627", "255", "15", "Авдалово", "Николая Чудотворца",
    1773,
    *page("?",
          *death_month(Month.JANUARY,
                       death(1, Gender.FEMALE, 19, None,
                             deceased=person("Акилина", "Иванова", residence="Журавкино"),
                             relatives=[relative(person("Маѯим", "Ивановъ" ), Relationship.HUSBAND)]),
                       ),
          *death_month(Month.MARCH,
                       death(2, Gender.FEMALE, 6, None,
                             deceased=person("Елена", "Владимирова"),
                             relatives=[relative(person("Михаилъ", "Феодотовъ"), Relationship.HUSBAND)]),
                       ),
          *death_month(Month.MAY,
                       death(3, Gender.FEMALE, 24, None,
                             deceased=person("Агафья", "Иванова", status=WIDOW)),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
    ),
)
