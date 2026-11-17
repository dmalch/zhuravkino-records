from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import YASAK_PEASANT_LEGAL_WIFE, YASAK_PEASANT_MAIDEN, YASAK_PEASANT_MALE

other_births_1837 = birth_records(
    "ЦГАРМ", "57", "6", "172", "Анаево", "Покровская",
    1837,
    *birth_month(Month.FEBRUARY,
        birth(5, Gender.FEMALE, 1, 1,
                 child=person("Ксения"),
                 father=person("Павел", "Григорьев", status=YASAK_PEASANT_MALE, residence="Журавкино"),
                 mother=person("Екатерина", "Федорова", status=YASAK_PEASANT_LEGAL_WIFE),
                 god_parent1=person("Стефан", "Федоров", status=YASAK_PEASANT_MALE, residence="Крюковка"),
                 god_parent2=person("Агафья", "Алексеева", status=YASAK_PEASANT_MAIDEN, residence="Крюковка"),
                 page="354"
                 ),
    ),
)
