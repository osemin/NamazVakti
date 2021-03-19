import requests
from win10toast import ToastNotifier
import time
import winsound
ezan_sesi= "ezan.wav"
parametreler = {

    "country":"Turkey",
    "city":"İstanbul",
    "method":13,
}

response=requests.get("http://api.aladhan.com/v1/timingsByCity/:date_or_timestamp",params=parametreler)
print(response.json()['data']['timings'])
saat_bilgisi=time.strftime("%H:%M")
print(saat_bilgisi)
bildirim=ToastNotifier()
while True:
    ezan_saati=time.strftime("%H:%M")
    if response.json()['data']['timings']['Fajr']:
        bildirim.show_toast(
        "Sabah Namazı",
        "Sabah Namazı Okunuyor",
        icon_path="pacman.ico",
        duration=60,
        threaded=True
        )
        winsound.PlaySound(ezan_sesi, winsound.SND_FILENAME)
    elif response.json()['data']['timings']['Dhuhr']:
        bildirim.show_toast(
        "Öğle Namazı",
        "Öğle Namazı Okunuyor",
        icon_path="pacman.ico",
        duration=60,
        threaded=True
        )
        winsound.PlaySound(ezan_sesi, winsound.SND_FILENAME)
    elif response.json()['data']['timings']['Asr']:
        bildirim.show_toast(
            "İkindi Namazı",
            "İkindi Namazı Okunuyor",
            icon_path="pacman.ico",
            duration=60,
            threaded=True
        )
        winsound.PlaySound(ezan_sesi, winsound.SND_FILENAME)

    elif response.json()['data']['timings']['Maghrib']:
        bildirim.show_toast(
            "Akşam Namazı",
            "Akşam Namazı Okunuyor",
            icon_path="pacman.ico",
            duration=60,
            threaded=True
        )
        winsound.PlaySound(ezan_sesi, winsound.SND_FILENAME)
    elif response.json()['data']['timings']['Isha']:
        bildirim.show_toast(
            "Yatsı Namazı",
            "Yatsı Namazı Okunuyor",
            icon_path="pacman.ico",
            duration=60,
            threaded=True
        )
        winsound.PlaySound(ezan_sesi, winsound.SND_FILENAME)





