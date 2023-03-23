import discord
from discord.ext import commands
from discord import app_commands

class Bot(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        '''when bot is online, set status and print to console'''
        await self.bot.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Activity(type=discord.ActivityType.listening, name="U Can't Touch This by MC 🔨"))
        print('------')
        print(f'Logged in as {self.bot.user} (ID: {self.bot.user.id}!)')
        print('------')

async def setup(bot: commands.Bot):
    await bot.add_cog(Bot(bot))