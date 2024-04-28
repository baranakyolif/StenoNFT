This python code hides another image in the most relevant pixels of the image using the Least
Significant Bit (LSB) shorthand technique. Picture-in-picture logic is used to hide another linked image inside an NFT.





Output of the version with the sizing issue fixed (Python)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from google.colab import drive

drive.mount('/content/drive', force_remount=True)  # Eğer önceden monte edilmişse, zorla tekrar monte edin

def load_image(image_path):
    """Verilen yoldan resmi yükler ve RGB formatına dönüştürür."""
    img = Image.open(image_path).convert('RGB')
    return img

def encode_image(carrier_img, secret_img, num_lsb):
    """Taşıyıcı resim içerisine gizli resmi LSB metodu ile gizler."""
    carrier = np.array(carrier_img)
    # secret_img'yi carrier_img'in boyutlarına uygun şekilde yeniden boyutlandır
    secret = np.array(secret_img.resize((carrier_img.width, carrier_img.height), Image.LANCZOS))
    
    # Gizli resmi, taşıyıcı resmin en az anlamlı bitlerine yerleştir
    for i in range(3):  # RGB kanalları için
        carrier[:, :, i] = (carrier[:, :, i] & ~(2**num_lsb - 1)) | (secret[:, :, i] >> (8 - num_lsb))
    
    # Yeni resmi oluştur ve döndür
    encoded_image = Image.fromarray(carrier)
    return encoded_image

def decode_image(encoded_img, num_lsb):
    """Kodlanmış resimden gizli resmi çıkarır."""
    encoded = np.array(encoded_img)
    secret = np.zeros_like(encoded)

    # Gizli resmi kodlanmış resmin en az anlamlı bitlerinden çıkar
    for i in range(3):
        secret[:, :, i] = (encoded[:, :, i] & (2**num_lsb - 1)) << (8 - num_lsb)

    secret_image = Image.fromarray(secret)
    return secret_image

def main():
    carrier_path = '/content/drive/My Drive/2.jpg'
    secret_path = '/content/drive/My Drive/3.jpg'
    
    carrier_image = load_image(carrier_path)
    secret_image = load_image(secret_path)
    
    encoded_image = encode_image(carrier_image, secret_image, num_lsb=2)
    decoded_image = decode_image(encoded_image, num_lsb=2)
    
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 3, 1)
    plt.imshow(carrier_image)
    plt.title('Taşıyıcı Resim')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(encoded_image)
    plt.title('Kodlanmış Resim')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(decoded_image)
    plt.title('Çözümlenmiş Gizli Resim')
    plt.axis('off')
    
    plt.show()

if __name__ == "__main__":
    main()




















First Version:
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_image(image_path):
    """Resmi yükler ve numpy dizisine dönüştürür."""
    img = Image.open(image_path)
    return np.array(img)

def encode_image(carrier_img, secret_img, num_lsb):
    """Taşıyıcı resim içerisine gizli resmi gizler."""
    carrier = np.array(carrier_img)
    secret = np.array(secret_img.resize(carrier.shape[0:2], Image.ANTIALIAS))
    
    # Gizli resmin kanallarını, taşıyıcı resmin en az anlamlı bitlerine gizle
    for i in range(3):  # RGB kanalları için
        carrier[:, :, i] = (carrier[:, :, i] & (255 << num_lsb)) | (secret[:, :, i] >> (8 - num_lsb))

    # Yeni resmi oluştur
    encoded_image = Image.fromarray(carrier)
    return encoded_image

def decode_image(encoded_img, num_lsb, original_size):
    """Gizlenmiş resmi çıkarır."""
    encoded = np.array(encoded_img)
    secret = np.zeros_like(encoded)

    # Gizli resmi en az anlamlı bitlerden çıkar
    for i in range(3):
        secret[:, :, i] = (encoded[:, :, i] & (2**num_lsb - 1)) << (8 - num_lsb)

    # Orijinal boyutlarına geri döndür
    secret_image = Image.fromarray(secret)
    secret_image = secret_image.resize(original_size, Image.ANTIALIAS)
    return secret_image

def main():
    # Google Drive'dan resim yolları
    carrier_path = '/content/drive/My Drive/1.png'
    secret_path = '/content/drive/My Drive/ll.png'
    
    # Resimleri yükle
    carrier_image = Image.open(carrier_path)
    secret_image = Image.open(secret_path)
    
    # Encode işlemi
    num_lsb = 2
    encoded_image = encode_image(carrier_image, secret_image, num_lsb)
    encoded_image.save('/content/drive/My Drive/encoded_image.png')
    
    # Decode işlemi
    decoded_image = decode_image(encoded_image, num_lsb, secret_image.size)
    decoded_image.save('/content/drive/My Drive/decoded_image.png')
    
    # Resimleri göster
    plt.figure(figsize=(10, 8))
    plt.subplot(1, 3, 1)
    plt.imshow(carrier_image)
    plt.title('Carrier Image')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(encoded_image)
    plt.title('Encoded Image')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(decoded_image)
    plt.title('Decoded Image')
    plt.axis('off')
    
    plt.show()

if __name__ == "__main__":
    main()
