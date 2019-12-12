import discord  #디스코드 불러오는것
import urllib.request   #웹사이트 읽을려고
from bs4 import BeautifulSoup  # web scraping 해서 필요한것들만 찾으려는 작업 web data extraction

client = discord.Client() # 디스코드 셋업하기 위하는 용도

class DiscordBot:

    @client.event
    async def on_ready():      #initializing bot
        print(client.user.id)
        print('ready')
        game= discord.Game('test_bot') #봇 상태를 알려주기 위해서 재미로 넣음
        await client.change_presence(status=discord.Status.online, activity=game)

    #봇이 온라인 상태일떄 이 메세지를 받고 응답하고 아니면 대답안함.
    @client.event
    async def on_message(message): #slected message 들어오면 실행

        if(discord.Status.online):
            if message.content.startswith('hi') | message.content.startswith('hello'):
                await message.channel.send('sup bro!')

            if message.content.startswith('what are you doing?'):
                await message.channel.send('I am here to help you ')

            if message.content.startswith('do you want to hangout with me?'):
                await message.channel.send('nah, I need to go to bed')

            if message.content.startswith('can you speak korean?'):
                await message.channel.send('노 아임 어메키칸')

            if message.content.startswith('who are you?'):
                await message.channel.send('I am a errand boy')

            if message.content.startswith('top tv shows'):
                url = 'https://www.rottentomatoes.com/top-tv/'
                html = urllib.request.urlopen(url).read()    # resulting data from the website provided by url
                soup = BeautifulSoup(html, 'html.parser')    # parse the result

                titleList = soup.find_all(class_='bold articleLink unstyled', limit=10)   # 이 클라스 이름을 써서 열개의 결과를 줘라

                for title in titleList:    # loop thru the every title in the title of list
                    await message.channel.send(title.getText())
                    await message.channel.send('http://www.rottentomatoes.com' + title.attrs['href'])

            if message.content.startswith('logout'):
                await client.change_presence(status=discord.Status.offline)

        if message.content.startswith('connect'):
            await client.change_presence(status=discord.Status.online)

    file_content = open("secret.txt").read()
    client.run(file_content)        # 커넥션할때 토큰 써야함

bot = DiscordBot() # 이 클라스를 실행하라
