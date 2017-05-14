import http.server
import socketserver
import time

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()

arr = [{'desc': '\n'
          '\t"A equipe se portou muito bem, mesmo no primeiro tempo. Faltou '
          'criar mais oportunidades, mas a gente tinha a posse de bola. Em '
          'um lance de azar, eles acharam um gol. Se fosse para alguém sair '
          'vencedor hoje, seria nossa equipe, criamos muitas chances. É um '
          'concorrente direto, conseguimos um ponto. Se vencermos em casa, '
          'somamos quatro. Foi um bom resultado"\n',
  'id': '1932417',
  'time': 'Fim de jogo'},
 {'desc': '\n'
          '\t"Fico muito feliz. É um reconhecimento de toda a torcida do '
          'Flamengo. Pude fazer minha estreia. Quero agradecer ao Zé '
          'Ricardo, toda a comissão que me deu a oportunidade. Eagradecer a '
          'todo o grupo também que me recebeu bem. Que seja um ano de '
          'muitas vitórias, que a gente conquiste muitos títulos. Pedi a '
          'camisa do Robinho antes, ele falou que ia me dar. Ele era meu '
          'ídolo desde pequeno. Hoje pude jogar com ele, estou muito '
          'feliz"\n',
  'id': '1932410',
  'time': 'Fim de jogo'},
 {'desc': '\n'
          '\tO árbitro apita pela última vez no Maracanã. Flamengo e '
          'Atlético ficam no empate por 1 a 1.\n',
  'id': '1932397',
  'time': "49'2º tempo"},
 {'desc': '\n'
          '\tFaltam alguns segundos para o jogo acabar. A bola está '
          'dominada pelo Atlético, no meio-campo.\n',
  'id': '1932390',
  'time': "48'2º tempo"},
 {'desc': '\n\tVamos aos 49 minutos neste segundo tempo.\n',
  'id': '1932379',
  'time': "47'2º tempo"},
 {'desc': '\n'
          '\tFlamengo pressiona muito na reta final. A bola é lançada na '
          'área, mas Elias consegue o corte. É lateral pro time da casa.\n',
  'id': '1932370',
  'time': "45'2º tempo"},
 {'desc': '\n'
          '\tAtlético faz a ligação direta com Rafael Moura, isolado no '
          'ataque. Ele está impedido. A bola volta para o Flamengo.\n',
  'id': '1932357',
  'time': "43'2º tempo"},
 {'desc': '\n'
          '\tElias bate o lateral errado, sem querer. Vai ter que cobrar de '
          'novo.\n',
  'id': '1932352',
  'time': "42'2º tempo"},
 {'desc': '\n'
          '\tVinicius Júnior faz tabela com Ederson pela esquerda. Elias '
          'chega por baixo, com muita vitalidade, e recupera para o '
          'Atlético.\n',
  'id': '1932345',
  'time': "41'2º tempo"},
 {'desc': '\n'
          '\tGabriel tenta a ligação direta com o ataque. A bola fica com a '
          'defesa do Flamengo, que organiza a saída.\n',
  'id': '1932339',
  'time': "40'2º tempo"},
 {'desc': '\n'
          '\tVinicius Júnior domina pela esquerda, avança e cruza na '
          'segunda trave. A bola sai com muita força, direto para fora. É '
          'tiro de meta.\n',
  'id': '1932331',
  'time': "39'2º tempo"},
 {'desc': '\n'
          '\tVinicius Júnior é acionado pela esquerda pela primeira vez no '
          'jogo. Ele não consegue o domínio, e a bola sai pela lateral. É '
          'do Atlético.\n',
  'id': '1932326',
  'time': "39'2º tempo"},
 {'desc': '\n'
          '\tJogo fica muito pegado nos minutos finais, com os dois times '
          'querendo muito a vitória. A joia Vinicius Júnior está em campo, '
          'e a torcida responde nas arquibancadas.\n',
  'id': '1932321',
  'time': "38'2º tempo"},
 {'desc': '\n'
          '\tA bola volta a rolar no Maracanã. Atlético cobra lateral no '
          'meio-campo, pela esquerda, e troca passes.\n',
  'id': '1932292',
  'time': "35'2º tempo"},
 {'desc': '\n\tVictor sente o tornozelo e é atendido em campo.\n',
  'id': '1932286',
  'time': "33'2º tempo"},
 {'desc': '\n'
          '\tBerrío recebe mais uma bola dentro da área, pedala, dribla e '
          'chuta para o gol. Ela explode na zaga atleticana e sai pela '
          'linha de fundo. É escanteio.\n',
  'id': '1932271',
  'time': "31'2º tempo"},
 {'desc': '\n'
          '\tBerrío tenta o passe para Pará, na direita do ataque '
          'flamenguista. Ela sai com muita força, direto pela linha de '
          'fundo. É tiro de meta para Victor.\n',
  'id': '1932267',
  'time': "31'2º tempo"},
 {'desc': '\n'
          '\tAtlético chega bem ao ataque mais uma vez, com Elias e '
          'Cazares. O equatoriano tenta finalizar, mas a bola desvia e fica '
          'nas mãos de Muralha.\n',
  'id': '1932263',
  'time': "30'2º tempo"},
 {'desc': '\n'
          '\tGuerrero é acionado no ataque flamenguista, mas está marcado '
          'por dois e não consegue passar. O Galo recupera e sai jogando.\n',
  'id': '1932250',
  'time': "28'2º tempo"},
 {'desc': '\n'
          '\tDefesa do Atlético vacila na saída de bola, e o Flamengo '
          'recupera. Na sequência, quem vacila é o time da casa, que '
          'devolve de graça para o Galo.\n',
  'id': '1932237',
  'time': "27'2º tempo"},
 {'desc': '\n'
          '\tFred sai da área, recebe o passe, protege, ganha de Márcio '
          'Araújo na disputa de corpo e finaliza. A bola sai com muita '
          'força, mas passa longe do gol de Muralha. É tiro de meta.\n',
  'id': '1932231',
  'time': "26'2º tempo"},
 {'desc': '\n'
          '\tElias domina no meio-campo e avança sozinho, tentando a jogada '
          'individual. A defesa dobra a marcação e tira o perigo dali.\n',
  'id': '1932226',
  'time': "25'2º tempo"},
 {'desc': '\n'
          '\tRobinho vê a passagem de Fábio Santos pela esquerda do ataque '
          'do Atlético e tenta o lançamento. A bola sai com muita força, '
          'direto para fora. É do Flamengo.\n',
  'id': '1932223',
  'time': "24'2º tempo"},
 {'desc': '\n'
          '\tEm mais uma chegada do Flamengo, Felipe Santana divide a bola '
          'com Guerrero, por baixo. O árbitro não marca a falta, mas o '
          'atacante flamenguista fica no chão, sentindo dores no '
          'tornozelo.\n',
  'id': '1932218',
  'time': "23'2º tempo"},
 {'desc': '\n'
          '\tO Galo chega mais uma vez ao ataque com Robinho, que entrega a '
          'Fred. Ele não consegue o domínio e acaba cometendo uma falta de '
          'ataque.\n',
  'id': '1932217',
  'time': "22'2º tempo"},
 {'desc': '\n'
          '\tEverton dispara pela esquerda com muita liberdade e tenta o '
          'cruzamento. A defesa do Atlético consegue o corte e puxa o '
          'contra-ataque rápido.\n',
  'id': '1932213',
  'time': "21'2º tempo"},
 {'desc': '\n'
          '\tAtlético faz uma tabela produtiva pela direita, com Cazares e '
          'Robinho. O equatoriano recebe excelente bola, invade a área e '
          'chuta com muita força, direto para o gol. A bola explode na '
          'defesa e sobe muito. Na sequência, o corte é feito.\n',
  'id': '1932205',
  'time': "20'2º tempo"},
 {'desc': '\n'
          '\tAtlético recupera a bola no campo de ataque, com Carlos César. '
          'Ele tenta uma jogada individual, mas a defesa consegue o corte. '
          'É escanteio.\n',
  'id': '1932199',
  'time': "19'2º tempo"},
 {'desc': '\n'
          '\tPará cruza com muita força para a área, e o ataque '
          'flamenguista tenta o domínio para finalizar. A bola sobe muito, '
          'e Felipe Santana sobe mais do que todo mundo para tirar de '
          'cabeça.\n',
  'id': '1932195',
  'time': "18'2º tempo"},
 {'desc': '\n'
          '\tRenê participa pela primeira vez no jogo. Domina pela esquerda '
          'e cruza para Berrío, que tenta a finalização de primeira. A bola '
          'sobe demais e passa por cima do gol de Victor.\n',
  'id': '1932185',
  'time': "17'2º tempo"},
 {'desc': '\n'
          '\tElias faz a bola chegar até Robinho. Próximo à área mas muito '
          'marcado, ele tenta o drible, mas perde. O Flamengo recupera e '
          'tenta sair jogando com velocidade.\n',
  'id': '1932179',
  'time': "16'2º tempo"},
 {'desc': '\n'
          '\tFlamengo coloca a bola no chão e tenta partir para o ataque. '
          'Atlético pressiona a saída de bola.\n',
  'id': '1932171',
  'time': "15'2º tempo"},
 {'desc': '\n'
          '\tFlamengo tenta o lançamento direto com Guerrero, no campo de '
          'ataque. Ele sobe com Felipe Santana e sofre a falta, já cobrada '
          'com rapidez. O Rubro-Negro toca a bola e procura um espaço.\n',
  'id': '1932147',
  'time': "13'2º tempo"},
 {'desc': '\n'
          '\tAtlético troca passes pelo meio, e Rafael Carioca toca para '
          'Fred, já próximo à área. Ele tenta ajeitar de primeira, mas a '
          'bola sai sem direção e fica com a defesa flamenguista.\n',
  'id': '1932143',
  'time': "12'2º tempo"},
 {'desc': '\n'
          '\tBerrío e Arão fazem uma boa tabela pela direita. O colombiano '
          'coloca na frente com muita velocidade. Gabriel, zagueiro do '
          'Atlético, se recupera bem e fica com ela.\n',
  'id': '1932133',
  'time': "11'2º tempo"},
 {'desc': '\n'
          '\tGuerrero está caído no gramado, com a mão na cabeça, sentindo '
          'dores. Será atendido pelos médicos do Flamengo.\n',
  'id': '1932115',
  'time': "10'2º tempo"},
 {'desc': '\n'
          '\tAtlético tenta a jogada pela esquerda, e a bola chega para '
          'Robinho, no meio. Ele não consegue o domínio, e o Flamengo '
          'recupera para sair jogando.\n',
  'id': '1932095',
  'time': "08'2º tempo"},
 {'desc': '\n'
          '\tTrauco dispara com muito espaço pela esquerda. Ele tenta o '
          'cruzamento para Guerrero, colega de seleção do Peru, mas a bola '
          'sai sem força dos pés do lateral. Gabriel fica com ela.\n',
  'id': '1932087',
  'time': "07'2º tempo"},
 {'desc': '\n'
          '\tCarlos César domina passe de Carioca e tenta partir para cima '
          'de Everton. O atacante, voluntarioso na marcação, consegue o '
          'corte. É lateral para o Atlético no campo de ataque.\n',
  'id': '1932080',
  'time': "07'2º tempo"},
 {'desc': '\n'
          '\tAtlético troca passes no meio-campo e procura o melhor lado '
          'para tentar a jogada ofensiva. Flamengo marca bem e reduz os '
          'espaços.\n',
  'id': '1932077',
  'time': "06'2º tempo"},
 {'desc': '\n'
          '\tJogadores do Atlético reclamam muito de lance anterior, quando '
          'Fred teria sofrido uma falta na meia-lua da grande área. O '
          'juizão mandou seguir.\n',
  'id': '1932068',
  'time': "05'2º tempo"},
 {'desc': '\n'
          '\tFred tenta o domínio para finalizar, disputa a bola com o '
          'marcador e cai no chão. O árbitro não marca a falta.\n',
  'id': '1932073',
  'time': "04'2º tempo"},
 {'desc': '\n'
          '\tFred aparece pela direita, como um ponta. Ele domina e cruza '
          'na área. A bola quase chega a Robinho, mas é desviada pela '
          'defesa, que afasta o perigo.\n',
  'id': '1932061',
  'time': "04'2º tempo"},
 {'desc': '\n'
          '\tCazares cruza da direita, em um lance de escanteio. Fred '
          'cabeceia, a bola desvia na defesa do Flamengo e sai pela linha '
          'de fundo. Novo escanteio.\n',
  'id': '1932047',
  'time': "02'2º tempo"},
 {'desc': '\n'
          '\tA bola rola para o segundo tempo no Maracanã! A saída, agora, '
          'é do Atlético.\n',
  'id': '1932030',
  'time': "00'2º tempo"},
 {'desc': '\n\tA bola vai rolar para o segundo tempo\n',
  'id': '1932028',
  'time': 'Intervalo'},
 {'desc': '\n'
          '\t"A gente fez um bom primeiro tempo. Temos que ser mais rápidos '
          'no ataque, demoramos um pouco pra tocar a bola. Tomamos um gol '
          'bobo, isso dificultou. Manter o mesmo ritmo, vamos ver o que o '
          'Roger diz para a gente melhorar no segundo tempo"\n',
  'id': '1931937',
  'time': 'Intervalo'},
 {'desc': '\n'
          '\t"Na verdade, no gol, eu tentei cruzar para o Guerrero, que tem '
          'muita presença de área. Procurei ele, mas acabou dando certo, a '
          'bola enganhou o Victor. Ele achou que o Guerrero ia desviar, ela '
          'acabou entrando. Feliz pelo gol e por ajudar a equipe. Eu '
          'procuro sempre dar o meu melhor. Agora é continuar trabalhando, '
          'o jogo é difícil, o time deles tem muita qualidade pelo meio. '
          'Tentar matar o jogo. Ver o que o professor vai falar com a '
          'gente"\n',
  'id': '1931929',
  'time': 'Intervalo'},
 {'desc': '\n'
          '\tO árbitro apita pela última vez neste primeiro tempo. Até '
          'aqui, vitória flamenguista por 1 a 0 no Maracanã.\n',
  'id': '1931913',
  'time': "47'1º tempo"},
 {'desc': '\n\tVamos aos 47 minutos neste primeiro tempo.\n',
  'id': '1931896',
  'time': "44'1º tempo"},
 {'desc': '\n'
          '\tFlamengo inverte bola com muita precisão para a esquerda, onde '
          'estão Everton e Trauco. Os dois tentam uma tabela, mas Carlos '
          'César chega bem para tirar dali. É escanteio.\n',
  'id': '1931881',
  'time': "42'1º tempo"},
 {'desc': '\n'
          '\tCarlos César recebe de Adilson na direita, olha para a área e '
          'faz o cruzamento. Réver, bem posicionado, domina no peito e sai '
          'jogando.\n',
  'id': '1931876',
  'time': "42'1º tempo"},
 {'desc': '\n'
          '\tAtlético evolui para o ataque mais uma vez e busca uma jogada '
          'de ataque. Fábio Santos tenta o toque para o meio, mas sem '
          'direção. Arão recupera para o Flamengo.\n',
  'id': '1931872',
  'time': "41'1º tempo"},
 {'desc': '\n'
          '\tRobinho briga pela bola próximo à linha de fundo, e ela sai '
          'pela linha de fundo. O atacante fica bravo, pedindo o escanteio, '
          'mas a arbitragem marca tiro de meta para Muralha.\n',
  'id': '1931863',
  'time': "40'1º tempo"},
 {'desc': '\n'
          '\tAtlético também contra-ataca com muito perigo e muitos '
          'jogadores. A bola chega até Elias, no meio, que ajeita para '
          'Robinho. Se dominasse, o camisa 7 sairia na cara do gol de Alex '
          'Muralha. Antes disso, Márcio Araújo toma a frente e rouba a bola '
          'sem falta.\n',
  'id': '1931854',
  'time': "39'1º tempo"},
 {'desc': '\n'
          '\tFlamengo acelera no contra-ataque e tenta inverter o jogo para '
          'Guerrero, que aparece bem na área, pela direita. No meio do '
          'caminho, a bola é desviada e sai pela linha de fundo. É '
          'escanteio.\n',
  'id': '1931843',
  'time': "38'1º tempo"},
 {'desc': '\n'
          '\tOtero cobra nova falta de muito longe, desta vez lançando na '
          'área, pelo alto. A bola vai até a segunda trave, onde está '
          'Felipe Santana. O zagueirão tenta ajeitar de cabeça para o meio '
          'da área, mas ela sai sem direção, direto pela linha de fundo. É '
          'só tiro de meta.\n',
  'id': '1931840',
  'time': "37'1º tempo"},
 {'desc': '\n'
          '\tAtlético tenta nova tabela ofensiva, com Fred fazendo a função '
          'de pivô. Ele tenta ajeitar de calcanhar para o meio, mas a '
          'defesa flamenguista se recupera bem.\n',
  'id': '1931831',
  'time': "36'1º tempo"},
 {'desc': '\n'
          '\tFlamengo responde rapidamente e com muito perigo. A defesa '
          'atleticana vacila, Berrío invade a área pela direita e cruza '
          'rasteiro. Guerrero arruma o corpo para finalizar, mas Rafael '
          'Carioca chega primeiro e corta. Boa chegada!\n',
  'id': '1931822',
  'time': "35'1º tempo"},
 {'desc': '\n'
          '\tAtlético avança para o ataque, e Fred sofre falta. É de longe, '
          'mas Otero já está na bola e costuma arriscar desta distância. '
          'Será que vem o chute direto?\n',
  'id': '1931808',
  'time': "34'1º tempo"},
 {'desc': '\n'
          '\tPará e Fábio Santos disputam a bola no campo de ataque do '
          'Flamengo. Melhor para o atleticano, que consegue o desvio. Os '
          'dois, no ar, batem as respectivas cabeças. Tudo certo com os '
          'dois.\n',
  'id': '1931802',
  'time': "33'1º tempo"},
 {'desc': '\n'
          '\tFábio Santos cruza com muita força na área, buscando Otero. '
          'Muralha sai do gol e consegue dar um soco nela, evitando a '
          'finalização do venezuelano.\n',
  'id': '1931795',
  'time': "32'1º tempo"},
 {'desc': '\n'
          '\tNa cobrança, a bola fica com a defesa do Flamengo, que puxa um '
          'rápido contra-ataque. Desta vez, Gabriel consegue recuperar para '
          'o Galo e devolver para Victor, que começa tudo de novo.\n',
  'id': '1931789',
  'time': "31'1º tempo"},
 {'desc': '\n'
          '\tOtero faz boa jogada pela direita, passa por Trauco e abre '
          'espaço para o cruzamento. O lateral do Flamengo toca por último '
          'na bola, que sai pela linha de fundo. É esacanteio.\n',
  'id': '1931782',
  'time': "30'1º tempo"},
 {'desc': '\n'
          '\tOtero levanta no miolo da área. Réver sobe mais que todo mundo '
          'e corta de cabeça, tirando o perigo dali.\n',
  'id': '1931773',
  'time': "29'1º tempo"},
 {'desc': '\n'
          '\tPor baixo, Trauco comete falta em Carlos César, no campo de '
          'ataque do Atlético. É de média distância. Otero na bola para '
          'levantar na área.\n',
  'id': '1931766',
  'time': "29'1º tempo"},
 {'desc': '\n'
          '\tAtlético ronda a área do Flamengo e busca o gol de empate. O '
          'cruzamento vem na área, mas a defesa consegue cortar. Na '
          'sequência, Elias tenta o arremate de primeira, mas pega muito '
          'mal na bola, que passa longe do gol.\n',
  'id': '1931762',
  'time': "28'1º tempo"},
 {'desc': '\n'
          '\tGabriel, zagueiro do Atlético, avança até o meio-campo e tenta '
          'lançamento direto para Fred, que pede bola na área. Ela sai com '
          'muita força, passa longe do atacante e sai pela linha de fundo. '
          'É tiro de meta.\n',
  'id': '1931756',
  'time': "27'1º tempo"},
 {'desc': '\n'
          '\tRafael Vaz erra passe na defesa do Flamengo, e a bola vai '
          'direto pela linha lateral, de presente para o Atlético.\n',
  'id': '1931751',
  'time': "26'1º tempo"},
 {'desc': '\n'
          '\tMatheus Sávio está no chão, sendo atendido pelos médicos (está '
          'tudo bem com ele). Zé Ricardo e Roger Machado aproveitam para '
          'passar orientações aos jogadores.\n',
  'id': '1931746',
  'time': "25'1º tempo"},
 {'desc': '\n'
          '\tAtlético tenta responder com Otero, pela esquerda. Com as '
          'portas fechadas, o venezuelano é obrigado a recuar para Adilson. '
          'O Galo toca a bola e busca a melhor opção para ameaçar o gol do '
          'Flamengo.\n',
  'id': '1931739',
  'time': "24'1º tempo"},
 {'desc': '\n'
          '\tAtlético chega bem ao ataque, com triangulação pelo meio. '
          'Robinho, esperto, vê Fred invadindo a área e tenta o lançamento '
          'pelo alto. Atenta, a defesa do Flamengo corta de cabeça.\n',
  'id': '1931721',
  'time': "22'1º tempo"},
 {'desc': '\n'
          '\tGabriel acha Fábio Santos, já no campo de ataque. O lateral '
          'erra o domínio de bola e perde para Berrío, que domina. Na '
          'sequência, na tentativa de recuperação, Fábio Santos comete a '
          'falta no atacante flamenguista.\n',
  'id': '1931711',
  'time': "20'1º tempo"},
 {'desc': '\n'
          '\tAtlético é quem troca passes no campo de defesa. Desta vez, '
          'Flamengo não pressiona muito a saída de bola e espera um pouco '
          'mais.\n',
  'id': '1931704',
  'time': "19'1º tempo"},
 {'desc': '\n'
          '\tWillian Arão recupera a bola no meio-campo e toca para Berrío, '
          'que entrega de primeira para Guerrero. O atacante se complica '
          'com a bola e perde para Gabriel, que consegue a roubada de bola '
          'limpa.\n',
  'id': '1931697',
  'time': "18'1º tempo"},
 {'desc': '\n'
          '\tAtlético tenta a ligação direta com o ataque, onde está Fred. '
          'O atacante corre muito, mas a bola fica com a defesa '
          'flamenguista. Márcio Araújo sai jogando.\n',
  'id': '1931684',
  'time': "17'1º tempo"},
 {'desc': '\n'
          '\tFlamengo tenta uma tabela esperta entre Flamengo e Pará, pela '
          'direita. O lateral exagera na força do passe, que sai pela linha '
          'de fundo. É novo tiro de meta para o goleiro atleticano.\n',
  'id': '1931680',
  'time': "16'1º tempo"},
 {'desc': '\n'
          '\tVictor, pressionado por Guerrero, é obrigado a isolar a bola '
          'para o ataque. Sem ninguém do Atlético por lá, ela fica com a '
          'defesa flamenguista, que sai jogando com tranquilidade.\n',
  'id': '1931672',
  'time': "15'1º tempo"},
 {'desc': '\n'
          '\tBerrío domina no meio-campo e tenta um passe para Matheus '
          'Sávio, que invadia a área atleticana. Antes dele, Gabriel se '
          'recupera bem e fica com a bola para o Atlético.\n',
  'id': '1931669',
  'time': "14'1º tempo"},
 {'desc': '\n'
          '\tFlamengo ganha a disputa de cabeça no meio-campo, e a bola '
          'sobra para Guerrero. Mais uma vez, ele está impedido. A bola '
          'volta para o Atlético, que sai jogando.\n',
  'id': '1931655',
  'time': "13'1º tempo"},
 {'desc': '\n'
          '\tEverton cobra fechado, buscando um desvio na segunda trave. A '
          'bola passa por todo mundo e sai direto pela linha de fundo. É '
          'apenas tiro de meta para Victor.\n',
  'id': '1931649',
  'time': "13'1º tempo"},
 {'desc': '\n'
          '\tPará fica com a bola na extrema direita do ataque '
          'flamenguista, perto da bandeirinha de escanteio. Ele faz uma '
          'graça pra cima de Felipe Santana, passa por ele e é derrubado. '
          'Nova falta para o Flamengo, que pressiona.\n',
  'id': '1931643',
  'time': "12'1º tempo"},
 {'desc': '\n'
          '\tMatheus Sávio levanta na área, mas Fred, ajudando a defesa, '
          'corta de cabeça.\n',
  'id': '1931640',
  'time': "11'1º tempo"},
 {'desc': '\n'
          '\tFlamengo recupera a bola no meio-campo com Everton, que '
          'dispara com muita velocidade pela esquerda. Rafael Carioca '
          'acompanha na corrida e comete a falta, marcada pela arbitragem. '
          'É de longe, mas vem bola na área.\n',
  'id': '1931638',
  'time': "10'1º tempo"},
 {'desc': '\n'
          '\tAtlético também tenta o lançamento direto para o ataque, mas a '
          'defesa do Flamengo, sem brincar, tira o perigo e isola pra muito '
          'longe.\n',
  'id': '1931624',
  'time': "09'1º tempo"},
 {'desc': '\n'
          '\tGuerrero é lançado mais uma vez no ataque Flamenguista, por '
          'trás da defesa. Ele domina bonito com o peito, mas novamente '
          'está em posição irregular. Impedimento marcado.\n',
  'id': '1931617',
  'time': "08'1º tempo"},
 {'desc': '\n'
          '\tAtlético-MG recupera a bola no campo de ataque, com Otero e '
          'Robinho. O camisa 7 tenta a finalização que levaria muito '
          'perigo, mas a defesa do Flamengo, por baixo, consegue travar.\n',
  'id': '1931613',
  'time': "07'1º tempo"},
 {'desc': '\n'
          '\tGuerrero é lançado na área e está completamente livre para '
          'finalizar. Mas não vale nada. O peruano está em posição de '
          'impedimento.\n',
  'id': '1931605',
  'time': "06'1º tempo"},
 {'desc': '\n'
          '\tAtlético tenta responder com contra-ataque, e Robinho é '
          'acionado na direita. Márcio Araújo chega primeiro e domina. Na '
          'sequência, o flamenguista é puxado pelo atleticano. Falta para o '
          'Flamengo no meio.\n',
  'id': '1931598',
  'time': "05'1º tempo"},
 {'desc': '\n'
          '\tEverton recebe excelente bola no ataque do Flamengo, pela '
          'esquerda, em profundidade e com muito espaço para avançar. Ele '
          'leva até a linha de fundo e cruza rasteiro, buscando o Guerrero. '
          'Carlos César dá um carrinho na hora certa e corta para '
          'escanteio. Boa chegada do Flamengo!\n',
  'id': '1931593',
  'time': "04'1º tempo"},
 {'desc': '\n'
          '\tTrauco evolui pela esquerda, passa para o campo de ataque e '
          'tenta achar Everton, já próximo à área. Felipe Santana, bem '
          'posicionado, recupera a bola para o Atlético.\n',
  'id': '1931585',
  'time': "03'1º tempo"},
 {'desc': '\n'
          '\tOtero cobra escanteio muito fechado, e a defesa do Flamengo '
          'consegue cortar. A bola volta nos pés dele para um novo '
          'cruzamento, mas o venezuelano erra o domínio e deixa a bola sair '
          'pela lateral.\n',
  'id': '1931582',
  'time': "03'1º tempo"},
 {'desc': '\n'
          '\tAtlético-MG chega perto da área do Flamengo pela primeira vez. '
          'Robinho faz jogada individual pela esquerda e tenta o cruzamento '
          'na área. Willian Arão chega bem para fazer o corte. É '
          'escanteio.\n',
  'id': '1931579',
  'time': "02'1º tempo"},
 {'desc': '\n'
          '\tAtlético-MG domina a bola no meio-campo e tenta avançar pela '
          'esquerda, com Fábio Santos. O lateral é derrubado com falta, '
          'marcada pelo juiz. A bola segue com o Galo.\n',
  'id': '1931574',
  'time': "01'1º tempo"},
 {'desc': '\n'
          '\tFlamengo tenta uma primeira chegada pela esquerda. O '
          'cruzamento vem na área, buscando Guerrero, mas a defesa '
          'atleticana consegue se recuperar. Adilson consegue tirar o '
          'perigo dali.\n',
  'id': '1931566',
  'time': "00'1º tempo"},
 {'desc': '\n'
          '\tComeça o jogo no Maracanã! A saída é do Flamengo neste '
          'primeiro tempo.\n',
  'id': '1931562',
  'time': "00'1º tempo"},
 {'desc': '\n'
          '\tSobre a estratégia para o jogo: "Depende do momento do jogo, '
          'depende como a partida vai estar. A gente precisa se defender '
          'bem, mas não abrir mão de jogar. É um clássico, estreia no '
          'Brasileiro. É muito importante começar bem e levar ponto daqui"\n',
  'id': '1931558',
  'time': 'Pré-Jogo'},
 {'desc': '\n'
          '\t"Campeonato de 38 rodadas. A gente sabe que o Atlético-MG, na '
          'teoria, vai brigar pelo título. É importante começar com o pé '
          'direito. Consequência natural a gente trazer o Matheus Sávio, dá '
          'um dinamismo, auxilia o Guerrero. O Vinícius Jr tem muito '
          'talento, as coisas vão acontecer com naturalidade pra ele"\n',
  'id': '1931555',
  'time': 'Pré-Jogo'},
 {'desc': '\n'
          '\tOs dois times se cumprimentam, trocam faixas. Todo aquele '
          'protocolo antes da bola rolar.\n',
  'id': '1931544',
  'time': 'Pré-Jogo'},
 {'desc': '\n'
          '\tHino Nacional Brasileiro é executado no Maracanã. A bola vai '
          'rolar em instantes!\n',
  'id': '1931530',
  'time': 'Pré-Jogo'},
 {'desc': '\n', 'id': '1931385', 'time': 'Pré-Jogo'},
 {'desc': '\n'
          '\tJailson Macedo Freitas (foto) é o árbitro do jogo. Ele será '
          'auxiliado por Alessandro Rocha de Matos e Elicarlos Franco de '
          'Oliveira. O trio é da Bahia.\n',
  'id': '1931380',
  'time': 'Pré-Jogo'},
 {'desc': '\n'
          '\tMais de 36 mil ingressos foram vendidos antecipadamente para o '
          'jogão de logo mais. O Macaranã vai receber excelente público. '
          'Esperamos, claro, um bom jogo!\n',
  'id': '1931359',
  'time': 'Pré-Jogo'},
 {'desc': '\n'
          '\tFlamengo e Atlético-MG entram no Brasileirão como candidatos '
          'ao título. Os dois foram campeões estaduais, têm bons elencos e '
          'uma torcida empolgada. Além disso, têm centroavantes em '
          'excelente fase. Pelo lado carioca, Guerrero está voando, fazendo '
          'gol de tudo que é jeito. Pelo lado mineiro, Fred também está '
          'demais, marcando "até sem querer". E hoje, quem leva a melhor?\n',
  'id': '1931355',
  'time': 'Pré-Jogo'},
 {'desc': '\n', 'id': '1931346', 'time': 'Pré-Jogo'},
 {'desc': '\n', 'id': '1931344', 'time': 'Pré-Jogo'},
 {'desc': '\n'
          '\tBoa tarde, amigo internauta! Aposto que todos estão morrendo '
          'de saudade do Brasileirão, né? Pois é, ele voltou! Logo mais, às '
          '16h (de Brasília), a bola rola no Maracanã para Flamengo e '
          'Atlético-MG, primeiro jogo da primeira rodada do Brasileirão '
          '2017. A partir de agora, você acompanha tudo, em tempo real. '
          'Seja bem-vindo!\n',
  'id': '1931340',
  'time': 'Pré-Jogo'}]

for upd in arr:
    with open("mock.html", "a") as myfile:
        myfile.write("""<li style="display: list-item; id=""")
        myfile.write(arr['id'])
        myfile.write(""" class="lance-normal tr-fade-in tr-lance periodo_5" title="Lance normal"><div class="tempo-lance"><span class="minuto-lance">""")
        myfile.write(arr['time'])
        myfile.write("""</span><div class="lance"><i class="fa fa-circle indicador-lance borda-branca"></i><div class="conteudo-lance"><span class="descricao-lance">""")
        myfile.write(arr['desc'])
        myfile.write("""</span>""")
    time.sleep(60)