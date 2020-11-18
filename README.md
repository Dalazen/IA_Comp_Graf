# IA_Comp_Graf

Desenvolvimento e tutorial da criação de algoritmos de treinamento e teste de inteligência artificial com cunho estudantil para a matéria de Computação Gráfica sob supervisão do professor Marcos Santos.

Desenvolvedores: Gabriel Pilger e Guilherme Dalazen.

# Tutorial

1. É necessário para um ambiente de treinamento do IA as seguintes aplicações: OpenCV nativo, lib do OpenCV, e a urlib. Para facilitar os comandos do OpenCV definimos o mesmo como variável de ambiente, caso contrário deveriamos inserir o diretório de onde se encontra a pasta do OpenCV. Ex: C:\Users\Sora\Desktop\opencv\build\x64\vc14\bin opencv_annotation...

2. Para iniciar você deve ter duas pastas de amostragem de imagens, uma delas contendo as imagens daquilo que você deseja que sua IA capte, e outra com imagens que não contenham aquilo que voce deseja captar, em resumo uma pasta de analises positivas e outra de analises negativas. Tendo essas pastas, a com nome de Positivas, onde estarão as amostragens de identificação, e a nomeada como Negativas, onde estarão as amostragens sem a identificação positiva, pode-se começar o setup para treinamento.

3. Deve-se atentar que tanto nas amostragens positivas quanto negativas as imagens não podem ter titulos contendo o caracter "espaço", para tanto em cada uma das IAs deste repositório ja temos uma aplicação que pode fazer isto por nós, remover o "espaço" dos nomes, o código RenameFiles.py.

4. Usamos uma outra aplicação chamada listaNegativas.py que usará os nomes e endereços de todas as imagens negativas, montando assim uma lista para que usemos mais tarde no treinamento.

5. Usaremos o código: opencv_annotation --annotations=saida.txt --images=positivas/ para utilizar a função annotation do OpenCV nativo, assim podemos realizar a marcação das amostragens nas imagens positivas tendo como saida uma lista das coordenadas dos pontos de interesse em cada uma das imagens.

6. Entrando agora em fase de pré treino useremos o comando: opencv_createsamples -info saida.txt -bg negativas.txt -vec vec.vec -w 24 -h 24 para gerarmos um arquivo com os parametros de fusao das listas positiva e negativa, esse que será usado como base do treino.

7. Finalmente chegamos a parte mais demorada da criação de uma IA, usaremos o comando: 
opencv_traincascade -data treinamento -vec vec.vev -bg negativas.txt -numPos 450 -numNeg 435 -w 24 -h 24 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -numStages 80 -acceptanceRatioBreakValue 1.0e-5
para iniciar o treinamento da nossa IA, se tudo correu certo ao fim do treino, seja pelo fim dos estagios ou pelo range de aceitação, você terá um arquivo cascade pronto para ser usado em seus códigos de identificação do que você desejar.

Obrigado Por LER!

