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
weight = captureFloat "How much do you weigh?? ";
& Boolean Values &
covid19 = captureBool "Do you have the Coronavirus?? [True/False]";
```

### If Statements

Also very easy.

If you want to use an if statement, jut type `completeIf <case> { <contents>; }`

(Almost) Same for Elif/Else if:

`completeElseIf <case> { <contents>; }`

And lastly for else:

`otherwise { <contents>; }`

Example:
```
name = captureStr "What is your name?";
completeIf name == "Magnus Carlsen" {
  stampLn "Wow, at least someone visists this.";
}
completeElseIf name == "Billy Bob Joe" {
  stampLn "Don't lie, the force tells me it is not.";
}
otherwise {
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
  otherwise {
    advance;
    counter += 1;
  }
}
```

### For Loops

> Note: Currently, for loops can only loop numbers as in a statement like `for x in range(0, 10)` in Python, and not through arrays, since arrays have not been added yet

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
  otherwise {
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

### Functions

Yes, they're finally here! Functions! There are currently two types, and they're not too flexible, but I'll change that later, I'm focusing on *functionality* not *flexibility*.

Structure: `defFunc <function name> <( param1 , param2 )> {&Things to do& }`

Example:
```
defFunc add <( x , y )> {
  answer = x + y;
  stampLn "The answer is: ";
  stampLn answer;
}

add ( 5 , 5 );
```

You can also use `give <return value>;` to return a value for a function. And here's the harder part:

#### Inline Functions

What in the world are Inline Functions in this lang? They're when you call a function inside a variable, that's what! They're pretty non-flexible, and I'm trying to remove this difference, but it'll have to do for now.

Example:
```
function = add(7,8) - subtract(10,7);
```
Yeah, no spaces for you.

### The Built-In Functions

Yesssss... there are even built-ins, which makes it easier to do stuff. They are a module that comes in automatically, so you don't have to import anything.

#### How to use/Guide:

There are only 5 functions that come as built-ins, but here's a small guide to each of them.

List of Functions:

- string()
- integer()
- float()
- bool()
- reverse()

The names might sound familiar...

STRING()

Basically converts the given value to a string

INTEGER()

Does the same thing as a string, but converts the value into a whole number

FLOAT()

Same as integer, but only it returns a floating number

BOOL()

This is getting obvious, converts the given value to a Boolean

REVERSE()

The most interesting function: Returns a reversed version of a given string!

### Non-Built-In Packages

Hooray, these are here too! There are now packages that you can install manually.

> Warning: The packages install partially, so you have to use the following syntax to call functions and variables inside of the package: `<PACKAGENAMEHERE>.<FUNCTIONNAMEHERE>`

So what are the packages?

List of packages that I want in my language at the release of V1:

- [x] Color Package
- [x] Random Package
- [x] A timing package, like `time` in Python
- [x] A math package, like `math` in Python

That's it!

#### How to Use

Just type: `use <package name>;` and it's complete!
Example: `use colors;`

> Note: This is very minimal and I will upgrade it if I have time 

#### Colors

A small color guidebook, so you don't have to type the colors yourself.

This guidebook uses a few simple colors and a BOLD_ prefix if you want the color to be bold.

List of colors:
- Black
- Red
- Green
- Yellow
- Blue
- Magenta
- Cyan
- White

These use ANSI codes, so make sure your shell supports them.

Type the color code in capitals, like `BLUE` and you should be good!

#### Random

Second GuideBook!

The keyword is `lenrandom`, if you plan to import the package.

Functions:
- randomint( start , end ) - chooses a random number from `start` to `end`
- randFloat( start , end ) - same as randomint only with floating numbers
- randomDec() - returns a random decimal value from 0 to 1
- selectRandom ( item ) - Selects a random letter from a string.

#### Time Package

Third GuideBook!

The keyword is `clocktime` this time!

Functions:
- delay ( seconds ) - delays the program for a given amount of time
- getTime () - returns time since epoch
- toDayTime ( epoch ) - this one takes an epoch number and turns it into a date, like `Sun Aug 23 15:20:49 2020`
- zone () - Gives you your time zone

#### Last, but not least, the math package!

The keyword is `mathematics`!

Functions:
- sqRoot ( value ) - returns the square root of a given value.
- leftOver ( num1 , num2 ) - returns the remainder of `num1` ÷ `num2`
- exponent ( number , exp ) - returns `number` to the power of `exp`

### Reading Files

Lenstadt has this too.

All you have to do is:

```
readFile "PUTYOURFILEPATHHERE" as VARIABLENAME;
```

And the contents of that file will be stored in a variable.

### Writing to Files

Also simple:

```
writeFile "FILEPATH" as CONTENT;
```

And the file's content will be replaced with the CONTENT.


### More complex data structures

#### Tuples

Tuples are the only type of complex data structure that there is right now, so bear with me. Here is a basic tuple:

```
tuple = ( "Hello", "This", "Is", "A", "Taco", ( "Yes", "It", "Is" ) );
stampLn tuple;
```

