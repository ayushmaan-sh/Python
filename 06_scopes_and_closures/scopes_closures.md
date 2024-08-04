
# Scopes and Closures in Python

## 1. **Scope in Python**

### **Definition**
Scope in Python refers to the region of the code where a particular variable is accessible. Python uses the LEGB (Local, Enclosing, Global, Built-in) rule to determine the scope of a variable.

### **Types of Scope**

1. **Local Scope**: 
   - Variables defined within a function.
   - Accessible only inside that function.

   ```python
   def my_function():
       x = 10  # Local scope
       print(x)

   my_function()
   print(x)  # This will raise a NameError
   ```

2. **Enclosing Scope**: 
   - This applies to nested functions.
   - The outer function's variables are accessible in the inner function.

   ```python
   def outer_function():
       y = 20  # Enclosing scope

       def inner_function():
           print(y)  # Accessing the enclosing variable

       inner_function()

   outer_function()
   ```

3. **Global Scope**: 
   - Variables defined at the top-level of a script or module.
   - Accessible throughout the module or script.

   ```python
   z = 30  # Global scope

   def my_function():
       print(z)

   my_function()
   print(z)
   ```

4. **Built-in Scope**: 
   - Contains names preassigned in Python.
   - Accessible from anywhere in your code.

   ```python
   print(len("Hello"))  # len() is a built-in function
   ```

## 2. **Closures in Python**

### **Definition**
A closure in Python is a function object that remembers values in enclosing scopes even if they are not present in memory. Closures are used to create functions with some data pre-loaded.

### **Example of a Closure**

```python
def outer_function(msg):
    message = msg  # Enclosing variable

    def inner_function():
        print(message)  # Accessing the enclosing variable

    return inner_function

closure_function = outer_function("Hello, World!")
closure_function()  # Outputs: Hello, World!
```

### **When to Use Closures**
Closures can be used:
- To avoid using global variables.
- To create function factories (functions that return other functions).
- For data encapsulation.

### **Example: Function Factory**

```python
def multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

multiply_by_3 = multiplier_of(3)
print(multiply_by_3(10))  # Outputs: 30

multiply_by_5 = multiplier_of(5)
print(multiply_by_5(10))  # Outputs: 50
```

### **Benefits of Closures**
- Provide a way to maintain state without using global variables.
- Can lead to more readable and maintainable code, especially in scenarios where small stateful functions are needed.

## **Conclusion**
Understanding scopes and closures is crucial for writing efficient and effective Python code. Scopes help manage variable accessibility, while closures allow functions to retain access to variables even after the outer function has finished execution.
