# LISKOV SUBSTITUTION PRINCIPLE  
### Princípio da Substituição de Liskov  
*"Se S é um subtipo de T, então objetos do tipo T devem poder ser substituídos por objetos do tipo S sem alterar o comportamento esperado."*

---

### O que isso significa na prática?

Se uma classe filha herda de uma classe pai, ela deve **cumprir o que a classe pai promete**. Ou seja, **não deve surpreender o sistema** com comportamentos inesperados.

---

### Aplicação no exemplo abaixo:

```python
class Bird:
    pass


class FlyingBird(Bird):
    def fly(self):
        print("Flying...")


class OtherFlyingBird(FlyingBird):
    pass  # herda o comportamento e não quebra expectativa


class NotFlyingBird(Bird):
    pass  # nunca prometeu voar, então está tudo certo
