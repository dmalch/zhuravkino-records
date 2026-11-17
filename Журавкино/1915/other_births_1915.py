from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import MESHCHANIN, PEASANT_GIRL, PEASANT_MALE, PEASANT_WIFE

# Журавкинцы въ книгѣ чужого прихода 1915 г. — ЦГАРМ 57-7-54 (Подлясово), найдено по OCR Яндексъ.Архива,
# прочитано по скану 07.11.2026; reviewed=False.

other_births_1915_podlyasovo = birth_records(
    "ЦГАРМ", "57", "7", "54", "Подлясово", "",
    1915,
    *birth_month(Month.JUNE,
        birth(32, Gender.MALE, 27, 29,
              child=person("Георгій"),
              father=person("Иванъ", "Егоровъ", last_name_orig="Амелькинъ", status=PEASANT_MALE, residence="Журавкино"),
              mother=person("Домна", "Егорова", status=PEASANT_WIFE),
              god_parent1=person("Николай", "Ивановъ", last_name_orig="Буренинъ", status=MESHCHANIN, residence="Кадом"),
              god_parent2=person("Анна", "Григорьева", last_name_orig="Цукарова", status=PEASANT_GIRL, residence="Подлясово", comment="фамилія читается неувѣренно"),
              comment="Яндексъ.Архивъ 57-7-54, сканъ 380; умеръ 7 іюля того же года (other_deaths_1915)"),
    ),
    reviewed=False,
)

# Авдаловцы въ московской книгѣ 1915 г. — ЦГА Москвы 203-782-628 (Николаевская въ Столпахъ ц. Сретенскаго сорока;
# второй экземпляръ — 2126-2-120, сканъ 102), прочитано по оригиналу 07.11.2026.
other_births_1915_moscow_nikolaevskaya = birth_records(
    "ЦГА Москвы", "203", "782", "628", "Москва", "Николаевская",
    1915,
    *birth_month(Month.JULY,
        birth(191, Gender.FEMALE, 12, 15,
              child=person("Марія"),
              father=person("Прокопій", "Михайловъ", last_name_orig="Шеровъ", status=PEASANT_MALE, residence="Авдалово"),
              mother=person("Марія", "Егорова", status=PEASANT_WIFE),
              god_parent1=person("Стефанъ", "Емельяновъ", last_name_orig="Савушкинъ", status=PEASANT_MALE, comment="Рязанской губ., Пронскаго у., Юраковской вол.; фамилія читается неувѣренно"),
              god_parent2=person("Варвара", "Васильева", last_name_orig="Нефедова", status=PEASANT_WIFE, comment="Рязанскаго у., Троице-Лисуновской вол., села Незнанова"),
              comment="Яндексъ.Архивъ 203-782-628, сканъ 133; крестилъ протоіерей Алексій Грузовъ"),
    ),
    reviewed=False,
)
