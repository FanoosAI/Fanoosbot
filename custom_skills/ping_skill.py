import logging

from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class PingSkill(Skill):
    @match_regex(r'ping')
    async def ping(self, event):
        logging.info(f"Ping skill -> {event}")
        await event.respond('pong')
