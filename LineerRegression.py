import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

class LinearRegression:
    def __init__(self):
        self.w = 0  # Ağırlık
        self.b = 0  # Bias

    def fit(self, X, y):
        n = len(X)
        X_mean = np.mean(X)
        y_mean = np.mean(y)

        # Ağırlık hesaplama
        self.w = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean) ** 2)

        # Bias hesaplama
        self.b = y_mean - self.w * X_mean

    def predict(self, X):
        return self.w * X + self.b

def analyze():
    X = []
    y = []

    # Girdi alanlarını kontrol et ve verileri al
    for i in range(5):
        try:
            reklam_butcesi = float(entry_reklam[i].get())
            satis_miktari = float(entry_satis[i].get())
            X.append([reklam_butcesi])
            y.append([satis_miktari])
        except ValueError:
            messagebox.showerror("Hata", f"{i+1}. veriyi düzgün bir şekilde giriniz.")
            return

    # Yeni bir reklam bütçesi için tahmin yapma
    try:
        yeni_budce = float(entry_tahmin.get())
    except ValueError:
        messagebox.showerror("Hata", "Tahmin etmek istediğiniz veriyi düzgün bir şekilde giriniz.")
        return

    X = np.array(X)
    y = np.array(y)

    # Modeli eğitme
    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(np.array([[yeni_budce]]))
    messagebox.showinfo("Tahmin", f"Tahmin edilen satış miktarı: {predictions[0][0]} TL")

    # Görselleştirme
    plt.figure(figsize=(12, 8))  # Grafik boyutunu ayarlama
    plt.scatter(X, y, color='blue', label='Gerçek Veriler', s=100, edgecolor='black')  # Veri noktaları
    plt.plot(X, model.predict(X), color='red', linewidth=2, label='Doğrusal Regresyon Modeli')  # Regresyon çizgisi
    plt.scatter(np.array([[yeni_budce]]), predictions, color='green', s=100, edgecolor='black', label='Tahminler')  # Tahmin noktası

    # Grafik başlıkları ve etiketleri
    plt.title('Reklam Bütçesi ve Satış Miktarı İlişkisi', fontsize=16)
    plt.xlabel('Reklam Bütçesi (TL)', fontsize=14)
    plt.ylabel('Satış Miktarı (TL)', fontsize=14)
    plt.legend()
    plt.grid(True)  # Izgara çizgileri
    plt.xlim(0, 700)  # X ekseni sınırları
    plt.ylim(0, max(y) + 100)  # Y ekseni sınırları

    # Kullanıcı girdileri ve tahminlerin yer aldığı bölüm (grafik dışında)
    plt.figtext(0.15, 0.15, 'Kullanıcı Girdileri ve Tahminler:', fontsize=14, bbox=dict(facecolor='white', alpha=0.5))
    for i in range(5):
        plt.figtext(0.15, 0.15 - (i + 1) * 0.05, f'Bütçe: {X[i][0]} TL, Satış: {y[i][0]} TL', fontsize=12)
    plt.figtext(0.15, 0.15 - (6) * 0.05, f'Tahmin (Bütçe: {yeni_budce} TL): {predictions[0][0]} TL', fontsize=12, color='green')

    plt.show()

# Arayüz oluşturma
root = tk.Tk()
root.title("Doğrusal Regresyon Analizi")

# Veri girişi için etiketler ve giriş kutuları
entry_reklam = []
entry_satis = []
for i in range(5):
    tk.Label(root, text=f"{i+1}. Reklam bütçesi (TL):").grid(row=i, column=0)
    entry_reklam.append(tk.Entry(root))
    entry_reklam[i].grid(row=i, column=1)

    tk.Label(root, text=f"{i+1}. Satış miktarı (TL):").grid(row=i, column=2)
    entry_satis.append(tk.Entry(root))
    entry_satis[i].grid(row=i, column=3)

# Tahmin girişi
tk.Label(root, text="Tahmin etmek istediğiniz reklam bütçesini girin (TL):").grid(row=5, column=0, columnspan=2)
entry_tahmin = tk.Entry(root)
entry_tahmin.grid(row=5, column=2, columnspan=2)

# Analiz et butonu
tk.Button(root, text="Analiz Et", command=analyze).grid(row=6, column=0, columnspan=4)

root.mainloop()
