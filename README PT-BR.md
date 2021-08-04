# ETL de um arquivo Excel (XLS)

ETL - Extract, Transform and Load, é o nome dado ao processo de extração de dados, transformação/formatação dos mesmos e, por fim, alimentar algum sistema de inteligência com esses dados.

### Sobre o projeto

Serviço freelance feito para uma empresa de consultoria de negócios em Foz do Iguaçu/Brasil que consistiu em automatizar a captura de dados financeiros e fluxo de caixa para carregar em uma plataforma de Business Intelligence.

### Etapa1 - Compreender como era feito o processo de analise de dados antes da automatização

Em reunião com os analistas financeiros da empresa de consultoria foi  mostrando que os mesmos de conectavam remotamente no computador  principal da Padaria e Cafeteria, acessavam o ERP (Sistema Comercial) do cliente e tiravam um relatório em XLS/Excel. Sendo assim, a partir disso era feita a análise e tratamento dos dados visualmente e manualmente para uma segunda planilha que posteriormente seria  lida por uma plataforma de business intelligence.

### Etapa2 - Minhas propostas de solução para automatizar a captura e formatação dos dados.

#### Melhor proposta para a automatização

Conversar com a empresa terceirizada que administrava o ERP do cliente para uma tentativa de obter acesso direto ao banco de dados com um usuário que apenas permitiria fazer SELECT QUERY. Posteriormente estudar as relações das tabelas e encontrar os dados, preparar um script query que seria implementado futuramente em Python que se conectaria diretamente ao servidor do banco de dados. Sendo assim, tendo uma automatização da captura de dados desde sua fonte.

#### Contraproposta caso a primeira não fosse possível

Negado a proposta (como foi o caso) pela a outra empresa terceirizada que detinha a administração do banco de dados, foi sugerido por mim que automatizássemos a partir do que já teriam controle, que foi explicado já na **Etapa1** deste mesmo README. Em outras palavras, foi desenvolvido um software em Python que teria como entrada o arquivo financeiro e de fluxo de caixa da Padaria e Cafeteria que era gerado por meio do ERP pelos analistas financeiros.

### Etapa3 - Entendendo os dados do arquivo XLS

Em reunião com os analistas financeiros, perguntei quais dados do relatório gerado pelo ERP eram pertinentes. Na imagem seguinte eu destaquei em **verde** as informações que me foram apontadas como importantes. 

![worksheetPart1](https://github.com/thplira/ETL-from-XLS-Excel-File-BakeryCoffeeShop-/blob/master/github-img/part1.png)

![part1](C:\Users\THPL\Desktop\NK - Sabor e Cia\github-img\part1.png)

![worksheetPart2](https://github.com/thplira/ETL-from-XLS-Excel-File-BakeryCoffeeShop-/blob/master/github-img/part2.png)

![part2](C:\Users\THPL\Desktop\NK - Sabor e Cia\github-img\part2.png)

**OBS:** O relatório original é inteiramente em português, eu traduzi propositalmente pro inglês para fins de tornar público de forma universal esse projeto.

**OBS²:** Os relatórios originais continham de 3000 a 4000 KBs (Em torno de 30mil linhas de dados financeiros mensais), o arquivo disposto neste GitHub é apenas um exemplo com apenas 69 KBs.

![originalDiff](https://github.com/thplira/ETL-from-XLS-Excel-File-BakeryCoffeeShop-/blob/master/github-img/exemploKB.png)

![exemploKB](C:\Users\THPL\Desktop\NK - Sabor e Cia\github-img\exemploKB.png)

### Etapa4 - Testes

Testes

