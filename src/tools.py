import discord


async def get_member_by_id(ctx, str_id):
    for char in "<@!>":
        str_id = str_id.replace(char, "")
    return await ctx.guild.fetch_member(int(str_id))


async def get_all_roles(ctx):
    roles = await ctx.guild.fetch_roles()
    return roles


async def get_category(ctx, category):
    for cat in ctx.guild.categories:
        if cat.name == category:
            return cat


async def get_role(ctx, game):
    roles = await get_all_roles(ctx)
    for role in roles:
        if role.name == game:
            return role


async def create_category_and_channels(ctx, role):
    category = await ctx.guild.create_category(name=role.name, overwrites={
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        role: discord.PermissionOverwrite(read_messages=True)
    })
    await ctx.guild.create_voice_channel(name="vocal", category=category, permissions_synced=True)
    await ctx.guild.create_text_channel(name="discussions", category=category, permissions_synced=True)
    await ctx.send(f"The category and the channels are created for __**{category}**__, enjoy your game.")


async def create_role(ctx, game):
    role = await ctx.guild.create_role(name=game, mentionable=True,
                                       permissions=discord.Permissions(
                                           read_messages=True,
                                           send_messages=True,
                                           speak=True,
                                           change_nickname=True
                                       ))
    await ctx.send(f"You can now use the role __**{role}**__.")
    return role
