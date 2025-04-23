import rarfile
import itertools
import string
import os

# unrar.exe'nin tam yolunu belirtin
rarfile.UNRAR_TOOL = "C:\Program Files\WinRAR\UnRAR.exe"  # Windows için

# RAR dosyasının yolunu belirtin
rar_path = "C:/Users/husey/Desktop/text.rar"

# Çıktı klasörünü oluştur
output_folder = "çıktı_klasörü"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Karakter seti ve maksimum şifre uzunluğu
charset = string.ascii_letters + string.digits + string.punctuation  # Harfler, rakamlar ve özel karakterler
max_length = 8  # Maksimum şifre uzunluğu

# RAR dosyasını aç
rf = rarfile.RarFile(rar_path)

def brute_force():
    total_attempts = 0  # Toplam deneme sayısı
    for length in range(1, max_length + 1):  # Şifre uzunluğunu artırarak dene
        for attempt in itertools.product(charset, repeat=length):
            password = ''.join(attempt)  # Kombinasyonu birleştir
            total_attempts += 1
            print(f"Denenen şifre: {password} (Toplam deneme: {total_attempts})")
            try:
                rf.extractall(path=output_folder, pwd=password)
                print(f"Şifre bulundu: {password}")
                return password
            except rarfile.BadRarFile:
                continue  # Şifre yanlışsa devam et
            except rarfile.RarCannotExec:
                print("UnRAR aracı bulunamadı. Lütfen UnRAR yolunu kontrol edin.")
                return None
    print("Şifre bulunamadı.")
    return None

# Brute-force işlemini başlat
brute_force()