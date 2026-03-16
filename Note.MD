Cara Upload ke GitHub
1 Buat folder project
Salin kode

mkdir instagram-scam-report-helper
cd instagram-scam-report-helper
Masukkan semua file tadi.
2 Init Git
Salin kode

git init
git add .
git commit -m "first commit"
3 Hubungkan ke GitHub
Buat repository baru di
GitHub
lalu jalankan:
Salin kode

git remote add origin https://github.com/USERNAME/instagram-scam-report-helper.git
git branch -M main
git push -u origin main
📱 Cara Menjalankan di Termux
Install package:
Salin kode

pkg update
pkg upgrade
pkg install python git
Clone project:
Salin kode

git clone https://github.com/USERNAME/instagram-scam-report-helper
cd instagram-scam-report-helper
Install library:
Salin kode

pip install -r requirements.txt
Jalankan:
Salin kode

python main.py
💻 Cara Menjalankan di Windows
Install Python.
Lalu di CMD:
Salin kode

pip install -r requirements.txt
python main.py
🐧 Linux
Salin kode

sudo apt install python3 python3-pip
pip3 install -r requirements.txt
python3 main.py
