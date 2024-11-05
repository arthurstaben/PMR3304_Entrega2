from django.db import migrations

def create_categories(apps, schema_editor):
    Category = apps.get_model('posts', 'Category')
    initial_categories = [
        {'name': 'Elencos Internacionais', 'description': 'Nessa categoria, você será capaz de encontrar os times mais icônicos e memoráveis de fora do Brasil, destacando formações campeãs (ou não) históricas que conquistaram o mundo.'},
        {'name': 'Elencos Nacionais', 'description': 'Essa categoria celebra os times mais marcantes do futebol brasileiro, homenageando esquadrões que encantaram nossa pátria amada.'},
        {'name': 'Seleções', 'description': 'Aqui você poderá encontrar as mais lendárias formações de equipes que defenderam seus países, que protagonizaram momentos inesquecíveis.'},
    ]
    for category_data in initial_categories:
        Category.objects.create(**category_data)

class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0007_remove_category_posts_post_categories'),  # substitua pelo nome da última migração
    ]

    operations = [
        migrations.RunPython(create_categories),
    ]