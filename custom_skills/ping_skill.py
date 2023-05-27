import logging

from opsdroid.skill import Skill
from opsdroid.matchers import match_regex, match_event
from opsdroid.events import Typing, Message


class PingSkill(Skill):
    @match_regex(r'ping')
    async def ping(self, event):
        logging.info(f"Ping skill -> {event}")
        await event.respond('pong')

