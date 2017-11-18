import discord
from discord.ext import commands

class lykak:
    def __init__(self, bot):
        self.bot = bot
        self.uselessswitchb = 0

    @commands.command()
    async def uselessswitch(self):
        """Useless Switch"""
        if self.uselessswitchb:
        	self.uselessswitchb = 0
        	await self.bot.say("Useless switch is now... **OFF**!")
        else:
        	self.uselessswitchb = 1
        	await self.bot.say("Useless switch is now... **ON**!")

    @commands.command()
    async def killthedemons(self, *, user : discord.Member):
    	"""Refrenced to DOOM: Repercussions of Evil"""
    	await self.bot.say("No, " + user.mention + ". You are the demons!")

def setup(bot):
    bot.add_cog(lykak(bot))