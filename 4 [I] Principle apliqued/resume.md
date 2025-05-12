# Princípio da Segregação de Interface (ISP)

### O que é o ISP?
O **ISP** diz que uma classe não deve ser forçada a implementar métodos que ela não vai usar. Ou seja, se você tem uma classe que não precisa de certos comportamentos, **não force ela a implementá-los**.

---

### Em termos simples:
- **Evite interfaces grandes e genéricas.**
- **Crie interfaces menores e específicas** para que cada classe só implemente os métodos que realmente precisa.
- Isso deixa o código mais **flexível**, **modular** e **fácil de manter**.

---

### Exemplo de problema:

Imagine que temos uma interface `Worker` com dois métodos: `work()` e `eat()`. Agora, se você criar uma classe como `RobotWorker`, ela vai ter que implementar `eat()`, mesmo que um robô não coma, o que não faz sentido.

---

### A solução:

Em vez de uma única interface gigante, crie interfaces pequenas:
- Uma para quem **trabalha** (`Workable`).
- Outra para quem **come** (`Eatable`).

Assim, `RobotWorker` vai implementar apenas `Workable`, e `HumanWorker` vai implementar ambas.

---

### Por que isso é bom?

- **Evita que classes implementem métodos desnecessários.**
- **Fica mais fácil modificar o sistema** no futuro sem quebrar nada.
- **O código fica mais limpo** e fácil de entender.

---

### Resumo:
Sempre que possível, **separe a interface** em partes menores e faça com que as classes implementem **só o que realmente precisam**. Isso vai tornar seu código mais simples e mais fácil de manter.

