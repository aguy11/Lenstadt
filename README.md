## Lenstadt

> A Computer Language

Introducing Lenstadt, a still-developing computer language.

### Comments

Comments in Lenstadt are surrounded by two `&`s, which makes it easy to create singe-line and multi-line comments.

Here would be an example:

```
& Single Line Comments&

& Mutli
Line 
Comments
&
```

### Variables

Variables are also pretty easy:

Structure: `<var name> <var operator> <var value>;`

Example:

```
name = "Bill";
```

Lenstadt supports both '' strings and "" strings.

### Output

Also pretty easy:

Structure: `stampLn <output value>;`

Example:

```
lang = "Lenstadt";
stampLn lang;
stampLn "That's my language!";
```

### Input

This *has* to be done inside of a variable. It would look like this:

```
& Strings &
food = captureStr "What is your favorite food? ";
& Integers &
age = captureInt "What is your age?";
& Floats &
weight = captureFloar "How much do you weigh?? ";
& Boolean Values &
covid19 = captureBool "Do you have the Coronavirus?? [True/False]";
```

### If Statements

Also very easy.

Structure: `completeIf <case> { &Things to do& }`

Elif Structure: Just use `completeElseIf` instead of `completeIf`

Else Structure: Use `completeElse` instead of `completeIf`
