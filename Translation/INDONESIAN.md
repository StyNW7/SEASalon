# SEA Salon Full Stack menggunakan Django + Front-end Dasar

Repositori ini dibuat untuk seleksi di Software Engineering Academy oleh Compfest Academy 2024 🔥🔥

Proyek ini sudah di-deploy di pythonanywhere, jadi Anda dapat melihat website-nya dengan mengklik URL ini:

<a href="https://xstynwx.pythonanywhere.com/">https://xstynwx.pythonanywhere.com/</a>

## Daftar Isi
1. [Gambaran Proyek](https://github.com/StyNW7/SEASalon#Gambaran-Proyek)
2. [Prasyarat](https://github.com/StyNW7/SEASalon#Prasyarat)
3. [Cara Menggunakan Website](https://github.com/StyNW7/SEASalon#Cara-Menggunakan-Website)
4. [Informasi Website](https://github.com/StyNW7/SEASalon#Informasi-Website)
5. [Pemilik](https://github.com/StyNW7/SEASalon#Pemilik)

## Gambaran Proyek

### Nama Website
SEA Salon

### Penjelasan

Memperkenalkan SEA Salon, bintang yang sedang naik daun di industri salon yang dikenal dengan layanan luar biasa dan ulasan yang sangat baik. Dengan klien yang berkembang pesat dan reputasi yang luar biasa, SEA Salon adalah tujuan utama Anda untuk semua kebutuhan kecantikan Anda. Karena itu, SEA Salon telah mendapatkan banyak pelanggan. Untuk menangani pelanggan baru, tim manajemen SEA Salon memutuskan untuk mengembangkan Aplikasi SEA Salon baru.
Aplikasi ini memungkinkan pengguna dengan mudah menelusuri layanan yang tersedia, memilih stylist pilihan mereka, dan memesan janji temu dengan cepat. Dengan antarmuka yang ramah pengguna dan integrasi pemesanan yang mulus, membuat reservasi dengan stylist teratas tidak pernah semudah ini!
Tugas ini akan dibagi menjadi lima level progresif. Semakin tinggi levelnya, semakin banyak poin yang bisa Anda dapatkan. Perhatikan bahwa setiap level dibangun di atas level sebelumnya, jadi Anda harus menyelesaikan level sebelumnya sebelum melanjutkan ke level yang lebih tinggi.

### Teknologi dan Infrastruktur

Fullstack menggunakan Django + Front-end Dasar

Detail:
- Back-end: Django
- Database: Database SQlite
- Front-end: HTML, CSS, JavaScript, dan jQuery

## Prasyarat

1. Python 3.x sudah terinstal di sistem Anda.
2. Pip (manajer paket untuk Python) sudah terinstal di sistem Anda.
3. Git sudah terinstal di sistem Anda (Jika Anda lebih suka menggunakan Git)

## Cara Menggunakan Website

#### *Website ini tidak di-deploy*

Oleh karena itu, berikut adalah panduan untuk menggunakan website ini

### Langkah 1: Unduh Repositori (Lokal / Fork Repositori)

Pengguna dapat mengunduh repositori ini secara lokal atau fork / salin repositori ini ke repositori pribadi mereka
<br> <br>
Sementara itu, jika pengguna ingin meng-clone repositori melalui URL, pengguna dapat menggunakan URL berikut:

<code> https://github.com/StyNW7/SEASalon.git </code>

#### Pengguna juga dapat meng-clone repositori ini (Ingat branch utama adalah: master bukan main)

<code> git clone https://github.com/StyNW7/SEASalon.git </code>

### Langkah 2: Lingkungan Virtual (Opsional)

Jika Anda lebih suka menggunakan Lingkungan Virtual, Anda dapat menggunakan langkah ini untuk membuat Lingkungan Virtual:

<code> python -m venv env </code>

Untuk mengaktifkan dan menggunakan Lingkungan Virtual di Windows

<code> .\env\Scripts\activate </code>

Untuk mengaktifkan dan menggunakan Lingkungan Virtual di MacOS / Linux

<code> source env/bin/activate </code>

Namun, repositori ini juga menawarkan Folder Lingkungan Virtual (jika Anda tidak mengunduh Folder Lingkungan Virtual)

### Langkah 3: Pindah ke Folder utama (seasalon)

Setelah Anda mengunduh atau meng-clone repositori, Anda harus cd ke folder utama yaitu seasalon

Gunakan ini di Terminal:

<code> cd seasalon </code>

### Langkah 4: Instal Dependensi

Langkah ini penting untuk menggunakan website. Pertama, Anda harus menginstal semua dependensi yang digunakan di Website ini

Jalankan kode ini di terminal

<code> pip install -r requirements.txt </code>

### Langkah 5: Pengaturan Database (Opsional)

Saya sudah menyediakan database, namun jika ada perubahan yang ingin Anda lakukan, Anda harus menjalankan kode ini

Cukup jalankan kode ini (jalankan di terminal):

<code> python manage.py makemigrations </code>
<br>
<code> python manage.py migrate </code>

### Langkah 6: Jalankan Server

Jika Anda sudah mengikuti langkah-langkah di atas, server dapat dijalankan menggunakan ini (jalankan di terminal):

<code> python manage.py runserver </code>

Setelah itu, server akan mulai berjalan dan Anda dapat mengklik server localhost seperti ini:

<code> Starting development server at http://127.0.0.1:8000/ </code>

Atau Anda juga dapat membuka browser Anda dan ketik <code> http://127.0.0.1:8000/ </code> secara manual

Namun, jika Anda menggunakan server localhost yang berbeda, Anda dapat pergi ke port server localhost Anda sendiri

<!-- Panduan Lain -->

## Informasi Website

### Daftar dan Masuk

Pengguna dapat mendaftar akun baru, namun pengguna hanya dapat membuat Akun Pelanggan baru

Kemudian pengguna dapat masuk menggunakan akun yang sudah ada

### Membuat Pengguna Admin

Jika Anda ingin membuat pengguna Admin baru, Anda harus mengikuti langkah ini:

Jalankan ini di Terminal:

<code> python manage.py create_custom_user </code>

Cukup masukkan data dan pastikan bahwa username dan field lainnya unik dari data lain di Database

Setelah Berhasil Membuat Pengguna Kustom, Anda dapat masuk di Website menggunakan username dan password yang Anda buat dan pengguna tersebut pasti memiliki peran Admin.

### Contoh Akun

Jika Anda ingin menguji peran pelanggan dan admin, Anda dapat menggunakan Akun ini:

#### Peran Pelanggan

username: customer1
<br>
password: Customer123

#### Peran Admin

username: thomas
<br>
password: Admin123

##### Semoga dokumentasi ini dan panduannya berguna dan membantu dalam menggunakan website!

<!-- Terjemahan -->

## Terjemahan

Saya juga menyediakan Terjemahan Dokumentasi dalam Bahasa Inggris di sini:

<a href="../README.md"> Terjemahan Bahasa Inggris </a>

<!-- Pemilik -->

## Pemilik

Repositori ini dibuat oleh:
- Stanley Nathanael Wijaya

<code> Soli Deo Gloria ✨✨ </code>