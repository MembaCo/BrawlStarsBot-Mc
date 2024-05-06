# BrawlStarsBot
⚠️ **YASAL UYARI!!!** ****Botu kullanırken kupa kaybedebilirsiniz!!! Botun amacı ustalık toplamak** ⚠️

Tek başına hesaplaşma yoluyla çiftlik ustalığı için Brawl yıldızları botu. Bot çalıları bulacak ve saklanacak, ayrıca menzil içindeyse düşmanlara saldıracak. Makro, yenildiğinde otomatikleştirmek için koda entegre edilmiştir, otomatik olarak başka bir maç için sıraya girecektir. 

## Bilgi
“Learn Code By Gaming”](https://www.youtube.com/watch?v=KecMlLUuiE4&list=PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI) ve [“How To Train YOLOv5 For Recognizing Game Objects In Real-Time” by “Jes Fink-Jensen”](https://betterprogramming.pub/how-to-train-yolov5-for-recognizing-custom-game-objects-in-real-time-9d78369928a8) [OpenCV Object Detection in Games Python Tutorial çalma listesinden esinlenilmiştir.]

Bluestacks uygulama oynatıcısı, Brawl Stars'ı bilgisayara taklit etmek için kullanılır ve bot için özel bir Bluestacks kontrolü kullanılır. Bot, tank gibi savaşçılarla ve küçük engellerin (duvar, çalı, çit vb.) ve çok sayıda çalının bulunduğu haritalarda iyi çalışır.
Botu çalıştırmak için önerilen bir harita, Frank, Sam, Buster, Pearl, Nita, vb. gibi kısa / orta menzilli ve tanky brawlers kullanarak ada istilasıdır ...

## Bot özellikleri
- Tam otomatik
   - Oyuncu yenildiğinde, maçtan çıkacaktır
   - Başka bir eşleşme iste
   - Yükleme sırasında botu başlatın
- En yakın çalıyı bul ve içine saklan. 
- Menzil içindeyken düşmana saldırın
- Düşman oyuncuya yaklaştığında aygıtı etkinleştirin
- Bot için özel Bluestack oyun kontrolü

  
## Botun demosu
[![Videoyu izleyin](https://github.com/Jooi025/BrawlStarsBot/blob/main/misc/image/youtube_thumbnail.jpg)](https://youtu.be/TWmNfkQBVYk?si=CXaSBoAV-YknJPLt)

## Gereksinim
* Windows İşletim Sistemi
* [Bluestacks 5](https://www.bluestacks.com/download.html) Brawl Star'ı çalıştırmak ve özel kontrol için
* Python sürüm 3.11.6

## Bot nasıl kurulur ve çalıştırılır?
### [Öğretici ve yaygın hata düzeltme oynatma listesini izleyin](https://youtube.com/playlist?list=PLD9X_geub8rmkcpJSWzvoqmB9VZk-9TfO&si=7vrCV9s1kLviRaTL)
### Klon Repo
1. Depoyu klonlayın 
```
git clone https://github.com/Jooi025/BrawlStarsBot.git
```
2. Gerekli kütüphaneyi yükleyin
```
cd BrawlStarsBot
pip install -r requirements.txt
```
[Yazma talimatı](https://github.com/Jooi025/BrawlStarsBot/blob/main/misc/textInstruction.md)
### Repo'yu Güncelle 
```
cd BrawlStarsBot
git pull
```
 ## Yapılması gereken iyileştirmeler
 - [ ] bot güç küpü kutularına saldırabilir ve onları toplayabilir
 - [x] düşman tespitini iyileştirir (daha az yanlış tespit)
 - [ ] oyuncu tespitini değiştirin ve HSF'yi ölçmenize gerek yok 
 - [x] fırtına yönü fonksiyonunu iyileştirir 
 - [x] “mağlup” ekran algılamasını iyileştirin
 - [x] “botu durdur” ifadesinin spam olarak yazdırılmasını düzeltin 
 - [x] düşük performanslı bilgisayar için fps'yi iyileştir 