"""The landlords' statuses of Журавкино's and Авдалово's books (one parish): Слепцовы, Ишеевы,
Енгалычевы, Кугушевы, Свищов, Моисеева, Путятин.

One of the villages' modules of the corpus's statuses (2026-11-16): `corpus.statuses` gathers them under the
name the DSL imports and the library reads; a village's public repository (tools/publish_village) carries its
own module alone. Their names are in every record's ratchet print: renaming one is DSL v2, never a cleanup.
"""
from verso.ru.dsl import Gender, Status

# In definition order, not sorted: the order is the catalog's (corpus/statuses.py gathers
# the villages' modules in it).
__all__ = [  # noqa: RUF022
    "SLEPTSOV_MI_PEASANT_MALE",
    "SLEPTSOV_IT_PEASANT_MALE",
    "SLEPTSOV_IT_PEASANT_GIRL",
    "SLEPTSOV_TI_PEASANT_MALE",
    "SLEPTSOV_TI_PEASANT_FEMALE",
    "SLEPTSOV_GM_PEASANT_MALE",
    "SLEPTSOV_GM_PEASANT_FEMALE",
    "SLEPTSOV_GM_PEASANT_GIRL",
    "SLEPTSOV_GM_PEASANT_WIFE",
    "SLEPTSOV_PL_PEASANT_MALE",
    "SLEPTSOV_EF_PEASANT_MALE",
    "SLEPTSOV_EF_PEASANT_FEMALE",
    "SLEPTSOV_EF_PEASANT_SON",
    "SLEPTSOV_EF_PEASANT_BOY",
    "SLEPTSOV_EFD_PEASANT_MALE",
    "SLEPTSOV_G_PEASANT_MALE",
    "SLEPTSOV_G_PEASANT_FEMALE",
    "SLEPTSOV_GM_PEASANT_SON",
    "SLEPTSOV_TI_PEASANT_GIRL",
    "SLEPTSOV_TI_PEASANT_BOY",
    "SLEPTSOV_AT_PEASANT_MALE",
    "SLEPTSOV_AT_PEASANT_FEMALE",
    "SLEPTSOV_AT_PEASANT_GIRL",
    "SLEPTSOV_AT_PEASANT_BOY",
    "SLEPTSOV_AT_PEASANT_SON",
    "SLEPTSOV_AT_PEASANT_DAUGHTER",
    "SLEPTSOV_AT_DVOROVY",
    "SLEPTSOV_AT_DVOROVY_SON",
    "SLEPTSOV_AT_DVOROVY_DAUGHTER",
    "SLEPTSOV_AI_PEASANT_MALE",
    "SLEPTSOV_AI_PEASANT_FEMALE",
    "SLEPTSOV_AI_PEASANT_LEGAL_WIFE",
    "SLEPTSOV_AI_PEASANT_GIRL",
    "SLEPTSOV_AI_PEASANT_MAIDEN",
    "SLEPTSOV_AI_PEASANT_BOY",
    "SLEPTSOV_AI_PEASANT_SON",
    "SLEPTSOV_AI_PEASANT_DAUGHTER",
    "SLEPTSOV_AI_SOLDIER_WIFE",
    "SLEPTSOV_AI_DVOROVY",
    "SLEPTSOV_AI_DVOROVY_WIFE",
    "SLEPTSOV_AI_DVOROVY_SON",
    "SLEPTSOV_AI_DVOROVY_DAUGHTER",
    "SLEPTSOV_GG_PEASANT_MALE",
    "SLEPTSOV_GG_PEASANT_MAIDEN",
    "SLEPTSOV_AG_DVOROVY",
    "SLEPTSOV_AG_DVOROVY_LEGAL_WIFE",
    "SLEPTSOV_AG_DVOROVY_SON",
    "SLEPTSOV_AG_DVOROVY_DAUGHTER",
    "SLEPTSOV_AG_PEASANT_MALE",
    "SLEPTSOV_AG_PEASANT_FEMALE",
    "SLEPTSOV_AG_PEASANT_SON",
    "SLEPTSOV_AG_PEASANT_DAUGHTER",
    "SLEPTSOV_AG_PEASANT_WIFE",
    "SLEPTSOV_AG_PEASANT_MAIDEN",
    "SLEPTSOV_GM_PEASANT_BOY",
    "SLEPTSOV_E_PEASANT_MALE",
    "SLEPTSOV_EF_PEASANT_GIRL",
    "SLEPTSOV_GG_PEASANT_FEMALE",
    "SLEPTSOV_GG_PEASANT_DAUGHTER",
    "SLEPTSOV_GG_PEASANT_DAUGHTER_MAIDEN",
    "SLEPTSOV_GG_DVOROVY",
    "SLEPTSOV_GG_DVOROVY_LEGAL_WIFE",
    "SLEPTSOV_GG_DVOROVY_SON",
    "SLEPTSOV_GG_DVOROVY_DAUGHTER",
    "SLEPTSOV_GG_LEGAL_WIFE",
    "SLEPTSOV_AG_LEGAL_WIFE",
    "SLEPTSOV_AI_LEGAL_WIFE",
    "SLEPTSOV_AT_LEGAL_WIFE",
    "SLEPTSOV_LA_PEASANT_MALE",
    "SLEPTSOV_LA_PEASANT_FEMALE",
    "SLEPTSOV_LA_LEGAL_WIFE",
    "SLEPTSOV_ED_PEASANT_MALE",
    "SLEPTSOV_ED_PEASANT_FEMALE",
    "SLEPTSOV_ED_LEGAL_WIFE",
    "SLEPTSOV_GM_PEASANT_DAUGHTER",
    "SLEPTSOV_EF_PEASANT_DAUGHTER",
    "SLEPTSOV_GG_PEASANT_SON",
    "SLEPTSOV_TI_PEASANT_SON",
    "SLEPTSOV_TI_PEASANT_DAUGHTER",
    "SLEPTSOV_ED_PEASANT_SON",
    "SLEPTSOV_ED_PEASANT_DAUGHTER",
    "SLEPTSOV_LA_PEASANT_SON",
    "SLEPTSOV_LA_PEASANT_DAUGHTER",
    "SLEPTSOV_IT_PEASANT_SON",
    "SLEPTSOV_IT_PEASANT_DAUGHTER",
    "SLEPTSOV_PL_PEASANT_SON",
    "SLEPTSOV_PL_PEASANT_DAUGHTER",
    "SLEPTSOV_MI_PEASANT_SON",
    "SLEPTSOV_MI_PEASANT_DAUGHTER",
    "ISHEEV_ET_PEASANT_MALE",
    "ISHEEV_ET_PEASANT_FEMALE",
    "ISHEEV_ET_PEASANT_SON",
    "ISHEEV_ET_PEASANT_DAUGHTER",
    "ISHEEV_ET_PEASANT_MAIDEN",
    "ISHEEV_ET_LEGAL_WIFE",
    "ISHEEV_VP_PEASANT_MALE",
    "ISHEEV_VP_PEASANT_FEMALE",
    "ISHEEV_VP_PEASANT_SON",
    "ISHEEV_VP_PEASANT_DAUGHTER",
    "ENGALYCHEV_IA_PEASANT_MALE",
    "ENGALYCHEV_IA_COL_PEASANT_MALE",
    "ENGALYCHEV_IAL_PEASANT_MALE",
    "ENGALYCHEV_AI_PEASANT_MALE",
    "ENGALYCHEV_AI_PEASANT_FEMALE",
    "ENGALYCHEV_AN_PEASANT_MALE",
    "ENGALYCHEV_AN_PEASANT_FEMALE",
    "ENGALYCHEV_NA_PEASANT_MALE",
    "ENGALYCHEV_NA_PEASANT_FEMALE",
    "ENGALYCHEV_NA_PEASANT_SON",
    "ENGALYCHEV_NA_PEASANT_DAUGHTER",
    "ENGALYCHEV_NA_PEASANT_MAIDEN",
    "ENGALYCHEV_NA_LEGAL_WIFE",
    "ENGALYCHEV_MI_PEASANT_MALE",
    "ENGALYCHEV_MI_PEASANT_FEMALE",
    "ENGALYCHEV_MI_PEASANT_SON",
    "ENGALYCHEV_MI_PEASANT_DAUGHTER",
    "ENGALYCHEV_AI_PEASANT_SON",
    "ENGALYCHEV_AI_PEASANT_DAUGHTER",
    "ENGALYCHEV_IA_PEASANT_SON",
    "ENGALYCHEV_IA_PEASANT_DAUGHTER",
    "ENGALYCHEV_IAL_PEASANT_SON",
    "ENGALYCHEV_IAL_PEASANT_DAUGHTER",
    "KUGUSHEV_VI_PEASANT_MALE",
    "KUGUSHEV_AI_PEASANT_MALE",
    "KUGUSHEV_AI_PEASANT_FEMALE",
    "KUGUSHEV_IV_PEASANT_MALE",
    "KUGUSHEV_IV_PEASANT_FEMALE",
    "KUGUSHEV_IV_PEASANT_SON",
    "KUGUSHEV_IV_LEGAL_WIFE",
    "KUGUSHEV_AI_LEGAL_WIFE",
    "KUGUSHEV_IV_PEASANT_DAUGHTER",
    "KUGUSHEV_IV_PEASANT_MAIDEN",
    "KUGUSHEV_AI_PEASANT_SON",
    "KUGUSHEV_AI_PEASANT_DAUGHTER",
    "KUGUSHEV_VI_PEASANT_SON",
    "KUGUSHEV_VI_PEASANT_DAUGHTER",
    "SVISHCHOV_IV_PEASANT_MALE",
    "MOISEEVA_PB_PEASANT_MALE",
    "SVISHCHOV_IV_PEASANT_SON",
    "SVISHCHOV_IV_PEASANT_DAUGHTER",
    "MOISEEVA_PB_PEASANT_SON",
    "MOISEEVA_PB_PEASANT_DAUGHTER",
    "PUTYATIN_DS_PEASANT_MALE",
    "PUTYATIN_DS_PEASANT_FEMALE",
    "PUTYATIN_DS_LEGAL_WIFE",
    "PUTYATIN_DS_PEASANT_SON",
    "PUTYATIN_DS_PEASANT_DAUGHTER",
]

# Landlord peasants — Слепцов (Авдалово/Журавкино)
SLEPTSOV_MI_PEASANT_MALE = Status("крестьянин помещика Михаила Ивановича Слепцова", Gender.MALE)
SLEPTSOV_IT_PEASANT_MALE = Status("крестьянин помещика Ивана Трофимовича Слепцова", Gender.MALE)
SLEPTSOV_IT_PEASANT_GIRL = Status("девка из крестьян помещика Ивана Трофимовича Слепцова", Gender.FEMALE)
SLEPTSOV_TI_PEASANT_MALE = Status("крестьянин помещика Трофима Ивановича Слепцова", Gender.MALE)
SLEPTSOV_TI_PEASANT_FEMALE = Status("крестьянка помещика Трофима Ивановича Слепцова", Gender.FEMALE)
SLEPTSOV_GM_PEASANT_MALE = Status("крестьянин помещика Григория Михайловича Слепцова", Gender.MALE)
SLEPTSOV_GM_PEASANT_FEMALE = Status("крестьянка помещика Григория Михайловича Слепцова", Gender.FEMALE)
SLEPTSOV_GM_PEASANT_GIRL = Status("девка из крестьян помещика Григория Михайловича Слепцова", Gender.FEMALE)
SLEPTSOV_GM_PEASANT_WIFE = Status("крестьянская жена помещика Григория Михайловича Слепцова", Gender.FEMALE)
SLEPTSOV_PL_PEASANT_MALE = Status("крестьянин помещицы Прасковьи Львовны Слепцовой", Gender.MALE)
SLEPTSOV_EF_PEASANT_MALE = Status("крестьянин помещицы Екатерины Фирсовны Слепцовой", Gender.MALE)
SLEPTSOV_EF_PEASANT_FEMALE = Status("крестьянка помещицы Екатерины Фирсовны Слепцовой", Gender.FEMALE)
SLEPTSOV_EF_PEASANT_SON = Status("крестьянский сын помещицы Екатерины Фирсовны Слепцовой", Gender.MALE)
SLEPTSOV_EF_PEASANT_BOY = Status("отрок из крестьянин помещицы Екатерины Фирсовны Слепцовой", Gender.MALE)
SLEPTSOV_EFD_PEASANT_MALE = Status("крестьянин помещицы Екатерины Федосиевны Слепцовой", Gender.MALE)
SLEPTSOV_G_PEASANT_MALE = Status("крестьянин помещика Григория Слепцова", Gender.MALE)
SLEPTSOV_G_PEASANT_FEMALE = Status("крестьянка помещика Григория Слепцова", Gender.FEMALE)
SLEPTSOV_GM_PEASANT_SON = Status("крестьянский сын помещика Григория Михайловича Слепцова", Gender.MALE)
SLEPTSOV_TI_PEASANT_GIRL = Status("девка из крестьян помещика Трофима Ивановича Слепцова", Gender.FEMALE)
SLEPTSOV_TI_PEASANT_BOY = Status("отрок из крестьян помещика Трофима Ивановича Слепцова", Gender.MALE)
SLEPTSOV_AT_PEASANT_MALE = Status("крестьянин помещика Алексея Трофимовича Слепцова", Gender.MALE)
SLEPTSOV_AT_PEASANT_FEMALE = Status("крестьянка помещика Алексея Трофимовича Слепцова", Gender.FEMALE)
SLEPTSOV_AT_PEASANT_GIRL = Status("девка из крестьян помещика Алексея Трофимовича Слепцова", Gender.FEMALE)
SLEPTSOV_AT_PEASANT_BOY = Status("отрок из крестьян помещика Алексея Трофимовича Слепцова", Gender.MALE)
SLEPTSOV_AT_PEASANT_SON = Status("крестьянский сын помещика Алексея Трофимовича Слепцова", Gender.MALE)
SLEPTSOV_AT_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Алексея Трофимовича Слепцова", Gender.FEMALE)
SLEPTSOV_AT_DVOROVY = Status("дворовый человек помещика Алексея Трофимовича Слепцова", Gender.MALE)
SLEPTSOV_AT_DVOROVY_SON = Status("сын дворового человека помещика Алексея Трофимовича Слепцова", Gender.MALE)
SLEPTSOV_AT_DVOROVY_DAUGHTER = Status("дочь дворового человека помещика Алексея Трофимовича Слепцова", Gender.FEMALE)
SLEPTSOV_AI_PEASANT_MALE = Status("крестьянин помещицы Анастасии Ивановны Слепцовой", Gender.MALE)
SLEPTSOV_AI_PEASANT_FEMALE = Status("крестьянка помещицы Анастасии Ивановны Слепцовой", Gender.FEMALE)
SLEPTSOV_AI_PEASANT_LEGAL_WIFE = Status("законная жена крестьянина помещицы Анастасии Ивановны Слепцовой", Gender.FEMALE)
SLEPTSOV_AI_PEASANT_GIRL = Status("девка из крестьян помещицы Анастасии Ивановны Слепцовой", Gender.FEMALE)
SLEPTSOV_AI_PEASANT_MAIDEN = Status("девица из крестьян помещицы Анастасии Ивановны Слепцовой", Gender.FEMALE)
SLEPTSOV_AI_PEASANT_BOY = Status("отрок из крестьян помещицы Анастасии Ивановны Слепцовой", Gender.MALE)
SLEPTSOV_AI_PEASANT_SON = Status("крестьянский сын помещицы Анастасии Ивановны Слепцовой", Gender.MALE)
SLEPTSOV_AI_PEASANT_DAUGHTER = Status("крестьянская дочь помещицы Анастасии Ивановны Слепцовой", Gender.FEMALE)
SLEPTSOV_AI_SOLDIER_WIFE = Status("солдатская жена из крестьян помещицы Анастасии Ивановны Слепцовой", Gender.FEMALE)
SLEPTSOV_AI_DVOROVY = Status("дворовый человек помещицы Анастасии Ивановны Слепцовой", Gender.MALE)
SLEPTSOV_AI_DVOROVY_WIFE = Status("жена дворового человека помещицы Анастасии Ивановны Слепцовой", Gender.FEMALE)
SLEPTSOV_AI_DVOROVY_SON = Status("сын дворового человека помещицы Анастасии Ивановны Слепцовой", Gender.MALE)
SLEPTSOV_AI_DVOROVY_DAUGHTER = Status("дочь дворового человека помещицы Анастасии Ивановны Слепцовой", Gender.FEMALE)
SLEPTSOV_GG_PEASANT_MALE = Status("крестьянин помещика Григория Григорьевича Слепцова", Gender.MALE)
SLEPTSOV_GG_PEASANT_MAIDEN = Status("девица из крестьян помещика Григория Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_AG_DVOROVY = Status("дворовый человек помещика Алексея Григорьевича Слепцова", Gender.MALE)
SLEPTSOV_AG_DVOROVY_LEGAL_WIFE = Status("законная жена дворового человека помещика Алексея Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_AG_DVOROVY_SON = Status("сын дворового человека помещика Алексея Григорьевича Слепцова", Gender.MALE)
SLEPTSOV_AG_DVOROVY_DAUGHTER = Status("дочь дворового человека помещика Алексея Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_AG_PEASANT_MALE = Status("крестьянин помещика Алексея Григорьевича Слепцова", Gender.MALE)
SLEPTSOV_AG_PEASANT_FEMALE = Status("крестьянка помещика Алексея Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_AG_PEASANT_SON = Status("крестьянский сын помещика Алексея Григорьевича Слепцова", Gender.MALE)
SLEPTSOV_AG_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Алексея Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_AG_PEASANT_WIFE = Status("жена крестьянина помещика Алексея Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_AG_PEASANT_MAIDEN = Status("девица из крестьян помещика Алексея Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_GM_PEASANT_BOY = Status("отрок из крестьян помещика Григория Михайловича Слепцова", Gender.MALE)
SLEPTSOV_E_PEASANT_MALE = Status("крестьянин помещицы Екатерины Слепцовой", Gender.MALE)
SLEPTSOV_EF_PEASANT_GIRL = Status("девка из крестьян помещицы Екатерины Фирсовны Слепцовой", Gender.FEMALE)
SLEPTSOV_GG_PEASANT_FEMALE = Status("крестьянка помещика Григория Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_GG_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Григория Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_GG_PEASANT_DAUGHTER_MAIDEN = Status("крестьянская дочь девица помещика Григория Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_GG_DVOROVY = Status("дворовый человек помещика Григория Григорьевича Слепцова", Gender.MALE)
SLEPTSOV_GG_DVOROVY_LEGAL_WIFE = Status("законная жена дворового человека помещика Григория Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_GG_DVOROVY_SON = Status("сын дворового человека помещика Григория Григорьевича Слепцова", Gender.MALE)
SLEPTSOV_GG_DVOROVY_DAUGHTER = Status("дочь дворового человека помещика Григория Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_GG_LEGAL_WIFE = Status("законная жена крестьянина помещика Григория Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_AG_LEGAL_WIFE = Status("законная жена крестьянина помещика Алексея Григорьевича Слепцова", Gender.FEMALE)
SLEPTSOV_AI_LEGAL_WIFE = Status("законная жена крестьянина помещицы Анастасии Ивановны Слепцовой", Gender.FEMALE)
SLEPTSOV_AT_LEGAL_WIFE = Status("законная жена крестьянина помещика Алексея Трофимовича Слепцова", Gender.FEMALE)
SLEPTSOV_LA_PEASANT_MALE = Status("крестьянин помещицы Любви Александровны Слепцовой", Gender.MALE)
SLEPTSOV_LA_PEASANT_FEMALE = Status("крестьянка помещицы Любви Александровны Слепцовой", Gender.FEMALE)
SLEPTSOV_LA_LEGAL_WIFE = Status("законная жена крестьянина помещицы Любви Александровны Слепцовой", Gender.FEMALE)
SLEPTSOV_ED_PEASANT_MALE = Status("крестьянин помещицы Елизаветы Дмитриевны Слепцовой", Gender.MALE)
SLEPTSOV_ED_PEASANT_FEMALE = Status("крестьянка помещицы Елизаветы Дмитриевны Слепцовой", Gender.FEMALE)
SLEPTSOV_ED_LEGAL_WIFE = Status("законная жена крестьянина помещицы Елизаветы Дмитриевны Слепцовой", Gender.FEMALE)

# Слепцов child forms completing the estates attested as birth parents, so
# `child_status_for` (below) can derive a newborn's сословие from the parent.
# Wording is the mechanical transform of each estate's _MALE form —
# «крестьянин помещика X» → «крестьянский сын/крестьянская дочь помещика X» —
# matching the already-attested pairs (e.g. SLEPTSOV_EF_PEASANT_SON).
SLEPTSOV_GM_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Григория Михайловича Слепцова", Gender.FEMALE)
SLEPTSOV_EF_PEASANT_DAUGHTER = Status("крестьянская дочь помещицы Екатерины Фирсовны Слепцовой", Gender.FEMALE)
SLEPTSOV_GG_PEASANT_SON = Status("крестьянский сын помещика Григория Григорьевича Слепцова", Gender.MALE)
SLEPTSOV_TI_PEASANT_SON = Status("крестьянский сын помещика Трофима Ивановича Слепцова", Gender.MALE)
SLEPTSOV_TI_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Трофима Ивановича Слепцова", Gender.FEMALE)
SLEPTSOV_ED_PEASANT_SON = Status("крестьянский сын помещицы Елизаветы Дмитриевны Слепцовой", Gender.MALE)
SLEPTSOV_ED_PEASANT_DAUGHTER = Status("крестьянская дочь помещицы Елизаветы Дмитриевны Слепцовой", Gender.FEMALE)
SLEPTSOV_LA_PEASANT_SON = Status("крестьянский сын помещицы Любви Александровны Слепцовой", Gender.MALE)
SLEPTSOV_LA_PEASANT_DAUGHTER = Status("крестьянская дочь помещицы Любви Александровны Слепцовой", Gender.FEMALE)
SLEPTSOV_IT_PEASANT_SON = Status("крестьянский сын помещика Ивана Трофимовича Слепцова", Gender.MALE)
SLEPTSOV_IT_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Ивана Трофимовича Слепцова", Gender.FEMALE)
SLEPTSOV_PL_PEASANT_SON = Status("крестьянский сын помещицы Прасковьи Львовны Слепцовой", Gender.MALE)
SLEPTSOV_PL_PEASANT_DAUGHTER = Status("крестьянская дочь помещицы Прасковьи Львовны Слепцовой", Gender.FEMALE)
SLEPTSOV_MI_PEASANT_SON = Status("крестьянский сын помещика Михаила Ивановича Слепцова", Gender.MALE)
SLEPTSOV_MI_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Михаила Ивановича Слепцова", Gender.FEMALE)

# Landlord peasants — Ишеев (Авдалово/Журавкино)
# Екатерина Трофимовна Ишеева (ISHEEV_ET) is NÉE СЛЕПЦОВА — b. 1792 d. 1856,
# daughter of Трофим Иванович Слепцов, so a sister of SLEPTSOV_AT / SLEPTSOV_IT,
# and wife of ISHEEV_VP below. The 1816 Авдалово revision calls her Слепцова;
# only the 1833+ metric books call her Ишеева. Same landlady, so a peasant moving
# between the two forms has NOT changed owner. See
# regional-rules/zhuravkino/names-and-estates.md.
ISHEEV_ET_PEASANT_MALE = Status("крестьянин помещицы Екатерины Трофимовны Ишеевой", Gender.MALE)
ISHEEV_ET_PEASANT_FEMALE = Status("крестьянка помещицы Екатерины Трофимовны Ишеевой", Gender.FEMALE)
ISHEEV_ET_PEASANT_SON = Status("крестьянский сын помещицы Екатерины Трофимовны Ишеевой", Gender.MALE)
ISHEEV_ET_PEASANT_DAUGHTER = Status("крестьянская дочь помещицы Екатерины Трофимовны Ишеевой", Gender.FEMALE)
ISHEEV_ET_PEASANT_MAIDEN = Status("девица из крестьян помещицы Екатерины Трофимовны Ишеевой", Gender.FEMALE)
ISHEEV_ET_LEGAL_WIFE = Status("законная жена крестьянина помещицы Екатерины Трофимовны Ишеевой", Gender.FEMALE)
ISHEEV_VP_PEASANT_MALE = Status("крестьянин помещика Василия Петровича Ишеева", Gender.MALE)
ISHEEV_VP_PEASANT_FEMALE = Status("крестьянка помещика Василия Петровича Ишеева", Gender.FEMALE)
# Ишеев child forms for `child_status_for` (see the Слепцов block above).
ISHEEV_VP_PEASANT_SON = Status("крестьянский сын помещика Василия Петровича Ишеева", Gender.MALE)
ISHEEV_VP_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Василия Петровича Ишеева", Gender.FEMALE)

# Landlord peasants — Енгалычев (Авдалово/Журавкино)
ENGALYCHEV_IA_PEASANT_MALE = Status("крестьянин помещика Ивана Алексеевича Енгалычева", Gender.MALE)
ENGALYCHEV_IA_COL_PEASANT_MALE = Status("крестьянин полковника Ивана Алексеевича Енгалычева", Gender.MALE)
ENGALYCHEV_IAL_PEASANT_MALE = Status("крестьянин помещика Ивана Александровича Енгалычева", Gender.MALE)
ENGALYCHEV_AI_PEASANT_MALE = Status("крестьянин помещика Александра Ивановича Енгалычева", Gender.MALE)
ENGALYCHEV_AI_PEASANT_FEMALE = Status("крестьянка помещика Александра Ивановича Енгалычева", Gender.FEMALE)
ENGALYCHEV_AN_PEASANT_MALE = Status("крестьянин помещицы Анны Ивановны Енгалычевой", Gender.MALE)
ENGALYCHEV_AN_PEASANT_FEMALE = Status("крестьянка помещицы Анны Ивановны Енгалычевой", Gender.FEMALE)
ENGALYCHEV_NA_PEASANT_MALE = Status("крестьянин помещика Николая Александровича Енгалычева", Gender.MALE)
ENGALYCHEV_NA_PEASANT_FEMALE = Status("крестьянка помещика Николая Александровича Енгалычева", Gender.FEMALE)
ENGALYCHEV_NA_PEASANT_SON = Status("крестьянский сын помещика Николая Александровича Енгалычева", Gender.MALE)
ENGALYCHEV_NA_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Николая Александровича Енгалычева", Gender.FEMALE)
ENGALYCHEV_NA_PEASANT_MAIDEN = Status("девица из крестьян помещика Николая Александровича Енгалычева", Gender.FEMALE)
ENGALYCHEV_NA_LEGAL_WIFE = Status("законная жена крестьянина помещика Николая Александровича Енгалычева", Gender.FEMALE)
ENGALYCHEV_MI_PEASANT_MALE = Status("крестьянин помещицы Марии Ивановны Енгалычевой", Gender.MALE)
ENGALYCHEV_MI_PEASANT_FEMALE = Status("крестьянка помещицы Марии Ивановны Енгалычевой", Gender.FEMALE)
# Енгалычев child forms for `child_status_for` (see the Слепцов block above).
# ENGALYCHEV_IA children use the помещик wording; the полковник variant
# (ENGALYCHEV_IA_COL_PEASANT_MALE) folds onto the same estate.
ENGALYCHEV_MI_PEASANT_SON = Status("крестьянский сын помещицы Марии Ивановны Енгалычевой", Gender.MALE)
ENGALYCHEV_MI_PEASANT_DAUGHTER = Status("крестьянская дочь помещицы Марии Ивановны Енгалычевой", Gender.FEMALE)
ENGALYCHEV_AI_PEASANT_SON = Status("крестьянский сын помещика Александра Ивановича Енгалычева", Gender.MALE)
ENGALYCHEV_AI_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Александра Ивановича Енгалычева", Gender.FEMALE)
ENGALYCHEV_IA_PEASANT_SON = Status("крестьянский сын помещика Ивана Алексеевича Енгалычева", Gender.MALE)
ENGALYCHEV_IA_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Ивана Алексеевича Енгалычева", Gender.FEMALE)
ENGALYCHEV_IAL_PEASANT_SON = Status("крестьянский сын помещика Ивана Александровича Енгалычева", Gender.MALE)
ENGALYCHEV_IAL_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Ивана Александровича Енгалычева", Gender.FEMALE)

# Landlord peasants — Кугушев (Авдалово/Журавкино)
KUGUSHEV_VI_PEASANT_MALE = Status("крестьянин помещика Василия Ивановича Кугушева", Gender.MALE)
KUGUSHEV_AI_PEASANT_MALE = Status("крестьянин помещицы Анны Ивановны Кугушевой", Gender.MALE)
KUGUSHEV_AI_PEASANT_FEMALE = Status("крестьянка помещицы Анны Ивановны Кугушевой", Gender.FEMALE)
KUGUSHEV_IV_PEASANT_MALE = Status("крестьянин помещика Ивана Васильевича Кугушева", Gender.MALE)
KUGUSHEV_IV_PEASANT_FEMALE = Status("крестьянка помещика Ивана Васильевича Кугушева", Gender.FEMALE)
KUGUSHEV_IV_PEASANT_SON = Status("крестьянский сын помещика Ивана Васильевича Кугушева", Gender.MALE)
KUGUSHEV_IV_LEGAL_WIFE = Status("законная жена крестьянина помещика Ивана Васильевича Кугушева", Gender.FEMALE)
KUGUSHEV_AI_LEGAL_WIFE = Status("законная жена крестьянина помещицы Анны Ивановны Кугушевой", Gender.FEMALE)
# Кугушев child forms for `child_status_for` (see the Слепцов block above).
KUGUSHEV_IV_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Ивана Васильевича Кугушева", Gender.FEMALE)
KUGUSHEV_IV_PEASANT_MAIDEN = Status("девица из крестьян помещика Ивана Васильевича Кугушева", Gender.FEMALE)
KUGUSHEV_AI_PEASANT_SON = Status("крестьянский сын помещицы Анны Ивановны Кугушевой", Gender.MALE)
KUGUSHEV_AI_PEASANT_DAUGHTER = Status("крестьянская дочь помещицы Анны Ивановны Кугушевой", Gender.FEMALE)
KUGUSHEV_VI_PEASANT_SON = Status("крестьянский сын помещика Василия Ивановича Кугушева", Gender.MALE)
KUGUSHEV_VI_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Василия Ивановича Кугушева", Gender.FEMALE)

# Landlord peasants — other (Авдалово/Журавкино)
SVISHCHOV_IV_PEASANT_MALE = Status("крестьянин помещика Ивана Владимировича Свищова", Gender.MALE)
MOISEEVA_PB_PEASANT_MALE = Status("крестьянин помещицы Прасковьи Богдановны Моисеевой", Gender.MALE)
# Свищов / Моисеева child forms for `child_status_for` (see the Слепцов block above).
SVISHCHOV_IV_PEASANT_SON = Status("крестьянский сын помещика Ивана Владимировича Свищова", Gender.MALE)
SVISHCHOV_IV_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Ивана Владимировича Свищова", Gender.FEMALE)
MOISEEVA_PB_PEASANT_SON = Status("крестьянский сын помещицы Прасковьи Богдановны Моисеевой", Gender.MALE)
MOISEEVA_PB_PEASANT_DAUGHTER = Status("крестьянская дочь помещицы Прасковьи Богдановны Моисеевой", Gender.FEMALE)
# Путятин — first attested in МК Журавкино 1840 (рождение №6), spelled «помещика
# Дмитрия Степановича ПУТЯШИНА»: same given name and patronymic, one letter from
# Путятинъ, same Авдалово estate, the year before the next mention. Read as the same
# landlord and given these constants; if the scan shows a genuinely different family,
# this is the record to revisit.
#
# 1841 (рождения №5, №11, №31; смерть №25) calls him «помѣщика Путятина» with no given
# name. The given name that the DS key and these full-form statuses are built on comes
# from брак №2 of 1842 — «Помѣщика Димитрія Степанова Путятина» — and the 1840 record
# independently carries the same Дмитрий Степанович.
#
# The estate is Авдалово: all 25 people booked to it across 1840-1842 are there
# (`[landlords]` of corpus/estates.toml).
PUTYATIN_DS_PEASANT_MALE = Status("крестьянин помещика Дмитрия Степановича Путятина", Gender.MALE)
PUTYATIN_DS_PEASANT_FEMALE = Status("крестьянка помещика Дмитрия Степановича Путятина", Gender.FEMALE)
PUTYATIN_DS_LEGAL_WIFE = Status("законная жена крестьянина помещика Дмитрия Степановича Путятина", Gender.FEMALE)
# Путятин child forms for `child_status_for` (see the Слепцов block above).
PUTYATIN_DS_PEASANT_SON = Status("крестьянский сын помещика Дмитрия Степановича Путятина", Gender.MALE)
PUTYATIN_DS_PEASANT_DAUGHTER = Status("крестьянская дочь помещика Дмитрия Степановича Путятина", Gender.FEMALE)


# Estates the catalog spells under several bases, for `child_status_for` — the corpus's part
# of `verso.ru.domain.statuses._ESTATE_ALIASES`: the полковник is the помещик Иван Алексеевич
# Енгалычев.
CHILD_ESTATE_ALIASES: dict[str, str] = {
    "ENGALYCHEV_IA_COL_PEASANT": "ENGALYCHEV_IA_PEASANT",
}

# The corpus's part of `parent_status.ESTATE_ALIASES` (PSA): the полковник's peasants are the помещик's.
ESTATE_ALIASES: dict[str, str] = {
    "ENGALYCHEV_IA_COL_PEASANT": "ENGALYCHEV_IA_PEASANT",
}
