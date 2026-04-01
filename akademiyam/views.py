from django.shortcuts import render, redirect
from .models import Kurs
import urllib.request
import urllib.parse

# Sening maxfiy kalitlaring
BOT_TOKEN = '7929964351:AAFq3qpvOcJGDkPdFpjnhm_iKBY6Qxy6tag'
CHAT_ID = '7993416038'

def home(request):
    hamma_kurslar = Kurs.objects.all()
    return render(request, 'index.html', {'kurslar': hamma_kurslar})

def botga_yuborish(request, kurs_id):
    if request.method == 'POST':
        ism = request.POST.get('ism')
        tel = request.POST.get('tel')
        kurs = Kurs.objects.get(id=kurs_id)
        
        # Telegramga boradigan xabar dizayni
        matn = (
            f"🚀 **YANGI BUYURTMA!**\n\n"
            f"👤 **Mijoz:** {ism}\n"
            f"📞 **Telefon:** {tel}\n"
            f"📚 **Kurs:** {kurs.nomi}\n\n"
            f"✅ *Tezda bog'laning!*"
        )
        
        # Telegram API ga yuborish
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={urllib.parse.quote(matn)}&parse_mode=Markdown"
        try:
            urllib.request.urlopen(url)
        except Exception as e:
            print("Xatolik:", e)
            
        return render(request, 'success.html', {'ism': ism})
    
    return redirect('home')