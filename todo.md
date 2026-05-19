#   Makefile

-   Rules: build, run, debug, clean
-   Add pip, poetry
-   run: returns \_.exe
-   debug: make run -> pudb

#   pip

-   Imports: pip, poetry, pydantic, custom
-   Use: termios, tty, stdout/stdin
-   Restrictions: no other imports, all custom-made functions
-   Allowed file extensions: \*.py, \*.toml, custom extension

#   Custom extensions

-   Custom CLI extension for this!! (.txt but parser.py rules)

#   Root

-   ./setup.py: install dependencies, alias to sh if allowed
-   ./src/__main__.py
-   ./src/\*.py
-   ./mods/plugins: \*.py files
-   ./plugins.?

The goal is to be able to make a command-line interface, nothing fancy.
Framework, works under a mods/plugins folder.
This is not minishell!
