# Tugas PBP Gasal 2024/2025
### M. Arvin Wijayanto - 2306259780 - Kelas D
### Nama Proyek: GROSA

## Tautan Deployment
Deployment tugas Individu PBP Gasal ini dapat dilihat pada m-arvin-grosa.pbp.cs.ui.ac.id

## Tugas 5 - PBP 2024/2025

## 1. Urutan Prioritas CSS Selector
Ketika terdapat beberapa CSS selector yang diterapkan pada elemen HTML yang sama, CSS menggunakan aturan prioritas (specificity) untuk menentukan selector mana yang dipakai. Urutan prioritasnya adalah sebagai berikut:

1. **Inline Styles** (misalnya `style="color: red;"`) memiliki prioritas tertinggi.
2. **ID Selector** (misalnya `#header`) memiliki prioritas lebih tinggi dari class atau elemen.
3. **Class Selector** (misalnya `.menu`) lebih kuat daripada tag HTML.
4. **Tag Selector** (misalnya `h1`, `p`) memiliki prioritas terendah.
5. **Important Rule** (`!important`) dapat mengesampingkan semua urutan di atas dan memberikan prioritas tertinggi untuk suatu property.

### Contoh:
```html
<div id="header" class="menu">Title</div>
```

Jika terdapat CSS berikut:
```css
#header { color: blue; }
.menu { color: green; }
div { color: red; }
```
Maka elemen tersebut akan memiliki warna **biru** karena **ID selector** memiliki prioritas tertinggi.

### Penjelasan Spesifisitas:
- **Inline styles**: 1000 poin.
- **ID selector**: 100 poin.
- **Class selector**, **attribute selector**, dan **pseudo-class**: 10 poin.
- **Tag selector** dan **pseudo-element**: 1 poin.

---

## 2. Mengapa Responsive Design Penting?
**Responsive design** adalah pendekatan dalam desain web di mana tampilan halaman web dapat menyesuaikan diri dengan berbagai ukuran dan orientasi layar perangkat pengguna. Konsep ini penting karena pengguna mengakses web dari berbagai perangkat seperti komputer desktop, tablet, dan ponsel pintar.

### Keuntungan Responsive Design:
- Pengalaman pengguna yang lebih baik di berbagai perangkat.
- Aksesibilitas yang lebih luas.
- SEO lebih baik karena mesin pencari menghargai situs web yang ramah perangkat seluler.

### Contoh Aplikasi yang Sudah Menerapkan Responsive Design:
- **Google**: Halaman pencarian yang responsif di berbagai perangkat.
- **Airbnb**: Menyediakan pengalaman yang seragam di ponsel, tablet, dan desktop.

### Contoh Aplikasi yang Belum Menerapkan Responsive Design:
- **SIAK NG**: Hanya menyediakan tampilan yang rapih untuk mode desktop

## 3. Perbedaan antara Margin, Border, dan Padding
### 1. **Margin**: Ruang di luar elemen, antara elemen dengan elemen lainnya.
### 2. **Border**: Garis yang membungkus elemen, terletak di antara margin dan padding.
### 3. **Padding**: Ruang di dalam elemen, antara konten dan border.

### Cara Implementasi:
```css
div {
    margin: 20px;    /* Ruang luar elemen */
    border: 2px solid black;    /* Garis di sekitar elemen */
    padding: 10px;   /* Ruang dalam elemen */
}
```

---

## 4. Konsep Flexbox dan Grid Layout

### **Flexbox**
Flexbox (Flexible Box) adalah metode layout yang digunakan untuk mengatur elemen dalam satu dimensi, baik secara horizontal maupun vertikal. Flexbox memudahkan pembuatan layout yang fleksibel dan responsif.

#### Kegunaan Flexbox:
- Menyusun elemen secara dinamis dalam satu baris atau kolom.
- Memungkinkan elemen untuk diperluas atau diperkecil sesuai dengan ruang yang tersedia.

#### Contoh Penggunaan Flexbox:
```css
.container {
    display: flex;
    justify-content: space-between; /* Membagi elemen secara merata */
}
```

### **Grid Layout**
Grid Layout adalah sistem layout dua dimensi yang memungkinkan pengembang untuk membuat desain halaman yang lebih kompleks, dengan baris dan kolom. Grid Layout sangat cocok untuk mengatur elemen dalam struktur grid yang rapi.

#### Kegunaan Grid Layout:
- Membuat layout dua dimensi (baris dan kolom).
- Cocok untuk desain yang lebih kompleks dan berstruktur.

#### Contoh Penggunaan Grid Layout:
```css
.container {
    display: grid;
    grid-template-columns: 1fr 2fr; /* Dua kolom, kolom kedua dua kali lebih besar */
    grid-gap: 10px; /* Jarak antar kolom */
}
```

---