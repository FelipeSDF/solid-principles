# SINGLE RESPONSIBILITY PRINCIPLE 
### Princípio da Responsabilidade Única:
***"Uma classe deve ter um, e apenas um, motivo para mudar."***

Perceba que cada classe tem uma responsabilidade única:
- Uma classe apenas valida a lista
- Outra apenas transformam os elementos para strings
- A classe principal só concatena listas

Isso faz com que a gente não precise modificar o método para verificar **se** é um array ou **se** é uma string  cada classe tem a sua funcionalidade, e caso o usuário não a respeite, **a validação adequada será feita antes da operação acontecer**.

Além disso, o código foi estruturado para manter as responsabilidades ainda mais bem definidas:

- `ArrayValidator` é responsável **apenas pela validação** da entrada (por exemplo, se é uma lista com mais de um item).
- `ArrayToStrTransformator` transforma todos os elementos da lista em strings.
- `ArrayConcatenator` utiliza essas duas classes para **orquestrar o processo de concatenação**, sem assumir responsabilidades que não sejam suas.

Dessa forma, se alguma regra de validação ou transformação mudar futuramente, **modificamos somente a classe relacionada**, mantendo as demais intactas.  
Isso torna o código **mais modular, testável e fácil de manter**
