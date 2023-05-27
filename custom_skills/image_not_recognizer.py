import logging
from opsdroid.skill import Skill
from opsdroid.matchers import match_event
from opsdroid.events import Image, Message


class ImageNotRecognizerSkill(Skill):
    @match_event(Image)
    async def image_not_recognized(self, event):
        logging.info(f"image not recognizer -> {event}")
        await event.respond(Message('I don\'t understand images! stop sending me them! goddd!'))
