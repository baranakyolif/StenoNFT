 #ENCODE - FOR COLAP (BLUE VALUE)

def mesaji_resime_kodla(kaynak_resim_yolu, mesaj, cikti_resim_yolu):
    img = Image.open(kaynak_resim_yolu)
    pixels = img.load()

    width, height = img.size
    if len(mesaj) > width:
        raise ValueError("Mesaj resme kodlanacak kadar kısa olmalı")
 
    for i in range(len(mesaj)):
        r, g, b = pixels[i, 0]
        pixels[i, 0] = (r, g, ord(mesaj[i]))

   
    r, g, b = pixels[width-1, height-1]
    pixels[width-1, height-1] = (r, g, len(mesaj))

   
    img.save(cikti_resim_yolu, 'PNG')

 
kaynak_resim_yolu = '/content/drive/My Drive/1.png'
cikti_resim_yolu = '/content/drive/My Drive/modified_image.png'
mesaj = "Merhaba, Dünya!"
mesaji_resime_kodla(kaynak_resim_yolu, mesaj, cikti_resim_yolu)
print("Mesaj resme kodlandı.")


 # DECODE
from PIL import Image

def mesaji_resimden_cikar(resim_yolu):
    img = Image.open(resim_yolu)
    pixels = img.load()

  
    width, height = img.size
    mesaj_uzunlugu = pixels[width-1, height-1][2]

 
    mesaj = ""
    for j in range(mesaj_uzunlugu):
        pixel = pixels[j, 0]
        mesaj += chr(pixel[2])   

    return mesaj

# Örnek kullanım
resim_yolu = '/content/drive/My Drive/modified_image.png'
mesaj = mesaji_resimden_cikar(resim_yolu)
print("Çözülen mesaj:", mesaj)

 
