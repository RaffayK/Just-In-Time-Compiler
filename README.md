# Just-In-Time-Compiler

1. **Problem Specification**: Building a programming language for learning compiler workings.
   
2. **Specification of Rules & Attributes**: Defining data types, keywords, syntax rules, comments, operators, and constructs like loops, conditionals, functions, etc.

3. **Specification of Programming Language Constructs**: Covers sequences, selections, and iterations, fundamental for program design.

4. **Possible Techniques to Implement Lexical Analyzer**: Methods like Finite State Automata, Regular Expressions, Table-Driven, or Hybrid approach.

5. **Available Techniques/Algorithms to Implement Parser**: Includes Recursive Descent, LL(k), LR Parsing, Earley Parsing, etc.

6. **Selected Parsing Technique and Application with Examples**: Opting for LL(1) parser for simplicity, efficiency, and predictive parsing capabilities, with examples of its applications.

7. **Description of Errors for Each Phase**: Covers errors in Lexical Analysis, Syntax Analysis, Semantic Analysis, Code Generation, and Linking.

8. **Description of All Semantic Rules**:
   
Semantic rules describe the meaning of the symbols and structures in a language and are used to check 
the semantic correctness of a program. These rules are used during the semantic analysis phase of the 
compiler to ensure that the program is semantically valid and to generate appropriate intermediate 
representations.
Some examples of semantic rules include:
 Type checking: This rule checks that the types of operands match the expected types of the 
operation being performed. For example, an operation that expects two integers as operands will 
raise an error if one of the operands is a floating-point number.
 Variable declaration: This rule checks that a variable has been declared before it is used and that 
it has a unique identifier.
 Scope resolution: This rule checks that variables and functions are used in the correct scope and 
that their visibility is respected.
 Function call: This rule checks that the number of arguments passed to a function matches the 
number of parameters expected by the function and that the types of the arguments match the 
types of the parameters.
 Array access: This rule checks that the index used to access an array is within the bounds of the 
array.
 Constant folding: This rule evaluates constant expressions at compile time and replaces them 
with their values.
 Constant propagation: This rule propagates the values of constants throughout the program and 
eliminates dead code.
 Control flow analysis: This rule checks that the program has a well-defined control flow and that 
all branches of the program are reachable and terminates.
 Overloading resolution: This rule checks that the correct version of an overloaded function is 
called based on the types of the arguments passed.
 Inheritance: This rule checks that a subclass inherits the properties and methods of its superclass 
and that it respects the visibility and accessibility of the inherited members.
 Memory management: This rule checks that the program does not leak memory and that all 
dynamically allocated memory is freed when it is no longer needed.
 Threading: This rule checks that the program does not have race conditions or deadlocks when 
using threads.
All these rules are used by the compiler to ensure that the program is semantically valid and that it will 
behave as expected. However, the set of semantic rules varies from language to language and from 
compiler to compiler and some languages may have additional semantic rules that are specific to their 
design and purpose.
It's worth noting that the semantic rules are not always enforced by the compiler but by the language's 
runtime or interpreter. For instance, some languages like python don't have strict typing rules and the 
type checking is done at runtime.
Additionally, semantic rules are not always deterministic and sometimes the compiler or the interpreter 
may have multiple options for resolving a semantic issue. In these cases, the compiler or the interpreter 
may use heuristics or conventions to make a choice, sometimes even with a configuration options to 
adjust the behavior to the user's needs.
Overall, semantic rules play a crucial role in ensuring that the program is semantically correct and that it 
will behave as intended. The set of semantic rules varies depending on the language and the compiler, 
and they are used to check the semantic correctness of the program and to generate appropriate 
intermediate representation


