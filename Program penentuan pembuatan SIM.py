print(f"{'PROGRAM MENGHITUNG USIA PEMBUATAN SIM':^60}")
print(f"{'-'*60:^60}")
nama = input("Masukkan Namaa Anda :")
umur = int(input("Masukkan Usia Anda :"))

if(umur < 17):
    print(f"Mohon Maaf {nama}\nAnda Belum Cukup Umur Untuk Membuat SIM")

elif(umur >= 17 and umur <= 80):
    print(f"Selamat {nama}\nUsia Anda Telah Mencukupi Untuk Membuat SIM")

else:
    print(f"Mohon Maaf {nama}\nDemi Keselamatan Berkendara Lebih Baik Jika Tidak Mengemudi Ketika Usia Lanjut")
