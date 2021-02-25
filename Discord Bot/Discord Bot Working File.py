import discord

# https://discordapp.com/oauth2/authorize?client_id=814592689865228309&scope=bot&permissions=0 -> bot toevoegen
# server id Testserver = 814591913268215890

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "algemeen":
            await channel.send(f"""Welkom in onze server {member.mention}!""")


@client.event
async def on_message(message):
    id = client.get_guild(814591913268215890)
    channels = ["imbit-bot"]
    special_users = ["DeSmoek#1551"]

    if str(message.channel) in channels and str(message.author) in special_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")
    else:
        print(f"""Gebruiker:{message.author} heeft {message.content} geprobeerd in  #{message.channel}""")

    if message.content == "!help":
        embed = discord.Embed(title="Help pagina", description="IMBIT bot commands")
        embed.add_field(name="!hello", value="Groet")
        embed.add_field(name="!users", value="Print het aantal leden")
        await message.channel.send(content=None, embed=embed)

@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("imbit") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="Da gaan we ni doen")


client.run(token)
