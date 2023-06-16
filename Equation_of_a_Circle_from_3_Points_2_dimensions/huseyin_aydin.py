
import math


class Nokta:
    def __init__(self, x, y):
        self.x = x  # Noktanın x koordinatıdır
        self.y = y  # Noktanın y koordinatıdır

    def uzaklik(self, nokta):
        dx = self.x - nokta.x  # x koordinatları arasındaki fark
        dy = self.y - nokta.y  # y koordinatları arasındaki fark
        return math.sqrt(dx**2 + dy**2)  # İki nokta arasındaki mesafeyi hesaplar burası

class Cember:
    def __init__(self, nokta1, nokta2, nokta3):
        self.nokta1 = nokta1  # Çemberin üzerinde bulunan birinci nokta
        self.nokta2 = nokta2  # Çemberin üzerinde bulunan ikinci nokta
        self.nokta3 = nokta3  # Çemberin üzerinde bulunan üçüncü nokta

    def merkez_yaricap_hesapla(self):
        def orta_nokta(nokta1, nokta2):
            orta_x = (nokta1.x + nokta2.x) / 2  # İki noktanın x koordinatlarının ortalaması
            orta_y = (nokta1.y + nokta2.y) / 2  # İki noktanın y koordinatlarının ortalaması
            return Nokta(orta_x, orta_y)  # Orta noktanın oluşturulması ve döndürülmesi

        def uzaklik_hesapla(nokta1, nokta2):
            dx = nokta1.x - nokta2.x  # x koordinatları arasındaki fark
            dy = nokta1.y - nokta2.y  # y koordinatları arasındaki fark
            return math.sqrt(dx**2 + dy**2)  # İki nokta arasındaki mesafeyi hesaplar

        def egim_hesapla(nokta1, nokta2):
            return (nokta2.y - nokta1.y) / (nokta2.x - nokta1.x)  # İki nokta arasındaki doğrunun eğimini hesaplar

        def dik_egim_hesapla(orta_nokta, egim):
            return -1 / egim  # Verilen doğrunun dikey eğimini hesaplar

        def kesisim_noktasi_bul(e1, b1, e2, b2):
            x = (b2 - b1) / (e1 - e2)  # İki doğrunun kesişim noktasının x koordinatı
            y = e1 * x + b1  # İki doğrunun kesişim noktasının y koordinatı
            return Nokta(x, y)  # Kesişim noktasının oluşturulması ve döndürülmesi

        orta1 = orta_nokta(self.nokta1, self.nokta2)  # nokta1 ve nokta2 arasındaki orta noktanın bulunması
        orta2 = orta_nokta(self.nokta2, self.nokta3)  # nokta2 ve nokta3 arasındaki orta noktanın bulunması

        egim1 = egim_hesapla(self.nokta1, self.nokta2)  # nokta1 ve nokta2'yi birleştiren doğrunun eğiminin hesaplanması
        egim2 = egim_hesapla(self.nokta2, self.nokta3)  # nokta2 ve nokta3'ü birleştiren doğrunun eğiminin hesaplanması

        dik_egim1 = dik_egim_hesapla(orta1, egim1)  # nokta1 ve nokta2'yi birleştiren doğrunun orta noktasından geçen dikey doğrunun eğiminin hesaplanması
        dik_egim2 = dik_egim_hesapla(orta2, egim2)  # nokta2 ve nokta3'ü birleştiren doğrunun orta noktasından geçen dikey doğrunun eğiminin hesaplanması

        merkez = kesisim_noktasi_bul(dik_egim1, orta1.y - dik_egim1 * orta1.x, dik_egim2, orta2.y - dik_egim2 * orta2.x)  # Dikey doğruların kesişim noktasının bulunması (çemberin merkezi)

        yaricap = uzaklik_hesapla(self.nokta1, merkez)  # Merkez noktası ile nokta1 arasındaki mesafenin hesaplanması (çemberin yarıçapı)

        return merkez, yaricap  # Çemberin merkezi ve yarıçapının döndürülmesi

    def noktalari_yazdir(self):
       
        print("Verilen Noktalar:")
        print("Nokta 1: ({}, {})".format(self.nokta1.x, self.nokta1.y))
        print("Nokta 2: ({}, {})".format(self.nokta2.x, self.nokta2.y))
        print("Nokta 3: ({}, {})".format(self.nokta3.x, self.nokta3.y))


nokta1 = Nokta(6, 3)  # x=6 ve y=3 olan bir Nokta nesnesi oluşturulması
nokta2 = Nokta(4, 1)  # x=4 ve y=1 olan bir Nokta nesnesi oluşturulması
nokta3 = Nokta(2.59, 1.59)  # x=2.59 ve y=1.59 olan bir Nokta nesnesi oluşturulması

cember = Cember(nokta1, nokta2, nokta3)  # Cember nesnesinin oluşturulması
cember.noktalari_yazdir()  # Noktaları yazdırma
merkez, yaricap = cember.merkez_yaricap_hesapla()  # Çemberin merkezini ve yarıçapını hesaplama
print("Çemberin Merkezi: ({}, {})".format(merkez.x, merkez.y))
print("Çemberin Yarıçapı: {}".format(yaricap))
