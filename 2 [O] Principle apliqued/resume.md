# OPEN/CLOSED PRINCIPLE  
### Princípio Aberto/Fechado  
*"Classes devem estar abertas para extensão, mas fechadas para modificação."*

Na prática, isso significa que você deve conseguir adicionar novos comportamentos ao sistema **sem precisar mexer no código que já está funcionando**.

No exemplo abaixo, eu criei uma interface chamada `TaxesCalculator` e duas implementações concretas:
- Uma para calcular tarifas no Brasil
- Outra para os EUA

Cada uma tem sua própria lógica de cálculo. Se eu quiser adicionar tarifas da Europa amanhã, só preciso criar uma nova classe, **sem tocar nas existentes**.

---

### Por que isso importa?

Se toda vez que eu quisesse adicionar um novo país eu tivesse que editar um `if` dentro de uma função gigante, o código ficaria cada vez mais frágil e difícil de manter.

Com o OCP:
- O código atual continua intocado
- Eu só **estendo o sistema** com novas classes
- Fica mais fácil testar, manter e evoluir

---

### Esse é o espírito do "O" no SOLID:  
**crescer com segurança, sem quebrar o que já funciona.**
