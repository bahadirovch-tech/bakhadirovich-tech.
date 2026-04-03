from django.shortcuts import render, redirect
import urllib.request
import urllib.parse

# Sening maxfiy kalitlaring (Buzilmagan!)
BOT_TOKEN = '7929964351:AAFq3qpvOcJGDkPdFpjnhm_iKBY6Qxy6tag'
CHAT_ID = '7993416038'

def home(request):
    # Kurslar HTML da borligi uchun bazadan chaqirish shart emas
    return render(request, 'index.html')

def botga_yuborish(request, kurs_id):
    if request.method == 'POST':
        ism = request.POST.get('ism')
        tel = request.POST.get('tel')
        
        # BAZADAN QIDIRMAYMIZ! ID ga qarab nomini o'zimiz biriktiramiz:
        kurs_nomi = "Noma'lum kurs"
        if str(kurs_id) == '1':
            kurs_nomi = "AI & SMART BOTS"
        elif str(kurs_id) == '2':
            kurs_nomi = "KIBERXAVFSIZLIK PRO"
        elif str(kurs_id) == '3':
            kurs_nomi = "WEB: FULL-STACK"
        
        # Telegramga boradigan xabar dizayni
        matn = (
            f"🚀 **YANGI BUYURTMA!**\n\n"
            f"👤 **Mijoz:** {ism}\n"
            f"📞 **Telefon:** {tel}\n"
            f"📚 **Kurs:** {kurs_nomi}\n\n"
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