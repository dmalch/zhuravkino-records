from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import YASAK_PEASANT_GIRL, YASAK_PEASANT_MALE, YASAK_PEASANT_WIDOW

other_marriages_1833 = marriage_records(
    "ЦГАРМ", "57", "6", "153", "Вадовские Селищи", "Покровская",
    1833,
    *marriage_month(Month.JANUARY,
        marriage(1, 9,
                 village="Анаево", church="Покровская",
                 groom=person("Иван", "Фомин", status=YASAK_PEASANT_MALE, residence="Каргашино"),
                 bride=person("Настасья", "Стефанова", status=YASAK_PEASANT_GIRL, residence="Журавкино"),
                 witness1=person("Семен", "Федоров", status=YASAK_PEASANT_MALE, residence="Каргашино"),
                 witness2=person("Илья", "Андреев", status=YASAK_PEASANT_MALE, residence="Каргашино"),
                 witness3=person("Николай", "Давидов", status=YASAK_PEASANT_MALE, residence="Каргашино"),
                 witness4=person("Григорий", "Петров", status=YASAK_PEASANT_MALE, residence="Каргашино"),
                 page="772"),
    ),
    *marriage_month(Month.APRIL,
        marriage(13, 14,
                 groom=person("Гаврила", "Еремеев", last_name_orig="Щукин", status=YASAK_PEASANT_MALE, residence="Подлясово"),
                 bride=person("Прасковья", "Григорьева", status=YASAK_PEASANT_WIDOW, residence="Журавкино"),
                 witness1=person("Прокопий", "Никанов", last_name_orig="Щукин", status=YASAK_PEASANT_MALE, residence="Подлясово"),
                 witness2=person("Яков", "Прокопиев", last_name_orig="Щукин", status=YASAK_PEASANT_MALE, residence="Подлясово"),
                 witness3=person("Макар", "Федосеев", last_name_orig="Щукин", status=YASAK_PEASANT_MALE, residence="Селищи"),
                 page="802"),
    ),
)
