# Desafio de Projeto do Potencia Tech IFood da DIO 
## Criando e aperfeiçoando um sistema bancário
Desafio de Projeto sobre Python: Criando e aperfeiçoando um sistema bancário foi divido em dois arquivos cuja as regra se encontram abaixo

### Regras para o desafio: Criando um sistema bancário (arquivo: sistemaBancario1.py)
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.  
Deve ser possível depositar valores positivos para a minhaconta bancária. A v1 do projeto trabalha apenas com 1 usuário,
dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos
devem ser armazenados em uma variável e exibidos na operação de extrato.  
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha
saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de
saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.  
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o
saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.  
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:  
1500.45 = R$ 1500.45
### Regras para o desafio: Criando um sistema bancário otimizado (arquivo: sistemaBancarioOtimizado.py)
Criar um sistema bancário com as operações: sacar, depositar, visualizar extrato, criar usuário e criar conta.  
Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos nesse módulo, cada função
vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.  
* Saque: A função saque deve receber os argumentos por nome (keyword only). Sugestão de argumentos: saldo, valor, extrado. Sugestão de retorno: saldo,extrato.
* Depósito: A função depósito deve recebeer os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo,extrato.
* Extrato:  A função extrato deve receber os argumentos por posição e nome. Argumentos posicionais: saldo. Argumentos nomeados: extrato.
* Criar usuário: O programa deve armazenar os usuarios em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: lougradouro,nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do cpf. Não podemos cadastrar 2 usuários com o mesmo cpf.
* Criar conta Corrente: O programa deve armazenar contas em uma lista, uma conta é composta pos: agencia, numero da conta e usuario. O número da conta é sequêncial, iniciado em 1. O número da agência é fixo "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário. 
