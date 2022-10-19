# Generated by Django 4.1.1 on 2022-09-30 15:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.PositiveIntegerField(default=0)),
                ('final_price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая цена')),
                ('in_order', models.BooleanField(default=False)),
                ('for_anonymous_user', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=True, max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Glasses_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Форма оправы',
                'verbose_name_plural': 'Форма оправ',
            },
        ),
        migrations.CreateModel(
            name='Glasses_frame_material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Материал оправы',
                'verbose_name_plural': 'Материалы оправ',
            },
        ),
        migrations.CreateModel(
            name='Glasses_frame_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Тип оправы',
                'verbose_name_plural': 'Типы оправ',
            },
        ),
        migrations.CreateModel(
            name='Glasses_gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Пол',
                'verbose_name_plural': 'Пол',
            },
        ),
        migrations.CreateModel(
            name='Glasses_manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='Glasses_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name': 'Размер очков',
                'verbose_name_plural': 'Размеры очков',
            },
        ),
        migrations.CreateModel(
            name='Glasses_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Тип оправы',
                'verbose_name_plural': 'Типы оправ',
            },
        ),
        migrations.CreateModel(
            name='Lenses_manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Производитель линз',
                'verbose_name_plural': 'Производители линз',
            },
        ),
        migrations.CreateModel(
            name='Lenses_material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Материал линз',
                'verbose_name_plural': 'Материалы линз',
            },
        ),
        migrations.CreateModel(
            name='Lenses_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Тип линз',
                'verbose_name_plural': 'Типы линз',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.PositiveIntegerField(default=0)),
                ('in_order', models.BooleanField(default=False)),
                ('for_anonymous_user', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='glasses.customer', verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Понравившееся',
                'verbose_name_plural': 'Понравившееся',
            },
        ),
        migrations.CreateModel(
            name='LikeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='glasses.like', verbose_name='Нравится')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.customer', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Понравившийся продукт',
                'verbose_name_plural': 'Понравившиеся продукты',
            },
        ),
        migrations.AddField(
            model_name='like',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_like', to='glasses.likeproduct'),
        ),
        migrations.CreateModel(
            name='Lenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('meaning', models.BooleanField(default=0)),
                ('moisture', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Влагосодержание')),
                ('oxygen', models.IntegerField(verbose_name='Пропускание кислорода')),
                ('diameter', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Линзы',
                'verbose_name_plural': 'Линзы',
            },
        ),
        migrations.CreateModel(
            name='Glasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('Lenses_height', models.IntegerField(verbose_name='Высота линзы')),
                ('Lenses_width', models.IntegerField(verbose_name='Ширина линзы')),
                ('Lenses_length', models.IntegerField(verbose_name='Длина линзы')),
                ('Lenses_bridge', models.IntegerField(verbose_name='Высота линзы')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.category', verbose_name='Категория')),
                ('frame_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.glasses_frame_material', verbose_name='Материал оправы')),
                ('frame_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.glasses_frame_type', verbose_name='Тип оправы')),
                ('glasses_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.glasses_form', verbose_name='Форма очков')),
                ('glasses_gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.glasses_gender', verbose_name='Пол')),
                ('glasses_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.glasses_size', verbose_name='Размер очков')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.glasses_manufacturer', verbose_name='Производитель')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.glasses_type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Очки',
                'verbose_name_plural': 'Очки',
            },
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='glasses.cart', verbose_name='Корзина')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.customer', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Продукт в корзине',
                'verbose_name_plural': 'Продукты в корзине',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='glasses.customer', verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='glasses.cartproduct'),
        ),
    ]