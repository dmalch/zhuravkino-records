from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import PEASANT_GIRL, PEASANT_MALE, PEASANT_WIFE, WIDOW

# Журавкинцы и авдаловцы въ московскихъ книгахъ 1906 г. — ЦГА Москвы 2126-2-112 (Крестовоздвиженская ц.
# Сретенскаго сорока) и 203-782-267 (Екатерининская ц. Воспитательнаго дома), найдено по OCR Яндексъ.Архива,
# прочитано по оригиналамъ 07.11.2026; reviewed=False. Записи 2126-2-112 повторены въ 203-782-517 (сканы 121,
# 258) — второй экземпляръ той же книги.

other_births_1906_moscow_krestovozdvizhenskaya = birth_records(
    "ЦГА Москвы", "2126", "2", "112", "Москва", "Крестовоздвиженская",
    1906,
    *birth_month(Month.FEBRUARY,
        birth(47, Gender.MALE, 27, 1, k_month=Month.MARCH,
              child=person("Алексій"),
              father=person("Прокопій", "Михайловъ", last_name_orig="Шеровъ", status=PEASANT_MALE, residence="Авдалово", comment="«въ домѣ Миронова»; въ другихъ записяхъ — «Шеринъ», «Шаровъ»"),
              mother=person("Марія", "Егорова", status=PEASANT_WIFE),
              god_parent1=person("Никифоръ", "Павловъ", last_name_orig="Ильяковъ", status=PEASANT_MALE, comment="«Майданской волости и села Майданова»"),
              god_parent2=person("Агрипина", "Ѳедорова", last_name_orig="Шерова", status=PEASANT_GIRL),
              comment="Яндексъ.Архивъ 2126-2-112, сканъ 234; крестилъ свящ. Николай Романскій"),
    ),
    *birth_month(Month.DECEMBER,
        birth(288, Gender.FEMALE, 8, 17,
              child=person("Евдокія"),
              father=person("Михаилъ", "Прокопіевъ", last_name_orig="Мыськовъ", status=PEASANT_MALE, residence="Авдалово"),
              mother=person("Анна", "Егорова", status=PEASANT_WIFE),
              god_parent1=person("Трофимъ", "Филипповъ", last_name_orig="Волковъ", status=PEASANT_MALE, residence="Авдалово"),
              god_parent2=person("Агрипина", "Ѳедорова", last_name_orig="Ширина", status=PEASANT_GIRL),
              comment="Яндексъ.Архивъ 2126-2-112, сканъ 365; крестилъ свящ. Василій Смирновъ"),
    ),
    reviewed=False,
)

other_births_1906_moscow_vospitatelny_dom = birth_records(
    "ЦГА Москвы", "203", "782", "267", "Москва", "Екатерининская",
    1906,
    *birth_month(Month.SEPTEMBER,
        birth(770, Gender.FEMALE, 3, 7,
              child=person("Анна", comment="«Анна Александрова»; незаконнорожденная"),
              mother=person("Евгенія", "Михайлова", last_name_orig="Калинкина", status=PEASANT_GIRL, residence="Авдалово"),
              god_parent1=person("Параскева", "Николаева", last_name_orig="Суркова", status=WIDOW),
              comment="Яндексъ.Архивъ 203-782-267, сканъ 506; крестилъ свящ. Александръ Никитинъ"),
    ),
    *birth_month(Month.DECEMBER,
        birth(1150, Gender.FEMALE, 4, 10,
              child=person("Варвара"),
              father=person("Іоаннъ", "Іоанновъ", last_name_orig="Игнатовъ", status=PEASANT_MALE, residence="Журавкино", comment="«имя и отч. мужа — со словъ жены»"),
              mother=person("Ксенія", "Александрова", status=PEASANT_WIFE),
              god_parent1=person("Іоаннъ", "Онисимовъ", last_name_orig="Ѳедуловъ", status=PEASANT_MALE),
              god_parent2=person("Марія", "Михайлова", last_name_orig="Михайлова", status=PEASANT_GIRL, comment="мѣщанка г. Богородицка"),
              comment="Яндексъ.Архивъ 203-782-267, сканъ 670; повторено въ 2123-2-1, сканъ 673"),
    ),
    reviewed=False,
)
