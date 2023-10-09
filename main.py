import discord

intents = discord.Intents.default()
intents.message_content = True


cumle = random.randint(1,3)

if cumle == 1:
    return("onu oradan kaldır")

elif cumle == 2:
    return("Yapma")

elif cumle == 3:
    return("Çöp kovasına atlayabilirsin")




cop = ["çöp","çop","cop"]







@bot.event
async def on_message(message):
    if message.author != bot.user:
        content = message.content.lower()  
        for kelime in cop:
            if kelime in content:
                response = cumle()
                await message.channel.send(response)
                break


bot.run("MTE2MDk4ODE4MzIxNjAxMzMxMg.G_TYFU.UnpAl_Y7Lboq0Xk9nqCpeqxhDNsRDi70DhJBrQ")
