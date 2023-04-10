import re
import time
import os

class Kayit:
    def __init__(self, program_ad):
        self.program_adi = program_ad
        self.dongu = True

    def program(self):
        secim = self.menu()

        if secim == "1":
            print("Kayıt ekleme menüsüne yönlendiriliyorsunuz")
            time.sleep(1)
            self.kayit_ekle()

        elif secim == "2":
            print("Kayıt silme menüsüne yönlendiriliyorsunuz")
            time.sleep(1)
            self.kayit_sil()

        elif secim == "3":
            print("Verilere erişiliyor")
            time.sleep(1)
            self.kayit_show()

        elif secim == "4":
            print("Sistem kapatiliyor")
            time.sleep(1)
            self.cikis()

        else:
            print("Hatali secim")
            self.program()

    def menu(self):  # kullanıcıdan hangi islemi yapacagini alacak

        def kontrol(secim):
            if re.search("[^1-4]", secim):  # kisinin sadece 1 2 3 veya 4 secmesini sağlamamız lazım
                raise Exception("Lütfen 1 ve 4 arasında geçerli bir seçimin yapiniz")
            # secim 14 veya 41 114 ... girilirse yukardaki kısım çalışmaz
            elif len(secim) != 1:
                raise Exception("Lütfen 1 ve 4 arasında geçerli bir seçimin yapiniz")

        while True:
            try:
                secim = input(
                    "Merhabalar {} otomasyon sistemine hosgeldiniz\nYapmak istediğiniz işlemi seçiniz\n1- Kayit Ekle\n2- Kayit Sil\n3- Kayitlari Göster\n4- Cikis Yap\nSeciminiz: ".format(
                        self.program_adi))
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(1)
            else:
                break
        return secim

    def kayit_ekle(self):  # dosya kayıt
        if not os.path.isfile("Bilgiler.txt"):  # eğer bu isimde klasör yoksa oluşturuyoruz.
            with open("Bilgiler.txt", "w") as file:
                print("Bilgiler.txt isimli dosya oluşturuldu.")
                pass

        def kontrol_ad(name):
            if name.isalpha() == False:
                raise Exception("Adınız sadece alfabetik karakterlerden oluşmaldıır")

        while True:
            try:
                name = input("Name: ")
                kontrol_ad(name)
            except Exception as hata:
                print(hata)
                time.sleep(1)
            else:
                break

        def kontrol_soyad(surname):
            if surname.isalpha() == False:
                raise Exception("Soyadınız sadece alfabetik karakterlerden oluşmaldıır")

        while True:
            try:
                surname = input("Surname: ")
                kontrol_soyad(surname)
            except Exception as hata:
                print(hata)
                time.sleep(1)
            else:
                break

        def kontrol_yas(age):
            if age.isdigit() == False:
                raise Exception("Yasiniz sadece rakamlardan oluşmaldıır")

        while True:
            try:
                age = input("Age: ")
                kontrol_yas(age)
            except Exception as hata:
                print(hata)
                time.sleep(1)
            else:
                break

        def kontrol_id(id):
            if id.isdigit() == False:
                raise Exception("ID sadece rakamlardan oluşmaldıır")
            elif len(id) != 7:
                raise Exception("ID 7 karakterden oluşmaldıır")

        while True:
            try:
                id = input("ID: ")
                kontrol_id(id)
            except Exception as hata:
                print(hata)
                time.sleep(1)
            else:
                break

        def kontrol_mail(mail):
            if not re.search("@", mail):
                raise Exception("Geçerli bir mail adresi giriniz!")
            elif not re.search("\.com", mail):  # . ile bir problem var?
                raise Exception("Geçerli bir mail adresi giriniz!")

        while True:
            try:
                mail = input("Mail: ")
                kontrol_mail(mail)
            except Exception as hata:
                print(hata)
                time.sleep(1)
            else:
                break

        # önce dosyayı okuyacaz. eğer dosya boşsa dosya_no 1'den başlayacak dosya doluysa uygun sayıdan başlayacak
        with open("Bilgiler.txt", "r", encoding="utf-8") as file:
            satir_sayisi = file.readlines()
        if len(satir_sayisi) == 0:
            dosya_no = 1
        else:
            dosya_no = len(satir_sayisi) + 1

        with open("Bilgiler.txt", "a+", encoding="utf-8") as file:
            file.write("{}-{} {} {} {} {}\n".format(dosya_no, name, surname, age, id, mail))
            print("Veriler ekleniyor...")
            time.sleep(1)
        self.menu_don()

    def kayit_sil(self):
        id_numarasi = input("Kaydı silincek kişinin id numarasını giriniz: ")
        my_list = []
        with open("Bilgiler.txt", "r", encoding="utf-8") as file:
            for line in file.readlines():
                my_list.append(line.strip()[2:])

        bulunan_index = None
        for index, eleman in enumerate(my_list):
            if id_numarasi in eleman:
                bulunan_index = index
                break

        if bulunan_index is not None:
            my_list.pop(bulunan_index)
            with open("Bilgiler.txt", "w", encoding="utf-8") as file:
                for index, eleman in enumerate(my_list):
                    file.write(f"{index + 1}-{eleman}\n")
            print("Kayıt başarıyla silindi")
        self.menu_don()

    def kayit_show(self):  # dosya içerigini printleme
        print("Kullanici bilgileri veriliyor")
        with open("Bilgiler.txt", "r", encoding="utf-8") as file:
            for i in file:
                print(i, end="")
        time.sleep(1)
        self.menu_don()

    def cikis(self):  # sistemden cikis
        print("Sistem kapatılıyor")
        time.sleep(1)
        self.dongu = False
        exit()

    def menu_don(self):  # menuye dönme secenegi
        while True:
            x = input("Ana menüye dönmek için 6'ya, sistemden çıkmak için 5'e basınız: ")
            if x == "6":
                print("Ana menü yükleniyor")
                time.sleep(1)
                self.program()
                break
            elif x == "5":
                self.cikis()
                break
            else:
                print("Hatali bir deger girdiniz")


sistem = Kayit("Kullanici Kayit Sistemi")
while sistem.dongu:
    sistem.program()  # menü'nün sürekli olarak karşımıza çıkmasını sağlıyacak
