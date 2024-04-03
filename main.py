#from youtube_search import YoutubeSearch
from Rooz import Download
from kvsqlite.sync import Client
from telebot import types
#from time import sleep
import telebot,requests,os
from keep_alive import keep_alive
keep_alive()

#https://youtu.be/eI_jUoAdEMw هو?si=9NhI

db = Client('pn.hex')

bot = telebot.TeleBot('6251076172:AAHHiqsSzStW2AYN9Ay_MqZUsNP0fqnQsLQ')


boss = types.InlineKeyboardMarkup(row_width=2)
rkkuu = types.InlineKeyboardButton(text='SiRius ♪ ,',url='rKKuu.t.me')
boss.add(rkkuu)


#aov = types.InlineKeyboardMarkup(row_width=2)
#audio = types.InlineKeyboardButton(text='• ملف صوتي ♪',callback_data='au')
#video = types.InlineKeyboardButton(text='• مقطع فيديو 🎞️ ',callback_data='vid')
#aov.add(audio,video)



@bot.message_handler(commands=['start'])
def start(message):
  fe = types.InlineKeyboardMarkup(row_width=2)
  dirt = types.InlineKeyboardButton(text='🧑🏻‍💻',url='XuuDD.t.me')
  fe.add(dirt)
  iid = message.from_user.id
  name = message.from_user.first_name
  ms = message.chat.id
  db.set(f'n_{ms}',name)
  id = message.from_user.id
#	db.set(f'id_{iid}',id)
  dmj = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
  db.set(f'n_{ms}',dmj)
  bot.reply_to(message,f'• اهلاً بك في بوت التحميل من بنتريست ✓\nارسل رابط الفيديو ليتم تحميله ^-^',parse_mode='markdown',reply_markup=fe)

@bot.message_handler(func=lambda m:True)
def SaD(m):
  iid = m.from_user.id
  name = m.from_user.first_name
  ms = m.chat.id
  mm = m.text
  if m.text.startswith("https://pin.it/") or m.text.startswith('https://www.pinterest.com/pin/'):
  	do = Download(mm).DownPinterest()['video']
  	req = requests.get(do).content
  	ow = open(f'{iid}.mp4','wb')
  	ow.write(req)
  	rb = open(f'{iid}.mp4','rb')
  	bot.send_video(ms,video=rb,
  	caption='Done ✓',
  	reply_markup=boss)
  	os.remove(f'{iid}.mp4')
  else:
  	bot.reply_to(m,'خطأ في الرابط :(')
		
bot.infinity_polling()	
