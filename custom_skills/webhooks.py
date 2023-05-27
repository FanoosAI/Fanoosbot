import json
import logging
from aiohttp.web import Request, Response
from opsdroid.skill import Skill
from opsdroid.matchers import match_webhook


class ButtonsSkill(Skill):
    @match_webhook('buttons')
    async def buttons(self, event: Request):
        logging.info(f"Request for buttons -> {event}")
        data = await event.json()
        logging.info(f"Request data: {data}")
        response_body = [
            {
                "name": "Hi",
                "id": 1
            },
            {
                "name": "Bye",
                "id": 2
            },
            {
                "name": "Help?",
                "id": 3
            },
        ]
        response_body = json.JSONEncoder().encode(response_body)
        return Response(body=response_body, status=200)

    @match_webhook('health_check')
    async def health_check(self, event: Request):
        logging.info("Health check request")
        return Response(body="OK", status=200)
