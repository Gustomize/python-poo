# POO com Python

## Classes e Objetos

Uma classe pode ser considerado um agrupamento lógico de atributos e funções.

```python
  class MinhaClasse:
    pass
```

Um objeto é uma instância de uma classe que possui acesso aos tatributos e métodos da classe. O processo da cração deste objeto é chamado de instânciação.

```python
minha_instancia = MinhaClasse()
```

## Atributos e Metódos

Membros de dados são atributos declarados dentro de uma classe. São propriedades que definem melhor uma classe. Existem dois tipos de atributos: atributos de classe e atributos de instância.

Um atributo comum a todas as instâncias de uma classe é chamado atributo de classe. Os atributos de classe são acessados usando o nome da classe como prefixo.

```python
Example:
class Employee:
  number_of_employees = 0
  employee_one = Employee()
  employee_two = Employee()

Employee.number_of_employees += 1
print(employee_one.number_of_employees)
print(employee_two.number_of_employees)
```

Um atributo que é específico para cada instância de uma classe é chamado atributo de instância. Os atributos da instância são acessados dentro de um método de instância usando o objeto `self`.

```python
class Employee:
  def employee_details(self, name):
    self.name = name
```

Cada método de instância aceita possui um parâmetro padrão que está sendo aceito. Por convenção, esse parâmetro é denominado `self`. O parâmetro `self` é usado para se referir aos atributos dessa instância da classe.

```python
class Employee:
  def set_name(self, name):
    self.name = name

employee = Employee()
employee.set_name('John')
Employee.set_name(employee, 'John')
# A declaração acima é inferida como Employee.setName (employee, 'John'), onde o objeto employee é considerado como argumento próprio. No método init, quando dizemos self.name, o Python na verdade leva como employee.name, que está sendo armazenado com o valor John.
```

Uma função dentro de uma classe que executa uma ação específica é chamada de método pertencente a essa classe. Os métodos são de dois tipos: método estático e método de instância.

Um método que pode acessar os atributos de instância de uma classe usando o objeto `self` é chamado de método de instância.

```python
class Employee:
  def employee_details(self, name):
    self.name = name
```

Um método que não tem acesso a nenhum dos atributos de instância de uma classe é chamado de método estático. O método estático usa um decorador `@staticmethod` para indicar que esse método não utilizará o parâmetro próprio padrão.

```python
class Employee:
  number_of_employees = 0

  @StaticMethod
  def update_mumber_of_employees():
    Employee.number_of_employees += 1

employee_one = Employee()
employee_two = Employee()
employee_one.update_mumber_of_employees()
employee_two.update_mumber_of_employees()

print(Employee.update_mumber_of_employees)
```

É possível acessar atributos e métodos de uma classe criando um objeto e acessando os atributos e objetos usando o nome da classe ou o nome do objeto, dependendo do tipo de atributo seguido pelo operador de ponto (.) E o nome do atributo ou nome do método.

```python
class Employee:
  number_of_employees = 0

  def print_mumber_of_employees(self):
    print(Employee.number_of_employees)

employee = Employee()
```

O método `__init__` é o construtor de uma classe que pode ser usada para inicializar membros de dados dessa classe. É o primeiro método que está sendo chamado na criação de um objeto.

```python
class Employee:
  def __init__(self):
    print("Welcome!")

employee = Employee()
```

## Abstração e Encapsulação

Abstração é o processo de etapas seguidas para alcançar
encapsulamento.

Já ocultar os detalhes de implementação do usuário final é chamado
de encapsulamento.

## Herança

Herdar os atributos e métodos de uma classe base em uma classe derivada é chamado de Herança.

```python
class Shape:
  unit_of_measurement = 'centimetre'

class Square(Shape):
  def __init__(self):

square = Square()
```

O mecanismo no qual uma classe derivada herda de duas ou mais classes base é chamado de herança múltipla

```python
class OperatingSystem:
  multi_tasking = True

class Apple:
  website = 'www.apple.com'

class MacOS(OperatingSystem, Apple):
  def __init__(self):
    if self.multi_tasking is True:
      print("MacOS is a multitasking operating system. Visit {} for more details".format(self.website))

mac = MacOS()
```

O mecanismo no qual uma classe derivada herda de uma classe base que foi derivada de outra classe base é chamado de herança multinível.

```python
class Apple:
  website = 'www.apple.com'

class MacBook(Apple):
  device_type = 'notebook computer'

class MacBookPro(MacBook):
  def __init__(self):
    print("This is a {}. Visit {} for more details".format(self.deviceType, self.website))

macbook = MacBookPro()
```

Uma classe base que contém métodos abstratos que devem ser substituídos em sua classe derivada é chamada de classe base abstrata. Eles pertencem ao módulo abc.

```python
from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
  @abstractmethod
  def area(self):
    pass

class Square(Shape):
  def area(self, side)
    return side * side
```

As convenções de nomenclatura usadas para membros privados, protegidos e públicos são:

| Modificador de acesso |  Código  |
| :-------------------: | :------: |
|        Privado        | `__nome` |
|       Protegido       | `_nome`  |
|        Público        |  `nome`  |

## Polimorfismo

A mesma interface existente em diferentes formas é chamada
polimorfismo.

**Exemplo:** Uma adição entre dois números inteiros 2 + 2 retorna 4
considerando que uma adição entre duas cadeias "Olá" + "Mundo"
concatena para "Olá Mundo"

Redefinir como um operador opera seus operandos é chamado
sobrecarga do operador.

```python
class Square:
  def __init__(self, side):
    self.side = side

  def __add__(sideOne, sideTwo):
    return(sideOne.side + sideTwo.side)

squareOne = Square(10)
squareTwo = Square(20)
```

Modificar o comportamento herdado dos métodos de uma classe pai em uma classe filha é chamado de sobreposição.

```python
class Shape:
  def area():
    pass

class Square(Shape):
  def area(self, side):
    return (side * side)
```

`super()` é usado para acessar os métodos da classe pai.

```python
class ClasseA:
  def say_hello():
    print("Hello World")

class ClasseB(ClasseA):
  def __init__(self):
    super().say_hello()
```
