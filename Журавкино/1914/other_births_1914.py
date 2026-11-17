from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_GIRL, PEASANT_MALE, PEASANT_WIFE

# Авдаловцы въ московской книгѣ 1914 г. — ЦГА Москвы 2126-2-119 (Крестовоздвиженская ц. Сретенскаго сорока),
# найдено по OCR Яндексъ.Архива, прочитано по оригиналамъ 07.11.2026; reviewed=False.

other_births_1914_moscow_krestovozdvizhenskaya = birth_records(
    "ЦГА Москвы", "2126", "2", "119", "Москва", "Крестовоздвиженская",
    1914,
    *birth_month(Month.JANUARY,
        birth(22, Gender.MALE, 12, 26,
              child=person("Алексій", comment="незаконнорожденный"),
              mother=person("Варвара", "Васильева", last_name_orig="Перевезенцева", status=PEASANT_GIRL, residence="Авдалово", comment="«въ д. Халаева»"),
              god_parent1=person("Николай", "Андреевъ", last_name_orig="Платоновъ", status=PEASANT_MALE, comment="Рузскаго у., Васильевской вол., дер. Савиной"),
              god_parent2=person("Александра", "Петрова", last_name_orig="Прошникова", status=PEASANT_GIRL, comment="Смоленской губ.; фамилія читается неувѣренно"),
              comment="Яндексъ.Архивъ 2126-2-119, сканъ 10; крестилъ протоіерей Алексій Аѳонскій"),
    ),
    *birth_month(Month.MAY,
        birth(132, Gender.MALE, 2, 6,
              child=person("Николай"),
              father=person("Прокопій", "Михайловъ", last_name_orig="Шеровъ", status=PEASANT_MALE, residence="Авдалово", comment="«Шеровъ, онъ же Шеринъ»; «въ д. Ведихина»"),
              mother=person("Марія", "Егорова", status=PEASANT_WIFE),
              god_parent1=person("Никифоръ", "Павловъ", last_name_orig="Ильяковъ", status=PEASANT_MALE, residence="Боковой Майдан"),
              god_parent2=person("Ольга", "Петрова", last_name_orig="Макушкина", status=PEASANT_FEMALE, comment="Рязанской губ., Пронскаго у., Юраковской вол., села Филатова"),
              comment="Яндексъ.Архивъ 2126-2-119, сканъ 61; крестилъ свящ. Симеонъ Ковганкинъ; умеръ 20 іюля"),
    ),
    reviewed=False,
)
