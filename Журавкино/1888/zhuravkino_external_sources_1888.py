from verso.ru.dsl import EventDate, Month, criminal_record, external_source_records, person
from verso.ru.dsl.statuses import PEASANT_MALE

# Судимость (criminal-record gazette) records — «Ведомости справок о судимости
# 1870–1927» (familio.org /catalogs/vss/). Журавкино residents found by searching
# the vss catalog by village surname and filtering the record text to
# с. Журавкина / Жеравкина, Майданская (Боково-Майданская) волость, Спасский уезд,
# Тамбовская губ. Each mints a duplicate proof profile to be reconciled later.
zhuravkino_external_sources_1888 = external_source_records(
    "Журавкино",
    criminal_record(
        person("Иванъ", "Ѳедоровъ", "Пуштаевъ", status=PEASANT_MALE, residence="Журавкино", occupation="хлебопашец"),
        age=44,  # → birth year derived: 1888 − 44 = 1844
        record_number=105086,
        date=EventDate(1888, Month.JUNE, 17),
        source_url="https://viewer.rsl.ru/ru/rsl01005425989?page=94",
        scan_file="scans/sudimost_ivan_pushtaev_1888.jpg",
        original_text=(
            "105086. ПУШТАЕВ, Иван Федоров. Кр. Спасск. у., Боково-Майданск. в., "
            "с. Журавкина (хлебопаш.), 44 л.; приг. Тамбов. Окр. С., по 3 ч. 354 ст. "
            "Улож., к тюрьму на 8 м. Исп. 17 Июня 1888 г."
        ),
        bibliography=(
            "Ведомость справок о судимости / изд. М-ва юстиции. — СПб.: Тип. "
            "Правительствующего Сената, 1872–1929. (РСЛ: rsl01005425989, скан с. 94.)"
        ),
        comment=(
            "Преступление: по ч. 3 ст. 354 Уложения о наказаниях уголовных и "
            "исправительных (конкретный состав в записи не раскрыт; нумерация "
            "статей зависит от редакции Уложения). "
            "Суд: Тамбовский окружной суд. "
            "Наказание: тюрьма 8 месяцев. Исполнено 17 июня 1888 г."
        ),
    ),
)
