from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIFE

# Авдаловцы въ московской книгѣ 1907 г. — ЦГА Москвы 203-782-525 (Крестовоздвиженская ц. Сретенскаго сорока;
# второй экземпляръ — 203-782-526), найдено по OCR Яндексъ.Архива, прочитано по оригиналу 07.11.2026;
# reviewed=False.

other_births_1907_moscow_krestovozdvizhenskaya = birth_records(
    "ЦГА Москвы", "203", "782", "525", "Москва", "Крестовоздвиженская",
    1907,
    *birth_month(Month.DECEMBER,
        birth(323, Gender.FEMALE, 23, 30,
              child=person("Анастасія"),
              father=person("Прокопій", "Михайловъ", last_name_orig="Шеровъ", status=PEASANT_MALE, residence="Авдалово", comment="«въ домѣ Миронова»"),
              mother=person("Марія", "Егорова", status=PEASANT_WIFE),
              god_parent1=person("Яковъ", "Спиридоновъ", last_name_orig="Васинъ", status=PEASANT_MALE, residence="Боковой Майдан"),
              god_parent2=person("Ольга", "Петрова", last_name_orig="Макушкина", status=PEASANT_FEMALE, comment="Рязанской губ., Пронскаго у., Юраковской вол., села Филатова"),
              comment="Яндексъ.Архивъ 203-782-525, сканъ 178; крестилъ свящ. Александръ Писаревъ; "
                      "умерла 13 февраля 1910 г. (other_deaths_1910)"),
    ),
    reviewed=False,
)
