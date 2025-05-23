from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='shop.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
