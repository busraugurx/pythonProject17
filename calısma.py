print("Hoşgeldiniz\nOyuncu Kaydetme Programı")

oyuncunun_adı=input("Oyuncu Adını girin: ")
oyuncunun_soyadı=input("Oyuncunun Soyadını Girin:")
oyuncunun_takımı=input("Oyuncunun Takımını Girin: ")

print("bilgiler kaydediliyor...")

Bilgiler=[oyuncunun_adı,oyuncunun_soyadı,oyuncunun_takımı]

print("OYUNCUNUN ADI: {}\nOYUNCUNUN SOYADI: {}\nOYUNCUNUN TAKIMI: {}\n" .format(Bilgiler[0],Bilgiler[1],Bilgiler[2]))