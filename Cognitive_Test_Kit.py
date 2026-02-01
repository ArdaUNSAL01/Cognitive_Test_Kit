import tkinter as tk
from tkinter import messagebox
import random
import time

root = tk.Tk()
root.title("Bilişsel Test Kiti")
root.geometry("300x425")

#veri araçları
def Giris_ekrani():
    kisisel_veri = tk.Toplevel(root)
    kisisel_veri.title("Katılımcı Bilgileri")
    kisisel_veri.geometry("400x300")

    etiket = tk.Label(kisisel_veri, text="Lütfen Bilgilerinizi Giriniz")
    etiket.pack(pady=10)

    tk.Label(kisisel_veri, text="İsim/Soyisim").pack(pady=5)
    entry_isim = tk.Entry(kisisel_veri)
    entry_isim.pack(pady=5)

    tk.Label(kisisel_veri, text="Yaş").pack(pady=5)
    entry_yas = tk.Entry(kisisel_veri)
    entry_yas.pack(pady=5)

    def verileri_kaydet():
        isim = entry_isim.get() # Get komutu ile veri elınır print ile de nasıl kaydeileceğini gösterir.
        yas = entry_yas.get()
        print(f"Kaydedilen Bilgiler -> İsim: {isim}, Yaş: {yas}")
        kisisel_veri.destroy()

    button_kaydet = tk.Button(kisisel_veri, text="Kaydet", command=verileri_kaydet)
    button_kaydet.pack(pady=10)
    
def Dikkat_testi():
    dikkat_testi = tk.Toplevel(root)
    dikkat_testi.title("Dikkat Testi")
    dikkat_testi.geometry("600x300")
    tuval = tk.Canvas(dikkat_testi, width=600, height=200, bg="white")
    tuval.pack(pady=10)
    
    etiket = tk.Label(dikkat_testi, text="Dikkat Testi")
    etiket.pack(pady=10)
    dikkat_testi.title("FARKLI OLAN HARFİ BUL")
        
    def harf_uret():
        for i in range(250): 
          x = random.randint(20, 580)
          y = random.randint(20, 180)
          tuval.create_text(x, y, text="L", font="Arial 14", fill="black")
        
        tx =random.randint(20, 580)
        ty =random.randint(20, 180)
        hedef_harf = tuval.create_text(tx, ty, text="T", font="Arial 14", fill="black")
        tuval.tag_bind(hedef_harf, "<Button-1>", hedef_harf_tiklandi)
    
    def hedef_harf_tiklandi(event):
        bitis = time.time()
        sure = round(bitis - baslangic, 2)
        print(f"Kanka hedefi {sure} saniyede buldun!")
        dikkat_testi.destroy() 
    
    def başalngiç_zaman():
        global baslangic
        baslangic = time.time()
        harf_uret()

    başalngiç_zaman()

def Digit_Span_Baslat():
    ds_penceresi = tk.Toplevel(root)
    ds_penceresi.title("Digit Span Testi")
    ds_penceresi.geometry("400x400")

    basamak_sayisi = 3
    hedef_sayi = ""
    bilgi_etiketi = tk.Label(ds_penceresi, text="Sayılar ekranda görünüp kaybolacak.\nAklında tutup aynısını yazmalısın.", font=("Arial", 12))
    bilgi_etiketi.pack(pady=20)

    soru_etiketi = tk.Label(ds_penceresi, text="Hazır mısın?", font=("Arial", 30, "bold"), fg="black")
    soru_etiketi.pack(pady=30)

    giris_kutusu = tk.Entry(ds_penceresi, font=("Arial", 14))
    giris_kutusu.pack(pady=10)
    giris_kutusu.config(state="disabled") 
   
    def sayi_uret():
        nonlocal hedef_sayi
        ilk = str(random.randint(1, 9))
        digerleri = "".join([str(random.randint(0, 9)) for _ in range(basamak_sayisi - 1)])
        hedef_sayi = ilk + digerleri
        soru_etiketi.config(text=hedef_sayi)
        ds_penceresi.after(2000, sayiyi_gizle) 

    def sayiyi_gizle():
        soru_etiketi.config(text="???")
        giris_kutusu.config(state="normal") 
        giris_kutusu.delete(0, tk.END)
        giris_kutusu.focus()
        buton_kontrol.config(state="normal")

    def kontrol_et():
        nonlocal basamak_sayisi
        girilen = giris_kutusu.get()
        
        if girilen == hedef_sayi:
            messagebox.showinfo("Tebrikler", f"Doğru! {basamak_sayisi} basamağı geçtin.")
            basamak_sayisi += 1 
            giris_kutusu.delete(0, tk.END)
            giris_kutusu.config(state="disabled")
            buton_kontrol.config(state="disabled")
            ds_penceresi.after(1000, sayi_uret)
        else:
            print(f"Digit Span Testi Sonucu -> Ulaşılan seviye: {basamak_sayisi-1}")
            messagebox.showerror("Hata", f"Yanlış! Doğru sayı: {hedef_sayi}\nSkorun: {basamak_sayisi-1} basamak.")
            ds_penceresi.destroy()

    def testi_baslat():
        buton_basla.pack_forget() 
        buton_kontrol.pack(pady=10) 
        sayi_uret()

    buton_basla = tk.Button(ds_penceresi, text="Testi Başlat", command=testi_baslat, font=("Arial", 12))
    buton_basla.pack(pady=10)

    buton_kontrol = tk.Button(ds_penceresi, text="Kontrol Et", command=kontrol_et, font=("Arial", 12))

def Stroop_testi():
    stroop_testi = tk.Toplevel(root)
    stroop_testi.title("Stroop Testi")
    stroop_testi.geometry("600x350")
    tuval = tk.Canvas(stroop_testi, width=600, height=200, bg="grey")
    tuval.pack(pady=10)
    
    etiket = tk.Label(stroop_testi, text="Stroop Testi")
    etiket.pack(pady=10)
    stroop_testi.title("Stroop Testi")
    renk_verileri = {"KIRMIZI": "red", "MAVI": "blue", "YEŞİL": "green", "SARI": "yellow", "MOR": "purple", "TURUNCU": "orange", "PEMBE": "pink", "KAHVERENGİ": "brown", "SİYAH": "black", "BEYAZ": "white"}
    
    dogru_sayisi = 0
    kayitli_veriler = []

    def testi_bitir():
        print(f"Toplam Doğru Sayısı: {dogru_sayisi}")
        print("Kayıtlı Veriler:", kayitli_veriler)
        stroop_testi.destroy()

    def stroop_renk_harf_uret(event=None):
        nonlocal dogru_sayisi
        if event:
            dogru_sayisi += 1
            kayitli_veriler.append(f"Tıklama {dogru_sayisi}: Doğru")

        metin_içeriği = random.choice(list(renk_verileri.keys()))
        kalan_renkler = list(renk_verileri.keys())
        kalan_renkler.remove(metin_içeriği)
        renk = random.choice(kalan_renkler)
        renk_kodu = renk_verileri[renk]
        
        tuval.delete("all")
        tuval.create_text(300, 100, text=metin_içeriği, fill=renk_kodu, font=("Arial", 40, "bold"))

    tuval.bind("<Button-1>", stroop_renk_harf_uret)
    
    btn_bitir = tk.Button(stroop_testi, text="Yanlış / Testi Bitir", command=testi_bitir, font=("Arial", 12), bg="red", fg="white")
    btn_bitir.pack(pady=20)

    stroop_renk_harf_uret()
    
aciklama = tk.Label(root, text="Bilişsel test kitine hoş geldiniz. Testlere başlamadan önce kişisel bilgilerinizi giriniz.", font=("Arial", 10), wraplength=250, justify="left")
aciklama.pack(padx=10)

button_basla = tk.Button(root, text="Kişisel bilgiler", command=Giris_ekrani)
button_basla.pack(pady=50, padx=20)

aciklama = tk.Label(root, text="Değerli katılımcı aşağıda teslerin isimleri yer almaktadır. Testlerden birine giriş yapmak için üstüne basın. Başarılar", font=("Arial", 10), wraplength=250, justify="left")
aciklama.pack(padx=20)

button_dikkat_testi = tk.Button(root, text="Dikkat Testi", command=Dikkat_testi)
button_dikkat_testi.pack(pady=20)

button_digit_span_testi = tk.Button(root, text="Digit Span Testi", command=Digit_Span_Baslat)
button_digit_span_testi.pack(pady=20)

button_stroop_testi = tk.Button(root, text="Stroop Testi", command=Stroop_testi)
button_stroop_testi.pack(pady=20)

root.mainloop()
    
    

