from discord.ext import commands
from secret import BOT_TOKEN
import discord
from helpers import largest_product

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Everything's all ready to go")


@bot.event
async def on_message(message):
    print("The message's content was", message.content)
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), args))

@bot.command(pass_context=True)
async def display_embed(ctx):
    embed = discord.Embed(
        title = 'Title',
        description = 'This is some description, this should be long text to show that it is description.',
        colour = discord.Colour.blue()
    )
    embed.set_footer(text='This is footer')
    embed.set_image(url='https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg')
    embed.set_thumbnail(url='https://www.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg')
    embed.set_author(name='Author name', icon_url='https://www.sciencemag.org/sites/default/files/styles/inline__450w__no_aspect/public/dogs_1280p_0.jpg?itok=4t_1_fSJ')
    embed.add_field(name='Field name', value='Field value', inline=False)
    embed.add_field(name='Field name', value='Field value', inline=True)
    embed.add_field(name='Field name', value='Field value', inline=True)
    await ctx.send('Hey this is embed', embed=embed)

@bot.command()
async def largest(ctx, digits, substring_length):
    await ctx.send(largest_product(digits, int(substring_length)))

bot.run('NjY4MDI2NTY5NzMzOTYzNzk2.XiLphg.3BmzRdRzMJT4Ns9sRwxK7O8lC6Y')