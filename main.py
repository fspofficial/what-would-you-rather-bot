import discord
import random
import os
from keep_alive import keep_alive
from discord.ext import commands
#----------------------# Main #--------------------------#
client = commands.Bot(command_prefix="r!")
tokaint = os.environ['TOKEN']
#--------------------------------------------------------#

#---------------------# TC Words #-----------------------#
tcm = ["OwO", "Cool", "Nice", "Reeeee", "Uhh", "EWEEEEE!"]
#---------------------# Embeds #-------------------------#
helpmenu = discord.Embed(title='This is all the Commands in What Would You Rather', description='This is a Type of Guessing game, You have to guess What you would do in 2 Situations', color=0xFF0000)
helpmenu.add_field(name="r!rather / r!rth", value='Loads a Rathering Question')
helpmenu.add_field(name="r!opt1 / r!opt 2", value='Choose the Option 1 / 2')
helpmenu.add_field(name="r!help",value='Loads the Help Menu')
helpmenu.add_field(name="r!support",value='Loads the Supporting Links', inline = True)
helpmenu.set_footer(text = "Bot by FSP Gang s' Admin#6899")
#--------------------------------------------------------#
option1 = discord.Embed(title= (random.choice(tcm)) + ', You Have Chosen Option 1', description='Option 1 Has been Chosen', color=0xFF0000)
option2 = discord.Embed(title= (random.choice(tcm)) + ', You Have Chosen Option 2', description='Option 2 Has been Chosen', color=0xFF0000)
additbr = discord.Embed(title= 'Add a Question', description="This feature is not done fully yet due to NSFW Scanner is not abliable in the bot but You can DM FSP Gang s' Admin#6899 to add Your Questions", color=0xFF0000)
#--------------------------------------------------------#
supportmnu = discord.Embed(title='This is all the Support Links in What Would You Rather', description='On here You can Vote or Support our Bot!', color=0xFF0000)
supportmnu.add_field(name="Creator s' YouTube Channel", value='https://www.youtube.com/channel/UCy3-B17ybXnA_z8CIShmyBw')
supportmnu.add_field(name="Top.gg Invite & Vote Link", value='https://top.gg/bot/832504593886871572/', inline = False)
supportmnu.set_footer(text = "Bot by FSP Gang s' Admin#6899")
#--------------------------------------------------------#
rat = [
	#1
	''' 
	1. Have the Power to Make Someone Love You
	2. Have the Power to Read Someone Mind
	''',
	#2
	'''
	1. Give Someone Discord Nitro
	2. Spam in Big Servers
	''',
	#3
	'''
	1. Eat the Burger
	2. Give it to a Poor Kid
	''',
	#4
	'''
	1. Have a Lamborgini
	2. Live in a Luxary House
	''',
	#5
	'''
	1. Be a Girl Forever
	2. Say the Words that are in Your heart to whom you want to say it
	''',
	#6
	'''
	1. Rickroll Someone
	2. Destroy your Device
	''',
	#7
	'''
	1. Learn Python
	2. Download Kali Linux
	''',
	#8
	"""
	1. Be a Famous Celebritiy
	2. Be a Everyone's YouTuber of all time
	""",
	#9
	'''
	1. Dislike a T-Series Video
	2. Subscribe to PewDiePie
	''',
	#10
	'''
	1. Buy Whatever your Friend Says
	2. Donate Money to Poor
	''',
	#11
	'''
	1. Kill Someone
	2. Destory Your / Your Sister Makeup
	''',
	#12
	'''
	1. Never Shave Again
	2. Never brush yout Teeth Again
	''',
	#13
	'''
	1. Always be Overdressed
	2. Always be Undressed
	''',
	#14
	'''
	1.Do 100 Pushups
	2. Run a Mile
	''',
	#15
	'''
	1. Be Homeless but genuinely happy
	2. Have a nic house but be depressed all the time
	''',
	#16
	'''
	1. Be alone
	2. Be in unhappy relationship
	''',
	#17
	'''
	1. Play only Single Player Games
	2. Play only Multiplayer Games
	''',
	#18
	'''
	1. Kiss a Spider
	2. Catch a Mouse
	''',
	#19
	'''
	1. Have the power to Talk to Birds
	2. Have the power to Talk to Dogs
	''',
	#20
	'''
	1. Have your Google Earth upgraded to see everything
	2. Have your Skype to be able to call anyone at any time
	''',
	#21
	'''
	1. Be 3 feet Shorter
	2. Be 3 feet Taller
	''',
	#22
	'''
	1. Instantly learn the Piano perfectly
	2. Instantly learn the Gutiar perfectly
	''',
	#23
	'''
	1. Win $5000 for yourself
	2. Win $50000 for Charity
	''',
	#24
	'''
	1. Find True Love
	2. Win 10 Million Dollars
	''',
	#25
	'''
	1. Win $70,000
	2. Let your best friend win $250,000
	''',
	#26
	'''
	1. Know the date of your death
	2. Know the cause of your death
	''',
	#27
	'''
	1. Be a Dragon
	2. Own a Dragon
	''',
	#28
	'''
	1. Have Shark Teeth
	2. Have No Teeth
	''',
	#29
	'''
	1. Be with Someone who is always late
	2. Be with Someone who is always early
	''',
	#30
	'''
	1. Marry who you love
	2. Marry a millionaire
	''',
	#31
	'''
	1. Be a Zombie
	2. Be a part of alien invasion
	''',
	#32
	'''
	1. Watch Comedy Flim
	2. Watch Horror Flim
	''',
	#33
	'''
	1. Be the best super villan
	2. Be a mediocre superhero
	''',
	#34
	'''
	1. Have someone annoying you all the time
	2. Have someone talking you all the time
	''',
	#35
	'''
	1. Change your eye color
	2. Change your hair color
	''',
	#36
	'''
	1. Recive a Gift
	2. Give someone a Gift
	''',
	#37
	'''
	1. Get serve frostbite
	2. Be severly burned
	''',
	#38
	'''
	1. Teach History
	2. Tech Maths
	''',
	#39
	'''
	1. Have everybody stare awkwardly
	2. Have everyone look awai in disgust
	''',
	#40
	'''
	1. Have to stand all day
	2. Have to sit all day
	''',
	#41
	'''
	1. Be burried alive
	2. Be eaten alive
	''',
	#42
	'''
	1. Go to Hogwards
	2. Go to Narina
	''',
	#43
	'''
	1. Live the rest of the life whitout sight
	2. Live the rest of your life whitout sound
	''',
	#44
	'''
	1. Know the truth about UFOs
	2. Know the truth about Bigfoot
	''',
	#45
	'''
	1. Go skiing
	2. Go surfing
	''',
	#46
	'''
	1. Eat a poisionus flower
	2. Be inside a burning house
	''',
	#47
	'''
	1. Have a Broken Heart
	2. Have a Broken Bone
	''',
	#48
	'''
	1. Go whitout the Internet for a Month
	2. Go whitout your car for a month 
	''',
	#49
	'''
	1. Never be able to feel emotions
	2. Never be able to show emotions
	''',
	#50
	'''
	1. Fight 100 duck sized horses
	2. Figt 1 horse sized duck
	''',
	#51
	'''
	1. Be born aged 100 and every birthday you get lower age
	2. Keep everything the same way
	''',
	#52
	'''
	1. Be famous in this lifetime
	2. Go down in history books
	''',
	#53
	'''
	1. Live in 1920s as a multi-millionaire
	2. Live in 2110s with $50,000
	''',
	#54
	"""
	1. Marry with someone you don't love
	2. Marry with someone who dosen't love you
	""",
	#55
	'''
	1. Be an Anti-Social Genius
	2. Be popular but un-intelligent
	''',
	#56
	'''
	1. Live the life of a Cat
	2. Live the life of a Dog
	''',
	#57
	'''
	1. Be in a famous movie
	2. Be on a Popular TV show
	''',
	#58
	'''
	1. Have 500 bad days followed by 250 good days
	2. Have 500 alternating good and bad days
	''',
	#59
	'''
	1. Lose half of your hair
	2. Lose haf of your ear
	''',
	#60
	'''
	1. Never pay for Taxes
	2. Never pay for Gas
	''',
	#61
	'''
	1. Eat everything you see
	2. Lick everything you see
	''',
	#62
	'''
	1. Have dilarrhoea every day for 3 Months
	2. Have a mosquito next to your ear for 3 Months
	''',
	#63
	'''
	1. Live in a Space Station
	2. Live in a Deep sea Sumbarine
	''',
	#64
	'''
	1. Spend 1 Year in Prison
	2. Spend 2 Years in Comma
	''',
	#65
	'''
	1. Lose your Favorie Apps
	2. Love all your Apps apart from your Favorite App
	''',
	#66
	'''
	1. Be Australian
	2. Be Indian
	''',
	#67
	'''
	1. Marry someone who is extremly attractive
	2. Marry someone who is rich
	''',
	#68
	'''
	1. Be a Horse Jockey
	2. Be a Nascar Driver
	''',
	#69
	'''
	1. Get electrocutes for 10 Seconds
	2. Get slapped by a girl 20 Times
	''',
	#70
	'''
	1. Be half your height
	2. Be double your weight
	''',
	#71
	'''
	1. Explore the Ocean
	2. Explore the Galaxy
	''',
	#72
	'''
	1. Be painted by Van Gogh
	2. Be painted by Da Vinci
	''',
	#73
	'''
	1. See everything blurry all the time
	2. See everything black and white
	''',
	#74
	'''
	1. Have a Boring Career
	2. Have an Exiting but life threateing Carrer 
	''',
	#75
	'''
	1. Never be able to stop dancing
	2. Never be able to stop singing
	''',
	#76
	'''
	1. Go the rest of your life whitout touching plastic
	2. Go the rest of your life whitout touching metal
	''',
	#77
	'''
	1. Have one wish granted today
	2. Have three wishes grated in 10 Years
	''',
	#78
	'''
	1. Arrive everywhere 5 minutes late
	2. Arrive everywhere 20 minutes early
	''',
	#79
	'''
	1. Drink 1 gallon of ocean salt water
	2. Drank 1 gallon of slime
	''',
	#80
	'''
	1. Be transported to a place and the time of your choosing in the past
	2. Be transported to a random place and in the future
	'''
	]
#--------------------------------------------------------#

@client.event
async def on_ready():
	print('[MMC Console]: 🔥 Bot is Online, Enjoy! 🔥')
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="What Would You Rather using r!rth  / r!rather"))

[...]
client.remove_command("help")

@client.command()
async def help(ctx):
	await ctx.send(embed=helpmenu)
	print('[MMC Console]: 🔥 Bot Got a Command = r!help 🔥')

@client.command()
async def support(ctx):
	await ctx.send(embed=supportmnu)
	print('[MMC Console]: 🔥 Bot Got a Command = r!support 🔥')

@client.command()
async def rather(ctx):
	rath = discord.Embed(title='What Would You Rather?', description='Choose using r!opt1 for Option 1 or r!opt2 for Option 2', color=0xFF0000)
	rath.add_field(name="Your Question:", value=(random.choice(rat)))

	await ctx.send(embed=rath)

	print('[MMC Console]: 🔥 Bot Got a Command = r!rather 🔥')


@client.command()
async def rth(ctx):
	rath1 = discord.Embed(title='What Would You Rather?', description='Choose using r!opt1 for Option 1 or r!opt2 for Option 2', color=0xFF0000)
	rath1.add_field(name="Your Question:", value=(random.choice(rat)))

	await ctx.send(embed=rath1)

	print('[MMC Console]: 🔥 Bot Got a Command = r!rth 🔥')

@client.command()
async def opt1(ctx):
	await ctx.send(embed=option1)
	print('[MMC Console]: 🔥 Bot Got a Command = r!opt1 🔥')

@client.command()
async def opt2(ctx):
	await ctx.send(embed=option2)
	print('[MMC Console]: 🔥 Bot Got a Command = r!opt2 🔥')

@client.command()
async def addq(ctx):
	await ctx.send(embed=additbr)
	print('[MMC Console]: 🔥 Bot Got a Command = r!addq 🔥')

keep_alive()
client.run(tokaint)