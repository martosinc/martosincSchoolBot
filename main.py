import discord
import datetime
from discord.ext import commands
from config import settings
# import requests

bot = commands.Bot(command_prefix = settings['prefix'])

days_of_week = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']

today_requests = []
tomorrow_requests = []
week_requests = []

timetables = {'пн':['математика', 'английский', 'русский язык', 'русский язык', 'физра'], 
              'вт':['русский язык', 'русский язык', 'математика', 'начертательная геометрия', 'история'], 
              'ср':['английский язык', 'русский', 'русский', 'география', 'математика', 'математика'], 
              'чт':['математика', 'английский', 'история', 'программирование', 'литература', 'биология'], 
              'пт':['математика', 'математика', 'у?', 'русский', 'введение в физику', 'информатика'], 
              'сб':['мат. кружок'], 
              'вс':[]
              }
bookstable = {'пн':['А.Н. Мерзляк', "Forward Student's book"], 
              'вт':['А.Н. Мерзляк', 'Всеобщая История'], 
              'ср':["Forward Student's book", 'А.Н. Мерзляк', 'География 5-6'], 
              'чт':['А.Н. Мерзляк', "Forward Student's book", 'Всеобщая История', 'Биология', 'Литература'], 
              'пт':['А.Н. Мерзляк']
              }

all_requests = []

@bot.command()
async def info(ctx):
    tomorrow = datetime.datetime.today().weekday()+1
    today = datetime.datetime.today().weekday()
    if tomorrow == 7:
        tomorrow = 0
    author = ctx.message.author
    await ctx.send(f'Привет, {author.mention}!\n/today для дальнешей информации о сегодняшнем дне({days_of_week[today]})\n/tomorrow для дальнейшей информации о завтрашнем дне({days_of_week[tomorrow]})\n/week для информации по неделе')

@bot.command()
async def today(ctx):
    author = ctx.message.author
    if author.id not in today_requests:
        today_requests.append(author.id)
        await ctx.send(f'Команды на сегодняшний день:\n/books - собрать учебники на сегодня\n/timetable - расписание на сегодня\n/events - важные события на сегодня(пока в бете)\n/all - вся информация на сегодня')
    else:
        await ctx.send(f'Вы уже написали эту команду!')
    if author.id in tomorrow_requests:
        tomorrow_requests.remove(author.id)
    f = open("/home/martos/Documents/code/python/SchoolBot/users", 'a')
    username = author.name
    # username = user.name
    f.write('\n'+username)
    f.close()

@bot.command()
async def tomorrow(ctx):
    author = ctx.message.author
    if author.id not in tomorrow_requests:
        tomorrow_requests.append(author.id)
        await ctx.send(f'Команды на завтрашний день:\n/books - собрать учебники на завтра\n/timetable - расписание на завтра\n/events - важные события на завтра(пока в бете)\n/all - вся информация на завтра')
    else:
        await ctx.send(f'Вы уже написали эту команду!')
    if author.id in today_requests:
        today_requests.remove(author.id)
    f = open("/home/martos/Documents/code/python/SchoolBot/users", 'a')
    username = author.name
    # username = user.name
    f.write('\n'+username)
    f.close()

@bot.command()
async def timetable(ctx):
    author = ctx.message.author
    if author.id in today_requests:
        today = datetime.datetime.today().weekday()
        date = days_of_week[today]
        await ctx.send(date)
        await ctx.send(str(len(timetables.get(date))) + ' уроков:')
        lesson_number = 1
        for i in timetables.get(date):
            await ctx.send(str(lesson_number) + '. ' + i)
            lesson_number += 1
        today_requests.remove(author.id)
    if author.id in tomorrow_requests:
        tomorrow = datetime.datetime.today().weekday() + 1
        if tomorrow == 7:
            tomorrow = 0
        date = days_of_week[tomorrow]
        await ctx.send(date)
        await ctx.send(str(len(timetables.get(date))) + ' уроков:')
        lesson_number = 1
        for i in timetables.get(date):
            await ctx.send(str(lesson_number) + '. ' + i)
            lesson_number += 1
        tomorrow_requests.remove(author.id)

@bot.command()
async def books(ctx):
    author = ctx.message.author
    if author.id in today_requests:
        today = datetime.datetime.today().weekday()
        date = days_of_week[today]
        await ctx.send(date)
        for i in bookstable.get(date):
            await ctx.send(i)
        today_requests.remove(author.id)
    if author.id in tomorrow_requests:
        tomorrow = datetime.datetime.today().weekday() + 1
        if tomorrow == 7:
            tomorrow = 0
        date = days_of_week[tomorrow]
        await ctx.send(date)
        for i in bookstable.get(date):
            await ctx.send(i)
        tomorrow_requests.remove(author.id)

@bot.command()
async def events(ctx):
    # author = ctx.message.author
    # if author.id in today_requests:
    #     if author.id in today_requests:
    #         today = datetime.datetime.today().weekday()
    #         date = days_of_week[today]
    await ctx.send('Команда пока не работает')

@bot.command()
async def all(ctx):
    author = ctx.message.author
    if author.id in today_requests:
        today = datetime.datetime.today().weekday()
        date = days_of_week[today]
        await ctx.send(date)
        await ctx.send(str(len(timetables.get(date))) + ' уроков:')
        lesson_number = 1
        for i in timetables.get(date):
            await ctx.send(str(lesson_number) + '. ' + i)
            lesson_number += 1
        await ctx.send('Книги:')
        for i in bookstable.get(date):
            await ctx.send(i)
        today_requests.remove(author.id)
    if author.id in tomorrow_requests:
        tomorrow = datetime.datetime.today().weekday() + 1
        if tomorrow == 7:
            tomorrow = 0
        date = days_of_week[tomorrow]
        await ctx.send(date)
        await ctx.send(str(len(timetables.get(date))) + ' уроков:')
        lesson_number = 1
        for i in timetables.get(date):
            await ctx.send(str(lesson_number) + '. ' + i)
            lesson_number += 1
        await ctx.send('Книги:')
        for i in bookstable.get(date):
            await ctx.send(i)
        tomorrow_requests.remove(author.id)

@bot.command()
async def week(ctx):
    f = open("/home/martos/Documents/code/python/SchoolBot/users", 'a')
    username = author.name
    f.write('\n'+username)
    f.close()
    for i in range(5):
        date = days_of_week[i]
        await ctx.send(date)
        await ctx.send(str(len(timetables.get(date))) + ' уроков:')
        lesson_number = 1
        for i in timetables.get(date):
            await ctx.send(str(lesson_number) + '. ' + i)
            lesson_number += 1
        await ctx.send('Книги:')
        for i in bookstable.get(date):
            await ctx.send(i)
bot.run(settings['token'])