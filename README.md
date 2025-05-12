<<<<<<< HEAD
=======
# **Projeto de Exemplificação dos Princípios SOLID**

## **Descrição do Projeto**
Este projeto tem como objetivo demonstrar a aplicação dos princípios **SOLID** em Python, com foco na melhoria da manutenção, escalabilidade e flexibilidade do código. Para isso, foram implementados exemplos de cada um dos princípios SOLID, incluindo:

1. **Single Responsibility Principle (SRP)**
2. **Open/Closed Principle (OCP)**
3. **Liskov Substitution Principle (LSP)**
4. **Interface Segregation Principle (ISP)**
5. **Dependency Inversion Principle (DIP)**

Cada princípio é explicado com um exemplo prático de código, buscando ilustrar como esses conceitos podem ser aplicados no dia a dia de desenvolvimento de software.

---

## **Objetivo**
O objetivo deste repositório é:

- **Mostrar a aplicação prática dos princípios SOLID**.
- **Demonstrar boas práticas de programação** em Python.
- **Facilitar o entendimento sobre a importância de cada princípio** na construção de sistemas mais robustos, fáceis de manter e evoluir.

---

## **Estrutura do Projeto**
A estrutura do projeto é simples e consiste em arquivos que contêm a implementação de cada princípio individualmente. Cada implementação é feita com base em um exemplo simples, onde são explicados os conceitos e como eles podem ser aplicados no código.

O código está dividido em classes que seguem os princípios SOLID. O principal exemplo segue a ideia de controle de dispositivos (como **lâmpadas** e **ventiladores**) com uma classe **Switch**.

### **Princípios SOLID Implementados**

1. **SRP (Single Responsibility Principle)**  
   Cada classe tem uma responsabilidade única, o que facilita a manutenção e a escalabilidade do código. Por exemplo, a classe de validação de dados está separada da classe de manipulação de strings.

2. **OCP (Open/Closed Principle)**  
   As classes estão abertas para extensão, mas fechadas para modificação. Para adicionar um novo tipo de dispositivo (como um ventilador), basta criar uma nova classe que implemente a interface `Switchable`, sem precisar alterar o código das classes existentes.

3. **LSP (Liskov Substitution Principle)**  
   As subclasses podem substituir suas classes base sem causar problemas no sistema. Por exemplo, qualquer tipo de dispositivo que implemente a interface `Switchable` pode ser usado pela classe `Switch` sem modificações adicionais.

4. **ISP (Interface Segregation Principle)**  
   A interface `Switchable` define apenas os métodos necessários, garantindo que as classes que a implementam não sejam obrigadas a incluir métodos que não fazem sentido para elas.

5. **DIP (Dependency Inversion Principle)**  
   A classe `Switch` depende de uma abstração (interface `Switchable`), e não de implementações concretas. Isso permite que a classe funcione com qualquer dispositivo, como **lâmpadas** ou **ventiladores**, sem precisar modificar seu código.

---


### **Requisitos**
- Python 3.x

### **Clone o repositório:**

```bash
https://github.com/FelipeSDF/solid-principles.git
```
----
>>>>>>> f3ab1e5 (Readme)
