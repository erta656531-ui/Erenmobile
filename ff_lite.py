import random
import time
import os

# Terminali temizleme fonksiyonu (Keke dostu görüntü)
def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

# Oyun başlangıç ayarları
oyuncu_adi = input("Keke, oyundaki adın ne olsun? ")
temizle()
print(f"--- {oyuncu_adi.upper()} FREE FIRE LITE LITE'A HOŞ GELDİN! ---")
print("Uçaktayız... Varenga adasına doğru süzülüyoruz.")
time.sleep(2)

# Harita bölgeleri
bolgeler = ["Stadyum", "Pilot Plaza", "Milli Park", "Tersane", "Eski Kasaba"]
secilen_bolge = random.choice(bolgeler)

print(f"\nUçaktan atladın ve {secilen_bolge} bölgesine indin.")
time.sleep(1)

# Başlangıç İstatistikleri
can = 100
zirh = 0
silah = "Mevcut Değil"
mermi = 0
hayatta_kalanlar = 50
kill_sayisi = 0

# Oyun döngüsü
while can > 0 and hayatta_kalanlar > 1:
    print("\n" + "="*30)
    print(f"CAN: {can} | ZIRH: {zirh} | SİLAH: {silah} (Mermi: {mermi})")
    print(f"HAYATTA KALAN: {hayatta_kalanlar} | LEŞ: {kill_sayisi}")
    print("="*30)
    
    # Keke'nin aksiyon seçimi
    print("\nNe yapmak istersin keke?")
    print("1. Loot ara (Silah/Can bul)")
    print("2. Başka bölgeye pus/git")
    print("3. Çatışma ara (Riskli!)")
    secim = input("Seçimin (1-3): ")
    
    temizle()
    
    if secim == "1":
        # Loot bulma ihtimali
        ganimet = random.choice(["Silah", "Can Kiti", "Zırh", "Boş"])
        if ganimet == "Silah":
            silahlar = ["M416", "AKM", "AWP", "UMP45"]
            silah = random.choice(silahlar)
            mermi = random.randint(30, 90)
            print(f"Efsane loot! {silah} ve {mermi} mermi buldun.")
        elif ganimet == "Can Kiti":
            if can < 100:
                can = min(100, can + 50)
                print("Can kiti bastın, canın tazelendi.")
            else:
                print("Canın zaten dolu, kiti çantaya attın (ama çanta yok).")
        elif ganimet == "Zırh":
            zirh = 100
            print("Seviye 3 yelek buldun! Bayağı dayanıklısın şimdi.")
        else:
            print("Bölgeyi talan ettin ama işe yarar bir şey bulamadın.")
            
    elif secim == "2":
        # Pusma veya kaçma
        print("Sessizce başka bir binaya geçip pusuyorsun...")
        time.sleep(1)
        if random.random() < 0.3:
            print("Alan daralıyor! Mavi bölgeden kaçarken biraz hasar yedin.")
            hasar = random.randint(5, 15)
            can -= hasar
        else:
            print("Alan içinde kaldın, güvendesin.")
            
    elif secim == "3":
        # Çatışma mekaniği
        if silah == "Mevcut Değil":
            print("Keke delirdin mi, silahsız çatışmaya mı girilir? Dayak yedin.")
            can -= random.randint(30, 60)
        else:
            print(f"{silah} ile çatışmaya giriyorsun... Sesler geliyor!")
            time.sleep(2)
            
            # Çatışma sonucu ihtimalleri (Zırh hasarı azaltır)
            basari = random.random()
            if zirh > 0:
                basari += 0.2 # Zırhın varsa kazanma ihtimalin artar
                zirh -= 20 # Ama zırhın hasar görür
            
            if basari > 0.5:
                # Kazandın
                kazanilan_kill = random.randint(1, 2)
                kill_sayisi += kazanilan_kill
                print(f"Bileğine kuvvet! {kazanilan_kill} kişi indirdin.")
                mermi -= random.randint(5, 15)
                # Düşmandan loot
                if random.random() < 0.4 and can < 100:
                    can = min(100, can + 30)
                    print("Düşmanın üzerinden can kiti çıktı, hemen bastın.")
            else:
                # Hasar yedin
                print("Çatışma sert geçti, yara aldın.")
                hasar = random.randint(20, 50)
                can -= hasar
                mermi -= random.randint(10, 20)
                
    else:
        print("Geçersiz seçim, keke. Zaman daralıyor, düzgün karar ver!")

    # Her turda hayatta kalanları azalt (Gerçekçilik)
    if can > 0:
        elenenler = random.randint(1, 5)
        hayatta_kalanlar = max(1, hayatta_kalanlar - elenenler - kill_sayisi)
    
    # Mermi kontrolü
    if mermi < 0:
        silah = "Mevcut Değil"
        mermi = 0
        print("\nMermin bitti, silahı attın! Silahsız kaldın keke.")
        
    time.sleep(1.5)

# Oyun Sonucu
temizle()
if can <= 0:
    print(f"\n--- OYUN BİTTİ, {oyuncu_adi.upper()} ---")
    print(f"Alan dışında veya çatışmada can verdin. Maalesef {hayatta_kalanlar}. oldun.")
    print(f"Toplam Leş Sayın: {kill_sayisi}")
    print("Üzülme keke, bir sonraki maça stadyuma atlarız!")
else:
    print(f"\n🔥🔥🔥 BOOYAH! WINNER WINNER CHICKEN DINNER! 🔥🔥🔥")
    print(f"Tebrikler {oyuncu_adi.upper()}! Adada hayatta kalan son kişi sen oldun.")
    print(f"Toplam Leş Sayın: {kill_sayisi}")
    print("Varenga'nın kralı sensin keke!")

input("\nÇıkmak için Enter'a bas...")
