# Generated by Django 2.0.13 on 2019-03-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("events", "0018_auto_20190220_2205")]

    operations = [
        migrations.AddField(
            model_name="event",
            name="visible",
            field=models.BooleanField(
                default=True,
                help_text="Denne brukes primært for å skjule eksisterende eventer.",
                verbose_name="Vis arrangementet utenfor Dashboard/admin-panelet",
            ),
        )
    ]
