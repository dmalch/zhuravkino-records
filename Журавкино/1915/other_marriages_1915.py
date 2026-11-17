from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import PEASANT_GIRL, PEASANT_MALE

# Журавкинка въ книгѣ чужого прихода 1915 г. — ЦГАРМ 57-4-1240 (Спасскій у., с. Булдыгино), найдено по OCR
# Яндексъ.Архива, прочитано по оригиналу 07.11.2026; reviewed=False. Въ отчетѣ по Яндексу записано 1905 —
# шапка листа «1915».
# Поручители: первые двое — со стороны жениха, вторые — невѣсты.

other_marriages_1915_buldygino = marriage_records(
    "ЦГАРМ", "57", "4", "1240", "Булдыгино", "",
    1915,
    *marriage_month(Month.APRIL,
        marriage(7, 3,
                 groom=person("Алексѣй", "Андреевъ", last_name_orig="Кочановъ", status=PEASANT_MALE, residence="Булдыгино"),
                 groom_marriage_num=1, groom_age=19,
                 bride=person("Матрона", "Евѳимова", last_name_orig="Косова", status=PEASANT_GIRL, residence="Журавкино"),
                 bride_marriage_num=1, bride_age=17,
                 witness1=person("Иванъ", "Евѳимовъ", last_name_orig="Шестаковъ", status=PEASANT_MALE, residence="Булдыгино"),
                 witness2=person("Матвѣй", "Игнатьевъ", last_name_orig="Ивановъ", status=PEASANT_MALE, residence="Булдыгино"),
                 witness3=person("Тимоѳей", "Ѳеодоровъ", last_name_orig="Митинъ", status=PEASANT_MALE, residence="Булдыгино"),
                 witness4=person("Матвѣй", "Ивановъ", last_name_orig="Ивашкинъ", status=PEASANT_MALE, residence="Булдыгино"),
                 comment="Яндексъ.Архивъ 57-4-1240, сканъ 103; вѣнчалъ свящ. Іоаннъ Платоновъ"),
    ),
    reviewed=False,
)
