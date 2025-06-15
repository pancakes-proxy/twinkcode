# GoonLang Language Specification

## Overview
GoonLang is a joke programming language where all valid syntax is based on variations of the phrase "i like femboys". Despite its unconventional approach, GoonLang is Turing complete and supports a wide range of programming constructs.

## Core Principle
Every line of GoonLang code must contain the phrase "i like femboys" (case-insensitive) or be a comment/string literal. The specific variation determines the operation performed.

## Token Types and Operations

### Basic Operations
| Syntax | Token Type | Operation | Description |
|--------|------------|-----------|-------------|
| `i like femboys` | BASIC | Print "Hello World" | Standard greeting |
| `I LIKE FEMBOYS` | SHOUT | Print "I LIKE FEMBOYS" | Echo in caps |
| `i like femboys!` | EXCITED | Increment accumulator | Add 1 to accumulator |
| `i like femboys?` | QUESTION | Print accumulator | Display current value |
| `i like femboys.` | STATEMENT | Reset accumulator | Set accumulator to 0 |

### Arithmetic Operations
| Syntax | Token Type | Operation | Description |
|--------|------------|-----------|-------------|
| `i like femboys femboys` | DOUBLE | Multiply by 2 | Double accumulator |
| `i like femboys femboys femboys` | TRIPLE | Multiply by 3 | Triple accumulator |
| `i  like  femboys` | SPACED | Add 10 per space pair | Multiple spaces = tens |
| `i like femboys+` | MATH_ADD | Push to stack | Store value for operation |
| `i like femboys-` | MATH_SUB | Subtract from stack | Pop and subtract |
| `i like femboys*` | MATH_MUL | Multiply with stack | Pop and multiply |
| `i like femboys/` | MATH_DIV | Divide with stack | Pop and divide |

### Control Flow
| Syntax | Token Type | Operation | Description |
|--------|------------|-----------|-------------|
| `i like femboys!!!` | LOOP_START | Begin loop | Start iteration |
| `i like femboys???` | LOOP_END | End loop | End iteration |
| `i like femboys??` | CONDITIONAL | If-then check | Test accumulator |

### Variables and Functions
| Syntax | Token Type | Operation | Description |
|--------|------------|-----------|-------------|
| `i like femboys=` | VARIABLE_SET | Store variable | Save accumulator |
| `i like femboys$` | VARIABLE_GET | Load variable | Retrieve value |
| `i like femboys:` | FUNCTION_DEF | Define function | Create function |
| `i like femboys()` | FUNCTION_CALL | Call function | Execute function |

### Data Structures
| Syntax | Token Type | Operation | Description |
|--------|------------|-----------|-------------|
| `[i like femboys` | ARRAY_START | Create array | Initialize array |
| `i like femboys]` | ARRAY_END | Add to array | Append value |

### Special Operations
| Syntax | Token Type | Operation | Description |
|--------|------------|-----------|-------------|
| `i like femboys!!!!!` | MULTI_EXCITED | Add exclamation count | Multiple increments |
| `i like femboys...` | WHISPER | Whisper output | Quiet print |
| `syobmef ekil i` | REVERSE | Reverse operation | Reverse last output |
| `I lIkE fEmBoYs` | MIXED_CASE | Mixed case detected | Special formatting |
| `i like 42 femboys` | NUMBERS | Add numbers | Extract and add digits |

### Meta Operations
| Syntax | Token Type | Operation | Description |
|--------|------------|-----------|-------------|
| `"i like femboys"` | STRING_MODE | String literal | Direct string output |
| `// i like femboys` | COMMENT | Comment | No operation |

## Memory Model
- **Accumulator**: Primary register for calculations
- **Stack**: For complex arithmetic operations
- **Variables**: Named storage (auto-generated names)
- **Functions**: Stored procedures (auto-generated names)
- **Arrays**: Dynamic lists (auto-generated names)

## Execution Model
1. Each line is tokenized based on pattern matching
2. Tokens are executed sequentially
3. State is maintained across lines
4. Output is collected and displayed at end

## Examples

### Fibonacci Sequence (Conceptual)
```goon
i like femboys!          // acc = 1
i like femboys=          // var_0 = 1
i like femboys!          // acc = 2
i like femboys=          // var_1 = 2
i like femboys$          // acc = var_1 = 2
i like femboys+          // push 2
// ... continue pattern
```

### Factorial (Conceptual)
```goon
i like 5 femboys         // acc = 5
i like femboys=          // var_0 = 5
i like femboys!!!        // loop start
i like femboys$          // get var_0
i like femboys-          // subtract 1
i like femboys=          // store back
i like femboys???        // loop end
```

## Error Handling
- Invalid syntax (not containing "femboys") is treated as empty line
- Division by zero produces error message
- Stack underflow is handled gracefully

## Philosophy
GoonLang demonstrates that:
1. Programming languages are about pattern recognition
2. Syntax is arbitrary - semantics matter
3. Even joke languages can be functionally complete
4. Creativity in language design has no bounds

## Implementation Notes
- Written in Python 3
- Uses regex for pattern matching
- Maintains interpreter state
- Supports file execution with `.goon` extension
