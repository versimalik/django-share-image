# Share Story

## Langkah - langkah
1. Buat project baru dengan nama `share_image`
2. Buat app baru dengan nama `main`
2. Buat routing sesuai dengan table berikut

|Project URL|App|App URL|Views|URL name|Template|
|---|---|---|---|---|---|
|`' '` |main|`' '`|`views.index`|`index`|`main/index.html`|

4. Buat model baru dengan nama `Image` dengan deskripsi sebagai berikut

```python
from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    
```

5. Buat 3 buah file html dan simpan di dalam `templates/main`
	- base.html
	- index.html

6. Siapkan folder static di sini
```treeview
./main/
├── admin.py
├── . . .
├── static/
│   └── main/
│       ├── css/
│       └── js/
├── templates/
│   └── main/
│       └── index.html
├── tests.py
├── urls.py
└── views.py
```