from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import PEASANT_GIRL, PEASANT_MALE, PEASANT_WIFE

# Журавкинцы въ книгѣ чужого прихода — ЦГАРМ 57-7-54 (Подлясово, 1900–1918), найдено по OCR Яндексъ.Архива,
# прочитано по скану 07.11.2026; reviewed=False. Годъ на листѣ ушелъ въ корешокъ: 1912 — по мѣсту въ дѣлѣ
# (части 1 слѣдующихъ лѣтъ начинаются на сканахъ ≈314, ≈345 и ≈375, а сканъ 380 — 1915 г.). Провѣрить.

other_births_1912_podlyasovo = birth_records(
    "ЦГАРМ", "57", "7", "54", "Подлясово", "",
    1912,
    *birth_month(Month.MARCH,
        birth(9, Gender.FEMALE, 24, 25,
              child=person("Матрена"),
              father=person("Иванъ", last_name_orig="Демешкинъ", status=PEASANT_MALE, residence="Журавкино", comment="отчество у корешка («…новъ»), фамилія читается неувѣренно"),
              mother=person("Домна", "Андреева", status=PEASANT_WIFE),
              god_parent1=person("Степанъ", "Ивановъ", last_name_orig="Вечняевъ", status=PEASANT_MALE),
              god_parent2=person("Марѳа", "Ѳеодорова", last_name_orig="Антошкина", status=PEASANT_GIRL, residence="Журавкино"),
              comment="Яндексъ.Архивъ 57-7-54, сканъ 288"),
    ),
    reviewed=False,
)

# Авдаловцы въ московской книгѣ 1912 г. — ЦГА Москвы 203-782-588 (Покровская ц. Сретенскаго сорока; второй
# экземпляръ — 2126-2-117, сканъ 173), прочитано по оригиналу 07.11.2026.
other_births_1912_moscow_pokrovskaya = birth_records(
    "ЦГА Москвы", "203", "782", "588", "Москва", "Покровская",
    1912,
    *birth_month(Month.DECEMBER,
        birth(347, Gender.MALE, 28, 28,
              child=person("Іоаннъ"),
              father=person("Прокопій", "Михайловъ", last_name_orig="Шаровъ", status=PEASANT_MALE, residence="Авдалово", comment="«Шаровъ, онъ же Шеринъ»; «въ домѣ Ведихина»"),
              mother=person("Марія", "Егорова", status=PEASANT_WIFE),
              god_parent1=person("Григорій", "Васильевъ", last_name_orig="Макушкинъ", status=PEASANT_MALE, comment="Рязанской губ., Пронскаго у., Юраковской вол., села Филатова"),
              god_parent2=person("Варвара", "Васильева", last_name_orig="Нефедова", status=PEASANT_WIFE, comment="Рязанскаго у., Троице-Лисуновской вол., села Незнанова"),
              comment="Яндексъ.Архивъ 203-782-588, сканъ 398; крестилъ свящ. Василій Смирновъ; умеръ 10 января 1913 г."),
    ),
    reviewed=False,
)
