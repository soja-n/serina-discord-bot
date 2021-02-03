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

    @commands.command(aliases=['newGame'])
    async def ng(self, ctx, *game):
        """Add a new game to the server."""
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

    @commands.command(aliases=['addGame'])
    async def ag(self, ctx, user, *game):
        """Attribute a game role to a user."""
        if user == "me":
            member = ctx.author
        else:
            member = await tools.get_member_by_id(ctx, user)
        game = " ".join(game)
        role = await tools.get_role(ctx, game)
        await member.add_roles(role)
        await ctx.send(f"{member.mention} plays {role}")
