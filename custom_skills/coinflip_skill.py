from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
import logging
import random


class CoinFlipSkill(Skill):
    @match_regex(r'flip a coin')
    async def flip_a_coin(self, event):
        logging.info(f"coin flip skill -> {event}")
        await event.respond(random.choice(['heads', 'tails']))
