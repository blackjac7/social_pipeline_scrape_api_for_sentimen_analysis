# Social Media Data and Trend Pipeline for Indonesia Economic Analysis (2019)

Pipeline ini mengumpulkan dan menyiapkan data opini publik dari berbagai platform sosial media terkait ekonomi Indonesia tahun 2019. Data yang terkumpul akan digunakan untuk analisis sentimen dan visualisasi lebih lanjut.

---

## 📁 Struktur Project

```bash
social_pipeline/
├── config.py                   # Konfigurasi environment dan API key
├── utils.py                    # Fungsi utilitas umum
├── pipeline.py                 # Main entry point pipeline
├── requirements.txt            # Daftar dependensi Python
├── fetchers/                   # Modul pengambil data per platform
│   ├── restcountries_fetcher.py
│   ├── twitterapiio_fetcher.py
│   ├── instagram_fetcher.py
│   ├── youtube_fetcher.py
│   └── trends_fetcher.py
```

---

## ✅ Fitur

- **REST Countries API**: Data ekonomi Indonesia
- **TwitterAPI.io**: Mengambil reply tweet tertentu (opini publik)
- **Instagram (Apify)**: Scraping komentar dari beberapa post publik
- **YouTube Data API**: Mengambil komentar dari video tertentu
- **Google Trends**: Data tren pencarian terkait ekonomi Indonesia
- **Unified JSON Output**: Semua data opini digabung dalam satu file siap olah

---

## 📦 Requirements

Install dependencies dengan:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```txt
requests
pandas
pytrends
python-dotenv
google-api-python-client
apify-client
```

---

## 🔐 Konfigurasi Environment

Buat file `.env` di root project Anda:

```env
TWITTER_API=your_twitterapiio_api_key
YOUTUBE_API_KEY=your_youtube_api_key
YOUTUBE_VIDEO_ID=your_youtube_video_id
INSTAGRAM_APIFY_TOKEN=your_apify_api_token
```

---

## 🚀 Menjalankan Pipeline

Jalankan pipeline dengan:

```bash
python pipeline.py
ATAU
py  pipeline.py
```

Pipeline akan:

1. Mengambil data demografi & ekonomi Indonesia dari REST Countries
2. Mengumpulkan opini publik dari:
   - Twitter (reply pada satu tweet)
   - Instagram (komentar dari beberapa post)
   - YouTube (komentar dari satu video)
3. Mengambil tren Google Trends terkait ekonomi Indonesia
4. Menyimpan hasil sebagai:
   - `country.json`
   - `trends.csv`
   - `tweets.json`
   - `instagram.json`
   - `youtube.json`
   - `opinion_of_all_texts.json` (gabungan semua opini)

---

## 📊 Format Output

File opini utama: `opinion_of_all_texts.json`  
Format: **JSON Lines** (setiap baris satu objek JSON):

```
{"id":"...","text":"...","timestamp":"...","source":"twitter"}
{"id":"...","text":"...","timestamp":"...","source":"instagram"}
{"id":"...","text":"...","timestamp":"...","source":"youtube"}
```

File ini siap untuk analisis sentimen di Python (pandas) dan dapat diimpor ke database/data warehouse untuk visualisasi di Grafana atau tools lain.

---

## 🧼 Best Practices

- Setiap fetcher hanya menangani satu platform
- `.env` untuk keamanan credential
- Utilitas umum di `utils.py`
- Output siap olah dan mudah diintegrasikan ke pipeline analitik berikutnya

---

## 📌 Catatan & Batasan

- Twitter hanya mengambil reply dari satu tweet (bisa diganti sesuai kebutuhan)
- Instagram scraping via Apify (tergantung kuota & limitasi Apify)
- YouTube hanya mengambil komentar dari satu video (ID diatur di `.env`)

---

## 🛠️ Next Steps

- Preprocessing & pembersihan teks
- Analisis sentimen (multilingual)
- Integrasi dengan data tren & demografi
- Visualisasi di Grafana atau dashboard lain

---

## 👨‍💻 Author

Developed by Febriansyah — Informatics Engineering Student & AI Enthusiast.

---

## 📄 License

MIT License - bebas digunakan, modifikasi, dan distribusi.
