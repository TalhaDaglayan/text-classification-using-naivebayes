import re
import os
import glob
from collections import Counter
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_txt_files(file_paths):
    all_content = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        all_content.append(content)
    return all_content

current_path = os.getcwd()

# Okunacak dosyaların bulunduğu dizin
directory_path = current_path + '/training data/'

# Tüm .txt dosyalarını bul
txt_files = glob.glob(directory_path + '*.txt')

# Tüm dosyaları oku
all_content = read_txt_files(txt_files)

# Ayırmış olduğumuz metni bir listeye çevir
separated_text = ["\n\n".join(content.split("\n\n")) for content in all_content]
list_format = [item.strip() for item in separated_text]



def preprocess_text(text):
    # İngilizce edat, bağlaç, zarf, zamir, yardımcı fiil, sayı ve noktalama işaretlerini kaldır
    text = re.sub(r'\b(?:yes|no|go|all|after|one|two|three|four|five|six|seven|eight|nine|ten|as|also|into|there|who|between|by|what|from|still|but|at|in|and|on|the|with|to|of|for|a|an|is|was|are|am|I|you|he|she|it|we|they|your|my|his|its|our|their|that|this|these|those|be|been|being|have|has|had|do|does|did|can|could|will|would|shall|should|may|might|must)\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\b\d+\b', '', text)  # Sayıları kaldır
    text = re.sub(r'[^\w\s]', '', text)  # Noktalama işaretlerini kaldır

    # Küçük harfe çevir ve kelimelere ayır
    words = re.findall(r'\b\w+\b', text.lower())

    return words

def count_word_occurrences(texts):
    # Tüm metinlerin kelimelerini birleştir
    all_words = []
    for text in texts:
        processed_words = preprocess_text(text)
        all_words.extend(processed_words)

    # Tekrar eden kelimeleri say
    word_counts = Counter(all_words)

    # Sözlük olarak frekansları döndür
    word_dict = dict(word_counts)

    return word_dict

# Kelime sayılarını hesapla
toplam_sozluk = count_word_occurrences(list_format)

print(list_format[0])

toplam_kelime = sum(toplam_sozluk.values())
sozcuk_kelime = len(toplam_sozluk)

print(toplam_word_occurrences_dict["turkish"])

print(f"metinlerdeki toplam kelime sayisi = {toplam_kelime}\nsozluge eklenen toplam kelime sayisi = {sozcuk_kelime}")


"""SPORTS"""
# Okuma fonksiyonu
def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

current_path = os.getcwd()

# Okunacak dosyaların bulunduğu dizin
directory_path = current_path + '/training data/'

# Tüm .txt dosyalarını bul
txt_files = glob.glob(directory_path + 'sports.txt')

# Her bir dosyayı oku
for file_path in txt_files:
    content = read_txt_file(file_path)   

# Metni boşluklardan ayır
separated_text = content.split("\n\n")

# Ayırmış olduğumuz metni listeye çevir
list_format = [item.strip() for item in separated_text]

def preprocess_text(text):
    # İngilizce edat, bağlaç, zarf, zamir, yardımcı fiil, sayı ve noktalama işaretlerini kaldır
    text = re.sub(r'\b(?:yes|no|go|all|after|one|two|three|four|five|six|seven|eight|nine|ten|as|also|into|there|who|between|by|what|from|still|but|at|in|and|on|the|with|to|of|for|a|an|is|was|are|am|I|you|he|she|it|we|they|your|my|his|its|our|their|that|this|these|those|be|been|being|have|has|had|do|does|did|can|could|will|would|shall|should|may|might|must)\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\b\d+\b', '', text)  # Sayıları kaldır
    text = re.sub(r'[^\w\s]', '', text)  # Noktalama işaretlerini kaldır
    
    # Küçük harfe çevir ve kelimelere ayır
    words = re.findall(r'\b\w+\b', text.lower())
    
    return words

def count_word_occurrences(texts):
    # Tüm metinlerin kelimelerini birleştir
    all_words = []
    for text in texts:
        processed_words = preprocess_text(text)
        all_words.extend(processed_words)
    
    # Tekrar eden kelimeleri say
    word_counts = Counter(all_words)
    
    # Sözlük olarak frekansları döndür
    word_dict = dict(word_counts)
    
    return word_dict

# Kelime sayılarını hesapla
spor_sozluk = count_word_occurrences(list_format)

sports_toplam_kelime = sum(spor_sozluk.values())
sports_sozcuk_kelime = len(spor_sozluk)






"""POLITICS"""
# Okuma fonksiyonu
def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

current_path = os.getcwd()

# Okunacak dosyaların bulunduğu dizin
directory_path = current_path + '/training data/'

# Tüm .txt dosyalarını bul
txt_files = glob.glob(directory_path + 'politics.txt')

# Her bir dosyayı oku
for file_path in txt_files:
    content = read_txt_file(file_path)   

# Metni boşluklardan ayır
separated_text = content.split("\n\n")

# Ayırmış olduğumuz metni listeye çevir
list_format = [item.strip() for item in separated_text]

def preprocess_text(text):
    # İngilizce edat, bağlaç, zarf, zamir, yardımcı fiil, sayı ve noktalama işaretlerini kaldır
    text = re.sub(r'\b(?:yes|no|go|all|after|one|two|three|four|five|six|seven|eight|nine|ten|as|also|into|there|who|between|by|what|from|still|but|at|in|and|on|the|with|to|of|for|a|an|is|was|are|am|I|you|he|she|it|we|they|your|my|his|its|our|their|that|this|these|those|be|been|being|have|has|had|do|does|did|can|could|will|would|shall|should|may|might|must)\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\b\d+\b', '', text)  # Sayıları kaldır
    text = re.sub(r'[^\w\s]', '', text)  # Noktalama işaretlerini kaldır
    
    # Küçük harfe çevir ve kelimelere ayır
    words = re.findall(r'\b\w+\b', text.lower())
    
    return words

def count_word_occurrences(texts):
    # Tüm metinlerin kelimelerini birleştir
    all_words = []
    for text in texts:
        processed_words = preprocess_text(text)
        all_words.extend(processed_words)
    
    # Tekrar eden kelimeleri say
    word_counts = Counter(all_words)
    
    # Sözlük olarak frekansları döndür
    word_dict = dict(word_counts)
    
    return word_dict

# Kelime sayılarını hesapla
politics_sozcuk = count_word_occurrences(list_format)

politics_toplam_kelime = sum(politics_sozcuk.values())
politics_sozcuk_kelime = len(politics_sozcuk)












"""CULTURE ARTS"""
# Okuma fonksiyonu
def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

current_path = os.getcwd()

# Okunacak dosyaların bulunduğu dizin
directory_path = current_path + '/training data/'

# Tüm .txt dosyalarını bul
txt_files = glob.glob(directory_path + 'culture_arts.txt')

# Her bir dosyayı oku
for file_path in txt_files:
    content = read_txt_file(file_path)   

# Metni boşluklardan ayır
separated_text = content.split("\n\n")

# Ayırmış olduğumuz metni listeye çevir
list_format = [item.strip() for item in separated_text]



def preprocess_text(text):
    # İngilizce edat, bağlaç, zarf, zamir, yardımcı fiil, sayı ve noktalama işaretlerini kaldır
    text = re.sub(r'\b(?:yes|no|go|all|after|one|two|three|four|five|six|seven|eight|nine|ten|as|also|into|there|who|between|by|what|from|still|but|at|in|and|on|the|with|to|of|for|a|an|is|was|are|am|I|you|he|she|it|we|they|your|my|his|its|our|their|that|this|these|those|be|been|being|have|has|had|do|does|did|can|could|will|would|shall|should|may|might|must)\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\b\d+\b', '', text)  # Sayıları kaldır
    text = re.sub(r'[^\w\s]', '', text)  # Noktalama işaretlerini kaldır
    
    # Küçük harfe çevir ve kelimelere ayır
    words = re.findall(r'\b\w+\b', text.lower())
    
    return words

def count_word_occurrences(texts):
    # Tüm metinlerin kelimelerini birleştir
    all_words = []
    for text in texts:
        processed_words = preprocess_text(text)
        all_words.extend(processed_words)
    
    # Tekrar eden kelimeleri say
    word_counts = Counter(all_words)
    
    # Sözlük olarak frekansları döndür
    word_dict = dict(word_counts)
    
    return word_dict

# Kelime sayılarını hesapla
culture_sozcuk = count_word_occurrences(list_format)

culturearts_toplam_kelime = sum(culture_sozcuk.values())
culturearts_sozcuk_kelime = len(culture_sozcuk)









"""HEALTH"""
# Okuma fonksiyonu
def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

current_path = os.getcwd()

# Okunacak dosyaların bulunduğu dizin
directory_path = current_path + '/training data/'

# Tüm .txt dosyalarını bul
txt_files = glob.glob(directory_path + 'health.txt')

# Her bir dosyayı oku
for file_path in txt_files:
    content = read_txt_file(file_path)   

# Metni boşluklardan ayır
separated_text = content.split("\n\n")

# Ayırmış olduğumuz metni listeye çevir
list_format = [item.strip() for item in separated_text]



def preprocess_text(text):
    # İngilizce edat, bağlaç, zarf, zamir, yardımcı fiil, sayı ve noktalama işaretlerini kaldır
    text = re.sub(r'\b(?:yes|no|go|all|after|one|two|three|four|five|six|seven|eight|nine|ten|as|also|into|there|who|between|by|what|from|still|but|at|in|and|on|the|with|to|of|for|a|an|is|was|are|am|I|you|he|she|it|we|they|your|my|his|its|our|their|that|this|these|those|be|been|being|have|has|had|do|does|did|can|could|will|would|shall|should|may|might|must)\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\b\d+\b', '', text)  # Sayıları kaldır
    text = re.sub(r'[^\w\s]', '', text)  # Noktalama işaretlerini kaldır
    
    # Küçük harfe çevir ve kelimelere ayır
    words = re.findall(r'\b\w+\b', text.lower())
    
    return words

def count_word_occurrences(texts):
    # Tüm metinlerin kelimelerini birleştir
    all_words = []
    for text in texts:
        processed_words = preprocess_text(text)
        all_words.extend(processed_words)
    
    # Tekrar eden kelimeleri say
    word_counts = Counter(all_words)
    
    # Sözlük olarak frekansları döndür
    word_dict = dict(word_counts)
    
    return word_dict

# Kelime sayılarını hesapla
health_sozcuk = count_word_occurrences(list_format)

health_toplam_kelime = sum(health_sozcuk.values())
health_sozcuk_kelime = len(health_sozcuk)




"""OLASILIK HESAPLAMALARI"""

p_sports = 0.25
p_politics = 0.25
p_culturearts = 0.25
p_health = 0.25

p_kelime_sports = {key: (value + 1) / (sports_toplam_kelime + sports_sozcuk_kelime) for key, value in toplam_sozluk.items()}
p_kelime_politics = {key: (value + 1) / (politics_toplam_kelime + politics_sozcuk_kelime) for key, value in toplam_sozluk.items()}
p_kelime_culturearts = {key: (value + 1) / (culturearts_toplam_kelime + culturearts_sozcuk_kelime) for key, value in toplam_sozluk.items()}
p_kelime_health = {key: (value + 1) / (health_toplam_kelime + health_sozcuk_kelime) for key, value in toplam_sozluk.items()}






"""TESTING DATA"""
def read_txt_files(file_paths):
    all_content = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        all_content.append(content)
    return all_content

# Get the current working directory
current_path = os.getcwd()

# Construct the full path to the directory
directory_path = os.path.join(current_path, 'testing data')

# Find all .txt files in the directory
txt_files = glob.glob(os.path.join(directory_path, '*.txt'))

# Read the content of all files
all_content = read_txt_files(txt_files)

# Assuming "testData.txt" is one of the files, get its content
test_data_content = all_content[txt_files.index(os.path.join(directory_path, 'testData.txt'))]

# Split the text using "#no" as a delimiter
separated_text = test_data_content.split("#")

# Convert the separated text to a list
list_format = [item.strip() for item in separated_text]


def preprocess_text(text):
    # İngilizce edat, bağlaç, zarf, zamir, yardımcı fiil, sayı ve noktalama işaretlerini kaldır
    text = re.sub(r'\b(?:yes|no|go|all|after|one|two|three|four|five|six|seven|eight|nine|ten|as|also|into|there|who|between|by|what|from|still|but|at|in|and|on|the|with|to|of|for|a|an|is|was|are|am|I|you|he|she|it|we|they|your|my|his|its|our|their|that|this|these|those|be|been|being|have|has|had|do|does|did|can|could|will|would|shall|should|may|might|must)\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\b\d+\b', '', text)  # Sayıları kaldır
    text = re.sub(r'[^\w\s]', '', text)  # Noktalama işaretlerini kaldır
    
    # Küçük harfe çevir ve kelimelere ayır
    words = re.findall(r'\b\w+\b', text.lower())
    
    return words

def count_word_occurrences(texts):
    # Tüm metinlerin kelimelerini birleştir
    all_words = []
    for text in texts:
        processed_words = preprocess_text(text)
        all_words.extend(processed_words)
    
    # Tekrar eden kelimeleri say
    word_counts = Counter(all_words)
    
    # Sözlük olarak frekansları döndür
    word_dict = dict(word_counts)
    
    return word_dict

test_sozlukler = []

for i in range(1, 13):
    test_sozluk = count_word_occurrences([list_format[i]])
    test_sozlukler.append(test_sozluk)

  


"""TAHMIN HESAPLAMA SPORTS"""

sozlukler = [p_kelime_sports, p_kelime_culturearts, p_kelime_politics, p_kelime_health]
kategoriler = {
    0:"Sports",
    1:"CultureArts",
    2:"Politics",
    3:"Health"
               }

for metin_index in range(0, len(test_sozlukler)):
    sonuc = []

    for index in range(4):
        # Ortak anahtarları belirle
        ortak_keys = set(test_sozlukler[metin_index].keys()) & set(sozlukler[index].keys())

        # Ortak anahtarları kullanarak değerlere eriş ve bir liste oluştur
        ortak_key_degerleri = [(key, test_sozlukler[metin_index][key], sozlukler[index][key]) for key in ortak_keys]

        carpim = 1
        # Sonuçları yazdır
        for olasilik in ortak_key_degerleri:
            carpim *= olasilik[2]

    
        sonuc.append((carpim) * (p_sports))
        
    max_sonuc = max(sonuc)  
    max_index = sonuc.index(max_sonuc)  
    print(f"degerler {sonuc}, kategori: {kategoriler[max_index]}")    
    print("\n")



kategori_kelime_sayilari = [sports_sozcuk_kelime, culturearts_sozcuk_kelime, politics_sozcuk_kelime, health_sozcuk_kelime]


print(f"sports kategorisi icin eklenen kelime sayisi: {kategori_kelime_sayilari[0]}")
print(f"culture Arts kategorisi icin eklenen kelime sayisi: {kategori_kelime_sayilari[1]}")
print(f"Politics kategorisi icin eklenen kelime sayisi: {kategori_kelime_sayilari[2]}")
print(f"Health kategorisi icin eklenen kelime sayisi: {kategori_kelime_sayilari[3]}")
    
print("\n")
print(f"sozluge toplam eklenen kelime sayisi: {toplam_kelime}")

"""GRAFIKLER"""



olasilik_dagilimi = [kategori_sayisi / toplam_kelime for kategori_sayisi in kategori_kelime_sayilari]


plt.figure(figsize=(8, 4))
plt.bar(['Sports', 'CultureArts', 'Politics', 'Health'], olasilik_dagilimi, color='skyblue')
plt.title('Öncül olasilik dagilimi')
plt.xlabel('Kategoriler')
plt.ylabel('olasilik')
plt.show()

print(p_kelime_sports)

ktgrler = ["politics", "culture arts"]

kelimeler = {'disney': 0.0012853470437017994,
             'buy': 0.0005141388174807198, 
             'star': 0.0033419023136246786, 
             'wars': 0.002827763496143959, 
             'production': 0.0010282776349614395,
             'company': 0.0012853470437017994, 
             'lucasfilm': 0.0012853470437017994, 
             '4bn': 0.0005141388174807198, 
             'creator': 0.0007712082262210797, 
             'films': 0.003084832904884319}

# Kelimelerin politics ve culture arts kategorileri için olasılıkları
politics_olasiliklar = [kelimeler[k] for k in kelimeler if k in kelimeler and kelimeler[k] > 0]
culture_arts_olasiliklar = [kelimeler[k] for k in kelimeler if k in kelimeler and kelimeler[k] > 0]

# Grafik 1: Politics Kategorisi İçin Koşullu Olasılıklar
plt.figure(figsize=(10, 4))
plt.bar(list(kelimeler.keys()), politics_olasiliklar, color='blue')
plt.title('Politics Kategorisi İçin Koşullu Olasılıklar')
plt.xlabel('Kelimeler')
plt.ylabel('Olasılık')
plt.xticks(rotation=45, ha='right')
plt.show()

# Grafik 2: Culture Arts Kategorisi İçin Koşullu Olasılıklar
plt.figure(figsize=(10, 4))
plt.bar(list(kelimeler.keys()), culture_arts_olasiliklar, color='green')
plt.title('Culture Arts Kategorisi İçin Koşullu Olasılıklar')
plt.xlabel('Kelimeler')
plt.ylabel('Olasılık')
plt.xticks(rotation=45, ha='right')
plt.show()

"""VERILERI TABLODA GOSTERME"""
data = {
    'Metin Index': list(range(1, 13)),
    'Gerçek Kategori': ['CultureArts', 'CultureArts', 'CultureArts', 'Politics', 'Politics', 'Politics', 'Sports', 'Sports', 'Sports', 'Health', 'Health', 'Health'],
    'Tahmin Edilen Kategori': ['CultureArts', 'CultureArts', 'CultureArts', 'Sports', 'Sports', 'CultureArts', 'CultureArts', 'Sports', 'CultureArts', 'CultureArts', 'Sports', 'Sports'],
    'CultureArts Olasılığı': [6.579171194998845e-161, 2.3609716145144438e-194, 2.7399501800859462e-118, 0.0, 0.0, 5.70038485756208e-205, 3.766385821434258e-197, 0.0, 2.9304572567420156e-295, 1.3433988743392883e-197, 0.0, 0.0],
    'Sports Olasılığı': [1.9081002620193337e-163, 2.2172480374884563e-197, 4.09706656450465e-120, 2.6121390292158485e-208, 2.34732504382085e-200, 6.201037331065943e-300, 9.276244305096367e-201,0.0 , 0.0, 0.0, 0.0, 0.0],
    'Politics Olasılığı': [1.6662668447222486e-164, 0.0, 1.2095306723727992e-198, 0.0, 0.0, 7.0931525084119214e-121, 7.0931525084119214e-121, 0.0, 0.0, 1.0562430622218229e-209, 1.0791209157601876e-201, 0.0],
    'Health Olasılığı': [2.053242040484825e-163,2.4199009831892352e-197, 4.318915684561624e-120, 0.0, 0.0, 2.8766674044972106e-208, 2.575080806974518e-200, 0.0, 7.097657781176266e-300, 0.0, 1.0163217722108034e-200, 0.0],
    
}

df = pd.DataFrame(data)


print(df)