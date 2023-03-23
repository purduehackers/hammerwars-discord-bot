import asyncio
import random
import discord
from discord.ext import commands
from discord import app_commands

# note: 305566021664899072 is Oohwo#1324's discord id

class Announcements(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name='morbius', description="Remember when [um] and then proceeded to [uh] all over everyone? [ah] times.")
    async def morbius(self, interaction: discord.Interaction, um: str, uh: str, ah: str) -> None:
        await prompt_wait(interaction.channel)
        await interaction.response.send_message(f'Remember when {um} and then proceeded to {uh} all over everyone?\n\n{ah} times.', ephemeral=True)
    
    # tbh there was probably a better way to do this but i got lazy
    # note to self: plan out embeds in discohook (website) and then send them either here or using the send_embed cmd
    @app_commands.command(name='send_faq', description="Send FAQ Message")
    async def send_faq(self, interaction: discord.Interaction):
        await prompt_wait(interaction.channel)
        if interaction.user.id == 305566021664899072:
            await interaction.response.send_message(f'FAQ Posted!', ephemeral=True)
            await interaction.channel.send(f'**Frequently Asked Questions**\nIf anyone has any questions about the competition, feel free to DM any of the organizers or post in #hammer-talk!')
            embed1=discord.Embed(title="**Is this a Hackathon?**", description=f"Nope, you will be solving coding interview problems through the CodeForces website.\nUntil then... you can also check for any [#⌨hackathons](https://discord.com/channels/772576325897945119/936335216459517993) by grabbing the Hackathon role in [#❓roles](https://discord.com/channels/772576325897945119/809619986275762178)!", color=discord.Color.from_str('#e47200'))
            await prompt_wait(interaction.channel)
            await interaction.channel.send(embed=embed1)
            embed2=discord.Embed(title="**Are we able to work in groups?**", description="Nope! You will tackle programming problems individually.", color=discord.Color.from_str('#e69b00'))
            await prompt_wait(interaction.channel)
            await interaction.channel.send(embed=embed2)
            embed3=discord.Embed(title="**How does CodeForces Work?**", description="Right now, we are planning on hosting an introductory workshop on how CodeForces works... this will be held on the day-of!\n\nYou will also receive an event packet a few days prior with instructions on how to work with CodeForces... stay tuned!", color=discord.Color.from_str('#e6b400'))
            await prompt_wait(interaction.channel)
            await interaction.channel.send(embed=embed3)
            embed4=discord.Embed(title="**Is this competition limited to only CS majors?**", description="This competition is open to all majors!", color=discord.Color.from_str('#e6cc00'))
            await prompt_wait(interaction.channel)
            await interaction.channel.send(embed=embed4)
            embed5=discord.Embed(title="**How do I know if I will be receiving a t-shirt?**", description="You will be notified by email if you will be receiving a t-shirt on the day-of!", color=discord.Color.from_str('#e5de00'))
            await prompt_wait(interaction.channel)
            await interaction.channel.send(embed=embed5)
        else:
            await interaction.response.send_message(f"You don't have permission to use this command!", ephemeral=True)

    @app_commands.command(name='send_readme', description="Send README Message")
    async def send_readme(self, interaction: discord.Interaction):
        if interaction.user.id == 305566021664899072:
            await prompt_wait(interaction.channel)
            await interaction.response.send_message(f'README Posted!', ephemeral=True)
            embed=discord.Embed(title="**Hammer Down and Code It Up!** 🔨💻", description=f"**HammerWars is back, bigger, and better than ever!**\n\n**Purdue Hackers** and the **Purdue Competitive Programming Union** will be hosting **HammerWars 2.0** — a Competitive Programming Competition sponsored by AWS and Deloitte on Saturday, April 1st. \n\nAll programmers, regardless of experience level, are welcome to participate. No prior experience in competitive programming is necessary. There will be free swag, food, as well as $1800 in prizes!\n\n**What is HammerWars?**\nHammerWars is a competitive programming competition that jumpstarts students' critical thinking skills by solving coding interview problems, which is essential to obtaining future internship and job opportunities.\n\nThe location, time, and venue will be released in the HammerWars category channels.\n\nBy signing up, you will receive an email containing a packet that includes all the necessary details for HammerWars a few days before the event.\n\nRegistration closes when we go over capacity. \n\nFor more information, check out our [website](https://hammerwars.purduehackers.com)!\n\nMake sure to join our Discord to receive updates and further communication about HammerWars!\n\nDiscord: https://puhack.horse/discord\nInstagram: [@PurdueHackers](https://www.instagram.com/purduehackers/)\nEmail: purduehackers@gmail.com", color=discord.Color.from_str('#e5de00'))
            embed.set_image(url="https://cdn.discordapp.com/attachments/426607203781312513/1087585527127080990/Hammer_Wars_Poster_1.jpg")
            await prompt_wait(interaction.channel)
            await interaction.channel.send(embed=embed)
        else:
            await interaction.response.send_message(f"You don't have permission to use this command!", ephemeral=True)

    @app_commands.command(name='send_msg', description="Send a message as a bot")
    async def send_msg(self, interaction: discord.Interaction, message: str, show:bool) -> None:
        if interaction.user.id == 305566021664899072:
            await interaction.response.send_message(f'Bang!', ephemeral=True)
            await prompt_wait(interaction.channel)
            await interaction.channel.send(f'{message}')
        else:
            await interaction.response.send_message(f"You don't have permission to use this command!", ephemeral=True)

    @app_commands.command(name='send_embed', description="Send an embed as a bot")
    async def send_embed(self, interaction: discord.Interaction, title: str, description: str, color: str):
        if interaction.user.id == 305566021664899072:
            await prompt_wait(interaction.channel)
            await interaction.response.send_message(f'Embed will be posted soon!', ephemeral=True)
            embed=discord.Embed(title=f'{title}', description=f'{description}', color=discord.Color.from_str(f'{color}'))
            await prompt_wait(interaction.channel)
            await interaction.channel.send(embed=embed)
        else:
            await interaction.response.send_message(f"You don't have permission to use this command!", ephemeral=True)

    @app_commands.command(name='send_prizes', description="Send Prizes Message")
    async def send_prizes(self, interaction: discord.Interaction):
        if interaction.user.id == 305566021664899072:
            await prompt_wait(interaction.channel)
            await interaction.response.send_message(f'Prizes Posted!', ephemeral=True)
            embed=discord.Embed(title="Check out our prizes!", color=discord.Color.from_str('#e5de00'))
            embed.set_image(url="https://cdn.discordapp.com/attachments/426607203781312513/1088267342049443860/Prizes_Poster.png")
            await prompt_wait(interaction.channel)
            await interaction.channel.send(embed=embed)
        else:
            await interaction.response.send_message(f"You don't have permission to use this command!", ephemeral=True)
    
async def prompt_wait(channel):
    '''shows lifelike typing in specified channel'''
    async with channel.typing():
        type_time = random.uniform(1, 2)
        await asyncio.sleep(type_time)

async def setup(bot: commands.Bot):
    await bot.add_cog(Announcements(bot))