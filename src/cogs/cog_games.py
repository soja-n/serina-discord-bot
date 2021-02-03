import discord
from discord.ext import commands
from src import tools


def setup(client):
    client.add_cog(GamesCommands(client))


class GamesCommands(commands.Cog):
    def __init__(self, client):
        """Main commands of the bot, helps create channels and roles for given games."""
        self.client = client

    @commands.command()
    async def count_user_by_tag(self, ctx, game):
        roles = await tools.get_role(ctx, game)
        await ctx.send(len(roles.members))
        return len(roles.members)

    @commands.command(aliases=['ng', 'newGame'])
    async def new_game(self, ctx, *game):
        game = " ".join(game)
        if game != "":
            if await tools.get_role(ctx, game):
                await ctx.send("Use your brain! The game already exists...")
                return
            else:
                role = await tools.create_role(ctx, game)
                await tools.create_category_and_channels(ctx, role)
        else:
            await ctx.send("Are you stupid? Just add a **game** in the command or use *?help*.")

    @commands.command(aliases=['gl', 'gamesList'])
    async def list_games(self, ctx):
        embed = discord.Embed(title="**Games List**", description="Games played in here :")
        embed.set_thumbnail(url="https://images.emojiterra.com/twitter/v13.0/512px/1f3ae.png")
        for game in await tools.get_all_roles(ctx):
            if game.name not in ["bots-factory", "@everyone"]:
                embed.add_field(name=game.name, value=str(len(game.members)))
        await ctx.send(embed=embed)

    @commands.command(aliases=['ag', 'addGame'])
    async def attribute_role(self, ctx, user, *game):
        if user == "me":
            member = ctx.author
        else:
            member = await tools.get_member_by_id(ctx, user)
        game = " ".join(game)
        role = await tools.get_role(ctx, game)
        await member.add_roles(role)
        await ctx.send(f"{member.mention} plays {role}")
