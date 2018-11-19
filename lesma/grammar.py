# Operators
PLUS = '+'
MINUS = '-'
MUL = '*'
DIV = '/'
FLOORDIV = '//'
MOD = '%'
POWER = '^'
ARITHMATIC_LEFT_SHIFT = '<<<'  # TODO
ARITHMATIC_RIGHT_SHIFT = '>>>'  # TODO
XOR = 'xor'
BINARY_ONES_COMPLIMENT = '~'  # TODO
BINARY_LEFT_SHIFT = '<<'  # TODO
BINARY_RIGHT_SHIFT = '>>'  # TODO
AND = 'and'
OR = 'or'
NOT = 'not'
IN = 'in'  # TODO
NOT_IN = 'not in'  # TODO
IS = 'is'  # TODO
IS_NOT = 'is not'  # TODO
LPAREN = '('
RPAREN = ')'
LSQUAREBRACKET = '['
RSQUAREBRACKET = ']'
LCURLYBRACKET = '{'
RCURLYBRACKET = '}'
COMMA = ','
COLON = ':'
DOT = '.'
RANGE = '..'
ELLIPSIS = '...'  # TODO
ARROW = '->'
CAST = '::'
ASSIGN = '='
PLUS_ASSIGN = '+='
MINUS_ASSIGN = '-='
MUL_ASSIGN = '*='
DIV_ASSIGN = '/='
FLOORDIV_ASSIGN = '//='
MOD_ASSIGN = '%='
POWER_ASSIGN = '^='
EQUALS = '=='
NOT_BANG = '!'
NOT_EQUALS = '!='
LESS_THAN = '<'
GREATER_THAN = '>'
LESS_THAN_OR_EQUAL_TO = '<='
GREATER_THAN_OR_EQUAL_TO = '>='
DECORATOR = '@'  # TODO

# Types
ANY = 'any'
INT = 'int'
INT8 = 'int8'
INT16 = 'int16'
INT32 = 'int32'
INT64 = 'int64'  # same as int but doesn't automatically promote to larger integer type upon overflow
INT128 = 'int128'
UINT = 'uint' # TODO
UINT8 = 'uint8' # TODO
UINT16 = 'uint16' # TODO
UINT32 = 'uint32' # TODO
UINT64 = 'uint64'  # TODO
UINT128 = 'uint128' # TODO
DEC = 'dec'
FLOAT = 'float'
COMPLEX = 'complex'  # TODO
STR = 'str'
BOOL = 'bool'
BYTES = 'bytes'  # TODO
ARRAY = 'array'
LIST = 'list'
SET = 'set'  # TODO
DICT = 'dict'
ENUM = 'enum'  # TODO
FUNC = 'func'
STRUCT = 'struct'
CLASS = 'class'

# Contstants
TRUE = 'true'
FALSE = 'false'
NULL = 'null' # TODO

# Keywords
IF = 'if'
ELSE_IF = 'else if'
ELSE = 'else'
FOR = 'for'
WHILE = 'while'
SWITCH = 'switch'
CASE = 'case'
DEFAULT = 'default'
DEF = 'def'
CONST = 'const'
NEW = 'new'  # TODO
SUPER = 'super'  # TODO
THIS = 'this'  # TODO
RETURN = 'return'
TRY = 'try'  # TODO
CATCH = 'catch'  # TODO
THROW = 'throw'  # TODO
FINALLY = 'finally'  # TODO
YIELD = 'yield'  # TODO
BREAK = 'break'
CONTINUE = 'continue'
DEL = 'del'  # TODO
FROM = 'from'  # TODO
IMPORT = 'import'  # TODO
WILDCARD = '*'  # TODO
WITH = 'with'  # TODO
AS = 'as'  # TODO
PASS = 'pass'
VOID = 'void'
ALIAS = 'alias'
OVERRIDE = 'override'  # TODO
ABSTRACT = 'abstract'  # TODO
ASSERT = 'assert'  # TODO

ARITHMETIC_OP = (PLUS, MINUS, MUL, DIV, MOD, FLOORDIV, POWER, ARITHMATIC_LEFT_SHIFT, ARITHMATIC_RIGHT_SHIFT)

ASSIGNMENT_OP = (ASSIGN, PLUS_ASSIGN, MINUS_ASSIGN, MUL_ASSIGN, DIV_ASSIGN, FLOORDIV_ASSIGN, MOD_ASSIGN, POWER_ASSIGN)

ARITHMETIC_ASSIGNMENT_OP = (PLUS_ASSIGN, MINUS_ASSIGN, MUL_ASSIGN, DIV_ASSIGN, FLOORDIV_ASSIGN, MOD_ASSIGN, POWER_ASSIGN)

COMPARISON_OP = (EQUALS, NOT_BANG, NOT_EQUALS, LESS_THAN, GREATER_THAN, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO)

LOGICAL_OP = (AND, OR, NOT)

BINARY_OP = (XOR, BINARY_ONES_COMPLIMENT, BINARY_LEFT_SHIFT, BINARY_RIGHT_SHIFT)

MEMBERSHIP_OP = (IN, NOT_IN)

IDENTITY_OP = (IS, IS_NOT)

MULTI_WORD_OPERATORS = (IS, IS_NOT, IN, NOT_IN, NOT)

OPERATORS = (
	LPAREN, RPAREN, LSQUAREBRACKET, RSQUAREBRACKET, LCURLYBRACKET, RCURLYBRACKET,
	ARROW, COMMA, COLON, DOT, DECORATOR, CAST, RANGE, ELLIPSIS,
) + ARITHMETIC_OP + ASSIGNMENT_OP + COMPARISON_OP + LOGICAL_OP + BINARY_OP + MEMBERSHIP_OP + IDENTITY_OP

SINGLE_OPERATORS = (
	LPAREN, RPAREN, LSQUAREBRACKET, RSQUAREBRACKET, LCURLYBRACKET, RCURLYBRACKET,
	BINARY_ONES_COMPLIMENT, COMMA, DECORATOR
)

KEYWORDS = (
	IF, ELSE, WHILE, FOR, SWITCH, CASE, DEF, SUPER, THIS, RETURN, TRY, CATCH, THROW,
	FINALLY, YIELD, BREAK, CONTINUE, DEL, IMPORT, FROM, WITH, AS, PASS, VOID,
	CONST, OVERRIDE, ABSTRACT, ASSERT, DEFAULT, NEW, ALIAS
)

MULTI_WORD_KEYWORDS = (IF, ELSE, ELSE_IF)

TYPES = (ANY, INT, INT8, INT16, INT32, INT64, INT128, DEC, FLOAT, COMPLEX, STR, BOOL, BYTES, ARRAY, LIST, DICT, ENUM, FUNC, STRUCT, CLASS)

CONSTANTS = (TRUE, FALSE, NULL)

PRINT = 'print'
INPUT = 'input'

BUILTIN_FUNCTIONS = (PRINT, INPUT)

# For Lexer
TYPE = 'TYPE'
NUMBER = 'NUMBER'
STRING = 'STRING'
OP = 'OP'
CONSTANT = 'CONSTANT'
NEWLINE = 'NEWLINE'
INDENT = 'INDENT'
KEYWORD = 'KEYWORD'
ANON = 'ANON'
NAME = 'NAME'
EOF = 'EOF'
ALPHANUMERIC = 'alphanumeric'
NUMERIC = 'numeric'
OPERATIC = 'operatic'
WHITESPACE = 'whitespace'
COMMENT = 'comment'
ESCAPE = 'escape'
