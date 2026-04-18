# th3lazyst4lker

A (somewhat functional) OSINT multi-tool for lazy researchers.

The first two versions were a complete mess, so this is the first one that actually made it out.  
No promises about updates — I’ll probably forget this exists at some point.

Still, it works well enough for initial reconnaissance and quick OSINT checks.

---

## Features

### Username search
- maigret  
- sherlock  
- socialscan  

### Email search
- holehe  
- socialscan  
- theHarvester (domain-based)  

### Name search
- recon-ng  
- spiderfoot  

- Intensity levels for scans  
- Opens interactive tools in separate terminals  

---

## Requirements

You need these installed and available in your PATH:

```bash
pip install maigret sherlock-project socialscan holehe --break-system-packages
pip install theHarvester recon-ng spiderfoot --break-system-packages
```

---

## Usage

### Username search
```bash
python th3_lazy_st4lker.py -u username
```

### Username (high intensity)
```bash
python th3_lazy_st4lker.py -u username -i 1
```

### Username (medium intensity)
```bash
python th3_lazy_st4lker.py -u username -i 2
```

### Username (low intensity)
```bash
python th3_lazy_st4lker.py -u username -i 3
```

---

### Email search
```bash
python th3_lazy_st4lker.py -e example@email.com
```

---

### Name search (opens other terminals)
```bash
python th3_lazy_st4lker.py -n "John Doe"
```

---

### Check tools
```bash
python th3_lazy_st4lker.py --check-tools
```

---

### Help
```bash
python th3_lazy_st4lker.py -h
```

---

## Known issues

- socialscan sometimes throws DNS errors  
  → not the script, your network/DNS  

- maigret might complain about too many connection failures  
  → lower intensity (`-i 3`)  

- recon-ng / spiderfoot may be missing dependencies:

```bash
pip install pyyaml cherrypy --break-system-packages
```

- if something shows as MISSING, it’s not installed or not in PATH  

---

## Notes

- this is not a full OSINT framework, just a wrapper around other tools  
- some tools are interactive and will open separately  
- results depend on rate limits, network, and how visible the target is  

---

## Contributing / messing with it

if you want to improve it or fix something, go ahead  
add tools, clean code, make it less cursed  or more, whatever suits you

(/^.^)/

---

## Disclaimer

use it responsibly  
don’t do anything dumb (without bringing me in on it)
