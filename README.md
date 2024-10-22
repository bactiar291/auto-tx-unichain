# auto-tx-unichain_sepolia
# utamakan "git pull" sebelum menjalankan
# khusus pengguna termux bisa scroll sampe bawah jika terjadi gagal saat instalasi dan run 
Selamat datang di repositori **Bactiar291**! 🎉
**via termux**

![Termux Screenshot](https://raw.githubusercontent.com/bactiar291/auto-tx-unichain/main/ss.png)


## Tentang Proyek Ini

Proyek ini dibuat oleh **Bactiar291** untuk tujuan [memudahkan pengguna]. Proyek ini bertujuan untuk memudahkan pengguna yang menggunakan ].

Jika Anda meng-clone atau fork repositori ini, pastikan untuk membaca instruksi di bawah ini untuk memulai.

## Tracking Trx Di explorer Cek 👇 :

    https://sepolia.uniscan.xyz/


## Cara Menggunakan

1. Clone repositori ini ke mesin lokal Anda:
    ```bash
    git clone https://github.com/bactiar291/auto-tx-unichain.git
    ```

2. salin perintah dibawah untuk masuk folder :
     ```bash
    cd auto-tx-unichain
    ```
2. Untuk meng-install dependencies secara manual (jika diperlukan)
   Script ini akan menginstall dependencies yang diperlukan jika ada :
    ```bash
    pip install -r requirements.txt
    ```

4. Jangan Lupa Untuk Mengganti :
    ```bash
    nano .env
    ```
Isi Alamat Address Dan Private Key Seperti Ini 
SENDER_ADDRESS=PASTE_ALAMAT_ADDRESS_KAMU_DISINI
PRIVATE_KEY=PASTE_PRIVATE_KEY_KAMU DISINI
    
6. Untuk menjalankan dependencies :
    ```bash
    python3 unichain_sepolia.py
    ```    

# khusus penggunaan di TERMUX jika kalian gagal dengan cara diatas bisa ikuti cara dibawah ini :

Masuk ke mode proot distro Ubuntu :
 ```bash
pkg install proot
pkg install openssh
pkg install git
curl -L -o proot_5.1.107-52_aarch64.deb https://github.com/SukunDev/termux-proot/raw/main/proot_5.1.107-52_aarch64.deb
dpkg -i proot_5.1.107-52_aarch64.deb
pkg install -y proot-distro
proot-distro install ubuntu
proot-distro login ubuntu
  ```    

masuk ke mode venv :
 
    
  
   ```bash
apt update && apt upgrade
apt install python3-pip
pip install --upgrade pip==24.2
apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate
pip install --upgrade pip setuptools
  ```    
(Jika ada pilihan zona pilih angka 5 yaitu asia dan 35 untuk waktu area jakarta selanjutnya klik y enter dan seterusnya)

kalo udah masuk langsung git clone github diatas  



7. Jalankan proyek dengan mengikuti instruksi yang ada di setiap file atau dokumentasi yang tersedia.

## Kontribusi

Kontribusi sangat dihargai! Jika Anda memiliki ide, saran, atau menemukan bug, jangan ragu untuk membuat _issue_ atau _pull request_.

## Lisensi

Proyek ini menggunakan lisensi [MIT]. Silakan baca file LICENSE untuk informasi lebih lanjut.

---

**Dibuat oleh Bactiar291**  
Terima kasih telah berkunjung ke repositori saya! 🚀
