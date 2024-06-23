from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffee',
            old_name='quatity',
            new_name='quantity',
        ),
    ]
