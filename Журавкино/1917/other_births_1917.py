from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_GIRL, PEASANT_MALE, PEASANT_WIFE

# Журавкинцы и авдаловцы въ книгахъ чужихъ приходовъ 1917 г. — ЦГАРМ 57-4-1308 (с. Покровскія Селищи),
# ЦГА Москвы 2132-2-202 (Московскій у.) и 203-780-4890 (с. Перово), найдено по OCR Яндексъ.Архива, прочитано по
# оригиналамъ 07.11.2026; reviewed=False.

other_births_1917_pokrovskie_selishchi = birth_records(
    "ЦГАРМ", "57", "4", "1308", "Покровские Селищи", "",
    1917,
    *birth_month(Month.MAY,
        birth(18, Gender.FEMALE, 31, 1, k_month=Month.JUNE,
              child=person("Анна"),
              father=person("Георгій", "Николаевъ", last_name_orig="Барминъ", status=PEASANT_MALE, residence="Журавкино"),
              mother=person("Евгенія", "Максимова", status=PEASANT_WIFE),
              god_parent1=person("Василій", "Аѳанасьевъ", last_name_orig="Абмашкинъ", status=PEASANT_MALE, residence="Журавкино"),
              god_parent2=person("Наталія", "Максимова", last_name_orig="Бункина", status=PEASANT_FEMALE, residence="Журавкино"),
              comment="Яндексъ.Архивъ 57-4-1308, сканъ 514; «Села Журовкина»; № 18 стоитъ въ первой графѣ счета "
                      "(книга, видимо, ведетъ одинъ счетъ); крестили свящ. Іоаннъ Короляковъ и Ермилъ Соколовъ"),
    ),
    reviewed=False,
)

other_births_1917_moscow_uezd = birth_records(
    "ЦГА Москвы", "2132", "2", "202", "Москва", "",
    1917,
    *birth_month(Month.SEPTEMBER,
        birth(3, Gender.MALE, 11, 14,
              child=person("Константинъ"),
              father=person("Ѳедоръ", "Сергѣевичъ", last_name_orig="Стручковъ", status=PEASANT_MALE, residence="Авдалово"),
              mother=person("Анна", "Абрамовна", status=PEASANT_WIFE),
              god_parent1=person("Прокопій", "Евѳимовичъ", last_name_orig="Родинъ", status=PEASANT_MALE, comment="Майданской вол., дер. Горбуновки"),
              god_parent2=person("Анна", "Васильевна", last_name_orig="Уткова", status=PEASANT_FEMALE, comment="Владимірской губ.; имя и фамилія читаются неувѣренно"),
              comment="Полныя отчества («Сергѣевичъ», «Абрамовна» …) — такъ въ подлинникѣ. Яндексъ.Архивъ 2132-2-202, сканъ 180 (Московскій уѣздъ, Шереметьевская …); крестилъ свящ. "
                      "Николай Холмогоровъ. Второй экземпляръ — 203-780-4923, сканъ 87: тамъ мать по OCR «Евдокія "
                      "Иванова Фролова» — не свѣрено"),
    ),
    reviewed=False,
)

other_births_1917_perovo = birth_records(
    "ЦГА Москвы", "203", "780", "4890", "Перово", "",
    1917,
    *birth_month(Month.FEBRUARY,
        birth(27, Gender.FEMALE, 3, 3,
              child=person("Анна"),
              father=person("Степанъ", "Яковлевъ", last_name_orig="Кузнецовъ", status=PEASANT_MALE, comment="«записанъ по запискѣ, принесенной воспріемникомъ Левинымъ»"),
              mother=person("Анна", "Иванова", last_name_orig="Кузнецова", status=PEASANT_WIFE, residence="Авдалово"),
              god_parent1=person("Димитрій", "Ульяновъ", last_name_orig="Левинъ", status=PEASANT_MALE, comment="Майдановской вол., села Пичкиряева"),
              god_parent2=person("Дарья", "Степанова", last_name_orig="Агапова", status=PEASANT_GIRL, comment="Спасскаго у., дер. Марьевки"),
              comment="Яндексъ.Архивъ 203-780-4890, сканъ 218; крестилъ протоіерей Василій Горскій; повторено въ "
                      "2132-2-145, сканъ 183"),
    ),
    reviewed=False,
)
