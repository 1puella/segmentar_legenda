## Para que serve

O Subtitle Edit já faz uma ótima segmentação de legenda **entre linhas**, levando em consideração as opções configuradas em "Ajustes > Ferramentas > Auto BR" e também o [arquivo `pt_NoBreakAfterList.xml` do português brasileiro](https://drive.google.com/uc?id=14ABAE9QbwsSCQ3-q6_cmKFS0VMVX1jLn&export=download) que podemos acrescentar dentro na pasta "Dictionaries" do software.

![Caixa com as opções de quebra de linha no Subtitle Edit](https://github.com/user-attachments/assets/9a91aded-1b44-43c9-a201-f879f9f3a370)

No entanto, essa segmentação não é tão eficaz **entre blocos de legenda**. Essa automação foi feita para ajustar os blocos de acordo com as boas práticas de segmentação de legendas.

## Como usar

Para funcionar, você tem que ter o [Python](https://www.python.org/downloads/) instalado no seu computador. Ai depois disso, você só precisa:

1. Clicar com o botão direito no arquivo `ajustar_quebra_bloco_legenda.py`, escolher "Abrir com > Python";
2. Escolher a pasta que contém as legendas VTT que você quer ajustar e clicar em "Selecionar pasta";

Prontinho. Lembrando que essa automação vai modificar TODAS as legendas da pasta selecionada, acrescentando o termo "ajustado" nos arquivos modificados.
