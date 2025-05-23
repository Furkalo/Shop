from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_slug'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(blank=True, related_name='cart', to='shop.Product'),
        ),
    ]
