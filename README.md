## Para que serve

O Subtitle Edit já faz uma ótima segmentação de legenda **entre linhas**, levando em consideração as opções configuradas em "Ajustes > Ferramentas > Auto BR" e também o [arquivo `pt_NoBreakAfterList.xml` do português brasileiro](https://drive.google.com/uc?id=14ABAE9QbwsSCQ3-q6_cmKFS0VMVX1jLn&export=download) que podemos acrescentar dentro na pasta "Dictionaries" do software.

![Caixa com as opções de quebra de linha no Subtitle Edit](https://github.com/user-attachments/assets/9a91aded-1b44-43c9-a201-f879f9f3a370)

No entanto, essa segmentação não é tão eficaz **entre blocos de legenda**. Essa automação foi feita para ajustar os blocos de acordo com as boas práticas de segmentação de legendas.

1. **Ajuste da Última Palavra do Bloco:** Se a última palavra de um bloco termina com pontuação e tem um espaço antes ou está em uma lista de palavras específicas (NoBreakAfterList), ela é movida para o início do próximo bloco de legenda, caso ele exista.
2. **Ajuste da Primeira Palavra do Bloco:** Se a primeira palavra de um bloco é seguida por pontuação (vírgula, ponto, interrogação) e a pontuação tem um espaço depois, essa palavra é movida para o final do bloco anterior.
	* Exceções:
		* A palavra não é movida se for a única palavra do bloco.
		* No caso de vírgula, a palavra não é movida se:
			* Começa com letra maiúscula.
			* A segunda palavra da linha também termina com vírgula.
  
![Captura de tela com o resultado da automação. Comparação de duas legendas lado a lado.](https://github.com/user-attachments/assets/5756ab7d-86ff-417d-aa1a-b38634287a77)

## Como usar

Para funcionar, você tem que ter o [Python](https://www.python.org/downloads/) instalado no seu computador. Ai depois disso, você só precisa:

1. Clicar com o botão direito no arquivo `ajustar_quebra_bloco_legenda.py`, escolher "Abrir com > Python";
2. Escolher a pasta que contém as legendas VTT que você quer ajustar e clicar em "Selecionar pasta";

Prontinho. Lembrando que essa automação vai modificar TODAS as legendas da pasta selecionada, acrescentando o termo "ajustado" nos arquivos modificados.
