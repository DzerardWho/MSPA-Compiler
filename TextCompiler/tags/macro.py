from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Type

if TYPE_CHECKING:
    from TextCompiler.tags.baseTag import BaseTag


class Macro:
    @staticmethod
    def parse(
            data: Dict[str, str],
            baseTag: Type[BaseTag],
            tempTags: Dict[str, Type[BaseTag]] = None
    ):
        if not (data['args']):
            return

        for i in data['args']:
            for new, old in i.items():
                new, old = new.lower(), old.lower()

                if tempTags is not None:
                    dst = tempTags
                    if old in tempTags:
                        src = tempTags
                    else:
                        src = baseTag.tags
                else:
                    dst = baseTag.tags
                    src = baseTag.tags

                if not (new and old) or new in dst:
                    continue

                tag = src.get(old)
                if tag:
                    dst[new] = tag
