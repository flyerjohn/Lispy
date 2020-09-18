# Type Definitions
Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Env = dict
Exp = (Atom, List)


def tokenize(chars: str) -> list: #converts a string of characters into a list of tokens.
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parser(program: str) -> Exp: # read a Scheme expression from a string.
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list) -> Exp: # read an expression from a sequence of tokens.
    if len(tokens) == 0:
        raise SyntaxError("unexpected EOF")
    
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop ) off
        return L
    elif token == ')':
        raise SyntaxError("unexpected )")
    else:
        return atom(token)

def atom(token: str) -> Atom: # numbers become numbers and every other token is a symbol
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)


a = "(begin (define r 10) (* pi (* r r)))"
print(parser(a))