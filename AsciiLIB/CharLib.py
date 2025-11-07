"""
AsciiLIB.CharLib module
Provides a centralized collection of Unicode glyphs commonly used for
terminal/console UIs, ASCII/box drawing, simple graphical elements in
text-based games, and related utilities.
Contents
- CharLib (dict): Top-level mapping from category name (str) to a mapping
    of symbol name -> character. Typical categories include:
        - "MAIN": Basic block and shape glyphs (blocks, squares, circles,
            triangles, shading characters).
        - "PIPE_ASCII": Simple ASCII fallbacks for box drawing (e.g. '-', '|',
            '/', '\\', '+').
        - "PIPE_EXTENDED": Extended box/pipe drawing characters (single, heavy,
            double, rounded variants and crosses).
        - "PIPE_BLOCKS": Quarter/half/full block glyphs for finer-grained
            block graphics.
        - "PIPE_EXTRAS": Additional line/edge/endpoint glyphs.
        - "DOTS": Ellipses, middot, bullet characters.
        - "ARROWS": Single and double arrow glyphs in multiple directions.
        - "BRAILLE": Programmatically generated mapping of integer indices to
            Unicode Braille Pattern characters (U+2800 + index). Keys for this
            sub-dictionary are integers (1..255) and values are the corresponding
            braille Unicode characters.
Usage examples
- Access a glyph by category and name:
        block = CharLib["MAIN"]["BLOCK"]
- Iterate categories and glyphs:
        for category, glyphs in CharLib.items():
                for name, ch in glyphs.items():
                        print(category, name, ch)
- Use braille patterns:
        braille_dot = CharLib["BRAILLE"][1]  # U+2801 (0x2800 + 1)
Notes and considerations
- All glyphs are Unicode characters. Ensure your environment/terminal/font
    supports the desired Unicode glyphs (box drawing, braille, blocks) and
    that your source file and runtime use UTF-8 encoding.
- The BRAILLE mapping is generated from the Unicode braille block by
    adding an offset (0x2800). The implemented mapping starts at index 1
    (0x2801) and covers the higher pattern values; index semantics follow
    the module implementation.
- The module includes a small __main__ block that prints all categories
    and glyphs when executed as a script; the CharLib mapping itself is
    designed to be imported and used programmatically.
- This structure is intentionally simple and easily extensible: add new
    categories or glyphs by updating the CharLib dictionary.
Intended use
- Creating text-based user interfaces, box-drawn layouts, minimal graphical
    representations in terminal games, and other situations where consistent
    references to special characters are helpful.
"""

CharLib = {
    "MAIN": {
        "BLANK": " ",
        "LIGHT_SHADE": "░",
        "MEDIUM_SHADE": "▒",
        "DARK_SHADE": "▓",
        "BLOCK": "█",
        "SQUARE_BLACK": "■",
        "SQUARE_WHITE": "□",   
        "CIRCLE_BLACK": "●",
        "CIRCLE_WHITE": "○",
        "DIAMOND_BLACK": "◆",
        "DIAMOND_WHITE": "◇",
        "TRIANGLE_UP_BLACK": "▲",
        "TRIANGLE_UP_WHITE": "△",
        "TRIANGLE_DOWN_BLACK": "▼",
        "TRIANGLE_DOWN_WHITE": "▽",
        "TRIANGLE_LEFT_BLACK": "◀",
        "TRIANGLE_LEFT_WHITE": "◁",
        "TRIANGLE_RIGHT_BLACK": "▶",
        "TRIANGLE_RIGHT_WHITE": "▷",
    },
    
    "PIPE_ASCII":{
        "HORIZONTAL": "-",
        "VERTICAL": "|",
        "TOP_LEFT": "/",
        "TOP_RIGHT": "\\",
        "CROSS": "+"
    },

    "PIPE_EXTENDED": {
        "HORIZONTAL": "─",
        "VERTICAL": "│",
        "BOTTOM_LEFT_TURN": "┌",
        "BOTTOM_RIGHT_TURN": "┐",
        "TOP_LEFT_TURN": "└",
        "TOP_RIGHT_TURN": "┘",
        "T_UP": "┴",
        "T_DOWN": "┬",
        "T_LEFT": "┤",
        "T_RIGHT": "├",
        "CROSS": "┼",
        #------------------------#
        "HEAVY_HORIZONTAL": "━",
        "HEAVY_VERTICAL": "┃",
        "HEAVY_BOTTOM_LEFT_TURN": "┏",
        "HEAVY_BOTTOM_RIGHT_TURN": "┓",
        "HEAVY_TOP_LEFT_TURN": "┗",
        "HEAVY_TOP_RIGHT_TURN": "┛",
        "HEAVY_T_UP": "┻",
        "HEAVY_T_DOWN": "┳",
        "HEAVY_T_LEFT": "┫",
        "HEAVY_T_RIGHT": "┣",
        "HEAVY_CROSS": "╋",
        #------------------------#
        "DOUBLE_HORIZONTAL": "═",
        "DOUBLE_VERTICAL": "║",
        "DOUBLE_BOTTOM_LEFT_TURN": "╔",
        "DOUBLE_BOTTOM_RIGHT_TURN": "╗",
        "DOUBLE_TOP_LEFT_TURN": "╚",
        "DOUBLE_TOP_RIGHT_TURN": "╝",
        "DOUBLE_T_UP": "╩",
        "DOUBLE_T_DOWN": "╦",
        "DOUBLE_T_LEFT": "╣",
        "DOUBLE_T_RIGHT": "╠",
        "DOUBLE_CROSS": "╬",
        #------------------------#
        "ROUNDED_BOTTOM_LEFT_TURN": "╭",
        "ROUNDED_BOTTOM_RIGHT_TURN": "╮",
        "ROUNDED_TOP_LEFT_TURN": "╰",
        "ROUNDED_TOP_RIGHT_TURN": "╯",
        "ROUNDED_T_UP": "┴",
        "ROUNDED_T_DOWN": "┬",
        "ROUNDED_T_LEFT": "┤",
        "ROUNDED_T_RIGHT": "├",
        "ROUNDED_CROSS": "┼"
    },

    "PIPE_BLOCKS": {
        "FULL_BLOCK": "█",
        "LOWER_HALF_BLOCK": "▄",
        "UPPER_HALF_BLOCK": "▀",
        "LEFT_HALF_BLOCK": "▌",
        "RIGHT_HALF_BLOCK": "▐",
        "LOWER_LEFT_QUARTER_BLOCK": "▖",
        "LOWER_RIGHT_QUARTER_BLOCK": "▗",
        "UPPER_LEFT_QUARTER_BLOCK": "▘",
        "UPPER_RIGHT_QUARTER_BLOCK": "▝",
        "LEFT_THREE_QUARTER_BLOCK": "▙",
        "RIGHT_THREE_QUARTER_BLOCK": "▛",
        "LOWER_THREE_QUARTER_BLOCK": "▟",
        "UPPER_THREE_QUARTER_BLOCK": "▜"
        #TODO: MORE TO COME!
    },

    "PIPE_EXTRAS": {
        "X": "╳",
        "HALF_LEFT_HORIZONTAL": "╴",
        "HALF_TOP_VERTICAL": "╵",
        "HALF_RIGHT_HORIZONTAL": "╶",
        "HALF_BOTTOM_VERTICAL": "╷",
        "END_LEFT": "╼",
        "END_TOP": "╽",
        "END_RIGHT": "╾",
        "END_BOTTOM": "╿"
    },

    "DOTS": {
        "ELLIPSE_MIDDLE": "⋯",
        "ELLIPSE_VERTICAL": "⋮",
        "ELLIPSE_DIAGONAL_RIGHT_TO_LEFT": "⋰",
        "ELLIPSE_DIAGONAL_LEFT_TO_RIGHT": "⋱",
        "MIDDOT": "·",
        "BULLET": "•",
    },

    "ARROWS": {
        "UP_ARROW": "↑",
        "DOWN_ARROW": "↓",
        "LEFT_ARROW": "←",
        "RIGHT_ARROW": "→",
        "UP_DOWN_ARROW": "↕",
        "LEFT_RIGHT_ARROW": "↔",
        "NORTH_WEST_ARROW": "↖",
        "NORTH_EAST_ARROW": "↗",
        "SOUTH_EAST_ARROW": "↘",
        "SOUTH_WEST_ARROW": "↙",
        "LEFT_RIGHT_ARROW": "↔",
        "DOUBLE_UP_ARROW": "⇑",
        "DOUBLE_DOWN_ARROW": "⇓",
        "DOUBLE_LEFT_ARROW": "⇐",
        "DOUBLE_RIGHT_ARROW": "⇒",
        "DOUBLE_LEFT_RIGHT_ARROW": "⇔",
        "DOUBLE_UP_DOWN_ARROW": "⇕"
        #TODO: THERE'S MORE ARROWS!
    },

    # Braille is generated programmatically
    #TODO: NAME BRAILLE DOTS
    "BRAILLE": {i: chr(0x2800 + i) for i in range(1, 256)}
}

if __name__ == "__main__":
    for category, chars in CharLib.items():
        print(f"Category: {category}")
        for name, char in chars.items():
            print(f"  {name}: {char}")
        print()