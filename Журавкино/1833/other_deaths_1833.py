from verso.ru.dsl import (Gender, Month, Relationship, death, death_month, death_records, person,
                          relative)
from verso.ru.dsl.statuses import SOLDIER_WIFE, YASAK_PEASANT_DAUGHTER

other_deaths_1833 = death_records(
    "ЦГАРМ", "57", "6", "153", "Вадовские Селищи", "Покровская",
    1833,
    *death_month(Month.FEBRUARY,
        death(9, Gender.FEMALE, 6, None,
                 deceased=person("Акилина", status=YASAK_PEASANT_DAUGHTER, residence="Журавкино", comment="незаконноприжитая"),
                 age=18,
                 relatives=[relative(person("Татьяна", "Сысоева", last_name_orig="Булаева", status=SOLDIER_WIFE ), Relationship.MOTHER)],
                 cause_of_death="от головы и нагрудной болезни",
                 page="807"
                 ),
    ),
)
