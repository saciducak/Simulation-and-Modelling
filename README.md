# Simulation-and-Modelling
simulation and modelling project with python numpy and matplotlib
- İki ayrı simulasyon hazırladım:
- Birincisi, çubukların „Denge durumları üzerinden ortalama uzaklığı hesaplayan“ bir simülasyon
- İkincisi „kopartma-ekleme işlemi üzerinde kısıtlama ile iki çubuk arası mesafeyi hesaplayan“ bir simulasyon
- Numpy ve Matplotlib kütüphanelerini dahil ettik. Grafiksel sonuçları elde etmek ve onları yorumlayabilmek için.
- Çubukların konumlarını bilmek için „Positions“ adlı bir dizi oluşturdum.
- kısıtlı değerlerle uzaklık hesapları için constrained dizisi oluşturdum
- eşik değeri, seçilmis çubuk(selected_bar), degisim degerleri vs gibi birçok değişkeni de tanımlayıp for döngüleri içinde çeşitli hesaplamaları yapıldı.
- En son olarak plt.show ile histogramlarımızı oluşturdum ve pdf. dosyamıza ekledim.