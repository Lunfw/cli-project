#   Makefile

-   ~~Rules: build, run, debug, clean~~
-   ~~Add pip, poetry~~
-   ~~run: runs program~~
-   ~~debug: make run -> pudb~~

#   ~~pip, uv~~

-   ~~Imports: pip, poetry, pydantic,~~ custom, std
-   ~~Use: termios, tty, stdout/stdin~~
-   ~~Restrictions: no other imports, all custom-made functions~~
-   ~~Allowed file extensions: \*.py, \*.toml, custom extension~~

#   Custom extensions

-   Custom CLI extension for this!! (loader.py rules)

#   Root

-   ~~./src/__main__.py~~
-   ./src/\*.py
-   ~~./plugins: \*.py base files~~
-   ./plugins.cli: TBD
-   ~~./config.json: load config, whether to hide cursor or not, etc...~~

#   _handle_command

-   Plugin loading
-   Command loading
-   Plugin template

The goal is to be able to make a command-line interface, nothing fancy.
Framework, works under a mods/plugins folder.
This is not minishell!
