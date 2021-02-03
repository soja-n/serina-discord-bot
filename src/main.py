import discord
from discord.ext import commands

TOKEN = open("discord-bot-token.txt", "r").read()
client = commands.Bot(command_prefix="?", description="roles management", help_command=None)
list_roles_untagged = ["bots-factory", "@everyone"]
cog_list = ["cogs.cog_admin", "cogs.cog_games"]


@client.event
async def on_ready():
    print("Ready")


@client.command(aliases=['h'])
async def help(ctx):
    embed = discord.Embed(title="**Commands help**", description="possible commands:")
    embed.set_thumbnail(url="https://hotemoji.com/images/dl/b/books-emoji-by-twitter.png")
    embed.add_field(name="**?ng *game* **",
                    value="Create new role and channels for a given game, use the game as an argument.",
                    inline=False)
    embed.add_field(name="**?gl **",
                    value="Return the list of all the played games on this server. Doesn't need any argument.",
                    inline=False)
    embed.add_field(name="**?ag @member *game* **",
                    value="Give a game role to a member, use user tag and game as arguments.",
                    inline=False)
    embed.add_field(name="**?clear *nb* **",
                    value="Allow an admin to remove a number nb of messages on the channel.",
                    inline=False)
    await ctx.send(embed=embed)


if __name__ == "__main__":
    print("Loading cogs : ")
    for cog in cog_list:
        try:
            client.load_extension(cog)
            print(cog.split(".")[1])
        except ImportError:
            print(f"failed to load {cog.split('.')[1]}")
    print("Logging in ...")
    client.run(TOKEN)
