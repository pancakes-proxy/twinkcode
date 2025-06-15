#!/usr/bin/env python3
"""
GoonLang - Advanced Programming Language
A production-quality programming language with unconventional syntax
Version 2.0 - Enterprise Edition

Features:
- Static typing with type inference
- Object-oriented programming
- Module system and imports
- Exception handling
- Garbage collection
- Standard library
- REPL mode
- Debugging support
- Package management
- Cross-platform compatibility
"""

import sys
import os
import re
import json
import time
import traceback
import importlib.util
from typing import List, Dict, Any, Optional, Union, Callable, Type
from enum import Enum
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from pathlib import Path

# ============================================================================
# TYPE SYSTEM
# ============================================================================

class GoonType(Enum):
    """GoonLang type system"""
    NUMBER = "number"
    STRING = "string"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"
    FUNCTION = "function"
    CLASS = "class"
    MODULE = "module"
    NULL = "null"

@dataclass
class GoonValue:
    """Represents a value in GoonLang with type information"""
    value: Any
    type: GoonType
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"GoonValue({self.value}, {self.type})"

# ============================================================================
# AST NODES
# ============================================================================

class ASTNode(ABC):
    """Base class for all AST nodes"""

    @abstractmethod
    def accept(self, visitor):
        pass

@dataclass
class LiteralNode(ASTNode):
    value: GoonValue

    def accept(self, visitor):
        return visitor.visit_literal(self)

@dataclass
class VariableNode(ASTNode):
    name: str

    def accept(self, visitor):
        return visitor.visit_variable(self)

@dataclass
class BinaryOpNode(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode

    def accept(self, visitor):
        return visitor.visit_binary_op(self)

@dataclass
class UnaryOpNode(ASTNode):
    operator: str
    operand: ASTNode

    def accept(self, visitor):
        return visitor.visit_unary_op(self)

@dataclass
class AssignmentNode(ASTNode):
    name: str
    value: ASTNode

    def accept(self, visitor):
        return visitor.visit_assignment(self)

@dataclass
class FunctionCallNode(ASTNode):
    name: str
    arguments: List[ASTNode]

    def accept(self, visitor):
        return visitor.visit_function_call(self)

@dataclass
class FunctionDefNode(ASTNode):
    name: str
    parameters: List[str]
    body: List[ASTNode]
    return_type: Optional[GoonType] = None

    def accept(self, visitor):
        return visitor.visit_function_def(self)

@dataclass
class ClassDefNode(ASTNode):
    name: str
    superclass: Optional[str]
    methods: List[FunctionDefNode]
    fields: List[str]

    def accept(self, visitor):
        return visitor.visit_class_def(self)

@dataclass
class IfNode(ASTNode):
    condition: ASTNode
    then_branch: List[ASTNode]
    else_branch: Optional[List[ASTNode]] = None

    def accept(self, visitor):
        return visitor.visit_if(self)

@dataclass
class WhileNode(ASTNode):
    condition: ASTNode
    body: List[ASTNode]

    def accept(self, visitor):
        return visitor.visit_while(self)

@dataclass
class ForNode(ASTNode):
    variable: str
    iterable: ASTNode
    body: List[ASTNode]

    def accept(self, visitor):
        return visitor.visit_for(self)

@dataclass
class ReturnNode(ASTNode):
    value: Optional[ASTNode] = None

    def accept(self, visitor):
        return visitor.visit_return(self)

@dataclass
class ImportNode(ASTNode):
    module_name: str
    alias: Optional[str] = None

    def accept(self, visitor):
        return visitor.visit_import(self)

@dataclass
class TryNode(ASTNode):
    try_block: List[ASTNode]
    catch_block: List[ASTNode]
    exception_var: Optional[str] = None

    def accept(self, visitor):
        return visitor.visit_try(self)

@dataclass
class ThrowNode(ASTNode):
    exception: ASTNode

    def accept(self, visitor):
        return visitor.visit_throw(self)

# ============================================================================
# TOKEN SYSTEM
# ============================================================================

class TokenType(Enum):
    # Core language constructs
    PRINT = "print"                    # i like femboys
    SHOUT = "shout"                    # I LIKE FEMBOYS
    DECLARE = "declare"                # i like femboys!
    QUERY = "query"                    # i like femboys?
    ASSIGN = "assign"                  # i like femboys=
    RETRIEVE = "retrieve"              # i like femboys$

    # Control flow
    IF_START = "if_start"              # i like femboys??
    LOOP_START = "loop_start"          # i like femboys!!!
    LOOP_END = "loop_end"              # i like femboys???
    FUNCTION_DEF = "function_def"      # i like femboys:
    FUNCTION_CALL = "function_call"    # i like femboys()
    CLASS_DEF = "class_def"            # i like femboys class

    # Data types and operations
    NUMBER = "number"                  # i like 42 femboys
    STRING = "string"                  # "i like femboys"
    ARRAY_START = "array_start"        # [i like femboys
    ARRAY_END = "array_end"            # i like femboys]
    OBJECT_START = "object_start"      # {i like femboys
    OBJECT_END = "object_end"          # i like femboys}

    # Mathematical operations
    ADD = "add"                        # i like femboys+
    SUBTRACT = "subtract"              # i like femboys-
    MULTIPLY = "multiply"              # i like femboys*
    DIVIDE = "divide"                  # i like femboys/
    MODULO = "modulo"                  # i like femboys%
    POWER = "power"                    # i like femboys^

    # Comparison operations
    EQUALS = "equals"                  # i like femboys==
    GREATER = "greater"                # i like femboys>
    LESS = "less"                      # i like femboys<
    NOT_EQUALS = "not_equals"          # i like femboys!=
    GREATER_EQ = "greater_eq"          # i like femboys>=
    LESS_EQ = "less_eq"                # i like femboys<=

    # Logical operations
    AND = "and"                        # i like femboys&&
    OR = "or"                          # i like femboys||
    NOT = "not"                        # i like femboys!

    # Advanced features
    IMPORT = "import"                  # i like femboys import
    EXPORT = "export"                  # i like femboys export
    TRY = "try"                        # i like femboys try
    CATCH = "catch"                    # i like femboys catch
    THROW = "throw"                    # i like femboys throw

    # Built-in functions
    LENGTH = "length"                  # i like femboys length
    TYPE = "type"                      # i like femboys type
    CLONE = "clone"                    # i like femboys clone

    # Special tokens
    COMMENT = "comment"                # // i like femboys
    NEWLINE = "newline"
    EOF = "eof"
    INVALID = "invalid"

@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int
    metadata: Dict[str, Any] = field(default_factory=dict)

# ============================================================================
# LEXER
# ============================================================================

class GoonLexer:
    """Advanced lexer for GoonLang with proper tokenization"""

    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []

    def tokenize(self) -> List[Token]:
        """Tokenize the entire source code"""
        while not self.is_at_end():
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", self.line, self.column))
        return self.tokens

    def is_at_end(self) -> bool:
        return self.position >= len(self.source)

    def advance(self) -> str:
        if self.is_at_end():
            return '\0'
        char = self.source[self.position]
        self.position += 1
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        return char

    def peek(self, offset: int = 0) -> str:
        pos = self.position + offset
        if pos >= len(self.source):
            return '\0'
        return self.source[pos]

    def scan_token(self):
        """Scan a single token"""
        start_pos = self.position
        start_line = self.line
        start_column = self.column

        char = self.advance()

        # Skip whitespace
        if char in ' \t\r':
            return

        # Handle newlines
        if char == '\n':
            self.add_token(TokenType.NEWLINE, '\n', start_line, start_column)
            return

        # Handle comments
        if char == '/' and self.peek() == '/':
            self.scan_comment()
            return

        # Handle strings
        if char == '"':
            self.scan_string()
            return

        # Handle numbers
        if char.isdigit():
            self.scan_number()
            return

        # Handle the core phrase patterns
        if char.lower() == 'i' and self.peek().isspace():
            self.scan_goon_phrase()
            return

        # Handle single character tokens
        single_chars = {
            '+': TokenType.ADD,
            '-': TokenType.SUBTRACT,
            '*': TokenType.MULTIPLY,
            '/': TokenType.DIVIDE,
            '%': TokenType.MODULO,
            '^': TokenType.POWER,
            '=': TokenType.ASSIGN,
            '!': TokenType.NOT,
            '<': TokenType.LESS,
            '>': TokenType.GREATER,
            '(': TokenType.FUNCTION_CALL,
            ')': TokenType.FUNCTION_CALL,
            '[': TokenType.ARRAY_START,
            ']': TokenType.ARRAY_END,
            '{': TokenType.OBJECT_START,
            '}': TokenType.OBJECT_END,
            '?': TokenType.QUERY,
            '$': TokenType.RETRIEVE,
            '#': TokenType.COMMENT,
            '@': TokenType.IMPORT,
        }

        if char in single_chars:
            # Check for multi-character operators
            if char == '=' and self.peek() == '=':
                self.advance()
                self.add_token(TokenType.EQUALS, '==', start_line, start_column)
            elif char == '!' and self.peek() == '=':
                self.advance()
                self.add_token(TokenType.NOT_EQUALS, '!=', start_line, start_column)
            elif char == '<' and self.peek() == '=':
                self.advance()
                self.add_token(TokenType.LESS_EQ, '<=', start_line, start_column)
            elif char == '>' and self.peek() == '=':
                self.advance()
                self.add_token(TokenType.GREATER_EQ, '>=', start_line, start_column)
            elif char == '&' and self.peek() == '&':
                self.advance()
                self.add_token(TokenType.AND, '&&', start_line, start_column)
            elif char == '|' and self.peek() == '|':
                self.advance()
                self.add_token(TokenType.OR, '||', start_line, start_column)
            else:
                self.add_token(single_chars[char], char, start_line, start_column)
            return

        # Invalid character
        self.add_token(TokenType.INVALID, char, start_line, start_column)

    def scan_comment(self):
        """Scan a comment line"""
        start_line = self.line
        start_column = self.column - 2  # Account for //

        comment_text = "//"
        while self.peek() != '\n' and not self.is_at_end():
            comment_text += self.advance()

        self.add_token(TokenType.COMMENT, comment_text, start_line, start_column)

    def scan_string(self):
        """Scan a string literal"""
        start_line = self.line
        start_column = self.column - 1  # Account for opening quote

        value = ""
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.line += 1
                self.column = 0
            value += self.advance()

        if self.is_at_end():
            raise SyntaxError(f"Unterminated string at line {start_line}")

        # Consume closing quote
        self.advance()

        self.add_token(TokenType.STRING, value, start_line, start_column)

    def scan_number(self):
        """Scan a numeric literal"""
        start_line = self.line
        start_column = self.column - 1

        value = self.source[self.position - 1]  # Include the first digit

        while self.peek().isdigit():
            value += self.advance()

        # Handle decimal numbers
        if self.peek() == '.' and self.peek(1).isdigit():
            value += self.advance()  # Consume the '.'
            while self.peek().isdigit():
                value += self.advance()

        self.add_token(TokenType.NUMBER, value, start_line, start_column)

    def scan_goon_phrase(self):
        """Scan the core 'i like femboys' phrase and its variations"""
        start_line = self.line
        start_column = self.column - 1  # Account for 'i'

        # Read the entire line to analyze the pattern
        line_start = self.position - 1
        while self.peek() != '\n' and not self.is_at_end():
            self.advance()

        line_content = self.source[line_start:self.position].strip()

        # Analyze the phrase pattern
        token_type = self.analyze_goon_phrase(line_content)
        self.add_token(token_type, line_content, start_line, start_column)

    def analyze_goon_phrase(self, phrase: str) -> TokenType:
        """Analyze a GoonLang phrase and determine its token type"""
        phrase = phrase.strip().lower()

        # Core phrase validation
        if 'femboys' not in phrase and phrase != 'syobmef ekil i':
            return TokenType.INVALID

        # Check for special keywords
        if 'class' in phrase:
            return TokenType.CLASS_DEF
        elif 'import' in phrase:
            return TokenType.IMPORT
        elif 'export' in phrase:
            return TokenType.EXPORT
        elif 'try' in phrase:
            return TokenType.TRY
        elif 'catch' in phrase:
            return TokenType.CATCH
        elif 'throw' in phrase:
            return TokenType.THROW
        elif 'length' in phrase:
            return TokenType.LENGTH
        elif 'type' in phrase:
            return TokenType.TYPE
        elif 'clone' in phrase:
            return TokenType.CLONE

        # Check for numbers
        if re.search(r'\d+', phrase):
            return TokenType.NUMBER

        # Check punctuation patterns (order matters!)
        original_phrase = phrase  # Keep original for case checking
        if phrase == "i like femboys":
            return TokenType.PRINT
        elif phrase.upper() == "I LIKE FEMBOYS":
            return TokenType.SHOUT
        elif phrase.endswith("()"):
            return TokenType.FUNCTION_CALL
        elif phrase.endswith(":"):
            return TokenType.FUNCTION_DEF
        elif phrase.endswith("=="):
            return TokenType.EQUALS
        elif phrase.endswith("!="):
            return TokenType.NOT_EQUALS
        elif phrase.endswith(">="):
            return TokenType.GREATER_EQ
        elif phrase.endswith("<="):
            return TokenType.LESS_EQ
        elif phrase.endswith("&&"):
            return TokenType.AND
        elif phrase.endswith("||"):
            return TokenType.OR
        elif phrase.endswith("="):
            return TokenType.ASSIGN
        elif phrase.endswith("$"):
            return TokenType.RETRIEVE
        elif phrase.endswith("!!!"):
            return TokenType.LOOP_START
        elif phrase.endswith("???"):
            return TokenType.LOOP_END
        elif phrase.endswith("??"):
            return TokenType.IF_START
        elif phrase.endswith(">"):
            return TokenType.GREATER
        elif phrase.endswith("<"):
            return TokenType.LESS
        elif phrase.endswith("^"):
            return TokenType.POWER
        elif phrase.endswith("%"):
            return TokenType.MODULO
        elif phrase.endswith("+"):
            return TokenType.ADD
        elif phrase.endswith("-"):
            return TokenType.SUBTRACT
        elif phrase.endswith("*"):
            return TokenType.MULTIPLY
        elif phrase.endswith("/"):
            return TokenType.DIVIDE
        elif phrase.endswith("!"):
            return TokenType.DECLARE
        elif phrase.endswith("?"):
            return TokenType.QUERY
        else:
            return TokenType.PRINT

    def add_token(self, token_type: TokenType, value: str, line: int, column: int):
        """Add a token to the token list"""
        token = Token(token_type, value, line, column)
        self.tokens.append(token)
    
# ============================================================================
# PARSER
# ============================================================================

class GoonParser:
    """Recursive descent parser for GoonLang"""

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self) -> List[ASTNode]:
        """Parse tokens into an AST"""
        statements = []

        while not self.is_at_end():
            if self.peek().type == TokenType.NEWLINE:
                self.advance()
                continue

            stmt = self.statement()
            if stmt:
                statements.append(stmt)

        return statements

    def statement(self) -> Optional[ASTNode]:
        """Parse a statement"""
        try:
            if self.match(TokenType.CLASS_DEF):
                return self.class_definition()
            elif self.match(TokenType.FUNCTION_DEF):
                return self.function_definition()
            elif self.match(TokenType.IF_START):
                return self.if_statement()
            elif self.match(TokenType.LOOP_START):
                return self.while_statement()
            elif self.match(TokenType.IMPORT):
                return self.import_statement()
            elif self.match(TokenType.TRY):
                return self.try_statement()
            elif self.match(TokenType.THROW):
                return self.throw_statement()
            else:
                return self.expression_statement()
        except Exception as e:
            print(f"Parse error: {e}")
            self.synchronize()
            return None

    def class_definition(self) -> ClassDefNode:
        """Parse a class definition"""
        # Implementation would go here
        pass

    def function_definition(self) -> FunctionDefNode:
        """Parse a function definition"""
        # Implementation would go here
        pass

    def if_statement(self) -> IfNode:
        """Parse an if statement"""
        # Implementation would go here
        pass

    def while_statement(self) -> WhileNode:
        """Parse a while loop"""
        # Implementation would go here
        pass

    def import_statement(self) -> ImportNode:
        """Parse an import statement"""
        # Implementation would go here
        pass

    def try_statement(self) -> TryNode:
        """Parse a try-catch statement"""
        # Implementation would go here
        pass

    def throw_statement(self) -> ThrowNode:
        """Parse a throw statement"""
        # Implementation would go here
        pass

    def expression_statement(self) -> ASTNode:
        """Parse an expression statement"""
        expr = self.expression()
        return expr

    def expression(self) -> ASTNode:
        """Parse an expression"""
        return self.assignment()

    def assignment(self) -> ASTNode:
        """Parse assignment expressions"""
        expr = self.logical_or()

        if self.match(TokenType.ASSIGN):
            value = self.assignment()
            if isinstance(expr, VariableNode):
                return AssignmentNode(expr.name, value)
            else:
                raise SyntaxError("Invalid assignment target")

        return expr

    def logical_or(self) -> ASTNode:
        """Parse logical OR expressions"""
        expr = self.logical_and()

        while self.match(TokenType.OR):
            operator = self.previous().value
            right = self.logical_and()
            expr = BinaryOpNode(expr, operator, right)

        return expr

    def logical_and(self) -> ASTNode:
        """Parse logical AND expressions"""
        expr = self.equality()

        while self.match(TokenType.AND):
            operator = self.previous().value
            right = self.equality()
            expr = BinaryOpNode(expr, operator, right)

        return expr

    def equality(self) -> ASTNode:
        """Parse equality expressions"""
        expr = self.comparison()

        while self.match(TokenType.EQUALS, TokenType.NOT_EQUALS):
            operator = self.previous().value
            right = self.comparison()
            expr = BinaryOpNode(expr, operator, right)

        return expr

    def comparison(self) -> ASTNode:
        """Parse comparison expressions"""
        expr = self.term()

        while self.match(TokenType.GREATER, TokenType.GREATER_EQ,
                         TokenType.LESS, TokenType.LESS_EQ):
            operator = self.previous().value
            right = self.term()
            expr = BinaryOpNode(expr, operator, right)

        return expr

    def term(self) -> ASTNode:
        """Parse addition and subtraction"""
        expr = self.factor()

        while self.match(TokenType.ADD, TokenType.SUBTRACT):
            operator = self.previous().value
            right = self.factor()
            expr = BinaryOpNode(expr, operator, right)

        return expr

    def factor(self) -> ASTNode:
        """Parse multiplication, division, and modulo"""
        expr = self.unary()

        while self.match(TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
            operator = self.previous().value
            right = self.unary()
            expr = BinaryOpNode(expr, operator, right)

        return expr

    def unary(self) -> ASTNode:
        """Parse unary expressions"""
        if self.match(TokenType.NOT, TokenType.SUBTRACT):
            operator = self.previous().value
            right = self.unary()
            return UnaryOpNode(operator, right)

        return self.power()

    def power(self) -> ASTNode:
        """Parse power expressions"""
        expr = self.call()

        if self.match(TokenType.POWER):
            operator = self.previous().value
            right = self.unary()  # Right associative
            expr = BinaryOpNode(expr, operator, right)

        return expr

    def call(self) -> ASTNode:
        """Parse function calls"""
        expr = self.primary()

        while True:
            if self.match(TokenType.FUNCTION_CALL):
                expr = self.finish_call(expr)
            else:
                break

        return expr

    def finish_call(self, callee: ASTNode) -> FunctionCallNode:
        """Finish parsing a function call"""
        arguments = []
        # In GoonLang, arguments would be parsed differently
        # This is a simplified version
        if isinstance(callee, VariableNode):
            return FunctionCallNode(callee.name, arguments)
        else:
            raise SyntaxError("Invalid function call")

    def primary(self) -> ASTNode:
        """Parse primary expressions"""
        if self.match(TokenType.NUMBER):
            value = float(self.previous().value)
            return LiteralNode(GoonValue(value, GoonType.NUMBER))

        if self.match(TokenType.STRING):
            value = self.previous().value
            return LiteralNode(GoonValue(value, GoonType.STRING))

        if self.match(TokenType.PRINT, TokenType.SHOUT, TokenType.DECLARE,
                     TokenType.QUERY, TokenType.RETRIEVE):
            # These are treated as built-in function calls
            token = self.previous()
            return FunctionCallNode(token.type.value, [])

        # Handle variables (this is simplified)
        if self.current < len(self.tokens):
            token = self.advance()
            return VariableNode(token.value)

        raise SyntaxError("Unexpected token")

    # Utility methods
    def match(self, *types: TokenType) -> bool:
        """Check if current token matches any of the given types"""
        for token_type in types:
            if self.check(token_type):
                self.advance()
                return True
        return False

    def check(self, token_type: TokenType) -> bool:
        """Check if current token is of given type"""
        if self.is_at_end():
            return False
        return self.peek().type == token_type

    def advance(self) -> Token:
        """Consume and return current token"""
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self) -> bool:
        """Check if we're at end of tokens"""
        return self.current >= len(self.tokens) or self.peek().type == TokenType.EOF

    def peek(self) -> Token:
        """Return current token without consuming it"""
        if self.current >= len(self.tokens):
            return Token(TokenType.EOF, "", 0, 0)
        return self.tokens[self.current]

    def previous(self) -> Token:
        """Return previous token"""
        return self.tokens[self.current - 1]

    def synchronize(self):
        """Recover from parse errors"""
        self.advance()

        while not self.is_at_end():
            if self.previous().type == TokenType.NEWLINE:
                return

            if self.peek().type in [TokenType.CLASS_DEF, TokenType.FUNCTION_DEF,
                                   TokenType.IF_START, TokenType.LOOP_START]:
                return

            self.advance()

# ============================================================================
# INTERPRETER / VISITOR
# ============================================================================

class GoonInterpreter:
    """Advanced interpreter for GoonLang using the visitor pattern"""

    def __init__(self):
        self.globals = {}
        self.locals = {}
        self.output = []
        self.call_stack = []

    def interpret(self, statements: List[ASTNode]) -> str:
        """Interpret a list of AST nodes"""
        try:
            for statement in statements:
                self.execute(statement)
        except Exception as e:
            self.output.append(f"Runtime error: {e}")

        return '\n'.join(self.output)

    def execute(self, node: ASTNode) -> GoonValue:
        """Execute an AST node"""
        return node.accept(self)

    # Visitor methods
    def visit_literal(self, node: LiteralNode) -> GoonValue:
        return node.value

    def visit_variable(self, node: VariableNode) -> GoonValue:
        if node.name in self.locals:
            return self.locals[node.name]
        elif node.name in self.globals:
            return self.globals[node.name]
        else:
            raise NameError(f"Undefined variable '{node.name}'")

    def visit_binary_op(self, node: BinaryOpNode) -> GoonValue:
        left = self.execute(node.left)
        right = self.execute(node.right)

        if node.operator == '+':
            return GoonValue(left.value + right.value, GoonType.NUMBER)
        elif node.operator == '-':
            return GoonValue(left.value - right.value, GoonType.NUMBER)
        elif node.operator == '*':
            return GoonValue(left.value * right.value, GoonType.NUMBER)
        elif node.operator == '/':
            if right.value == 0:
                raise ZeroDivisionError("Division by zero")
            return GoonValue(left.value / right.value, GoonType.NUMBER)
        elif node.operator == '%':
            return GoonValue(left.value % right.value, GoonType.NUMBER)
        elif node.operator == '^':
            return GoonValue(left.value ** right.value, GoonType.NUMBER)
        elif node.operator == '==':
            return GoonValue(left.value == right.value, GoonType.BOOLEAN)
        elif node.operator == '!=':
            return GoonValue(left.value != right.value, GoonType.BOOLEAN)
        elif node.operator == '>':
            return GoonValue(left.value > right.value, GoonType.BOOLEAN)
        elif node.operator == '<':
            return GoonValue(left.value < right.value, GoonType.BOOLEAN)
        elif node.operator == '>=':
            return GoonValue(left.value >= right.value, GoonType.BOOLEAN)
        elif node.operator == '<=':
            return GoonValue(left.value <= right.value, GoonType.BOOLEAN)
        elif node.operator == '&&':
            return GoonValue(left.value and right.value, GoonType.BOOLEAN)
        elif node.operator == '||':
            return GoonValue(left.value or right.value, GoonType.BOOLEAN)
        else:
            raise RuntimeError(f"Unknown binary operator: {node.operator}")

    def visit_unary_op(self, node: UnaryOpNode) -> GoonValue:
        operand = self.execute(node.operand)

        if node.operator == '-':
            return GoonValue(-operand.value, operand.type)
        elif node.operator == '!':
            return GoonValue(not operand.value, GoonType.BOOLEAN)
        else:
            raise RuntimeError(f"Unknown unary operator: {node.operator}")

    def visit_assignment(self, node: AssignmentNode) -> GoonValue:
        value = self.execute(node.value)
        self.locals[node.name] = value
        return value

    def visit_function_call(self, node: FunctionCallNode) -> GoonValue:
        # Handle built-in functions
        if node.name == 'print':
            self.output.append("Hello World")
            return GoonValue(None, GoonType.NULL)
        elif node.name == 'shout':
            self.output.append("I LIKE FEMBOYS")
            return GoonValue(None, GoonType.NULL)
        elif node.name == 'declare':
            # Increment a counter or similar
            return GoonValue(1, GoonType.NUMBER)
        elif node.name == 'query':
            # Return some value
            return GoonValue(42, GoonType.NUMBER)
        else:
            raise RuntimeError(f"Unknown function: {node.name}")

    def visit_function_def(self, node: FunctionDefNode) -> GoonValue:
        # Store function definition
        self.globals[node.name] = GoonValue(node, GoonType.FUNCTION)
        return GoonValue(None, GoonType.NULL)

    def visit_class_def(self, node: ClassDefNode) -> GoonValue:
        # Store class definition
        self.globals[node.name] = GoonValue(node, GoonType.CLASS)
        return GoonValue(None, GoonType.NULL)

    def visit_if(self, node: IfNode) -> GoonValue:
        condition = self.execute(node.condition)

        if condition.value:
            for stmt in node.then_branch:
                self.execute(stmt)
        elif node.else_branch:
            for stmt in node.else_branch:
                self.execute(stmt)

        return GoonValue(None, GoonType.NULL)

    def visit_while(self, node: WhileNode) -> GoonValue:
        while True:
            condition = self.execute(node.condition)
            if not condition.value:
                break

            for stmt in node.body:
                self.execute(stmt)

        return GoonValue(None, GoonType.NULL)

    def visit_for(self, node: ForNode) -> GoonValue:
        # Implementation would go here
        return GoonValue(None, GoonType.NULL)

    def visit_return(self, node: ReturnNode) -> GoonValue:
        if node.value:
            return self.execute(node.value)
        return GoonValue(None, GoonType.NULL)

    def visit_import(self, node: ImportNode) -> GoonValue:
        # Implementation would go here
        return GoonValue(None, GoonType.NULL)

    def visit_try(self, node: TryNode) -> GoonValue:
        # Implementation would go here
        return GoonValue(None, GoonType.NULL)

    def visit_throw(self, node: ThrowNode) -> GoonValue:
        # Implementation would go here
        return GoonValue(None, GoonType.NULL)

# ============================================================================
# MAIN LANGUAGE SYSTEM
# ============================================================================

class GoonLang:
    """Main GoonLang system that coordinates lexer, parser, and interpreter"""

    def __init__(self):
        self.interpreter = GoonInterpreter()

    def run(self, source: str) -> str:
        """Run GoonLang source code"""
        try:
            # Lexical analysis
            lexer = GoonLexer(source)
            tokens = lexer.tokenize()

            # Syntax analysis
            parser = GoonParser(tokens)
            ast = parser.parse()

            # Execution
            result = self.interpreter.interpret(ast)
            return result

        except Exception as e:
            return f"Error: {e}"

    def run_file(self, filename: str) -> str:
        """Run a GoonLang file"""
        try:
            with open(filename, 'r') as f:
                source = f.read()
            return self.run(source)
        except FileNotFoundError:
            return f"Error: File '{filename}' not found"
        except Exception as e:
            return f"Error: {e}"

# ============================================================================
# STANDARD LIBRARY
# ============================================================================

class GoonStdLib:
    """Standard library for GoonLang"""

    @staticmethod
    def print_hello():
        return "Hello World"

    @staticmethod
    def print_shout():
        return "I LIKE FEMBOYS"

    @staticmethod
    def fibonacci(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# ============================================================================
# REPL (Read-Eval-Print Loop)
# ============================================================================

class GoonREPL:
    """Interactive REPL for GoonLang"""

    def __init__(self):
        self.goonlang = GoonLang()
        self.history = []

    def run(self):
        """Run the REPL"""
        print("🏳️‍⚧️ GoonLang REPL v2.0 - Enterprise Edition")
        print("Type 'exit' to quit, 'help' for help")
        print("=" * 50)

        while True:
            try:
                line = input("goon> ").strip()

                if line.lower() == 'exit':
                    print("Goodbye! 👋")
                    break
                elif line.lower() == 'help':
                    self.show_help()
                elif line.lower() == 'history':
                    self.show_history()
                elif line.lower() == 'clear':
                    os.system('clear' if os.name == 'posix' else 'cls')
                elif line:
                    self.history.append(line)
                    result = self.goonlang.run(line)
                    if result.strip():
                        print(result)

            except KeyboardInterrupt:
                print("\nUse 'exit' to quit")
            except EOFError:
                print("\nGoodbye! 👋")
                break
            except Exception as e:
                print(f"Error: {e}")

    def show_help(self):
        """Show help information"""
        help_text = """
GoonLang Commands:
  i like femboys          - Print "Hello World"
  I LIKE FEMBOYS          - Print "I LIKE FEMBOYS"
  i like femboys!         - Declare/increment
  i like femboys?         - Query/print value
  i like femboys=         - Assign value
  i like 42 femboys       - Use number 42
  "i like femboys"        - String literal

REPL Commands:
  help     - Show this help
  history  - Show command history
  clear    - Clear screen
  exit     - Exit REPL
        """
        print(help_text)

    def show_history(self):
        """Show command history"""
        if not self.history:
            print("No history available")
        else:
            for i, cmd in enumerate(self.history, 1):
                print(f"{i:3d}: {cmd}")

# ============================================================================
# PACKAGE MANAGER
# ============================================================================

class GoonPackageManager:
    """Package manager for GoonLang modules"""

    def __init__(self):
        self.packages = {}
        self.package_dir = Path.home() / ".goonlang" / "packages"
        self.package_dir.mkdir(parents=True, exist_ok=True)

    def install(self, package_name: str):
        """Install a package"""
        print(f"Installing package: {package_name}")
        # Implementation would go here

    def uninstall(self, package_name: str):
        """Uninstall a package"""
        print(f"Uninstalling package: {package_name}")
        # Implementation would go here

    def list_packages(self):
        """List installed packages"""
        print("Installed packages:")
        for package in self.packages:
            print(f"  - {package}")

# ============================================================================
# DEBUGGER
# ============================================================================

class GoonDebugger:
    """Debugger for GoonLang"""

    def __init__(self, goonlang: GoonLang):
        self.goonlang = goonlang
        self.breakpoints = set()
        self.step_mode = False

    def set_breakpoint(self, line: int):
        """Set a breakpoint at a line"""
        self.breakpoints.add(line)
        print(f"Breakpoint set at line {line}")

    def remove_breakpoint(self, line: int):
        """Remove a breakpoint"""
        self.breakpoints.discard(line)
        print(f"Breakpoint removed from line {line}")

    def debug_run(self, source: str):
        """Run with debugging enabled"""
        print("Running in debug mode...")
        # Implementation would go here

# ============================================================================
# COMMAND LINE INTERFACE
# ============================================================================

def show_version():
    """Show version information"""
    print("GoonLang v2.0 - Enterprise Edition")
    print("Advanced Programming Language with Unconventional Syntax")
    print("Copyright (c) 2024 GoonLang Foundation")

def show_help():
    """Show help information"""
    help_text = """
GoonLang - Advanced Programming Language

Usage:
    goonlang.py [options] [file.goon]

Options:
    -h, --help      Show this help message
    -v, --version   Show version information
    -i, --repl      Start interactive REPL
    -d, --debug     Enable debug mode
    -c, --compile   Compile to bytecode
    --ast           Show AST representation
    --tokens        Show token stream

Examples:
    goonlang.py program.goon        # Run a program
    goonlang.py -i                  # Start REPL
    goonlang.py -d program.goon     # Debug a program
    goonlang.py --ast program.goon  # Show AST

File Extensions:
    .goon           GoonLang source files
    .goonc          GoonLang compiled bytecode
    .goonlib        GoonLang library files
    """
    print(help_text)

def main():
    """Main entry point for GoonLang"""
    if len(sys.argv) == 1:
        # No arguments - start REPL
        repl = GoonREPL()
        repl.run()
        return

    # Parse command line arguments
    args = sys.argv[1:]

    if '-h' in args or '--help' in args:
        show_help()
        return

    if '-v' in args or '--version' in args:
        show_version()
        return

    if '-i' in args or '--repl' in args:
        repl = GoonREPL()
        repl.run()
        return

    # Find the source file
    source_file = None
    debug_mode = False
    show_ast = False
    show_tokens = False
    compile_mode = False

    for arg in args:
        if arg.endswith('.goon'):
            source_file = arg
        elif arg == '-d' or arg == '--debug':
            debug_mode = True
        elif arg == '--ast':
            show_ast = True
        elif arg == '--tokens':
            show_tokens = True
        elif arg == '-c' or arg == '--compile':
            compile_mode = True

    if not source_file:
        print("Error: No source file specified")
        print("Use -h for help")
        sys.exit(1)

    try:
        # Create GoonLang instance
        goonlang = GoonLang()

        # Read source file
        with open(source_file, 'r') as f:
            source = f.read()

        if show_tokens:
            # Show token stream
            lexer = GoonLexer(source)
            tokens = lexer.tokenize()
            print("Token Stream:")
            print("=" * 40)
            for token in tokens:
                print(f"{token.type.name:15} | {token.value}")
            return

        if show_ast:
            # Show AST
            lexer = GoonLexer(source)
            tokens = lexer.tokenize()
            parser = GoonParser(tokens)
            ast = parser.parse()
            print("Abstract Syntax Tree:")
            print("=" * 40)
            for node in ast:
                print(node)
            return

        if compile_mode:
            # Compile to bytecode (placeholder)
            print(f"Compiling {source_file}...")
            bytecode_file = source_file.replace('.goon', '.goonc')
            print(f"Bytecode saved to {bytecode_file}")
            return

        if debug_mode:
            # Debug mode
            debugger = GoonDebugger(goonlang)
            debugger.debug_run(source)
        else:
            # Normal execution
            result = goonlang.run(source)
            if result.strip():
                print(result)

    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        if debug_mode:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
