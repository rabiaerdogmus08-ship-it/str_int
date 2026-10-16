def metni_sayiya_cevir(metin):#def komutu fonksiyon tanımlar
    #sözlük oluşturduk sayı sadece birler basamağındaysa birlerden alacak değilse de katlara göre devam
    birler = {"sıfır": 0, "bir": 1, "iki": 2, "üç": 3, "dört": 4, "beş": 5, "altı": 6, "yedi": 7, "sekiz": 8, "dokuz": 9}
    onlar = {"on": 10, "yirmi": 20, "otuz": 30, "kırk": 40, "elli": 50, "altmış": 60, "yetmiş": 70, "seksen": 80, "doksan": 90}
    katlar = {"yüz": 100, "bin": 1000, "milyon": 1000000}
    #bu alttaki kısımda metni küçük harfe çevirip kelimelere ayırıyoruz ve toplamı hesaplıyoruz
    kelimeler = metin.lower().split()
    toplam = 0
    gecici = 0
#dönüştürme işlemi için kelimeleri tek tek kontrol ediyoruz ve uygun sözlükten değerleri alıyoruz
    for kelime in kelimeler:
        if kelime in birler:
            gecici += birler[kelime]
        elif kelime in onlar:
            gecici += onlar[kelime]
        elif kelime == "yüz":
            gecici = (gecici if gecici != 0 else 1) * 100
        elif kelime in katlar:
            gecici = (gecici if gecici != 0 else 1) * katlar[kelime]
            toplam += gecici
            gecici = 0

    return toplam + gecici
#kullanıcıdan sayı girişi alıyoruz ve fonksiyonu çağırarak sonucu yazdırıyoruz
girdi = input("Bir sayı giriniz (yazıyla): ") 
sayi = metni_sayiya_cevir(girdi)#fonksiyonu kullanarak metni sayıya çeviriyoruz
print("Dönüştürülen Sayı:", sayi)