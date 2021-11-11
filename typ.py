
#위성사진 제공 : https://www.weather.go.kr (기상청)

import discord
import urllib.request
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
 
@client.event
async def on_message(message):
    if message.content.startswith('!위성'):
        url = 'https://www.weather.go.kr/weather/images/satellite_service.jsp'
        res = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(res, 'html.parser')
        soup = soup.find("div", class_="image-player-slide")
        imgUrl = 'https://www.weather.go.kr' + soup.find("img")["src"]

        typoonEmbed = discord.Embed(title='천리안 2A호 위성사진', description='제공: 기상청', colour=discord.Colour.blue())
        typoonEmbed.set_image(url=imgUrl)
        await message.channel.send(embed=typoonEmbed)


client.run('★TOKEN★')
