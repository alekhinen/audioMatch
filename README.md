# Assignment 4 - Rapid Prototype

### Team Members
- Nick Alekhine
- Michael 'Zig' Chadbourne
- John Meenagh
- Charles Perrone

### Rules to follow when working with Git/Github
- __Never__ push to master until application is ready for production
- When working on a new feature:
  - branch off of `develop`
  - name the branch in the following format: `FIRST_INITIALLAST_INITIAL\feature\FEATURE_NAME`.
    - e.g. `na\feature\interface`
- __Never__ merge your feature into `develop` until feature is pull requested and reviewed by at least one other member of the team.

### Sublime Text Project Configuration
If you are planning to work in Sublime Text, I usually set up my project using the following settings. This is to keep formatting consistent across all developer environments.

```
{
  "folders": [
    {
      "follow_symlinks": true,
      "path": "PATH/TO/REPO"
    }
  ],
  "settings": {
    "trim_trailing_white_space_on_save": true,
    "ensure_newline_at_eof_on_save": true,
    "translate_tabs_to_spaces": true,
    "detect_indentation": false,
    "tab_size": 2
  }
}
```
