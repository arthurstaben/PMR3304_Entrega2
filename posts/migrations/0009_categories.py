from django.db import migrations

def create_additional_categories(apps, schema_editor):
    Category = apps.get_model('posts', 'Category')
    new_categories = [
        {'name': 'Anos 80', 'description': 'Possivelmente, a época de ouro do futebol brasileiro, onde Flamengo e Grêmio conquistaram seus primeiros títulos mundiais e amargamos a derrota na copa de 1982. A Argentina viu o nascimento de Diego Maradona, enquanto aqui, vimos a era de Sócrates no Corinthians e a sua "Democracia Corinthiana".'},
        {'name': 'Anos 90', 'description': 'Época de talentos florescerem: Ronaldo, Zidane, Van Basten e, claro, nossa dupla: Bebeto e Romário, campeã da copa de 1994. Vimos também o surgimento de grandes clubes, como a Juventus de Del Piero e Zidane e o Manchester United de Sir Alex Ferguson, de Giggs e Cantona, que conquistaram a tríplice coroa em 1999. Mas não só de velho continente vive-se o mundo: aqui, vimos o São Paulo ser bicampeão mundial, com a estrela de Raí.'},
        {'name': 'Anos 2000', 'description': 'Nos anos 2000, o futebol se tornou mais global do que nunca, com as grandes ligas europeias se consolidando como o epicentro do esporte. Logo no início da década, vivemos o penta, vendo brilhar a estrela do Fenômeno, Rivaldo e R10: o Ronaldinho Gaúcho. Na Europa, a Liga dos Campeões ganhou um novo status, com o Real Madrid dos Galácticos de Zidane, Figo, Ronaldo, Beckham, deslumbrando os torcedores: sempre perdendo para o Barcelona de Ronaldinho. No Brasil, vimos a hegemonia do tricolor paulista, sendo tricampeão brasileiro seguido e mais uma vez, campeão mundial.'},
        {'name': 'Anos 2010', 'description': 'Enfim, a última era que vimos: era de domínio e revolução no futebol, com Lionel Messi e Cristiano Ronaldo. No ínicio da década, foi a época em que o Barcelona de Messi, Xavi e Iniesta, sob o comando de Guardiola, apresentou ao mundo o "tiki-taka", uma filosofia de jogo que conquistou títulos e encantou até os adversários. Do outro lado, depois de penar nas mãos do rival, chegou a vez do Real Madrid, vendo brilhar a estrela de Cristiano Ronaldo e um supertime ao seu redor: conquistando uma sequência histórica de quatro títulos da Liga dos Campeões em cinco anos. No Brasil, os anos 2010 viram o surgimento de Neymar como a grande esperança, levando o Santos ao título da Libertadores e se tornando uma estrela mundial. Os clubes brasileiros começaram a se modernizar, e a Libertadores ganhou ainda mais relevância, com estádios lotados e um clima de festa que só o futebol sul-americano pode proporcionar. Aqui, ainda vimos uma semi-final contra a Alemanha na copa de 2014, mas, melhor não comentar.'}
    ]

    for category_data in new_categories:
        Category.objects.create(**category_data)

class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0008_add_initial_categories'),  # Substitua pelo nome da última migração
    ]

    operations = [
        migrations.RunPython(create_additional_categories),
    ]