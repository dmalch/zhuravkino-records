from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import YASAK_PEASANT_GIRL, YASAK_PEASANT_MALE

other_marriages_1815 = marriage_records(
    "ЦГАРМ", "57", "1", "394", "Зарубкино", "Христорождественская",
    1815,
    *marriage_month(Month.FEBRUARY,
        marriage(11, 15,
                 groom=person("Макей", "Иванов", status=YASAK_PEASANT_MALE, residence="Куликовка"),
                 bride=person("Марья", "Иванова", status=YASAK_PEASANT_GIRL, residence="Журавкино"),
                 page="81"
                 ),
        marriage(3, 7,
                 village="Анаево", church="Покровская",
                 groom=person("Иван", "Казмин", status=YASAK_PEASANT_MALE, residence="Каргашино"),
                 bride=person("Федосья", "Осипова", status=YASAK_PEASANT_GIRL, residence="Журавкино"),
                 witness1=person("Трифон", "Кирилов", status=YASAK_PEASANT_MALE, residence="Анаево"),
                 witness2=person("Варлам", "Фатеев", status=YASAK_PEASANT_MALE, residence="Анаево"),
                 witness3=person("Михаил", "Ионин", status=YASAK_PEASANT_MALE, residence="Анаево"),
                 witness4=person("Климент", "Филипов", status=YASAK_PEASANT_MALE, residence="Анаево"),
                 witness5=person("Василей", "Кандратьев", status=YASAK_PEASANT_MALE, residence="Анаево"),
                 witness6=person("Давид", "Сидоров", status=YASAK_PEASANT_MALE, residence="Анаево"),
                 page="756"
                 ),
    ),
)
