import ply.lex as lex

# Define token names
tokens = (
    'INT',
    'BOOLEAN',
    'IF',
    'ELSE',
    'WHILE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'ID',
    'ASSIGN',
    'EQ',
    'NEQ',
    'TRUE',
    'FALSE',
    'COMMA',    
    'QUOTE',    
    'POINT',
    'LCURLY',  
    'RCURLY',   
    'PCOMMA',  
    'EXCLAMATION'  
)

# Regular expressions for token patterns
t_INT = r'int'
t_BOOLEAN = r'boolean'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_EQ = r'=='
t_NEQ = r'!='
t_TRUE = r'true'
t_FALSE = r'false'
t_COMMA = r','   
t_QUOTE = r"'"   
t_POINT = r'\.'
t_LCURLY = r'\{'  
t_RCURLY = r'\}' 
t_PCOMMA = r';'   
t_EXCLAMATION = r'!' 
# Token definitions for numbers and identifiers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t

# Ignore whitespace characters
t_ignore = ' \t\n'

# Define the error handling rule
def t_error(t):
    print(f"WARNING: No t_error rule is defined! Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)

# Create the lexer
lexer = lex.lex()

# Input text to be tokenized
input_text = "int x = 42; if (x == 42)  System.out.println('Hello, World!'); "

# Provide input to the lexer
lexer.input(input_text)

# Tokenize the input string and print tokens
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
