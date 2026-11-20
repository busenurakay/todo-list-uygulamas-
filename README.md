# BANKAMATİK
# Mini Bankamatik (ATM) Sistemi

Bu proje, Python temel veri yapıları, koşul ifadeleri, döngüler ve Nesne Tabanlı Programlama (`class`) kullanılarak geliştirilmiş konsol tabanlı bir Bankamatik uygulamasıdır.

## Sınıf ve Fonksiyon Yapısı
* **`Hesap` Sınıfı:** Hesap numarası ve bakiye bilgilerini tutar. `para_yatir()`, `para_cek()` ve `bakiye_goster()` metotları ile hesap işlemlerini gerçekleştirir.
* **`Kullanici` Sınıfı:** Müşteri adını, şifresini ve ilgili `Hesap` nesnesini tutar. `sifre_kontrol()` metodu ile güvenlik doğrulaması yapar.

## Akış Şeması (Flowchart)

```mermaid
flowchart TD
    A([Başlangıç - Giriş]) --> B[Şifre Gir]
    B --> C{Şifre Doğru mu?}
    C -- Hayır --> D[Hatalı Şifre Uyarısı] --> Z([Çıkış])
    C -- Evet --> E[ATM Menüsünü Göster]
    E --> F{İşlem Seçimi}
    F -- 1: Bakiye --> G[Bakiyeyi Yazdır] --> E
    F -- 2: Para Yatır --> H[Tutarı Al ve Ekle] --> E
    F -- 3: Para Çek --> I{Bakiye Yeterli mi?}
    I -- Evet --> J[Bakiyeden Düş] --> E
    I -- Hayır --> K[Yetersiz Bakiye Uyarısı] --> E
    F -- 4: Çıkış --> Z
```
