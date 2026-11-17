"""The landlords' statuses of this village's books. The DSL imports them from here (`from corpus.statuses
import …`); verso reads them through the workspace (`[corpus] dir`), in the order of `__all__`."""
from corpus import statuses_zhuravkino as _village
from corpus.statuses_zhuravkino import *  # noqa: F403

__all__: list[str] = []
__all__ += _village.__all__

CHILD_ESTATE_ALIASES: dict[str, str] = dict(_village.CHILD_ESTATE_ALIASES)
ESTATE_ALIASES: dict[str, str] = dict(_village.ESTATE_ALIASES)
