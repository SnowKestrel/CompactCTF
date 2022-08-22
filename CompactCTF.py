import os
import discord
from discord.ext.commands import bot

client = discord.Client()


challengesnflags = {
    "Rzek ef ivjk wfi kyv nztbvu": "Aint no rest for the wicked",
    "Sqd'j we je xubb yv mu'hu qbhuqto jxuhu": "Can’t go to hell if we’re already there",
    "Sb lqoic owek i wyghrxv": "An angel with a shotgun",
    "Jo uif ezjoh xpset pg bvhvtuvt, gpvoefs boe gjstu fnqfsps pg uif spnbo fnqjsf: Ibwf J qmbzfe uif qbsu xfmm? Uifo "
    "bqqmbve bt J fyju.": "In the dying words of augustus, founder and first emperor of the roman empire: Have I played "
                          "the part well? Then applaud as I exit.",

}


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # dm requirements to check: if message.guild is None and message.author isn't the bot itself
    if message.guild is None and message.author != message.author.bot:
        for flag in challengesnflags:
            if message.content == challengesnflags[flag]:
                await message.channel.send("Congratulations! You decrypted the text correctly!")
                flag_found = True
                if message.content != challengesnflags[flag] and flag_found == False:
                    await message.channel.send("Nope, that doesn't seem right")
                    break


    if message.content == "_/":
        await message.channel.send(
            "Hello! I am CompactCTF, and I am a challenge coordinator of sorts. I have plenty of "
            "cybersecurity challenges for you to complete. The goal of these are to help you practice"
            "your skills for when you may need them most!")
    if message.content == "_/challenges":
        await message.channel.send("Here are all the challenges I have for you this month! Please decrypt the following"
                                   "and dm me the final decrypted product!")
        for challenge in challengesnflags:
            await message.channel.send(challenge)


client.run(os.getenv("bot_key"))
