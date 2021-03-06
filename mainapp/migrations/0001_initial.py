# Generated by Django 3.1.2 on 2020-10-20 19:33

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonTrainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('displayname', models.CharField(blank=True, max_length=80, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('personal_website', models.URLField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('poke_ball', models.IntegerField(default=5)),
                ('great_ball', models.IntegerField(default=0)),
                ('ultra_ball', models.IntegerField(default=0)),
                ('master_ball', models.IntegerField(default=0)),
                ('exp', models.IntegerField(default=0)),
                ('currency', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('front_normal_image', models.CharField(max_length=100)),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('ability_One', models.CharField(max_length=40)),
                ('ability_Two', models.CharField(max_length=40)),
                ('ability_Three', models.CharField(max_length=40)),
                ('type_One', models.CharField(max_length=40)),
                ('type_Two', models.CharField(max_length=40)),
                ('base_experience', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CaughtPokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_caught', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poke_trainer', to=settings.AUTH_USER_MODEL)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poke', to='mainapp.pokemon')),
            ],
        ),
    ]
