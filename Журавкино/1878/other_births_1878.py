from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import KAZENNYJ_PEASANT_MALE, PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIDOW

# Журавкинецъ въ книгѣ чужого прихода 1878 г. — ЦГАРМ 57-2-138 (сводная книга Темниковскаго уѣзда, разделъ
# «Чершных» = с. Чермные), найдено по OCR Яндексъ.Архива, прочитано по скану 07.11.2026; reviewed=False.
# Церковь въ заголовкѣ книги не названа.

other_births_1878_chermnye = birth_records(
    "ЦГАРМ", "57", "2", "138", "Чермные", "",
    1878,
    *birth_month(Month.FEBRUARY,
        birth(11, Gender.FEMALE, 11, 12,
              child=person("Агафія"),
              father=person("Михаилъ", "Ивановъ", status=KAZENNYJ_PEASANT_MALE, residence="Журавкино", comment="умеръ до рожденія дочери"),
              mother=person("Ѳекла", "Иванова", status=PEASANT_WIDOW, residence="Юзга", comment="«оставшаяся беременной послѣ смерти мужа»"),
              god_parent1=person("Семенъ", "Ивановъ", status=PEASANT_MALE, comment="деревни «Гари» (?), читается неуверенно"),
              god_parent2=person("Матрена", "Васильева", status=PEASANT_FEMALE),
              comment="Яндексъ.Архивъ 57-2-138, сканъ 681"),
    ),
    reviewed=False,
)
