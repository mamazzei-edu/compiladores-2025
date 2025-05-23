# scanner_me.py
# Scanner simples em Python com máquina de estados
# Tipos de tokens
TOKEN_TYPES = {
    "IDENTIFIER": "IDENTIFIER",  # Identificador
    "INTEGER": "INTEGER",  # Número inteiro
    "LPAREN": "(",  # Abre parênteses
    "RPAREN": ")",  # Fecha parênteses
    "PLUS": "+",  # Operador de adição
    "MINUS": "‐",  # Operador de subtração
    "MULTIPLY": "*",  # Operador de multiplicação
    "DIVIDE": "/",  # Operador de divisão
    "EQUALS": "=",  # Operador de atribuição
}

# Estados da máquina de estado
START = "START"  # estado inicial
IN_IDENTIFIER = "IN_IDENTIFIER"  # em identificador
IN_NUMBER = "IN_NUMBER"  # em número
IN_SYMBOL = "IN_SYMBOL"  # em símbolo
ERROR = "ERROR"
# Variáveis globais para criar tokens
char_buffer = ""  # armazena uma palavra em formação
current_char = ""  # armazena o caratere lido (lookahead)
state = ""  # armazena o estado atual
pos = 0  # armazena a posição na entrada
tokens = []  # armazerna os tokens reconhecidos


def get_key_by_value(dictionary, value):
    """
    Retorna a chave correspondente ao valor no dicionário.
    Se o valor não for encontrado , retorna None.
    """
    for key, val in dictionary.items():
        if val == value:
            return key
    return None


def ACTION_GET_STR():
    """
    Função de ação usada para armazenar uma palavra reconhecida
    de modo incremental
    """
    # variáveis globais utilizadas
    global char_buffer
    global current_char
    # acumula a palavra no buffer
    char_buffer += current_char


def ACTION_MAKE_TOKEN():
    """
    Função de ação usada para retornar um token reconecido
    a partir de uma palavra no buffer
    """
    global char_buffer
    global state
    global tokens
    global TOKEN_TYPES
    if char_buffer != "":
        if state == IN_IDENTIFIER:
            token_type = "IDENTIFIER"
        elif state == IN_NUMBER:
            token_type = "NUMBER"
        else:
            token_type = get_key_by_value(TOKEN_TYPES, char_buffer)
        tokens.append({"type": token_type, "value": char_buffer})
        char_buffer = ""


def ACTION_PUSH_BACK():
    """
    Função de ação usada para devolver para a entrada um
    caractere que foi lido a mais para poder reconhecer
    uma palavra que havia antes dele
    """
    global pos
    # antes de voltar na entrada , crie o token
    # que está no buffer
    ACTION_MAKE_TOKEN()
    # volta uma posição na entrada
    pos -= 1


def ACTION_ERROR():
    """
    Função de ação usada para notificar erros detectados
    durante o processamento dos estados
    """
    global char_buffer
    global state
    global current_char
    raise Exception(
        "Caractere inválido: " + current_char + " em " + state + ": " + char_buffer
    )


#  Tabela de tansição de estados
# O par (ESTADO,SÍMBOLO) mapeia par (PRÓXIMO ESTADO, AÇÃO)
TRANSITION_TABLE = {
    (START, "LETTER"): (IN_IDENTIFIER, ACTION_GET_STR),
    (START, "DIGIT"): (IN_NUMBER, ACTION_GET_STR),
    (START, "SYMBOL"): (IN_SYMBOL, ACTION_GET_STR),
    (START, "SPACE"): (START, None),
    (IN_IDENTIFIER, "LETTER"): (IN_IDENTIFIER, ACTION_GET_STR),
    (IN_IDENTIFIER, "DIGIT"): (IN_IDENTIFIER, ACTION_GET_STR),
    (IN_IDENTIFIER, "SYMBOL"): (START, ACTION_PUSH_BACK),
    (IN_IDENTIFIER, "SPACE"): (START, ACTION_MAKE_TOKEN),
    (IN_NUMBER, "LETTER"): (ERROR, ACTION_ERROR),
    (IN_NUMBER, "DIGIT"): (IN_NUMBER, ACTION_GET_STR),
    (IN_NUMBER, "SYMBOL"): (START, ACTION_PUSH_BACK),
    (IN_NUMBER, "SPACE"): (START, ACTION_MAKE_TOKEN),
    (IN_SYMBOL, "LETTER"): (START, ACTION_PUSH_BACK),
    (IN_SYMBOL, "DIGIT"): (START, ACTION_PUSH_BACK),
    (IN_SYMBOL, "SYMBOL"): (START, ACTION_PUSH_BACK),
    (IN_SYMBOL, "SPACE"): (START, ACTION_MAKE_TOKEN),
    (ERROR, "LETTER"): (ERROR, ACTION_ERROR),
    (ERROR, "DIGIT"): (ERROR, ACTION_ERROR),
    (ERROR, "SYMBOL"): (ERROR, ACTION_ERROR),
    (ERROR, "SPACE"): (ERROR, ACTION_ERROR),
}

def get_char_type(char):
    """
    Retorna o tipo do caractere (LETTER, DIGIT, SYMBOL, SPACE).
    """
    if char.isalpha():
        return 'LETTER' 
    elif char.isdigit ():
        return 'DIGIT'
    elif char in {'(', ')', '+', '‐', '*', '/', '='}:
        return 'SYMBOL'
    elif char.isspace():
        return 'SPACE'
    else:
        raise ValueError(
            f"Caractere inesperado na posição {pos}: {char}")


def tokenize(code):
    '''Esta função lê um caractere por vez e determina , com a tabela de estados (TRANSITION_TABLE), determina o
    próximo estado e qual a ação a executar antes de transitar para o próximo estado '''
    global current_char , char_buffer , state, pos, tokens
    # primeira posição da cadeia
    pos = 0
    # estado inicial
    state = START
    # enquanto não alcançar o fim da cadeia
    while pos < len(code):
        # pega o caractere na posição atual
        current_char = code[pos]
        # determina o próximo estado e a ação a executar
        next_state , action = TRANSITION_TABLE[state, get_char_type(current_char)]
        # executar ação correspondente (se existir)
        if action:
            action()
        # avança para o próximo estado
        state = next_state
        # incrementa para a próxima posição da entrada
        pos += 1
    # Depois de varrer toda a entrada , descarrega o último token que estiver no buffer de caracteres
    ACTION_MAKE_TOKEN()
    # retorna a lista de tokens
    return tokens

# Exemplo de uso
if __name__ == '__main__':
    code = "tempC = 5*(tempF ‐ 32)/9"
    tokens = tokenize(code)
    for token in tokens:
        print(token)
