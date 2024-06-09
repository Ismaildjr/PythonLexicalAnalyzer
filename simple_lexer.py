import ply.lex as lex

# List of token names
tokens = ("OB", "CB", "COMMA", "CST")

# Define the regular expressions for the tokens
t_OB = r"\["
t_CB = r"\]"
t_COMMA = r","
t_CST = r"[0-9]+"

# Ignore spaces and tabs
t_ignore = " \t"

# Define the error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)

# Create the lexer
lexer = lex.lex()

# Provide input to the lexer
lexer.input("[1 2 4,5 6 753]")

# Tokenize the input string
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
