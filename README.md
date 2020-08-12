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

Example:
```
name = captureStr "What is your name?";
completeIf name == "Magnus Carlsen" {
  stampLn "Wow, at least someone visists this.";
}
completeElseIf name == "Billy Bob Joe" {
  stampLn "Don't lie, the force tells me it is not.";
}
completeElse {
  stampLn "Welcome!";
}
```

### While Loops

A new feature, looks somewhat like this:

Structure: `completeWhile <case> { &Things to do& } `

You can use `quitLoop` to break the loop and `advance` to continue it.

Example:
```
counter = 0;
completeWhile True {

  stampLn "Spammin' I am";
  completeIf counter == 16 {
    quitLoop;
  }
  completeElseIf counter > 16 {
    stampLn "Systematic Error.....";
  }
  completeElse {
    advance;
    counter += 1;
  }
}
```

### For Loops

> Note: Currently, for loops can only loop numbers as in a statement like `for x in range(0, 10)` in Python, and not through arrays, since arrays have not been added yet(They're next on my list!)

Structure: `loop <variable name> from <beginning value> to <ending value> { &Things to do& }`

Example:
```
completeWhile True {
  times = captureInt 'How many times to loop?';
  completeIf times > 1000 {
    stampLn "I'm afraid that'll crash your computer";
  }
  completeElseIf times < 1 {
    stampLn "You need to have at least one time!!!";
  }
  completeElse {
    quitLoop;
  }
}
increment = "."
number = 1
loop time from 1 to times + 1 {
  stampLn "Looping{increments * number} Loop time: {time}";
  completeIf number == 3 {
    number = 0;
  }
  number += 1;
}


```

