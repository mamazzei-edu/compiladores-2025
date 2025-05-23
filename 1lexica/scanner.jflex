/**
* Analisador léxico para expressões aritméticas
* 
*/
%%
%class Scanner
%type Token
%unicode
%debug
%standalone
%line
%column
%{
// Código Java que será incluído na classe gerada
// Classe pra representar tokens
public class Token {
    public String type;
    public String value;
    public Token(String type, String value) {
        this.type = type;
        this.value = value;
    }
    @Override
        public String toString() {
        return "Token [tipo=" + type + ", valor=" + value + "]";
        }
    }
%}
%eofval{
    return new Token("FIM_ARQUIVO", "‐1");
%eofval}
%eof{
    System.out.println("Análise léxica terminada com sucesso!");
%eof}
// Definições de padrões (expressões regulares)
DIGIT = [0‐9]
LETTER = [a‐zA‐Z]
IDENTIFIER = {LETTER}({LETTER}|{DIGIT})*
NUMBER = {DIGIT}+
SPACE = [ \t\n\r]+
// Definições de padrões (expressões regulares)
DIGIT = [0‐9]
LETTER = [a‐zA‐Z]
IDENTIFIER = {LETTER}({LETTER}|{DIGIT})*
NUMBER = {DIGIT}+
SPACE = [ \t\n\r]+
// Regras léxicas
%%
/* Regras e ações */
{SPACE} { /* Ignorar espaços em branco, tabulações e novas linhas */ }
{IDENTIFIER} { return new Token("IDENTIFIER", yytext()); }
{NUMBER} { return new Token("NUMBER", yytext()); }
"+" { return new Token("PLUS", yytext()); }
"-" { return new Token("MINUS", yytext()); }
"*" { return new Token("MULTIPLIER", yytext()); }
"/" { return new Token("DIVISION", yytext()); }
"=" { return new Token("ATRIB", yytext()); }
"(" { return new Token("LEFT_PAR", yytext()); }
")" { return new Token("RIGHT_PAR", yytext()); }
/* Qualquer outro ‐ gerar erro */
. { throw new Error("Caractere ilegal :" + yytext()) ; }
