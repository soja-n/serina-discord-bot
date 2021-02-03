from discord.ext import commands

client = commands.Bot(command_prefix="?", description="roles management")


@client.event
async def on_ready():
    print("Ready")


if __name__ == "__main__":
    print("Loading cogs : ")
    for cog in ["cogs.cog_admin", "cogs.cog_games"]:
        try:
            client.load_extension(cog)
            print(cog.split(".")[1])
        except ImportError:
            print(f"failed to load {cog.split('.')[1]}")
    print("Logging in ...")
    client.run(open("../discord-bot-token.txt", "r").read())
