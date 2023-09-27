# SOLID Principles

## S and D are Relevant for Dependency Injection

### The Single-Responsibility Principle
"In other words, every class should have only one responsibility."

### The Dependency Inversion Principle
"Depend upon abstractions, not concretions."

When following this principle, the conventional dependency relationships established from high-level, policy-setting modules to low-level, dependency modules are reversed. This renders high-level modules independent of the low-level module implementation details. The principle states:

1. **High-level modules** should not import anything from low-level modules. Both should depend on abstractions (e.g., interfaces).
2. **Abstractions** should not depend on details. Details (concrete implementations) should depend on abstractions.

By dictating that both high-level and low-level objects must depend on the same abstraction, this design principle inverts the way some people may think about object-oriented programming.

![Dependency Inversion](Dependency_inversion.png)

---

### Loose and tight coupling
if a motherboard manufactured by Company A is only compatible with RAM manufactured by Company B, this means they are dependent on each other. This is called tight coupling in software engineering. Now suppose that Company A has built the motherboard in such a way that its RAM slot will work with any company’s RAM, then this is known as loose coupling.

---

## And Now, Dependency Injection

### Three Questions:
1. How can a class be independent from the creation of the objects it depends on?
2. How can an application, and the objects it uses, support different configurations?
3. How can the behavior of a piece of code be changed without editing it directly?

In Software Engineering Dependency injection is a programming technique in which an object or function receives other objects or functions that it requires, as opposed to creating them internally. Dependency injection aims to separate the concerns of constructing objects and using them, leading to loosely coupled programs. The pattern ensures that an object or function which wants to use a given service should not have to know how to construct those services. Instead, the receiving 'client' (object or function) is provided with its dependencies by external code (an 'injector'), which it is not aware of.

---

### Types of Dependency Injection
- **Constructor Injection**: The above example uses constructor injection, where the dependency (Engine) is passed in via the constructor.
  
- **Method Injection**: Dependencies are provided through a setter method.
  
- **Property Injection**: Dependencies are set directly on properties after object creation.

---

### Advantages of Dependency Injection
- **Testability**: Easier to test classes in isolation.
- **Flexibility**: Easier to swap out dependencies.
- **Separation of Concerns**: Dependencies are managed outside the class.
