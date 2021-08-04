# ETL de um arquivo Excel (XLS)

### Sobre o projeto

Serviço freelance feito para uma empresa de consultoria de negócios em Foz do Iguaçu/Brasil que consistiu em automatizar a captura de dados financeiros e fluxo de caixa para carregar em uma plataforma de Business Intelligence.

### Etapa1 - Compreender como era feito o processo de analise de dados antes da automatização

 Em reunião com os analistas financeiros da empresa de consultoria foi  mostrando que os mesmos de conectavam remotamente no computador  principal da Padaria e Cafeteria, acessavam o ERP (Sistema Comercial) do cliente e tiravam um relatório em XLS/Excel. Sendo assim, a partir disso era feita a análise e tratamento dos dados visualmente e manualmente para uma segunda planilha que posteriormente seria  lida por uma plataforma de business intelligence.

### Etapa2 - Minhas propostas de solução para automatizar a captura e formatação dos dados.
##### Melhor proposta de automatização

Conversar com a empresa terceirizada que administrava o ERP do cliente para uma tentativa de obter acesso direto ao banco de dados com um usuário que apenas permitiria fazer SELECT QUERY. Posteriormente estudar as relações das tabelas e encontrar os dados, preparar um script query que seria implementado futuramente em Python que se conectaria diretamente ao servidor do banco de dados. Sendo assim, tendo uma automatização da captura de dados desde sua fonte.

##### Contraproposta caso a primeira não fosse aceita

Negado a proposta (como foi o caso) pela a outra empresa terceirizada que detinha a administração do banco de dados, foi sugerido por mim que automatizássemos a partir do que já teriam controle, que foi explicado já na Etapa1 deste mesmo README. Em outras palavras, foi desenvolvido um software em Python que teria como entrada o arquivo financeiro e de fluxo de caixa da Padaria e Cafeteria que era gerado por meio do ERP pelos analistas financeiros.

### Etapa3 - Desenvolvimento em Python (ou JavaScript) da Automatização
Desenvolver função útil de comunicação com banco;
Desenvolver função útil de alocação de dados vindos do SGBD;
Desenvolvimento de toda a automatização via programação, focado no Backend;

### Etapa4 - Testes
Testes

### ...

## DONE

