from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from django.utils import timezone

# Create your models here.

User = get_user_model()
#1 Category
#2 Product
#3 CartProduct
#4 Cart
#5 Order

#6 Custumer


#0 Work

def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})

class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:4]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:

    objects = LatestProductsManager()

#1 Category

class CategoryManager(models.Manager):

    CATEGORY_NAME_COUNT_NAME = {
        'Очки': 'glasses__count',
        'Линзы': 'lenses__count'
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_categories_for_left_sidebar(self):
        models = get_models_for_count('glasses', 'lenses')
        qs = list(self.get_queryset().annotate(*models).values())


class Category(models.Model):
    slug = models.SlugField(max_length=100, auto_created=True)
    name = models.CharField(max_length=100, verbose_name='Название категории')

    objects = CategoryManager()
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = ' Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

#2 Product

# 2.1 Glasses


class Glasses_manufacturer(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = '(1.1) Производители'

    def __str__(self):
        return self.title


class Glasses_frame_type(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тип оправы'
        verbose_name_plural = '(1.2) Типы оправ'

    def __str__(self):
        return self.title


class Glasses_frame_material(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Материал оправы'
        verbose_name_plural = '(1.3) Материалы оправ'

    def __str__(self):
        return self.title


class Glasses_size(models.Model):
    size = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Размер очков'
        verbose_name_plural = '(1.4) Размеры очков'

    def __str__(self):
        return self.size


class Glasses_gender(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = '(1.5) Пол'

    def __str__(self):
        return self.title


class Glasses_form(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Форма оправы'
        verbose_name_plural = '(1.6) Форма оправ'

    def __str__(self):
        return self.title


class Glasses_linces_sph(models.Model):
    value = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Сфера (Sph)')

    class Meta:
        verbose_name = 'Сфера (Sph)'
        verbose_name_plural = '(1.7.1) Сфера (Sph)'

    def __str__(self):
        return self.value


class Glasses_linces_cyl(models.Model):
    value = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Цилиндр (Cyl)')

    class Meta:
        verbose_name = 'Цилиндр (Cyl)'
        verbose_name_plural = '(1.7.2) Цилиндр (Cyl)'

    def __str__(self):
        return self.value


class Glasses_linces_ax(models.Model):
    value = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Ось (Ax)')

    class Meta:
        verbose_name = 'Ось (Ax)'
        verbose_name_plural = '(1.7.3) Ось (Ax)'

    def __str__(self):
        return self.value


class Glasses_linces_pd(models.Model):
    value = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='РМЦ (PD)')

    class Meta:
        verbose_name = 'РМЦ (PD)'
        verbose_name_plural = '(1.7.4) РМЦ (PD)'

    def __str__(self):
        return self.value


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image1 = models.ImageField(verbose_name='Изображение 1', blank=True)
    image2 = models.ImageField(verbose_name='Изображение 2', blank=True)
    image3 = models.ImageField(verbose_name='Изображение 3', blank=True)
    image4 = models.ImageField(verbose_name='Изображение 4', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='Цена')

    def __str__(self):
        return self.title

    def get_model_name(self):
        return self.__class__.__name__.lower()
class Glasses(Product):
    glasses_size = models.ForeignKey('Glasses_size', on_delete=models.CASCADE, verbose_name="Размер очков")
    glasses_gender = models.ForeignKey('Glasses_gender', on_delete=models.CASCADE, verbose_name="Пол")
    manufacturer = models.ForeignKey('Glasses_manufacturer', on_delete=models.CASCADE, verbose_name="Производитель")
    frame_material = models.ForeignKey('Glasses_frame_material', on_delete=models.CASCADE, verbose_name="Материал оправы")
    frame_type = models.ForeignKey('Glasses_frame_type', on_delete=models.CASCADE, verbose_name="Тип оправы")
    glasses_form = models.ForeignKey('Glasses_form', on_delete=models.CASCADE, verbose_name="Форма очков")
    Lenses_height = models.IntegerField(verbose_name="Высота линзы")
    Lenses_width = models.IntegerField(verbose_name="Ширина линзы")
    Lenses_length = models.IntegerField(verbose_name="Длина линзы")
    Lenses_bridge = models.IntegerField(verbose_name="Высота линзы")

    class Meta:
        verbose_name = '[1.0] Очки'
        verbose_name_plural = '(1.0) Очки'

    def __str__(self):
        return "{} : {}".format(self.category, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

# 2.2 Lenses


class Lenses_manufacturer(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Производитель линз'
        verbose_name_plural = '(2.1) Производители линз'


    def __str__(self):
        return self.title


class Lenses_type(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тип линз'
        verbose_name_plural = '(2.2) Типы линз'

    def __str__(self):
        return self.title




class Lenses_material(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Материал линз'
        verbose_name_plural = '(2.3) Материалы линз'


    def __str__(self):
        return self.title


class Lenses_Sph(models.Model):
    value = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Сфера (Sph)')

    class Meta:
        verbose_name = 'Сфера линз'
        verbose_name_plural = '(2.4.1) Сферы линз'


    def __str__(self):
        return self.value


class Lenses_rad(models.Model):
    value = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Радиус (Вс)')

    class Meta:
        verbose_name = 'Радиус линз'
        verbose_name_plural = '(2.4.2) Радиусы линз'


    def __str__(self):
        return self.value


class Lenses(Product):
    manufacturer = models.ForeignKey('Lenses_manufacturer', on_delete=models.CASCADE, verbose_name="Производитель")
    material = models.ForeignKey('Lenses_material', on_delete=models.CASCADE, verbose_name="Материал")
    type = models.ForeignKey('Lenses_type', on_delete=models.CASCADE, verbose_name="Тип")
    meaning = models.BooleanField(verbose_name="UVA/UVB защита", default=0)
    moisture = models.IntegerField(verbose_name="Влагосодержание", validators=[MaxValueValidator(100)])
    oxygen = models.IntegerField(verbose_name="Пропускание кислорода")
    diameter = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Диаметр')
    class Meta:
        verbose_name = 'Линзы'
        verbose_name_plural = '(2.0) Линзы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Sun_Glasses(Product):
    glasses_size = models.ForeignKey('Glasses_size', on_delete=models.CASCADE, verbose_name="Размер очков")
    glasses_gender = models.ForeignKey('Glasses_gender', on_delete=models.CASCADE, verbose_name="Пол")
    manufacturer = models.ForeignKey('Glasses_manufacturer', on_delete=models.CASCADE, verbose_name="Производитель")
    frame_material = models.ForeignKey('Glasses_frame_material', on_delete=models.CASCADE, verbose_name="Материал оправы")
    frame_type = models.ForeignKey('Glasses_frame_type', on_delete=models.CASCADE, verbose_name="Тип оправы")
    glasses_form = models.ForeignKey('Glasses_form', on_delete=models.CASCADE, verbose_name="Форма очков")
    Lenses_height = models.IntegerField(verbose_name="Высота линзы")
    Lenses_width = models.IntegerField(verbose_name="Ширина линзы")
    Lenses_length = models.IntegerField(verbose_name="Длина линзы")
    Lenses_bridge = models.IntegerField(verbose_name="Высота линзы")

    class Meta:
        verbose_name = '[3.0] Солнцезащитные очки'
        verbose_name_plural = '(3.0) Солнцезащитные очки'

    def __str__(self):
        return "{} : {}".format(self.category, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')



class Other_manufacturer(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Производитель линз'
        verbose_name_plural = '(2.1) Производители линз'


    def __str__(self):
        return self.title


class Other_type(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тип линз'
        verbose_name_plural = '(2.2) Типы линз'

    def __str__(self):
        return self.title


class Care_Products(Product):
    manufacturer = models.ForeignKey('Other_manufacturer', on_delete=models.CASCADE, verbose_name="Производитель")
    type = models.ForeignKey('Other_type', on_delete=models.CASCADE, verbose_name="Тип")

    class Meta:
        verbose_name = '[4.0] Средство по уходу'
        verbose_name_plural = '(4.0) Средства по уходу'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')



class Accessories(Product):
    manufacturer = models.ForeignKey('Other_manufacturer', on_delete=models.CASCADE, verbose_name="Производитель")
    type = models.ForeignKey('Other_type', on_delete=models.CASCADE, verbose_name="Тип")

    class Meta:
        verbose_name = '[5.0] Аксессуар'
        verbose_name_plural = '(5.0) Аксессуары'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Stocks(Product):
    new_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Новая цена')
    manufacturer = models.ForeignKey('Other_manufacturer', on_delete=models.CASCADE, verbose_name="Производитель")
    type = models.ForeignKey('Other_type', on_delete=models.CASCADE, verbose_name="Тип")

    class Meta:
        verbose_name = '[6.0] Акция'
        verbose_name_plural = '(6.0) Акции'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

#3 CartProduct

class CartProduct(models.Model):
    user = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name="Покупатель")
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, verbose_name="Корзина", related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')
    glist = models.TextField(verbose_name="Параметры", default='')
    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = '(7.2) Продукты в корзине'

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.content_object.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)

#4 Cart

class Cart(models.Model):

    owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = '(7.1) Корзины'

    def __str__(self):
        return str(self.id)



#5 LikeProduct

class LikeProduct(models.Model):
    user = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name="Покупатель")
    like = models.ForeignKey('Like', on_delete=models.CASCADE, verbose_name="Нравится", related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Понравившийся продукт'
        verbose_name_plural = '(7.3) Понравившиеся продукты'

    def __str__(self):
        return "Продукт: {} (Понравившееся)".format(self.product.title)

#6 Like


class Like(models.Model):

    owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(LikeProduct, blank=True, related_name='related_like')
    total_products = models.PositiveIntegerField(default=0)
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Понравившееся'
        verbose_name_plural = '(7.4) Понравившееся'


    def __str__(self):
        return str(self.id)

#5 Order

#6 Customer



class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_order')
    USERNAME_FIELD = "username"
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = '(7.0) Пользователи'


    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)

class Order(models.Model):

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )

    customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='related_orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name='Статус заказ',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name='Тип заказа',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)

    def __str__(self):
        return str(self.id)


    class Meta:
        verbose_name = '    Заказ'
        verbose_name_plural = '         Заказы'