#!/usr/bin/env python3
"""
Comprehensive test suite for GoonLang
Tests lexer, parser, interpreter, and all language features
"""

import unittest
import sys
import os

# Add parent directory to path to import goonlang
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from goonlang import (
    GoonLang, GoonLexer, GoonParser, GoonInterpreter,
    TokenType, GoonType, GoonValue, LiteralNode, VariableNode
)


class TestGoonLexer(unittest.TestCase):
    """Test the GoonLang lexer"""
    
    def setUp(self):
        self.lexer = None
    
    def test_basic_tokenization(self):
        """Test basic phrase tokenization"""
        source = "i like femboys"
        lexer = GoonLexer(source)
        tokens = lexer.tokenize()
        
        self.assertEqual(len(tokens), 2)  # phrase + EOF
        self.assertEqual(tokens[0].type, TokenType.PRINT)
        self.assertEqual(tokens[1].type, TokenType.EOF)
    
    def test_number_tokenization(self):
        """Test number tokenization"""
        source = "i like 42 femboys"
        lexer = GoonLexer(source)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.NUMBER)
    
    def test_string_tokenization(self):
        """Test string literal tokenization"""
        source = '"i like femboys"'
        lexer = GoonLexer(source)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.STRING)
        self.assertEqual(tokens[0].value, "i like femboys")
    
    def test_comment_tokenization(self):
        """Test comment tokenization"""
        source = "// i like femboys comment"
        lexer = GoonLexer(source)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.COMMENT)
    
    def test_operator_tokenization(self):
        """Test operator tokenization"""
        operators = [
            ("i like femboys+", TokenType.ADD),
            ("i like femboys-", TokenType.SUBTRACT),
            ("i like femboys*", TokenType.MULTIPLY),
            ("i like femboys/", TokenType.DIVIDE),
            ("i like femboys==", TokenType.EQUALS),
            ("i like femboys!=", TokenType.NOT_EQUALS),
        ]
        
        for source, expected_type in operators:
            with self.subTest(source=source):
                lexer = GoonLexer(source)
                tokens = lexer.tokenize()
                self.assertEqual(tokens[0].type, expected_type)


class TestGoonParser(unittest.TestCase):
    """Test the GoonLang parser"""
    
    def test_literal_parsing(self):
        """Test parsing literal values"""
        source = "42"
        lexer = GoonLexer(source)
        tokens = lexer.tokenize()
        parser = GoonParser(tokens)
        ast = parser.parse()
        
        self.assertEqual(len(ast), 1)
        self.assertIsInstance(ast[0], LiteralNode)
        self.assertEqual(ast[0].value.value, 42.0)
        self.assertEqual(ast[0].value.type, GoonType.NUMBER)
    
    def test_string_parsing(self):
        """Test parsing string literals"""
        source = '"hello world"'
        lexer = GoonLexer(source)
        tokens = lexer.tokenize()
        parser = GoonParser(tokens)
        ast = parser.parse()
        
        self.assertEqual(len(ast), 1)
        self.assertIsInstance(ast[0], LiteralNode)
        self.assertEqual(ast[0].value.value, "hello world")
        self.assertEqual(ast[0].value.type, GoonType.STRING)


class TestGoonInterpreter(unittest.TestCase):
    """Test the GoonLang interpreter"""
    
    def setUp(self):
        self.interpreter = GoonInterpreter()
    
    def test_literal_evaluation(self):
        """Test evaluating literal values"""
        node = LiteralNode(GoonValue(42, GoonType.NUMBER))
        result = self.interpreter.execute(node)
        
        self.assertEqual(result.value, 42)
        self.assertEqual(result.type, GoonType.NUMBER)
    
    def test_variable_assignment_and_retrieval(self):
        """Test variable operations"""
        # This would require implementing assignment nodes
        pass
    
    def test_arithmetic_operations(self):
        """Test arithmetic operations"""
        # This would require implementing binary operation nodes
        pass


class TestGoonLangIntegration(unittest.TestCase):
    """Integration tests for the complete GoonLang system"""
    
    def setUp(self):
        self.goonlang = GoonLang()
    
    def test_hello_world(self):
        """Test basic hello world program"""
        source = "i like femboys"
        result = self.goonlang.run(source)
        self.assertIn("Hello World", result)
    
    def test_shout_program(self):
        """Test shout program"""
        source = "I LIKE FEMBOYS"
        result = self.goonlang.run(source)
        self.assertIn("I LIKE FEMBOYS", result)
    
    def test_number_program(self):
        """Test number handling"""
        source = "i like 42 femboys"
        result = self.goonlang.run(source)
        # Result would depend on implementation
        self.assertIsInstance(result, str)
    
    def test_string_program(self):
        """Test string handling"""
        source = '"i like femboys string"'
        result = self.goonlang.run(source)
        self.assertIn("i like femboys string", result)
    
    def test_comment_program(self):
        """Test comment handling"""
        source = """
        // This is a comment
        i like femboys
        """
        result = self.goonlang.run(source)
        self.assertIn("Hello World", result)
    
    def test_multiline_program(self):
        """Test multiline programs"""
        source = """
        i like femboys
        I LIKE FEMBOYS
        "i like femboys test"
        """
        result = self.goonlang.run(source)
        lines = result.strip().split('\n')
        self.assertGreaterEqual(len(lines), 3)
    
    def test_error_handling(self):
        """Test error handling"""
        source = "invalid syntax here"
        result = self.goonlang.run(source)
        # Should handle gracefully without crashing
        self.assertIsInstance(result, str)


class TestGoonLangFeatures(unittest.TestCase):
    """Test advanced GoonLang features"""
    
    def setUp(self):
        self.goonlang = GoonLang()
    
    def test_function_definition(self):
        """Test function definition syntax"""
        source = "i like femboys:"
        result = self.goonlang.run(source)
        # Implementation dependent
        self.assertIsInstance(result, str)
    
    def test_function_call(self):
        """Test function call syntax"""
        source = "i like femboys()"
        result = self.goonlang.run(source)
        # Implementation dependent
        self.assertIsInstance(result, str)
    
    def test_variable_assignment(self):
        """Test variable assignment"""
        source = "i like femboys="
        result = self.goonlang.run(source)
        # Implementation dependent
        self.assertIsInstance(result, str)
    
    def test_variable_retrieval(self):
        """Test variable retrieval"""
        source = "i like femboys$"
        result = self.goonlang.run(source)
        # Implementation dependent
        self.assertIsInstance(result, str)
    
    def test_conditional_syntax(self):
        """Test conditional syntax"""
        source = "i like femboys??"
        result = self.goonlang.run(source)
        # Implementation dependent
        self.assertIsInstance(result, str)
    
    def test_loop_syntax(self):
        """Test loop syntax"""
        source = """
        i like femboys!!!
        i like femboys
        i like femboys???
        """
        result = self.goonlang.run(source)
        # Implementation dependent
        self.assertIsInstance(result, str)


class TestGoonLangStandardLibrary(unittest.TestCase):
    """Test GoonLang standard library functions"""
    
    def test_fibonacci_function(self):
        """Test Fibonacci function"""
        from goonlang import GoonStdLib
        
        result = GoonStdLib.fibonacci(10)
        self.assertEqual(result, 55)
    
    def test_prime_function(self):
        """Test prime checking function"""
        from goonlang import GoonStdLib
        
        self.assertTrue(GoonStdLib.is_prime(17))
        self.assertFalse(GoonStdLib.is_prime(16))
    
    def test_factorial_function(self):
        """Test factorial function"""
        from goonlang import GoonStdLib
        
        result = GoonStdLib.factorial(5)
        self.assertEqual(result, 120)


class TestGoonLangPerformance(unittest.TestCase):
    """Performance tests for GoonLang"""
    
    def test_large_program_performance(self):
        """Test performance with large programs"""
        goonlang = GoonLang()
        
        # Create a large program
        lines = ["i like femboys"] * 1000
        source = "\n".join(lines)
        
        import time
        start_time = time.time()
        result = goonlang.run(source)
        end_time = time.time()
        
        execution_time = end_time - start_time
        self.assertLess(execution_time, 5.0)  # Should complete in under 5 seconds
        self.assertIsInstance(result, str)
    
    def test_recursive_performance(self):
        """Test performance with recursive operations"""
        # This would test recursive function calls
        pass


class TestGoonLangEdgeCases(unittest.TestCase):
    """Test edge cases and error conditions"""
    
    def setUp(self):
        self.goonlang = GoonLang()
    
    def test_empty_program(self):
        """Test empty program"""
        result = self.goonlang.run("")
        self.assertEqual(result.strip(), "")
    
    def test_whitespace_only_program(self):
        """Test program with only whitespace"""
        result = self.goonlang.run("   \n\t\n   ")
        self.assertEqual(result.strip(), "")
    
    def test_invalid_syntax(self):
        """Test invalid syntax handling"""
        result = self.goonlang.run("this is not valid goonlang")
        # Should not crash
        self.assertIsInstance(result, str)
    
    def test_unicode_handling(self):
        """Test Unicode character handling"""
        source = '"i like femboys 🏳️‍⚧️"'
        result = self.goonlang.run(source)
        self.assertIn("🏳️‍⚧️", result)


if __name__ == '__main__':
    # Run all tests
    unittest.main(verbosity=2)
