from django.db import migrations
from django.utils import timezone

def create_initial_posts(apps, schema_editor):
    Post = apps.get_model('posts', 'Post')
    Category = apps.get_model('posts', 'Category')

    category_internacional = Category.objects.get(name='Elencos Internacionais')
    category_nacional = Category.objects.get(name='Elencos Nacionais')
    category_selecoes = Category.objects.get(name='Seleções')
    category_80 = Category.objects.get(name='Anos 80')
    category_90 = Category.objects.get(name='Anos 90')
    category_2000 = Category.objects.get(name='Anos 2000')
    category_2010 = Category.objects.get(name='Anos 2010')

    post1 = Post.objects.create(
        title="Bahia",
        year=1988,
        conteudo="O Esporte Clube Bahia de 1988 é lembrado como um dos times mais icônicos da história do futebol brasileiro. Naquele ano, o Bahia conquistou o Campeonato Brasileiro pela segunda vez, marcando a história do clube e do futebol do Nordeste. Sob o comando do técnico Evaristo de Macedo, o time contava com jogadores históricos como o cérebro Bobô (que virou música de Caetano Veloso) e o centro-avante Charles. Com um futebol vibrante e ofensivo, o Bahia surpreendeu adversários poderosos e, na final, derrotou o Internacional de Porto Alegre.",
        goleiro="Ronaldo",
        defesa="Tarantini, João Marcelo, Claudir, Edinho",
        meio="Paulo Rodrigues, Gil, Bobô, Zé Carlos",
        ataque="Marquinhos, Charles",
        poster_url="https://imortaisdofutebol.com/wp-content/uploads/2013/04/bahia-campeaobrasileiro-1988.jpg",
        data=timezone.now()
    )
    post1.categories.set([category_nacional, category_80]) 

    post2 = Post.objects.create(
        title="Brasil",
        year=2002,
        conteudo="Do outro lado do mundo, na Copa sediada na Coreia do Sul e no Japão, o Brasil protagonizou seu último título mundial: o pentacampeonato. Comandada pelo técnico Luiz Felipe Scolari, o Felipão, a canarinho terminou a competição com 100% de aproveitamento, vencendo todos os 7 jogos. O time contava com uma geração talentosa de jogadores, incluindo Rivaldo, Ronaldinho Gaúcho e Ronaldo, que se destacou como o artilheiro da competição e marcou os dois gols da final na vitória por 2 a 0.",
        goleiro="Marcos",
        defesa="Cafu, Lúcio, Edmílson, Roque Júnior, Roberto Carlos",
        meio="Gilberto Silva, Juninho Paulista/Kléberson, Ronaldinho, Rivaldo",
        ataque="Ronaldo",
        poster_url="https://assets.goal.com/images/v3/bltd409161d0ff73650/dfc913ae31fb4634e1959315a005ffe758b91bf2.jpg?auto=webp&format=pjpg&width=3840&quality=60",
        data=timezone.now()
    )
    post2.categories.set([category_selecoes])  

    post3 = Post.objects.create(
        title="Real Madrid",
        year=2017,
        conteudo="Campeões da UEFA Champions League e da Supercopa da Espanha, talvez o melhor dos 3 anos de dinastia Blanca como campeões da Europa. Com, possivelmente, a melhor versão de Cristiano Ronaldo vestindo a camisa 7 do clube espanhol, marcando dois hat-tricks na fase decisiva da Liga dos Campeões e marcando o gol na final, os merengues atropelaram todos durante a competição. Passando pelo Bayern de Munique e goleando seu rival local Atlético de Madrid, o Real Madrid atropelou a Juventus na final, com uma das finais mais dominantes - não só em placar - da história da competição: 4x1.",
        goleiro="Keylor Navas",
        defesa="Carvajal, Varane, Sergio Ramos, Marcelo",
        meio="Casemiro, Kroos, Modrić",
        ataque="Cristiano Ronaldo, Benzema, Isco",
        poster_url="https://pbs.twimg.com/media/E4IuidRVoA4x9wo.jpg",
        data=timezone.now()
    )
    post3.categories.set([category_internacional, category_2010])  

    post4 = Post.objects.create(
        title="Liverpool",
        year=2005,
        conteudo='Elenco do Liverpool campeão da UEFA Champions League 2004-05: time azarão na final, contra o poderoso AC Milan de Kaká, Seedorf, Shevchenko e Crespo, que abriu 3x0 no primeiro tempo e viu o time inglês tirar forças para empatar em 6 minutos, levando o jogo para os penâltis. Nas penalidades, a vitória de 3-2 dos Reds ficou conhecida como o "Milagre de Instambul".',
        goleiro="Dudek",
        defesa="Finnan, Carragher, Hyypiä, Traoré",
        meio="Xabi Alonso, Gerrard, Luis García, Riise, Kewell",
        ataque="Baroš",
        poster_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPRpeWtLqEpzoT116E0ltmTibu86jvWpH80A&s",
        data=timezone.now()
    )
    post4.categories.set([category_internacional, category_2000])  

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_categories'),  
    ]
    operations = [
        migrations.RunPython(create_initial_posts),
    ]