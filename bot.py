import discord
from discord import Activity
from discord import activity
from discord import member
from discord.colour import Color
from discord.embeds import Embed
from discord.errors import HTTPException
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands.errors import CheckFailure
from discord.flags import Intents
from discord.guild import Guild
from discord.utils import get
import time
import datetime
 
ID_Servidor = 387358429167222794 #ID do servidor de Discord
ID_BoasVindas = 757978075903426671 #ID do canal de BoasVindas
ID_Regras = 622502709223751690 #ID do canal de Regras
ID_Plataforma = 622424407809458189 #ID do canal para selecionar plataformas
ID_Anuncio = 622424535974805534 #ID do canal de anuncios
ID_Santuario = 622508155506786324 #ID do canal Santuario

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['dbd '], description='Bot', intents=intents)

@bot.command(name="santuario")
async def santuario(ctx, *,message):

    check_admin = ctx.author.guild_permissions.administrator #Variavel para identificar se o autor possui permissão de administrador
    check_1 = discord.utils.get(ctx.guild.roles, id=622508291041525770) #Variavel para identificar o cargo em questão  
    check_2 = discord.utils.get(ctx.guild.roles, id=622500636570681354) #Variavel para identificar o cargo em questão
    check_3 = discord.utils.get(ctx.guild.roles, id=622509004547162113) #Variavel para identificar o cargo em questão
    check_4 = discord.utils.get(ctx.guild.roles, id=689096500567080963) #Variavel para identificar o cargo em questão
    check_5 = discord.utils.get(ctx.guild.roles, id=900139946474610700) #Variavel para identificar o cargo em questão


    if check_1 in ctx.author.roles or check_2 in ctx.author.roles or check_3 in ctx.author.roles or check_4 in ctx.author.roles or check_5 in ctx.author.roles or check_admin:
        try:
            channel = bot.get_channel(ID_Santuario)
            titulo = message.split("|")[0]
            descricao = message.split("|")[1]
            foto = message.split("|")[2]

        except IndexError:
            await ctx.reply('Utilize: `dbd santuario  <Título e data> | <Descrição dos Perks> | <Imagem URL>`\nLembrando que a `<URL>` é opcional, porém é necessário utilizar o último `|`')

        embedVar = discord.Embed(title=titulo, description = descricao, colour = discord.Colour.random())
        embedVar.set_image(url=foto)
        embedVar.set_footer(text="Enviado por ⇨ {}".format(ctx.author), icon_url=ctx.author.avatar_url)
        embedVar.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embedVar)

    else:
        await ctx.reply("⇨ Você não pode usar isso!")
        return

@bot.command(name="anunciar")
async def anunciar(ctx, *,message):

    check = ctx.author.guild_permissions.administrator #Variavel para identificar se o autor possui permissão de administrador

    if check:
        channel = bot.get_channel(ID_Anuncio)
        try:
            titulo = message.split("|")[0]
            anuncio = message.split("|")[1]
            foto = message.split("|")[2]

        except IndexError:
            await ctx.reply('Utilize: `dbd anunciar <Título> | <Anúncio> | <URL>` \nLembrando que a `<URL>` é opcional, porém é necessário utilizar o último `|`.')
            return


        embedVar = discord.Embed(title=titulo, description = anuncio, colour = discord.Colour.random())
        embedVar.set_image(url=foto)
        embedVar.set_footer(text="Enviado por ⇨ {}".format(ctx.author), icon_url=ctx.author.avatar_url)
        embedVar.timestamp = datetime.datetime.utcnow()

        await channel.send("@everyone")
        await channel.send(embed = embedVar)

        
    else:
        await ctx.reply("⇨ Você não pode usar isso!")
        return

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(ID_Servidor) #ID do servidor do Discord
    channel = bot.get_channel(ID_BoasVindas) #ID do canal de BoasVindas
    member_count = guild.member_count
    activity = discord.Activity(name="Usuários ➝ ({})".format(member_count), type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    member_count_ = str(member_count)

    author = member.name
    pic = member.avatar_url

    embedVar = discord.Embed(title="<a:Welcome:800500859393540136> | Bem-vindo(a)! | <a:Welcome:800500859393540136>", description="__**{}**__, Seja bem-vindo ao Dead by Daylight Brasil! Você é {}º membro a entrar na comunidade!".format((author),(member_count_)), colour = discord.Colour.random())
    embedVar.set_author(name=author, icon_url=pic)
    embedVar.set_footer(text="©️ Todos os direitos reservados.")
    embedVar.set_image(url="https://i.imgur.com/ihFYWzG.png")
    embedVar.add_field(name="Evite punições <:Police:800500858030784523>", value="Leia as regras em <#{}> e fique por dentro das diretrizes da nossa comunidade".format(ID_Regras), inline=False)
    embedVar.add_field(name="Faça seu registro <:Register:800500857997230093>", value="Seleciona a plataforma que você utiliza para jogar Dead by Daylight em <#{}> e encontre outros players!".format(ID_Plataforma), inline=False)
    embedVar.set_thumbnail(url=pic)
    embedVar.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=embedVar)

    embedVar_ = discord.Embed(description="""{}, *Bem vindo(a) ao* **Dead by Daylight Brasil** *Antes de começar, leia as regras do canal* <#{}> \n
                                                 *Está comunidade tem o intuito de juntar vários jogadores de Dead by Daylight, procure grupos para jogar e faça novas amizades* \n 
                                                 *Para escolher sua plataforma basta ir no chat de* <#{}>""".format((member.mention),(ID_Regras),(ID_Plataforma)), colour=0xeeffee)
    embedVar_.set_thumbnail(url="https://i.imgur.com/T49IOQ6.png")
    embedVar_.set_footer(text="✔ Dead by Daylight Brasil")
    embedVar_.timestamp = datetime.datetime.utcnow()
    await member.send(embed=embedVar_)

    guild = bot.get_guild(ID_Servidor) #ID do servidor do Discord
    member_count = guild.member_count
    activity = discord.Activity(name="Usuários ➝ ({})".format(member_count), type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Estou Online!")

@bot.event
async def on_member_remove(member):
    guild = bot.get_guild(ID_Servidor) #ID do servidor do Discord
    member_count = guild.member_count 
    activity = discord.Activity(name="Usuários ➝ ({})".format(member_count), type = 3)
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.event
async def on_ready():
    guild = bot.get_guild(ID_Servidor) #ID do servidor do Discord
    member_count = guild.member_count
    activity = discord.Activity(name="Usuários ➝ ({})".format(member_count), type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Estou Online!")

bot.run() #Adicionar o token do bot