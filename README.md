# th3LazySt4lker

A lazy approach to OSINT - because doing reconnaissance shouldn't require PhD levels of energy.

SOOOOOO I am really lacking sleep BUT!! We are on the first deployment :D 
This one actually works. 
No promises about the future though - ᴵ'ˡˡ ᵖʳᵒᵇᵃᵇˡʸ ᶠᵒʳᵍᵉᵗ ᵗʰᶦˢ ᵉˣᶦˢᵗˢ.

---

## Installation

### With Docker
```bash
git clone <repo> th3lazyst4lker
cd th3lazyst4lker
docker build -t th3lazyst4lker .
docker run --rm th3lazyst4lker --help
```

### On Kali / Linux (Recommended)
```bash
git clone <repo> th3lazyst4lker
cd th3lazyst4lker
pip install -e .
st4lker --help
```

After install, `st4lker` works from anywhere (Probably).

### Requirements
- Python 3.11+
- Linux (we don't do Windows here)
- pip

---

## Usage

### Standard Mode

Search by username:
```bash
st4lker -u admin
```

Search by email:
```bash
st4lker -e test@gmail.com
```

Search by name:
```bash
st4lker -n "John Smith"
```

High intensity (slower, more thorough):
```bash
st4lker -u admin -i 1
```

### Check What Tools You Have
```bash
st4lker --check-tools
```

### Get Help
```bash
st4lker --help
st4lker -h
```

### Chaos Mode (The mess)

Run multiple tools with their specific parameters:
(Haven't properly tested it and I coded this while really sleep deprived)
```bash
st4lker -chaos sherlock "admin" holehe "test@gmail.com"
```

Put each tool's arguments inside quotes. Chain as many as you want:

```bash
st4lker -chaos sherlock "--timeout 10 admin user1" holehe "test@gmail.com --only-used" socialscan "username1 username2" -r
```

The `-r` flag generates a text report at the end.

---

## Tools Included

| Tool | Purpose |
|------|---------|
| **Sherlock** | Username search across 500+ sites |
| **Socialscan** | Email/username availability checker |
| **Holehe** | Email breach detector |
| **Maigret** | Detailed username search (sherlock++ mode) |
| **PhoneInfoqa** | Phone number OSINT |
| **Whois** | Domain and IP lookup |
| **Hunter** | Email finder and verifier |

---

## Intensity Levels

Use these with `-i` flag:

- **1 (High)** - Thorough but slow, hits everything
- **2 (Medium)** - Balanced (default)
- **3 (Low)** - Fast, minimal requests

Use lower intensity if targets are rate-limiting you.

---

## Examples

### Quick username check
```bash
st4lker -u admin
```

### Aggressive username search
```bash
st4lker -u admin -i 1
```

### Email verification
```bash
st4lker -e test@gmail.com
```

### Chaos mode with multiple tools and arguments
```bash
st4lker -chaos sherlock "--timeout 10 admin user1 user2" holehe "test@gmail.com" socialscan "username1 username2" -r
```

### Custom tool arguments
```bash
st4lker -chaos sherlock "admin --csv" whois "example.com"
```

---

## Project Structure

```
th3lazyst4lker/
├── st4lker/                 (the actual package)
│   ├── __init__.py
│   ├── cli.py              (main CLI interface)
│   ├── tools.py            (tool management)
│   ├── colors.py           (pretty output, just copy-pasted it from someone elses things)
│   └── reporter.py         (report generation) (NOT TESTED ACROSS ALL FEATURES)
├── setup.py                (pip setup)
├── requirements.txt        (dependencies)
├── Dockerfile              (for Docker lovers, also I used it because my VM got stuck)
├── .gitignore
└── README.md              (this file, right here)
```

---

## Contributing

Found a bug? Got a better idea? Want to add tools?

Go for it. PRs welcome. Don't expect super fast responses though, I will get to it when I remember I have an email.

---

## Disclaimer

Use responsibly. This tool is for authorized reconnaissance and educational purposes only.

Don't do anything dumb (without getting me on it).

---

Made with ~~blood, sweat, and tears~~ excessive Monster energy.

(/^.^)/

---

Comments, bugs, and requests
----------------------------
* Discord: mrcyberandy
* Email: worriednerd@protonmail.com