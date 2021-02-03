from discord.ext import commands
import discord


def setup(client):
    client.add_cog(AdminCommands(client))


class AdminCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, nb: int):
        messages = await ctx.channel.history(limit=nb + 1).flatten()
        for message in messages:
            await message.delete()

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.User, *reason):
        reason = " ".join(reason)
        await ctx.guild.kick(user, reason=reason)
        await ctx.send(f"{user} has been kicked!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.User, *reason):
        reason = " ".join(reason)
        await ctx.guild.ban(user, reason=reason)
        await ctx.send(f"{user} has been banned")
