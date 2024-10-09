# Tugas PBP Gasal 2024/2025
### M. Arvin Wijayanto - 2306259780 - Kelas D
### Nama Proyek: GROSA

## Tautan Deployment
Deployment tugas Individu PBP Gasal ini dapat dilihat pada m-arvin-grosa.pbp.cs.ui.ac.id

## Tugas 6 - PBP 2024/2025
### 1. Manfaat Penggunaan JavaScript dalam Pengembangan Aplikasi Web
JavaScript adalah bahasa pemrograman yang sangat penting dalam pengembangan aplikasi web karena beberapa alasan berikut:
- **Interaktivitas Dinamis:** JavaScript memungkinkan pembuatan halaman web yang lebih interaktif, seperti animasi, tombol yang responsif, dan manipulasi elemen HTML tanpa perlu memuat ulang seluruh halaman.
- **Asynchronous Programming:** JavaScript mendukung asynchronous programming melalui penggunaan teknik seperti `AJAX` dan `fetch()`, yang memungkinkan data diambil dari server secara dinamis tanpa memengaruhi pengalaman pengguna.
- **Validasi Frontend:** JavaScript memungkinkan validasi input di sisi klien sebelum dikirimkan ke server, mengurangi jumlah kesalahan yang sampai ke backend.
- **Cross-Platform Compatibility:** JavaScript dapat digunakan di berbagai platform dan peramban, menjadikannya solusi fleksibel dan luas digunakan di berbagai perangkat.

### 2. Fungsi dari `await` pada `fetch()` dan Konsekuensinya Jika Tidak Digunakan
Fungsi `await` pada penggunaan `fetch()` berfungsi untuk menunggu penyelesaian dari `fetch` (operasi asynchronous) sebelum melanjutkan eksekusi baris kode selanjutnya. Ini memungkinkan kita mendapatkan data hasil respons sebelum digunakan lebih lanjut.

Jika kita **tidak menggunakan `await`**, maka program akan melanjutkan eksekusi tanpa menunggu hasil dari `fetch()`, yang menyebabkan:
- **Promise Pending:** Hasil dari `fetch()` akan berupa `Promise` yang belum selesai (pending), sehingga kita tidak bisa langsung menggunakan data hasil pengambilan tersebut.
- **Masalah Akses Data:** Variabel yang seharusnya menampung data hasil `fetch()` mungkin kosong atau belum berisi data, menyebabkan error atau perilaku yang tidak diinginkan di aplikasi.

### 3. Mengapa Menggunakan Decorator `csrf_exempt` pada View untuk AJAX POST
CSRF (Cross-Site Request Forgery) adalah mekanisme keamanan di Django yang memastikan permintaan POST berasal dari sumber yang sah. Namun, ketika menggunakan **AJAX POST**, permintaan ini sering kali tidak membawa token CSRF secara otomatis, sehingga bisa memicu kegagalan validasi CSRF.

Decorator `@csrf_exempt` digunakan untuk **menonaktifkan pengecekan CSRF pada view tertentu**. Ini bermanfaat pada situasi berikut:
- **Permintaan dari sumber terpercaya:** Misalnya, jika AJAX request berasal dari bagian aplikasi yang hanya bisa diakses oleh pengguna yang telah diverifikasi.
- **Mencegah kegagalan permintaan:** Tanpa decorator ini, AJAX POST tanpa token CSRF akan ditolak oleh Django.

Namun, penting untuk menggunakan decorator ini dengan hati-hati karena menonaktifkan mekanisme keamanan penting. Pastikan untuk tetap menjaga keamanan dengan memastikan bahwa hanya request yang aman yang dapat mencapai view ini.

### 4. Alasan Pembersihan Data Input Dilakukan di Backend, Bukan Hanya di Frontend
Pembersihan data input pengguna di backend tetap dilakukan meskipun sudah ada validasi di frontend karena beberapa alasan penting:
- **Keamanan:** Validasi dan pembersihan data di frontend dapat dilewati oleh pengguna yang memanipulasi request menggunakan query-query atau dengan menonaktifkan JavaScript. Backend lebih aman dikarenakan data diproses secara lebih "tersembunyi" jika dibandingkan dengan diproses di frontend.
- **Integritas Data:** Backend bertanggung jawab untuk memastikan bahwa semua data yang masuk ke dalam sistem sesuai dengan aturan yang telah ditentukan. Jika hanya mengandalkan validasi frontend, data yang tidak valid bisa tetap masuk ke database. Misalnya, jika melakukan validasi nama yaitu hanya boleh 10 karakter melalui frontend (misalnya validasi form), timbul potensi serangan hacker yaitu dengan melakukan infiltrasi kepada API berupa mengirimkan nama dengan panjang 1000 karakter. Tentu hal ini bisa ditangani dengan baik jika diurus melalui database dan backend langsung.

## Langkah-langkah Implementasi Checklist
### 1. Ubahlah kode cards data mood agar dapat mendukung AJAX GET.
Untuk mengubah GET menjadi AJAX, saya menambahkan view tambahan pada `views.py` yaitu:
```python
@csrf_exempt
@require_POST
def create_product_form_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    user = request.user
    
    new_product = Product(
        name = name,
        price = price,
        description = description,
        user = user
    )
    
    new_product.save()
    
    return HttpResponse(b"CREATED", status=201)
```

View ini akan dipanggil melalui fetching javascript, oleh karena itu kita memerlukan sedikit modifikasi pada `urls.py`:
```python
  ...
    path('create-ajax', create_product_form_ajax, name='create-ajax'),
...
```

Kemudian, saya menghapus bagian yang me-mapping product. Bagian ini saya gantikan dengan sebuah div ber-id `product-container`. Div ini akan dimanipulasi secara DOM melalui script Javascript, yaitu dengan menambahkan fungsi berikut:
```js
....
async function refreshProducts() {
    console.log("Refreshing products...");
    
    document.getElementById("product-container").innerHTML = "";

    const products = await getProducts();


    let htmlString = "";
    let classNameString = "";

    if (products.length === 0) {
        htmlString = "<p>No products found</p>";
    }
    else {
        classNameString="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10";
        products.forEach(product => {
            const name = DOMPurify.sanitize(product.fields.name);
            const price = DOMPurify.sanitize(product.fields.price);
            const pk = DOMPurify.sanitize(product.pk);

            htmlString += `
                <div
                    class="rounded-3xl w-full md:w-[260px] border-[1px] border-black/10 shadow-xl p-5 text-black hover:shadow-xl cursor-pointer transition-all duration-300 flex flex-col gap-5"
                >
                    <div class="w-full h-[200px] bg-[#F6F6F6] rounded-xl p-8 relative">
                        <img
                            src=""
                            class="w-full object-contain h-full rounded-xl"
                        />
                    </div>
                        <div
                            class="flex flex-col "
                        >
                            <h3 class="m-0 font-medium text-sm">${ name }</h3>
                            <h1 class="m-0 text-xl font-bold">Rp${ price }</h1>
                            <h3 class="m-0 font-medium text-sm text-[#737373]">by AndrewStore</h3>
                            <h3 class="font-medium text-sm">4k Terjual</h3>
                            <div class="flex my-2 gap-2" >
                                <a href='edit/${ pk }' class="w-full">
                                    <button class="bg-[#7C00FE] w-full py-3 px-5 text-white text-sm font-semibold rounded-3xl h-full hover:scale-105 duration-300">Edit</button>
                                </a>
                                <a href='delete/${ pk }' class="w-full">
                                    <button class="bg-[#D91656] w-full py-3 px-5 text-white text-sm font-semibold rounded-3xl h-full hover:scale-105 duration-300">Delete</button>
                                </a>
                            </div>
                        </div>
                </div>
            `;
        });
    }

    document.getElementById("product-container").className = classNameString;
    document.getElementById("product-container").innerHTML = htmlString;
}
```

Fungsi ini akan melakukan fetching ke API product secara async. Jika data berhasil di fetch, maka tampilan dari view product akan diubah sehingga div dengan id `product-container` akan memuat product-product yang telah di fetch sebelumnya.

### 2.  Lakukan pengambilan data mood menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
Untuk menjamin data produk yang diambil melalui AJAX adalah kepunyaan user tertentu, kita perlu menambahkan argument `user=user` pada view `create_product_form_ajax`:
```python
...
    new_product = Product(
        name = name,
        price = price,
        description = description,
        user = user
    )
... 
```

### 3. Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
Pertama, saya membuat button yang jika diklik akan membuka modal. Button ini terletak di `products.html` tepatnya pada bagian:
```html
    <button
        data-modal-target="crudModal"
        data-modal-toggle="crudModal"
        class='bg-[#7C00FE] w-fit py-3 px-10 text-white text-sm font-semibold rounded-3xl h-full hover:scale-105 duration-300'
        onclick="showModal();"
    >
        + Create (AJAX)
    </button>
```

Jika button diklik, maka sebuah modal akan terbuka. HTML dari modal diletakkan pada file `create_product_modal.html` dan akan dipanggil melalui include di `product.html`
Kemudian, kita memerlukan semacam logika untuk membuka dan menutup modal. Berikut kode javascript untuk membuka dan menutup modal:
```js
function showModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modal.classList.remove('hidden');
    setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
    }, 50);
}

function hideModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modalContent.classList.remove('opacity-100', 'scale-100');
    modalContent.classList.add('opacity-0', 'scale-95');

    setTimeout(() => {
        modal.classList.add('hidden');
    }, 150);
}

document.getElementById("cancelButton").addEventListener("click", hideModal);
document.getElementById("closeModalBtn").addEventListener("click", hideModal);

document.getElementById("submitProductEntry").onclick = addProduct;
```

fungsi `hideModal()` digunakan untuk menutup modal, sedangkan fungsi `showModal()` digunakan untuk membuka modal. Selain itu, saya juga menambahkan logika jika cancel, close, dan submit button di klik.

### 4. Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data.
Seperti yang telah dijelaskan sebelumnya, saya mengimplementasikan ini melalui menambahkan view `create_product_form_ajax`

### 5. Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
Untuk mengimplementasi ini, saya membuat view dan menambahkan path pada `urls.py` (seperti yang telah dijelaskan sebelumnya)

### 6. Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
Form dalam modal akan dihubungkan ke path `/create-ajax/` melalui fetch() yang ada di dalam fungsi `addProduct()`

### 7. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan.
Kita tidak perlu melakukan refresh lagi setiap kali data ditambahkan, karena data sudah di GET secara async dan akan langsung di show tanpa melalui refresh