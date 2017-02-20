""" Python 'mazovia' Codec

Written by gta5700@gmail.com

Mazovia encoding is used under DOS to represent Polish texts.

https://en.wikipedia.org/wiki/Mazovia_encoding

NO WARRANTY.

"""

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_table)

    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input,self.errors,encoding_table)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input,self.errors,decoding_table)[0]

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

def getregentry():
    return codecs.CodecInfo(
        name='mazovia',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


### Decoding Table
decoding_table = (
    u'\x00'  # 0x0000 -> NULL
    u'\x01'  # 0x0001 -> START OF HEADING
    u'\x02'  # 0x0002 -> START OF TEXT
    u'\x03'  # 0x0003 -> END OF TEXT
    u'\x04'  # 0x0004 -> END OF TRANSMISSION
    u'\x05'  # 0x0005 -> ENQUIRY
    u'\x06'  # 0x0006 -> ACKNOWLEDGE
    u'\x07'  # 0x0007 -> BELL
    u'\x08'  # 0x0008 -> BACKSPACE
    u'\t'  # 0x0009 -> HORIZONTAL TABULATION
    u'\n'  # 0x000a -> LINE FEED
    u'\x0b'  # 0x000b -> VERTICAL TABULATION
    u'\x0c'  # 0x000c -> FORM FEED
    u'\r'  # 0x000d -> CARRIAGE RETURN
    u'\x0e'  # 0x000e -> SHIFT OUT
    u'\x0f'  # 0x000f -> SHIFT IN
    u'\x10'  # 0x0010 -> DATA LINK ESCAPE
    u'\x11'  # 0x0011 -> DEVICE CONTROL ONE
    u'\x12'  # 0x0012 -> DEVICE CONTROL TWO
    u'\x13'  # 0x0013 -> DEVICE CONTROL THREE
    u'\x14'  # 0x0014 -> DEVICE CONTROL FOUR
    u'\x15'  # 0x0015 -> NEGATIVE ACKNOWLEDGE
    u'\x16'  # 0x0016 -> SYNCHRONOUS IDLE
    u'\x17'  # 0x0017 -> END OF TRANSMISSION BLOCK
    u'\x18'  # 0x0018 -> CANCEL
    u'\x19'  # 0x0019 -> END OF MEDIUM
    u'\x1a'  # 0x001a -> SUBSTITUTE
    u'\x1b'  # 0x001b -> ESCAPE
    u'\x1c'  # 0x001c -> FILE SEPARATOR
    u'\x1d'  # 0x001d -> GROUP SEPARATOR
    u'\x1e'  # 0x001e -> RECORD SEPARATOR
    u'\x1f'  # 0x001f -> UNIT SEPARATOR
    u' '  # 0x0020 -> SPACE
    u'!'  # 0x0021 -> EXCLAMATION MARK
    u'"'  # 0x0022 -> QUOTATION MARK
    u'#'  # 0x0023 -> NUMBER SIGN
    u'$'  # 0x0024 -> DOLLAR SIGN
    u'%'  # 0x0025 -> PERCENT SIGN
    u'&'  # 0x0026 -> AMPERSAND
    u"'"  # 0x0027 -> APOSTROPHE
    u'('  # 0x0028 -> LEFT PARENTHESIS
    u')'  # 0x0029 -> RIGHT PARENTHESIS
    u'*'  # 0x002a -> ASTERISK
    u'+'  # 0x002b -> PLUS SIGN
    u','  # 0x002c -> COMMA
    u'-'  # 0x002d -> HYPHEN-MINUS
    u'.'  # 0x002e -> FULL STOP
    u'/'  # 0x002f -> SOLIDUS
    u'0'  # 0x0030 -> DIGIT ZERO
    u'1'  # 0x0031 -> DIGIT ONE
    u'2'  # 0x0032 -> DIGIT TWO
    u'3'  # 0x0033 -> DIGIT THREE
    u'4'  # 0x0034 -> DIGIT FOUR
    u'5'  # 0x0035 -> DIGIT FIVE
    u'6'  # 0x0036 -> DIGIT SIX
    u'7'  # 0x0037 -> DIGIT SEVEN
    u'8'  # 0x0038 -> DIGIT EIGHT
    u'9'  # 0x0039 -> DIGIT NINE
    u':'  # 0x003a -> COLON
    u';'  # 0x003b -> SEMICOLON
    u'<'  # 0x003c -> LESS-THAN SIGN
    u'='  # 0x003d -> EQUALS SIGN
    u'>'  # 0x003e -> GREATER-THAN SIGN
    u'?'  # 0x003f -> QUESTION MARK
    u'@'  # 0x0040 -> COMMERCIAL AT
    u'A'  # 0x0041 -> LATIN CAPITAL LETTER A
    u'B'  # 0x0042 -> LATIN CAPITAL LETTER B
    u'C'  # 0x0043 -> LATIN CAPITAL LETTER C
    u'D'  # 0x0044 -> LATIN CAPITAL LETTER D
    u'E'  # 0x0045 -> LATIN CAPITAL LETTER E
    u'F'  # 0x0046 -> LATIN CAPITAL LETTER F
    u'G'  # 0x0047 -> LATIN CAPITAL LETTER G
    u'H'  # 0x0048 -> LATIN CAPITAL LETTER H
    u'I'  # 0x0049 -> LATIN CAPITAL LETTER I
    u'J'  # 0x004a -> LATIN CAPITAL LETTER J
    u'K'  # 0x004b -> LATIN CAPITAL LETTER K
    u'L'  # 0x004c -> LATIN CAPITAL LETTER L
    u'M'  # 0x004d -> LATIN CAPITAL LETTER M
    u'N'  # 0x004e -> LATIN CAPITAL LETTER N
    u'O'  # 0x004f -> LATIN CAPITAL LETTER O
    u'P'  # 0x0050 -> LATIN CAPITAL LETTER P
    u'Q'  # 0x0051 -> LATIN CAPITAL LETTER Q
    u'R'  # 0x0052 -> LATIN CAPITAL LETTER R
    u'S'  # 0x0053 -> LATIN CAPITAL LETTER S
    u'T'  # 0x0054 -> LATIN CAPITAL LETTER T
    u'U'  # 0x0055 -> LATIN CAPITAL LETTER U
    u'V'  # 0x0056 -> LATIN CAPITAL LETTER V
    u'W'  # 0x0057 -> LATIN CAPITAL LETTER W
    u'X'  # 0x0058 -> LATIN CAPITAL LETTER X
    u'Y'  # 0x0059 -> LATIN CAPITAL LETTER Y
    u'Z'  # 0x005a -> LATIN CAPITAL LETTER Z
    u'['  # 0x005b -> LEFT SQUARE BRACKET
    u'\\'  # 0x005c -> REVERSE SOLIDUS
    u']'  # 0x005d -> RIGHT SQUARE BRACKET
    u'^'  # 0x005e -> CIRCUMFLEX ACCENT
    u'_'  # 0x005f -> LOW LINE
    u'`'  # 0x0060 -> GRAVE ACCENT
    u'a'  # 0x0061 -> LATIN SMALL LETTER A
    u'b'  # 0x0062 -> LATIN SMALL LETTER B
    u'c'  # 0x0063 -> LATIN SMALL LETTER C
    u'd'  # 0x0064 -> LATIN SMALL LETTER D
    u'e'  # 0x0065 -> LATIN SMALL LETTER E
    u'f'  # 0x0066 -> LATIN SMALL LETTER F
    u'g'  # 0x0067 -> LATIN SMALL LETTER G
    u'h'  # 0x0068 -> LATIN SMALL LETTER H
    u'i'  # 0x0069 -> LATIN SMALL LETTER I
    u'j'  # 0x006a -> LATIN SMALL LETTER J
    u'k'  # 0x006b -> LATIN SMALL LETTER K
    u'l'  # 0x006c -> LATIN SMALL LETTER L
    u'm'  # 0x006d -> LATIN SMALL LETTER M
    u'n'  # 0x006e -> LATIN SMALL LETTER N
    u'o'  # 0x006f -> LATIN SMALL LETTER O
    u'p'  # 0x0070 -> LATIN SMALL LETTER P
    u'q'  # 0x0071 -> LATIN SMALL LETTER Q
    u'r'  # 0x0072 -> LATIN SMALL LETTER R
    u's'  # 0x0073 -> LATIN SMALL LETTER S
    u't'  # 0x0074 -> LATIN SMALL LETTER T
    u'u'  # 0x0075 -> LATIN SMALL LETTER U
    u'v'  # 0x0076 -> LATIN SMALL LETTER V
    u'w'  # 0x0077 -> LATIN SMALL LETTER W
    u'x'  # 0x0078 -> LATIN SMALL LETTER X
    u'y'  # 0x0079 -> LATIN SMALL LETTER Y
    u'z'  # 0x007a -> LATIN SMALL LETTER Z
    u'{'  # 0x007b -> LEFT CURLY BRACKET
    u'|'  # 0x007c -> VERTICAL LINE
    u'}'  # 0x007d -> RIGHT CURLY BRACKET
    u'~'  # 0x007e -> TILDE
    u'\x7f'  # 0x007f -> DELETE

    u'\x00C7'  # 0x0080  ->  LATIN CAPITAL LETTER C WITH CEDILLA
    u'\x00FC'  # 0x0081  ->  LATIN SMALL LETTER U WITH DIAERESIS
    u'\x00E9'  # 0x0082  ->  LATIN SMALL LETTER E WITH ACUTE
    u'\x00E2'  # 0x0083  ->  LATIN SMALL LETTER A WITH CIRCUMFLEX
    u'\x00E4'  # 0x0084  ->  LATIN SMALL LETTER A WITH DIAERESIS
    u'\x00E0'  # 0x0085  ->  LATIN SMALL LETTER A WITH GRAVE
    u'\x0105'  # 0x0086  ->  LATIN SMALL LETTER A WITH OGONEK
    u'\x00E7'  # 0x0087  ->  LATIN SMALL LETTER C WITH CEDILLA
    u'\x00EA'  # 0x0088  ->  LATIN SMALL LETTER E WITH CIRCUMFLEX
    u'\x00EB'  # 0x0089  ->  LATIN SMALL LETTER E WITH DIAERESIS
    u'\x00E8'  # 0x008A  ->  LATIN SMALL LETTER E WITH GRAVE
    u'\x00EF'  # 0x008B  ->  LATIN SMALL LETTER I WITH DIAERESIS
    u'\x00EE'  # 0x008C  ->  LATIN SMALL LETTER I WITH CIRCUMFLEX
    u'\x0107'  # 0x008D  ->  LATIN SMALL LETTER C WITH ACUTE
    u'\x00C4'  # 0x008E  ->  LATIN CAPITAL LETTER A WITH DIAERESIS
    u'\x0104'  # 0x008F  ->  LATIN CAPITAL LETTER A WITH OGONEK
    u'\x0118'  # 0x0090  ->  LATIN CAPITAL LETTER E WITH OGONEK
    u'\x0119'  # 0x0091  ->  LATIN SMALL LETTER E WITH OGONEK
    u'\x0142'  # 0x0092  ->  LATIN SMALL LETTER L WITH STROKE
    u'\x00F4'  # 0x0093  ->  LATIN SMALL LETTER O WITH CIRCUMFLEX
    u'\x00F6'  # 0x0094  ->  LATIN SMALL LETTER O WITH DIAERESIS
    u'\x0106'  # 0x0095  ->  LATIN CAPITAL LETTER C WITH ACUTE
    u'\x00FB'  # 0x0096  ->  LATIN SMALL LETTER U WITH CIRCUMFLEX
    u'\x00F9'  # 0x0097  ->  LATIN SMALL LETTER U WITH GRAVE
    u'\x015A'  # 0x0098  ->  LATIN CAPITAL LETTER S WITH ACUTE
    u'\x00D6'  # 0x0099  ->  LATIN CAPITAL LETTER O WITH DIAERESIS
    u'\x00DC'  # 0x009A  ->  LATIN CAPITAL LETTER U WITH DIAERESIS
    u'\x00A2'  # 0x009B  ->  CENT SIGN
    u'\x0141'  # 0x009C  ->  LATIN CAPITAL LETTER L WITH STROKE
    u'\x00A5'  # 0x009D  ->  YEN SIGN
    u'\x015B'  # 0x009E  ->  LATIN SMALL LETTER S WITH ACUTE
    u'\x0192'  # 0x009F  ->  LATIN SMALL LETTER F WITH HOOK
    u'\x0179'  # 0x00A0  ->  LATIN CAPITAL LETTER Z WITH ACUTE
    u'\x017B'  # 0x00A1  ->  LATIN CAPITAL LETTER Z WITH DOT ABOVE
    u'\x00F3'  # 0x00A2  ->  LATIN SMALL LETTER O WITH ACUTE
    u'\x00D3'  # 0x00A3  ->  LATIN CAPITAL LETTER O WITH ACUTE
    u'\x0144'  # 0x00A4  ->  LATIN SMALL LETTER N WITH ACUTE
    u'\x0143'  # 0x00A5  ->  LATIN CAPITAL LETTER N WITH ACUTE
    u'\x017A'  # 0x00A6  ->  LATIN SMALL LETTER Z WITH ACUTE
    u'\x017C'  # 0x00A7  ->  LATIN SMALL LETTER Z WITH DOT ABOVE
    u'\x00BF'  # 0x00A8  ->  INVERTED QUESTION MARK
    u'\x2310'  # 0x00A9  ->  REVERSED NOT SIGN
    u'\x00AC'  # 0x00AA  ->  NOT SIGN
    u'\x00BD'  # 0x00AB  ->  VULGAR FRACTION ONE HALF
    u'\x00BC'  # 0x00AC  ->  VULGAR FRACTION ONE QUARTER
    u'\x00A1'  # 0x00AD  ->  INVERTED EXCLAMATION MARK
    u'\x00AB'  # 0x00AE  ->  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\x00BB'  # 0x00AF  ->  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\x2591'  # 0x00B0  ->  LIGHT SHADE
    u'\x2592'  # 0x00B1  ->  MEDIUM SHADE
    u'\x2593'  # 0x00B2  ->  DARK SHADE
    u'\x2502'  # 0x00B3  ->  BOX DRAWINGS LIGHT VERTICAL
    u'\x2524'  # 0x00B4  ->  BOX DRAWINGS LIGHT VERTICAL AND LEFT
    u'\x2561'  # 0x00B5  ->  BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE
    u'\x2562'  # 0x00B6  ->  BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE
    u'\x2556'  # 0x00B7  ->  BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE
    u'\x2555'  # 0x00B8  ->  BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE
    u'\x2563'  # 0x00B9  ->  BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    u'\x2551'  # 0x00BA  ->  BOX DRAWINGS DOUBLE VERTICAL
    u'\x2557'  # 0x00BB  ->  BOX DRAWINGS DOUBLE DOWN AND LEFT
    u'\x255D'  # 0x00BC  ->  BOX DRAWINGS DOUBLE UP AND LEFT
    u'\x255C'  # 0x00BD  ->  BOX DRAWINGS UP DOUBLE AND LEFT SINGLE
    u'\x255B'  # 0x00BE  ->  BOX DRAWINGS UP SINGLE AND LEFT DOUBLE
    u'\x2510'  # 0x00BF  ->  BOX DRAWINGS LIGHT DOWN AND LEFT
    u'\x2514'  # 0x00C0  ->  BOX DRAWINGS LIGHT UP AND RIGHT
    u'\x2534'  # 0x00C1  ->  BOX DRAWINGS LIGHT UP AND HORIZONTAL
    u'\x252C'  # 0x00C2  ->  BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    u'\x251C'  # 0x00C3  ->  BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    u'\x2500'  # 0x00C4  ->  BOX DRAWINGS LIGHT HORIZONTAL
    u'\x253C'  # 0x00C5  ->  BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    u'\x255E'  # 0x00C6  ->  BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE
    u'\x255F'  # 0x00C7  ->  BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE
    u'\x255A'  # 0x00C8  ->  BOX DRAWINGS DOUBLE UP AND RIGHT
    u'\x2554'  # 0x00C9  ->  BOX DRAWINGS DOUBLE DOWN AND RIGHT
    u'\x2569'  # 0x00CA  ->  BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    u'\x2566'  # 0x00CB  ->  BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    u'\x2560'  # 0x00CC  ->  BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    u'\x2550'  # 0x00CD  ->  BOX DRAWINGS DOUBLE HORIZONTAL
    u'\x256C'  # 0x00CE  ->  BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    u'\x2567'  # 0x00CF  ->  BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE
    u'\x2568'  # 0x00D0  ->  BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE
    u'\x2564'  # 0x00D1  ->  BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE
    u'\x2565'  # 0x00D2  ->  BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE
    u'\x2559'  # 0x00D3  ->  BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE
    u'\x2558'  # 0x00D4  ->  BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE
    u'\x2552'  # 0x00D5  ->  BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE
    u'\x2553'  # 0x00D6  ->  BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE
    u'\x256B'  # 0x00D7  ->  BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE
    u'\x256A'  # 0x00D8  ->  BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE
    u'\x2518'  # 0x00D9  ->  BOX DRAWINGS LIGHT UP AND LEFT
    u'\x250C'  # 0x00DA  ->  BOX DRAWINGS LIGHT DOWN AND RIGHT
    u'\x2588'  # 0x00DB  ->  FULL BLOCK
    u'\x2584'  # 0x00DC  ->  LOWER HALF BLOCK
    u'\x258C'  # 0x00DD  ->  LEFT HALF BLOCK
    u'\x2590'  # 0x00DE  ->  RIGHT HALF BLOCK
    u'\x2580'  # 0x00DF  ->  UPPER HALF BLOCK
    u'\x03B1'  # 0x00E0  ->  GREEK SMALL LETTER ALPHA
    u'\x00DF'  # 0x00E1  ->  LATIN SMALL LETTER SHARP S
    u'\x0393'  # 0x00E2  ->  GREEK CAPITAL LETTER GAMMA
    u'\x03C0'  # 0x00E3  ->  GREEK SMALL LETTER PI
    u'\x03A3'  # 0x00E4  ->  GREEK CAPITAL LETTER SIGMA
    u'\x03C3'  # 0x00E5  ->  GREEK SMALL LETTER SIGMA
    u'\x00B5'  # 0x00E6  ->  MICRO SIGN
    u'\x03C4'  # 0x00E7  ->  GREEK SMALL LETTER TAU
    u'\x03A6'  # 0x00E8  ->  GREEK CAPITAL LETTER PHI
    u'\x0398'  # 0x00E9  ->  GREEK CAPITAL LETTER THETA
    u'\x03A9'  # 0x00EA  ->  GREEK CAPITAL LETTER OMEGA
    u'\x03B4'  # 0x00EB  ->  GREEK SMALL LETTER DELTA
    u'\x221E'  # 0x00EC  ->  INFINITY
    u'\x03C6'  # 0x00ED  ->  GREEK SMALL LETTER PHI
    u'\x03B5'  # 0x00EE  ->  GREEK SMALL LETTER EPSILON
    u'\x2229'  # 0x00EF  ->  INTERSECTION
    u'\x2261'  # 0x00F0  ->  IDENTICAL TO
    u'\x00B1'  # 0x00F1  ->  PLUS-MINUS SIGN
    u'\x2265'  # 0x00F2  ->  GREATER-THAN OR EQUAL TO
    u'\x2264'  # 0x00F3  ->  LESS-THAN OR EQUAL TO
    u'\x2320'  # 0x00F4  ->  TOP HALF INTEGRAL
    u'\x2321'  # 0x00F5  ->  BOTTOM HALF INTEGRAL
    u'\x00F7'  # 0x00F6  ->  DIVISION SIGN
    u'\x2248'  # 0x00F7  ->  ALMOST EQUAL TO
    u'\x00B0'  # 0x00F8  ->  DEGREE SIGN
    u'\x2219'  # 0x00F9  ->  BULLET OPERATOR
    u'\x00B7'  # 0x00FA  ->  MIDDLE DOT
    u'\x221A'  # 0x00FB  ->  SQUARE ROOT
    u'\x207F'  # 0x00FC  ->  SUPERSCRIPT LATIN SMALL LETTER N
    u'\x00B2'  # 0x00FD  ->  SUPERSCRIPT TWO
    u'\x25A0'  # 0x00FE  ->  BLACK SQUARE
    u'\x00A0'  # 0x00FF  ->  NO-BREAK SPACE
)

### Encoding table
encoding_table=codecs.charmap_build(decoding_table)
