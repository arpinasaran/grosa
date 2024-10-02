# Tugas PBP Gasal 2024/2025
### M. Arvin Wijayanto - 2306259780 - Kelas D
### Nama Proyek: GROSA

## Tautan Deployment
Deployment tugas Individu PBP Gasal ini dapat dilihat pada m-arvin-grosa.pbp.cs.ui.ac.id

## Tugas 4 - PBP 2024/2025
### 1. Perbedaan antara `HttpResponseRedirect()` dan `redirect()`
- **`HttpResponseRedirect()`**:
  - Merupakan class bawaan Django yang mengembalikan respons HTTP 302 untuk melakukan redirect ke URL tertentu.
  - Biasanya digunakan ketika kita ingin memberikan lebih banyak kontrol dan modifikasi pada respon sebelum mengembalikannya (misalnya memasukkan cookies ataupun value kedalam localstorage website).
  - Contoh: 
    ```python
      .........
      def login_user(request):
         if (request.user.is_authenticated):
              return redirect('main:show_main')
         
         if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
      
            if form.is_valid():
                  user = form.get_user()
                  login(request, user)
                  response = HttpResponseRedirect(reverse('main:show_main'))
                  response.set_cookie('last_login', datetime.datetime.now())
                  return response
      
         else:
            form = AuthenticationForm(request)
      
         context = {'form': form}
         return render(request, 'auth/login.html', context)
      .........
    ```

- **`redirect()`**:
  - Merupakan shortcut function di Django yang secara implisit menggunakan `HttpResponseRedirect()`.
  - `redirect()` lebih praktis karena bisa menerima berbagai parameter (URL, named URL patterns, model instances, dll.) dan lebih singkat secara syntax.
  - Contoh:
    ```python
      .........
      # Authentication Views
      def register(request):
          form = UserCreationForm()
      
          if (request.method == "POST"):
              form = UserCreationForm(request.POST)
              if form.is_valid():
                  form.save()
                  messages.success(request, "User has been created")
                  return redirect('main:login')
              
          context = {'form': form }
          return render(request, 'auth/register.html', context)
      ......
    ```

**Perbedaan Utama**: `redirect()` adalah cara yang lebih sederhana untuk melakukan redirect dan fleksibel dalam hal parameter, sedangkan `HttpResponseRedirect()` memberi lebih banyak kontrol untuk modifikasi sebelum mengirimkan respons.

---

### 2. Cara Kerja Penghubungan Model `Product` dengan `User`
Dalam project ini, model `Product` biasanya dihubungkan dengan model `User` menggunakan **ForeignKey**. Ini menghubungkan setiap `Product` ke pengguna tertentu.

Contoh model `Product`:

```python
.........
class Product(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
```

- **Cara Kerja**:
  - Setiap kali pengguna membuat entri suasana hati, entri tersebut dikaitkan dengan tepat satu `User` yang login.
  - **ForeignKey** digunakan untuk membuat relasi many-to-one antara `Product` dan `User`. Dengan kata lain, satu User bisa memiliki banyak Product, tapi satu Product hanya bisa dimiliki oleh satu User.
---

### 3. Perbedaan antara Authentication dan Authorization
- **Authentication**: Proses verifikasi identitas User (misalnya melalui username dan password). Ini adalah langkah pertama untuk memastikan agar website kita dapat diakses oleh User yang memilki akun dan telah melewati proses verifikasi.
  - Contoh: Saat pengguna login dengan username dan password.

- **Authorization**: Proses memberikan izin kepada pengguna yang sudah diautentikasi untuk mengakses resource tertentu berdasarkan hak akses yang dimiliki.
  - Contoh: Setelah login, pengguna dapat menjadi Admin maupun User biasa. User biasa akan dibatasi agar tidak dapat mengakses endpoint /admin.

**Proses Login Pengguna**:
- Saat pengguna login, **authentication** dilakukan untuk memastikan identitas mereka benar.
- Setelah berhasil, Django memberikan **authorization** dengan mengecek izin pengguna untuk melihat apakah mereka boleh mengakses resource tertentu.

**Implementasi di Django**:
- Django menggunakan **middleware** untuk mengelola autentikasi dan otorisasi.
- Django menyimpan pengguna yang telah diotentikasi di objek request sebagai `request.user`.
- Untuk **authorization**, Django menggunakan **permissions** (izin) dan **groups** (kelompok), yang dapat diatur pada model atau view tertentu.

---

### 4. Bagaimana Django Mengingat Pengguna yang Telah Login
Django mengingat pengguna yang sudah login menggunakan **sessions** dan **cookies**.
- Setelah pengguna berhasil login, Django membuat session untuk pengguna dan menyimpan session ID dalam cookie di browser pengguna.
- Cookie berisi data dari User yang biasanya dienkripsi,
- Cookie ini kemudian dikirim ke server dengan setiap request berikutnya, sehingga untuk setiap request yang dilindungi, User harus menyertakan cookie.
- Cookie akan didekripsi menjadi data user asli. Data ini server akan menentukan apakah data user yang dikirimkan melalui cookie valid atau tidak.

**Kegunaan Lain dari Cookies**:
- Cookies bisa digunakan untuk melacak preferensi pengguna, menyimpan keranjang belanja, atau menyimpan data sementara lainnya yang berguna di antara permintaan.
  
**Keamanan Cookies**:
- Tidak semua cookies aman. Misalnya, cookies yang tidak dilindungi bisa rentan terhadap serangan **Cross-Site Scripting (XSS)**.
- Untuk membuat cookies lebih aman, Django menawarkan beberapa opsi seperti:
  - **`HttpOnly`**: Mencegah cookie diakses melalui JavaScript.
  - **`Secure`**: Mengirim cookie hanya melalui HTTPS.

---

# Langkah-langkah Implementasi Checklist
### 1. **Mengimplementasikan Fungsi Registrasi, Login, dan Logout**
- **Registrasi**:
  1. Buat form di dalam sebuah view untuk pendaftaran pengguna baru menggunakan `UserCreationForm`.
  ```python
    # Authentication Views
    def register(request):
        form = UserCreationForm()
    
        if (request.method == "POST"):
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "User has been created")
                return redirect('main:login')
            
        context = {'form': form }
        return render(request, 'auth/register.html', context)
  ```
   2. Buat template `auth/register.html` untuk menampilkan form registrasi.

- **Login**:
   1. Buat form login di sebuah view untuk login pengguna yang sudah terdaftar.
      ```python
      def login_user(request):
         if (request.user.is_authenticated):
              return redirect('main:show_main')
         
         if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
      
            if form.is_valid():
                  user = form.get_user()
                  login(request, user)
                  response = HttpResponseRedirect(reverse('main:show_main'))
                  response.set_cookie('last_login', datetime.datetime.now())
                  return response
      
         else:
            form = AuthenticationForm(request)
      
         context = {'form': form}
         return render(request, 'auth/login.html', context)
      ```
   2. Buat template `auth/login.html` untuk menampilkan form login

- **Logout**:
  1. Buat form logout di sebuah view untuk melakukan logout
     ```python
       def logout_user(request):
          logout(request)
          response = HttpResponseRedirect(reverse('main:login'))
          response.delete_cookie('last_login')
          return response
     ```
   2. Tambahkan link logout di template untuk memudahkan user logout melalui logout button:
      ```html
        <a href="{% url 'main:logout' %}">
            {% include "components/button.html" with text="Logout"%}
        </a>
      ```

Terakhir, pastikan semua view dipanggil melalui `urls.py`:
```python
  from django.urls import path
  from main.views import *
  
  app_name = 'main'
  
  urlpatterns = [
      path('', show_main, name='show_main'),
      path('add/', create_product_form, name='create_product_form'),
      path('xml/', show_all_xml, name='show_all_xml'),
      path('xml/<str:id>/', show_id_xml, name='show_id_xml'),
      path('json/', show_all_json, name='show_all_json'),
      path('json/<str:id>/', show_id_json, name='show_id_json'),
      path('register/', register, name='register'),
      path('login/', login_user, name='login'),
      path('logout/', logout_user, name='logout'),
      path('profile/', show_profile, name='profile'),
  ]
```

---

### 2. **Membuat Dua Akun Pengguna dengan Dummy Data**
- **Membuat Dua Akun**
  Untuk membuat akun, kita cukup melakukan dua kali registrasi user dengan akun yang berbeda.
- **Membuat Dummy Data**
  Untuk membuat dummy data, kita perlu login sebagai user yang kita inginkan. Setelah itu, kita bisa menambahkan dummy data baru melalui POST form yang telah dibuat pada Tugas 3 sebelumnya.

### 3. **Menghubungkan Model `Product` dengan `User`**
   - Buat model `Product` dan tambahkan ForeignKey ke `User`, sehingga setiap produk yang dibuat dapat dikaitkan dengan pengguna.

   **Langkah**:
  ```python
  from django.db import models
  import uuid 
  
  class Product(models.Model):
      user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
      id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
      name = models.CharField(max_length=100)
      price = models.IntegerField()
      description = models.TextField(max_length=500)
  ```

   - Jalankan migrasi untuk menerapkan perubahan:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

### 4. **Menampilkan Detail Pengguna yang Sedang Login**
- **Pastikan data last_login di cookie dan username user di send saat login**
  ```python
  ....
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.set_cookie('last_login', datetime.datetime.now())
    return response
  ....
  ```
- **Kirim data last_login ke `show_main
```python
@login_required(login_url='main:login')
def show_main(request):
    model = Product.objects.filter(user=request.user)

    context = {
        ...
        'last_login': request.COOKIES.get('last_login')
    }

    return render(request, 'index.html', context)
```
---

### 5. **Menerapkan Cookies untuk Last Login**
- Set cookies saat user login:
  ```python
  def login_user(request):
      ......
      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', datetime.datetime.now()) # Cookies diset disini
            return response
      ......
  ```
- Di template, tampilkan waktu login terakhir:
   ```html
   {% comment %} Ini ada didalam navbar.html {% endcomment %}
   <p class="text-sm" >
      Last Login: {{last_login}}
   </p>
   ```