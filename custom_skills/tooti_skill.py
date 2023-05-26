import logging
from opsdroid.skill import Skill
from opsdroid.matchers import match_parse


class TootiSkill(Skill):
    @match_parse(r'tooti {whatever}')
    async def tooti(self, event):
        logging.info(f"Ping tooti -> {event}")
        await event.respond(f"{event.entities['whatever']['value']} ba\'a\'a\'a\'a\'a\'a\'a\'")
