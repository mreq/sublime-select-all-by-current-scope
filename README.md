Select all by current scope
===========================

Provides a `select_all_by_current_scope` command, which (as the name suggests) select everything matching the current scope (that is the scope of your first cursor).

The command accepts an optional argument `scope_must_match` containing a regex string, which filters the long scope string to get a single scope name.

**This plugin doesn't have any default keybindings.** You have to assign them yourself.

Example keybindings
-------------------

Selects everything matching current scope:
```json
{
  {
    "keys": ["ctrl+alt+shift+a"],
    "command": "select_all_by_current_scope"
  }
}
```
Selects everything matching the first piece of current scope, which contains the word `embedded`:
```json
{
  {
    "keys": ["ctrl+alt+shift+a"],
    "command": "select_all_by_current_scope",
    "args": { "scope_must_match": "embedded" }
  }
}
```

Usecase
-------

Say you have a knitr/Sweave file with embedded R code. You might want to select all the R code. For that, I have the following keybinding:
```json
{
  {
    "keys": ["ctrl+alt+shift+a"],
    "command": "select_all_by_current_scope",
    "args": { "scope_must_match": "embedded" }
    "context":[
      { "key": "selector", "operator": "equal", "operand": "source.r.embedded.knitr" }
    ]
  }
}
```

How about all the javascript code from an HTML file? Src of all images/script tags/stylesheets in a HTML file? Bold text from a Markdown file? That's matched by default:
```json
{
  {
    "keys": ["ctrl+alt+shift+a"],
    "command": "select_all_by_current_scope"
  }
}
```