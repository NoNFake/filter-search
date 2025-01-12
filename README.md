# Custom Google Search Filter

Q: *Why Google?*

A: *becouse i use google, u can addit.*

A command-line tool that helps you search Google with customized website filters. Search results will be shown only from your configured trusted websites.

## Features

- Search Google with pre-configured website filters
- Toggle website filters on/off through an interactive menu
- Customizable website list through config file
- Opens results directly in Google Chrome

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd custom-google-search
pip install -r req.txt
```

## Usage
1. With `python`
```bash
python app.py <search-query>
```
2. With `app`
```bash
./build.sh
app <search-query>
```

## Commands
1. `app -c` Displays the configuration menu to toggle websites
```
1. geeksforgeeks.org :    True
2. w3schools.com :        True
3. stackoverflow.com :    True
4. github.com :           True
5. reddit.com :           True
6. youtube.com :          True
7. medium.com :           True
```
Enter the number to toggle a website on/off.

2. `app -h` Displays help information about available commands.

## Configuration
The tool uses `config_search.json` to store website perferences. Ypu You can manually edit this file to add or remove websites:
```json
{
    "websites": {
        "geeksforgeeks.org": true,
        "w3schools.com": true,
        "stackoverflow.com": true,
        "github.com": true,
        "reddit.com": true,
        "youtube.com": true,
        "medium.com": true,
        "stackexchange.com": true
    }
}
```

## Requirements

- Python 3.10+
- Google Chrome


## License
MIT License
