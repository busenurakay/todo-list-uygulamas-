# 1. SINIF: Kullanicinin banka hesabini ve para islemlerini yonetir
class Hesap:
    def __init__(self, hesap_no, bakiye):
        self.hesap_no = hesap_no      # Hesap numarasi
        self.bakiye = bakiye          # Baslangic bakiyesi

    # Fonksiyon 1: Hesaba para yatirma
    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye = self.bakiye + miktar
            print("Para yatirildi. Yeni bakiye:", self.bakiye, "TL")
        else:
            print("Gecersiz tutar!")

    # Fonksiyon 2: Hesaptan para cekme
    def para_cek(self, miktar):
        if miktar <= 0:
            print("Gecersiz tutar!")
        elif miktar > self.bakiye:
            print("Yetersiz bakiye! Mevcut bakiye:", self.bakiye, "TL")
        else:
            self.bakiye = self.bakiye - miktar
            print("Para cekildi. Kalan bakiye:", self.bakiye, "TL")

    # Fonksiyon 3: Bakiye gosterme
    def bakiye_goster(self):
        print("Hesap No:", self.hesap_no, "| Mevcut Bakiye:", self.bakiye, "TL")


# 2. SINIF: Musteri bilgilerini ve sifre kontrolunu yonetir
class Kullanici:
    def __init__(self, ad, sifre, hesap):
        self.ad = ad                  # Musterinin adi
        self.sifre = sifre            # Giris sifresi
        self.hesap = hesap            # Kullaniciya bagli Hesap nesnesi

    # Fonksiyon 4: Sifre dogrulama
    def sifre_kontrol(self, girilen_sifre):
        if girilen_sifre == self.sifre:
            return True
        else:
            return False


# --- PROGRAM BASLANGICI ---
# Ornek bir hesap ve kullanici olusturuyoruz
musteri_hesabi = Hesap("TR101", 1000)
musteri = Kullanici("Ahmet", "1234", musteri_hesabi)

# Sifre giris ekrani
girilen = input("Hos geldiniz! Lutfen sifrenizi girin: ")

if musteri.sifre_kontrol(girilen) == True:
    print("Giris basarili, hos geldin", musteri.ad)

    # Ana menu dongusu
    while True:
        print("\n1-Bakiye Sorgula | 2-Para Yatir | 3-Para Cek | 4-Cikis")
        secim = input("Seciminiz: ")

        if secim == "1":
            musteri.hesap.bakiye_goster()
        elif secim == "2":
            tutar = float(input("Yatirilacak tutar: "))
            musteri.hesap.para_yatir(tutar)
        elif secim == "3":
            tutar = float(input("Cekilecek tutar: "))
            musteri.hesap.para_cek(tutar)
        elif secim == "4":
            print("Kartiniz iade ediliyor. Iyi gunler!")
            break
        else:
            print("Hatali secim yaptiniz!")
else:
    print("Hatali sifre! Giris reddedildi.")
