import logging
from pprint import pprint

from opsdroid.skill import Skill
from opsdroid.matchers import match_parse
import aiohttp


class WeatherSkill(Skill):

    async def get_weather(self, city: str):
        api_url = "https://api.openweathermap.org/data/2.5/weather?q="
        parameters = "{}&units={}&appid={}".format(
            city, self.config['units'], self.config['api-key']
        )

        async with aiohttp.ClientSession() as session:
            response = await session.get(api_url + parameters)
        return await response.json()

    @match_parse(r'weather in {city}')
    async def weather(self, event):
        # print("\n\n\n")
        # pprint(event.entities)
        # print("\n\n\n")
        city = event.entities['city']['value']
        logging.info(f"weather request for -> {city}")
        weather_data = await self.get_weather(city)
        print(weather_data)

        await event.respond(f"It's {weather_data['weather'][0]['description']} in {city},"
                            f" temperature is {weather_data['main']['temp']} and humidity is"
                            f" {weather_data['main']['humidity']}")
