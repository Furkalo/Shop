from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
    ]
