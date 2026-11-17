from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import MESHCHANIN, PEASANT_FEMALE, PEASANT_GIRL, PEASANT_MALE, PEASANT_WIFE

# Журавкинцы и авдаловцы въ московскихъ книгахъ 1910 г. — ЦГА Москвы 203-782-178 (Ивановскій сорокъ) и
# 203-782-563 (Крестовоздвиженская ц. Сретенскаго сорока; второй экземпляръ — 2126-2-115), найдено по OCR
# Яндексъ.Архива, прочитано по оригиналамъ 07.11.2026; reviewed=False.

other_births_1910_moscow_ivanovsky = birth_records(
    "ЦГА Москвы", "203", "782", "178", "Москва", "",
    1910,
    *birth_month(Month.MARCH,
        birth(46, Gender.MALE, 27, 4, k_month=Month.APRIL,
              child=person("Валентинъ"),
              father=person("Ѳеодоръ", "Тимоѳеевъ", last_name_orig="Баландинъ", status=PEASANT_MALE, residence="Журавкино"),
              mother=person("Александра", "Филиппова", status=PEASANT_WIFE),
              god_parent1=person("Андрей", "Егоровъ", last_name_orig="Ѳоминъ", status=MESHCHANIN, comment="мѣщанинъ г. Коломны"),
              god_parent2=person("Іуліанія", "Тимоѳеева", last_name_orig="Журикова", status=PEASANT_GIRL, comment="Зарубкинской вол., дер. Новыхъ Выселокъ"),
              comment="Яндексъ.Архивъ 203-782-178, сканъ 162; «д. Ульянова»; годъ въ шапкѣ «1910»; крестилъ свящ. "
                      "Іаковъ Остроумовъ; повторено въ 2122-2-12 (сканъ 342) и 2122-1-323 (сканъ 61)"),
    ),
    reviewed=False,
)

other_births_1910_moscow_krestovozdvizhenskaya = birth_records(
    "ЦГА Москвы", "203", "782", "563", "Москва", "Крестовоздвиженская",
    1910,
    *birth_month(Month.OCTOBER,
        birth(265, Gender.FEMALE, 10, 12,
              child=person("Анастасія"),
              father=person("Прокопій", "Михайловъ", last_name_orig="Шеровъ", status=PEASANT_MALE, residence="Авдалово", comment="«въ домѣ Миронова»"),
              mother=person("Марія", "Егорова", status=PEASANT_WIFE),
              god_parent1=person("Григорій", "Васильевъ", last_name_orig="Макушкинъ", status=PEASANT_MALE, comment="Рязанской губ., Пронскаго у., Юраковской вол., села Филатова"),
              god_parent2=person("Варвара", "Васильева", last_name_orig="Нефедова", status=PEASANT_FEMALE, comment="Рязанскаго у., Троице-Лисуновской вол., села Незнанова"),
              comment="Яндексъ.Архивъ 203-782-563, сканъ 108 (второй экз. 2126-2-115, сканъ 135, «1910»); крестилъ "
                      "свящ. Александръ Писаревъ; названа по сестрѣ Анастасіи, умершей въ февралѣ того же года"),
    ),
    reviewed=False,
)
