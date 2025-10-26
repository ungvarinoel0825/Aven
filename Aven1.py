import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")  

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as: {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")


@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

@bot.tree.command(name="ping", description="Bot answers if its online")
async def ping_slash(interaction: discord.Interaction):
    await interaction.response.send_message("pong!")


#----------------------------other-----------------------------------

""""

@bot.command()
async def gay(ctx):
    await ctx.send("<@1327932281985302560>, <@744579226908491837>, <@1228896470330114103>, <@630407889357373450>, <@795557329831460865>, <@1285367274806710313>, <@1430699012536926279>, <@1089501219082485821>")

@bot.tree.command(name="gay", description="Shows a list of gays")
async def gay_slash(interaction: discord.Interaction):
    await interaction.response.send_message("<@1327932281985302560>, <@744579226908491837>, <@1228896470330114103>, <@630407889357373450>, <@795557329831460865>, <@1285367274806710313>, <@1430699012536926279>, <@1089501219082485821>")


@bot.command()
async def npc(ctx):
    await ctx.send("<@744579226908491837>")

@bot.tree.command(name="npc", description="Shows a list of npcs")
async def npc_slash(interaction: discord.Interaction):
    await interaction.response.send_message("<@744579226908491837>")


@bot.command()
async def shortae(ctx):
    await ctx.send("<@1228896470330114103>")

@bot.tree.command(name="shortae", description="Pings shortae")
async def shortae_slash(interaction: discord.Interaction):
    await interaction.response.send_message("<@1228896470330114103>")


@bot.command()
async def smelly(ctx):
    await ctx.send("<@1383012588186767411>")

@bot.tree.command(name="smelly", description="Pings smelly ppl")
async def smelly_slash(interaction: discord.Interaction):
    await interaction.response.send_message(" <@1383012588186767411>")


@bot.command()
async def eat(ctx):
    await ctx.send("Todays food is...  <@1383012588186767411>!")

@bot.tree.command(name="eat", description="who are we eating today...")
async def eat_slash(interaction: discord.Interaction):
    await interaction.response.send_message("Todays food is...  <@1383012588186767411>!")

@bot.command()
async def cute(ctx):
    await ctx.send("Fuh nah :wilted_rose:")

@bot.tree.command(name="cute", description="Is rain emojis cute")
async def cute_slash(interaction: discord.Interaction):
    await interaction.response.send_message("Fuh nah :wilted_rose:")

"""

@bot.command()
async def fish(ctx):
    await ctx.send(file=discord.File("fsh-spin.gif"))

@bot.tree.command(name="fish", description="fish")
async def fish_slash(interaction: discord.Interaction):
    await interaction.response.defer()  
    await interaction.followup.send(file=discord.File("fsh-spin.gif"))

 
#--------------------------------------------------------------------


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        embed = discord.Embed(title="Member Kicked", color=discord.Color.red())
        message = (
            f"Member: {member.mention} ||({member.id})||\n"
            f"Reason: {reason if reason else 'None'}\n"
            f"Moderator: {ctx.author.mention} ||({ctx.author.id})||"
        )
        embed.add_field(name="\u200b", value=message, inline=False)
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("No permission ❌")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.tree.command(name="kick", description="Kick a member")
@app_commands.checks.has_permissions(kick_members=True)
async def kick_slash(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    try:
        await interaction.response.defer()
        await member.kick(reason=reason)
        embed = discord.Embed(title="Member Kicked", color=discord.Color.red())
        message = (
            f"Member: {member.mention} ||({member.id})||\n"
            f"Reason: {reason if reason else 'None'}\n"
            f"Moderator: {interaction.user.mention} ||({interaction.user.id})||"
        )
        embed.add_field(name="\u200b", value=message, inline=False)
        await interaction.response.send_message(embed=embed)
    except discord.Forbidden:
        await interaction.response.send_message("No permission ❌")
    except Exception as e:
        await interaction.response.send_message(f"Error: {e}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        embed = discord.Embed(title="Member Banned", color=discord.Color.red())
        message = (
            f"Member: {member.mention} ||({member.id})||\n"
            f"Reason: {reason if reason else 'None'}\n"
            f"Moderator: {ctx.author.mention} ||({ctx.author.id})||"
        )
        embed.add_field(name="\u200b", value=message, inline=False)
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("No permission ❌")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.tree.command(name="ban", description="Ban a member")
@app_commands.checks.has_permissions(ban_members=True)
async def ban_slash(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    try:
        await interaction.response.defer()
        await member.ban(reason=reason)
        embed = discord.Embed(title="Member Banned", color=discord.Color.red())
        message = (
            f"Member: {member.mention} ||({member.id})||\n"
            f"Reason: {reason if reason else 'None'}\n"
            f"Moderator: {interaction.user.mention} ||({interaction.user.id})||"
        )
        embed.add_field(name="\u200b", value=message, inline=False)
        await interaction.response.send_message(embed=embed)
    except discord.Forbidden:
        await interaction.response.send_message("No permission ❌")
    except Exception as e:
        await interaction.response.send_message(f"Error: {e}")


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.User, *, reason=None):
    try:
        await ctx.guild.unban(user, reason=reason)
        embed = discord.Embed(title="Member Unbanned", color=discord.Color.green())
        message = (
            f"Member: {user.mention} ||({user.id})||\n"
            f"Reason: {reason if reason else 'None'}\n"
            f"Moderator: {ctx.author.mention} ||({ctx.author.id})||"
        )
        embed.add_field(name="\u200b", value=message, inline=False)
        await ctx.send(embed=embed)
    except discord.NotFound:
        await ctx.send("User not banned ❌")
    except discord.Forbidden:
        await ctx.send("No permission ❌")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.tree.command(name="unban", description="Unban a member")
@app_commands.checks.has_permissions(ban_members=True)
async def unban_slash(interaction: discord.Interaction, user: discord.User, reason: str = None):
    try:
        await interaction.response.defer()
        await interaction.guild.unban(user, reason=reason)
        embed = discord.Embed(title="Member Unbanned", color=discord.Color.green())
        message = (
            f"Member: {user.mention} ||({user.id})||\n"
            f"Reason: {reason if reason else 'None'}\n"
            f"Moderator: {interaction.user.mention} ||({interaction.user.id})||"
        )
        embed.add_field(name="\u200b", value=message, inline=False)
        await interaction.response.send_message(embed=embed)
    except discord.NotFound:
        await interaction.response.send_message("User not banned ❌")
    except discord.Forbidden:
        await interaction.response.send_message("No permission ❌")
    except Exception as e:
        await interaction.response.send_message(f"Error: {e}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return


    if bot.user.mentioned_in(message) and len(message.content.split()) == 1:
        prefix_commands = [cmd.name for cmd in bot.commands]
        slash_commands = [cmd.name for cmd in bot.tree.get_commands()]

        embed = discord.Embed(
            title="Available Commands",
            description="Here are the current avaliable commands::",
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="Prefix Commands (`.`)",
            value=", ".join([f".{c}" for c in prefix_commands]) or "No prefix commands.",
            inline=False
        )

        embed.add_field(
            name="Slash Commands (`/`)",
            value=", ".join([f"/{c}" for c in slash_commands]) or "No commands.",
            inline=False
        )

        await message.channel.send(embed=embed)

    await bot.process_commands(message)

#----------------info---------------------

@bot.tree.command(name="info", description="Get information about the bot")
async def info(interaction: discord.Interaction):
    await interaction.response.defer()  

    embed = discord.Embed(
        title="About me:",
        description="Aven - clean, fast, focused. The moderation bot that does exactly what it should, without a noise.",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Add to server",
        value="[Click here to invite the bot to your server](https://discord.com/oauth2/authorize?client_id=1431331007331696672&permissions=8&scope=bot%20applications.commands)",
        inline=False
    )

    embed.add_field(
        name="Commands",
        value=".ping, .kick, .ban, .unban, info, .fish",
        inline=False
    )

    embed.add_field(
      name="ToS | Privacy policy",
      value="[ToS](https://sites.google.com/view/aven-tos/főoldal) | [Privacy policy](https://sites.google.com/view/aven-privacy-policy/főoldal)",
      inline=False
    )

    embed.set_footer(text="Bot by u_noel")

    await interaction.followup.send(embed=embed)


@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="About me:",
        description="Aven - clean, fast, focused. The moderation bot that does exactly what it should, without a noise.",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="Add to server", 
        value="[Click here to invite the bot to your server](https://discord.com/oauth2/authorize?client_id=1431331007331696672&permissions=8&scope=bot%20applications.commands)", 
        inline=False
        )
    
    embed.add_field(
        name="Commands", 
        value=".ping, .kick, .ban, .unban, .info, .fish", 
        inline=False
        )
    
    embed.add_field(
        name="ToS | Privacy policy", 
        value="[ToS](https://sites.google.com/view/aven-tos/főoldal) | [Privacy policy](https://sites.google.com/view/aven-privacy-policy/főoldal)", 
        inline=False
        )
    
    embed.set_footer(text="Bot by u_noel")

    await ctx.send(embed=embed)

#-----------------------------------------------------

#bot.run("atokenem")

bot.run(TOKEN)
