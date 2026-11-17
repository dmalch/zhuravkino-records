from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import PEASANT_MALE, PEASANT_WIFE

# Журавкинцы въ московской книгѣ 1908 г. — ЦГА Москвы 203-782-308 (Василіе-Кесарійская ц. Никитскаго сорока;
# второй экземпляръ — 2124-2-36, сканъ 68), найдено по OCR Яндексъ.Архива, прочитано по оригиналу 07.11.2026;
# reviewed=False. Близнецы, крещены вмѣстѣ; восприемники записаны одной строкой на обоихъ.

other_births_1908_moscow_vasilie_kesariyskaya = birth_records(
    "ЦГА Москвы", "203", "782", "308", "Москва", "Василие-Кесарийская",
    1908,
    *birth_month(Month.FEBRUARY,
        birth(180, Gender.MALE, 18, 26,
              child=person("Іоаннъ"),
              father=person("Иванъ", "Ивановъ", last_name_orig="Игнатовъ", status=PEASANT_MALE, residence="Журавкино"),
              mother=person("Ксенія", "Александрова", status=PEASANT_WIFE),
              god_parent1=person("Михаилъ", "Владиміровъ", status="дворянин"),
              god_parent2=person("Таисія", "Владимірова", last_name_orig="Ильдашева", status="дворянка"),
              comment="Яндексъ.Архивъ 203-782-308, сканъ 69; близнецъ Евдокіи (жен. № 170); умеръ 7 марта"),
        birth(170, Gender.FEMALE, 18, 26,
              child=person("Евдокія"),
              father=person("Иванъ", "Ивановъ", last_name_orig="Игнатовъ", status=PEASANT_MALE, residence="Журавкино"),
              mother=person("Ксенія", "Александрова", status=PEASANT_WIFE),
              god_parent1=person("Михаилъ", "Владиміровъ", status="дворянин"),
              god_parent2=person("Таисія", "Владимірова", last_name_orig="Ильдашева", status="дворянка"),
              comment="Яндексъ.Архивъ 203-782-308, сканъ 69; близнецъ Іоанна (муж. № 180); умерла 25 іюня"),
    ),
    reviewed=False,
)
