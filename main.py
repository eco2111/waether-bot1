from telebot.async_telebot import AsyncTeleBot
import python_weather
import asyncio 

bot_api = "7500418777:AAGQ30NiW_368obzx7jSce7pRuJFLVhxeac"

bot = AsyncTeleBot( bot_api )

# bu satrt tugmasi bosilganda iwlaydi 
@bot.message_handler( command=['start'] )
#foydalanuvchi habari 
async def send_welcome( message ):
    await bot.reply_to( message, "Здравствуйте! Данный под служит для получение погоды указанного города:\nВы:Namangan \nбот: Namangan 1 °C" )
    # bot foydalnuvchi habarini olib uzizni habarinin qo'shib jonatadi 


@bot.message_handler()
# bu funksiya start dan tawqari bowqa habarlarga javob qaytaradi 
async def send_weather( message):
    # bullar hammasi obuhavoni qaytaradi 
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(message.text)
        wt = ( weather.temperature - 32 ) * (5 / 9)
        

# bu if-elif ga ohwab iwlaydi faqat 100% tochno bosa iwlatamiz match case 
    match str(weather.kind):
       case "Cloudy":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. bulutli havo" )
       case "Fog":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. tumanli havo " )
       case "Heavy Rain":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. kuchli yom'gir" )
       case "Heavy Showers":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. kuchli yomg'ir" )
       case "Heavy Snow ":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. kuchli qor" )
       case "Heavy Snow Showers":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. kuchli qor yog'ishi mumkin" )
       case "Light Rain":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. Yengil yomg'ir" )
       case "Light Showers":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. Yengil yomg'irlar" )
       case "Light Sleet":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. Yengil qorga " )
       case "Light Sleet Showers":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. Yengil qorga o'xshash yomg'irlar " )
       case "Light Snow":
           await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. Yengil qor " )
       case "Light Snow Showers":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. Qisman bulutli " )
       case "Sunny":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. quyoshli" )
       case "Thundery Heavy Rain":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. JALDIRAMAY OG'IR YOMGIN" )
       case "Thundery Showers":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. BULUTLI YOMGIN" )
       case "Thundery Snow Showers":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. MOMIQLI QOR YOMG'IRI" )
       case "Very Cloudy":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. JUDA BULUTLI" )
       case "Partly Cloudy":
          await bot.reply_to( message,f" Bugun   {message.text} da  {round(wt)} ℃. BULUTLI BULISHI MUMKIN 🥸🙂‍↔️ " )
          
# bu bzni botni doimi tarda iwlawni ta'millab beradi. 
asyncio.run(bot.polling())