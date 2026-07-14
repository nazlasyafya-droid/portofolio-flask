# Web Portofolio Dinamis - Flask

Aplikasi web portofolio dinamis yang dibangun menggunakan Python dan framework Flask, sebagai capstone project mata kuliah Pengantar Pemrograman.

## Fitur

### Halaman Publik
- Home - Menampilkan profil, headline, dan ringkasan singkat
- About - Deskripsi diri lengkap dan daftar skill (dinamis dari database)
- Portofolio - Daftar proyek dengan thumbnail, deskripsi, dan teknologi
- Detail Proyek - Informasi lengkap tiap proyek
- Kontak - Form kontak yang tersimpan ke database

### Dashboard Admin
- Login & Logout dengan session
- Ringkasan statistik (total proyek, pesan belum dibaca)
- CRUD Proyek (tambah, lihat, edit, hapus) dengan upload gambar
- Manajemen Profil dan Skill
- Kotak Masuk Pesan (tandai dibaca, hapus)

## Teknologi yang Digunakan

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2 (template engine)
- HTML5, CSS3

## Instalasi

1. Clone repository ini
```bash
git clone https://github.com/nazlasyafya-droid/portofolio-flask.git
cd portofolio-flask
```

2. Buat virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Jalankan aplikasi
```bash
python app.py
```

5. Buka browser di `http://127.0.0.1:5000`

## Akun Demo Dashboard

- URL: `/dashboard/login`
- Username: `admin`
- Password: `xxx1515`

## Struktur Folder
```
portofolio-flask/
├── app.py
├── models.py
├── extensions.py
├── requirements.txt
├── templates/
├── static/
```
## Penulis

Nazla Syafya - Mahasiswa Teknik Informatika