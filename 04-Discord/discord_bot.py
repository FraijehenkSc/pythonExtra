import discord

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)


filepointer=open(R"C:\Users\Ninor\OneDrive\Documenten\ma\School\DiscordbotToken.txt", "r")
bottoken=filepointer.readline()
filepointer.close()

@client.event
async def on_ready():
   
    guild = client.guilds[0]
  
    print(guild.name, "is the name of the server")


    print(client.user, "has connected to the client")

    channel = guild.text_channels[0]
    print(channel.name, "is the name of the channel")
    await channel.send("I'm online!")

@client.event
async def on_message(message):
    print(message.channel.name, "the message was posted from this channel")
    print(message.content)
    print(message.author,"is the user who wrote the message")
    print(message.created_at,"is when the message was posted")
    print(message.channel,"is the channel this message was posted in")
    

    if message.author.bot == False:
        await message.channel.send(str(message.author) + " is geweldig!")


client.run(bottoken)