# PharmaDose – Yapay Zekâ Kullanım Günlüğü

## 1. Proje Bilgileri

**Proje Adı:** PharmaDose – İlaç Kullanım Planlayıcısı  
**Ders:** GEP1316 – Kodlama Okuryazarlığı  
**Programlama Dili:** Python  
**Geliştirme Ortamı:** Visual Studio Code  
**Yapay Zekâ Aracı:** ChatGPT (OpenAI)

## 2. Yapay Zekâ Kullanım Amacı

PharmaDose projesinin geliştirilmesi sırasında ChatGPT'den programlama öğrenme, proje fikri geliştirme, Python kodlarını oluşturma, hata ayıklama ve test senaryolarını hazırlama konularında destek aldım.

Yapay zekâ tarafından önerilen kodları Visual Studio Code ortamında çalıştırarak kontrol ettim. Karşılaştığım hataları inceleyerek gerekli düzeltmeleri gerçekleştirdim.

## 3. Yapay Zekâ ile Etkileşim Günlüğü

### Prompt 1 – Proje Fikrinin Belirlenmesi

**Yapay zekâya yönelttiğim isteğin özeti:**

Eczacılık alanıyla ilişkili, Python kullanılarak geliştirilebilecek ve dersin ödev gerekliliklerini karşılayabilecek bir proje önerilmesini istedim.

**Yapay zekânın önerisi:**

ChatGPT, ilaç bilgilerini düzenleyen ve örnek kullanım saatleri oluşturan PharmaDose adlı bir uygulama geliştirmeyi önerdi.

**Kararım:** Kabul ettim.

**Gerekçem:**

Eczacılık eğitimimle ilişkili olması ve tekrar eden bilgi düzenleme işlemlerinin Python ile otomatikleştirilebilmesine imkân sağlaması nedeniyle bu projeyi seçtim.

### Prompt 2 – Python ve Visual Studio Code Kurulumu

**Yapay zekâya yönelttiğim isteğin özeti:**

MacBook bilgisayarımda Python ve Visual Studio Code kullanarak projeye nasıl başlayabileceğimi adım adım açıklamasını istedim.

**Yapay zekânın önerisi:**

Python kurulumu, Visual Studio Code kullanımı, proje klasörünün oluşturulması ve terminal üzerinden Python dosyasının çalıştırılması açıklandı.

**Kararım:** Kabul ettim.

**Gerekçem:**

Bu yönlendirmeler sayesinde geliştirme ortamımı hazırladım ve ilk Python programımı başarıyla çalıştırdım.

### Prompt 3 – Kullanıcıdan İlaç Bilgilerinin Alınması

**Yapay zekâya yönelttiğim isteğin özeti:**

Kullanıcıdan ilaç adı, doz, günlük kullanım sıklığı ve kullanım süresi bilgilerini alan bir Python programı oluşturulmasını istedim.

**Yapay zekânın önerisi:**

`input()`, `while`, `if/else` ve `try/except` yapılarından yararlanarak kullanıcı girdilerini kontrol eden fonksiyonlar önerildi.

**Kararım:** Test ederek kabul ettim.

**Gerekçem:**

Programın eksik veya geçersiz girdiler karşısında kapanmadan kullanıcıdan yeniden bilgi istemesini sağladım. Örneğin günlük kullanım sıklığına `abc` yazıldığında programın hata mesajı vererek tekrar sayı istediğini doğruladım.

### Prompt 4 – Ana Menü Sisteminin Oluşturulması

**Yapay zekâya yönelttiğim isteğin özeti:**

Kullanıcının ilaç ekleme, ilaçları görüntüleme ve programdan çıkma işlemlerini seçebileceği bir ana menü oluşturulmasını istedim.

**Yapay zekânın önerisi:**

`while True` döngüsü ve `if/elif/else` karar yapılarıyla çalışan bir menü sistemi önerildi.

**Kararım:** Değiştirerek kabul ettim.

**Gerekçem:**

Kodları mevcut dosyaya eklerken programın yapısında karışıklık yaşadım. Bu nedenle `main.py` dosyasını yeniden düzenleyerek fonksiyonların doğru sırada tanımlanmasını ve ana menünün düzgün çalışmasını sağladım.

### Prompt 5 – Örnek İlaç Saatlerinin Hesaplanması

**Yapay zekâya yönelttiğim isteğin özeti:**

Kullanıcının belirttiği günlük kullanım sıklığına göre örnek saatler hesaplayan bir fonksiyon oluşturulmasını istedim.

**Yapay zekânın önerisi:**

24 saatin günlük kullanım sıklığına bölünmesiyle eşit zaman aralıkları oluşturan bir algoritma önerildi. Örnek başlangıç saati 08.00 olarak belirlendi.

**Kararım:** Sınırlamalarını belirterek kabul ettim.

**Gerekçem:**

Algoritma, Python'da matematiksel işlemleri ve döngüleri kullanmayı öğrenmemi sağladı. Ancak her ilacın eşit zaman aralıklarıyla kullanılmasının tıbben uygun olmayabileceğini fark ettim. Bu nedenle uygulamanın yalnızca eğitim amaçlı olduğunu belirten bir uyarı ekledim.

### Prompt 6 – Bilgilerin TXT Dosyasına Kaydedilmesi

**Yapay zekâya yönelttiğim isteğin özeti:**

Kullanıcının eklediği ilaç bilgilerini ve oluşturulan örnek saatleri bir metin dosyasına kaydeden fonksiyon geliştirilmesini istedim.

**Yapay zekânın önerisi:**

Python'daki `open()` ve `write()` işlemleri kullanılarak `medication_schedule.txt` dosyasının oluşturulması önerildi.

**Kararım:** Hata ayıklama sonrasında kabul ettim.

**Gerekçem:**

Kodları düzenlerken `IndentationError` hatasıyla karşılaştım. Fonksiyonun altındaki kodların doğru girintilenmediğini belirledim. Gerekli düzenlemeleri yaptıktan sonra programı yeniden çalıştırdım ve TXT dosyasının başarıyla oluşturulduğunu doğruladım.

### Prompt 7 – Test Senaryolarının Hazırlanması

**Yapay zekâya yönelttiğim isteğin özeti:**

Programın doğru çalıştığını kontrol etmek için geçerli ve geçersiz kullanıcı girdilerini içeren test senaryoları hazırlanmasını istedim.

**Yapay zekânın önerisi:**

İlaç ekleme, ilaçları listeleme, hatalı sayı girişi, geçersiz menü seçimi, örnek saat hesaplama ve TXT dosyasına kaydetme işlemlerinin test edilmesi önerildi.

**Kararım:** Kabul ettim ve uyguladım.

**Gerekçem:**

Testleri terminal üzerinden gerçekleştirdim. Özellikle `abc` ve `0` gibi geçersiz kullanım sıklığı girdilerinde programın uygun uyarılar verdiğini kontrol ettim. Ayrıca TXT dosyasının oluştuğunu ve içeriğinin görüntülenebildiğini doğruladım.

## 4. Tespit Edilen Hatalar ve Çözümleri

**Hata 1 – Kod Yapısının Karışması**

Yeni fonksiyonların mevcut Python dosyasına eklenmesi sırasında kodların yerleşiminde karışıklık oluştu.

**Çözüm:** `main.py` dosyasındaki fonksiyonları yeniden düzenledim ve programı tekrar test ettim.

**Hata 2 – IndentationError**

Ana menü fonksiyonunun düzenlenmesi sırasında Python girintileme hatası verdi.

**Çözüm:** Hata mesajında belirtilen satırı kontrol ederek fonksiyon içindeki kodların girintilerini düzelttim.

**Hata 3 – Dosyanın Bulunamaması**

Terminalde Python dosyasını çalıştırırken dosya adının yanlış yazılması nedeniyle program başlatılamadı.

**Çözüm:** Dosya adını kontrol ederek `python3 main.py` komutunu doğru biçimde çalıştırdım.

## 5. Yapay Zekâ Önerilerinde Tespit Edilen Sınırlama

Yapay zekâ tarafından önerilen saat hesaplama algoritması, günlük kullanım sıklığına göre 24 saati eşit aralıklara bölmektedir.

Ancak ilaçların kullanım saatleri etken maddeye, farmasötik forma, reçete talimatlarına ve hastanın özelliklerine göre değişebilmektedir.

Bu nedenle algoritmanın gerçek tedavi planlamasında kullanılmasının uygun olmadığını değerlendirdim. Uygulamaya eğitim amaçlı kullanım uyarısı ekleyerek bu sınırlamayı belirttim.

## 6. Yapay Zekâ Kullanımına İlişkin Değerlendirmem

PharmaDose projesini geliştirirken ChatGPT'den yararlanmak, Python programlama dilinin temel yapılarını öğrenmemi kolaylaştırdı. Özellikle fonksiyonlar, döngüler, koşullu ifadeler, listeler, sözlükler ve dosya işlemleri hakkında uygulamalı deneyim kazandım.

Bununla birlikte yapay zekâ tarafından oluşturulan kodların her zaman doğrudan çalışmayabileceğini öğrendim. Kodların doğru yere yerleştirilmesi, girintilerin kontrol edilmesi ve farklı girdilerle test edilmesi gerektiğini deneyimledim.

Bu süreç, yapay zekânın öğrenmeyi destekleyen bir araç olduğunu ancak oluşturulan sonuçların kullanıcı tarafından değerlendirilmesi gerektiğini anlamamı sağladı.

## 7. Yapay Zekâ Kullanım Beyanı

Bu projenin geliştirilmesi sırasında OpenAI tarafından sunulan ChatGPT uygulamasından proje planlama, kod oluşturma, programlama kavramlarını öğrenme, hata ayıklama ve dokümantasyon hazırlama amacıyla yararlanılmıştır.

Yapay zekâ tarafından önerilen kodlar Visual Studio Code ortamında çalıştırılarak test edilmiş ve karşılaşılan hatalar düzeltilmiştir. Projenin eğitim amaçlı olduğu ve gerçek tıbbi karar verme süreçlerinde kullanılmaması gerektiği belirtilmiştir.

## 8. Kaynakça

OpenAI. (2026). *ChatGPT* [Büyük dil modeli]. https://chatgpt.com/
