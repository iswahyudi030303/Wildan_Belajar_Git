# Task Manager

Proyek ini adalah sistem manajemen tugas sederhana yang memungkinkan pengguna untuk membuat, melihat, dan menyelesaikan tugas. Proyek ini menggunakan implementasi Singleton Design Pattern untuk memastikan hanya ada satu instance TaskManager yang digunakan dalam aplikasi.

## Struktur Direktori

- `tasks/`: Direktori untuk menyimpan modul terkait tugas.
- `tests/`: Direktori untuk menyimpan file pengujian.
- `data/`: Direktori untuk menyimpan file data atau database sederhana.

## Implementasi Design Pattern

Proyek ini menggunakan Singleton Design Pattern dalam modul `tasks_manager.py` untuk memastikan hanya ada satu instance `TaskManager` yang digunakan dalam aplikasi. Ini dilakukan dengan membuat atribut kelas `_instance` yang hanya dibuat saat tidak ada instance sebelumnya.

## Modul Python

- `tasks/tasks_manager.py`: Modul ini berisi implementasi `TaskManager` yang mencakup fungsionalitas dasar untuk menambahkan, melihat, dan menyelesaikan tugas.

## Struktur Data

- `data/tasks.json`: File JSON yang digunakan untuk menyimpan data tugas. Format data adalah array JSON yang berisi objek tugas dengan atribut id, title, description, dan status.

## Pengujian

- `tests/test_tasks_manager.py`: File pengujian untuk modul `tasks_manager.py` menggunakan modul `unittest`. Pengujian dilakukan untuk memastikan bahwa Singleton Design Pattern berfungsi dengan baik dan fungsionalitas `TaskManager` berjalan sesuai yang diharapkan.

## Cara Menjalankan

1. Pastikan Python sudah terinstal di komputer Anda.
2. Clone repositori ini ke direktori lokal Anda.
3. Buka terminal dan navigasikan ke direktori proyek.
4. Jalankan skrip utama dengan perintah `python main.py`.
5. Ikuti instruksi untuk menambahkan, menyelesaikan, dan melihat tugas.

Selamat menggunakan Task Manager!
