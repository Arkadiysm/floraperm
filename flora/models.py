from django.db import models


class Goods(models.Model):

    MONO = 'mono'
    BIRTHDAY = 'birthday'
    HAT_BOXES = 'hat_boxes'
    MODERN = 'modern'
    LOVE = 'love'
    MEN = 'men'
    GOODS_TYPES = (
        (LOVE, 'Любовь'),
        (BIRTHDAY, 'День Рождения'),
        (MONO, 'Монобукеты'),
        (MEN, 'Мужчинам'),
        (HAT_BOXES, 'Шляпные коробки'),
        (MODERN, 'Современные букеты'),
    )

    goods_id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=200)
    goods_type = models.CharField(max_length=10, choices=GOODS_TYPES, default=LOVE)
    pub_date = models.DateTimeField('дата опубликования')
    price = models.IntegerField(default=0)
    goods_photo = models.ImageField(upload_to='images')
    photo_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.goods_name