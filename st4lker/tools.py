"""
the actual tools live here - sherlock, socialscan, holehe, maigret, phoneinfogas, etc
they're the actual workers here that do the reconaissance while we wait
"""

import subprocess
import shutil
from .colors import C

class ToolManager:
    """manages all the OSINT tools like a lazy commander"""
    
    AVAILABLE_TOOLS = {
        "sherlock": "username hunting across 500+ sites (the classic)",
        "socialscan": "checks if email/username exists anywhere (quick n dirty)",
        "holehe": "email breach detector (see if you got pwned)",
        "maigret": "username search on steroids (more detailed than sherlock)",
        "phoneinfoqa": "phone number OSINT (find who's behind that number)",
        "whois": "domain and IP lookup (know your target)",
        "hunter": "email finder and verifier (hunt business emails)",
    }
    
    def __init__(self):
        self.results = {}
        self.execution_log = []
    
    def resolve_bin(self, name):
        """find a tool - first check if it's installed, then check PATH"""
        try:
            if name == "sherlock":
                from sherlock import sherlock
                return "sherlock"
            elif name == "socialscan":
                import socialscan
                return "socialscan"
            elif name == "holehe":
                import holehe
                return "holehe"
            elif name == "maigret":
                import maigret
                return "maigret"
            elif name == "phoneinfoqa":
                return shutil.which("phoneinfoga") or ""
        except ImportError:
            pass
        
        found = shutil.which(name)
        return found or ""
    
    def is_installed(self, tool):
        """yeah... is it actually there?"""
        return bool(self.resolve_bin(tool))
    
    def run_cmd(self, cmd, show_cmd=True):
        """run a command and pray it works"""
        try:
            if show_cmd:
                print(f"{C.DIM}$ {' '.join(cmd)}{C.RESET}")
            
            result = subprocess.run(cmd, check=False)
            return result.returncode == 0, "", ""
        except Exception as e:
            print(f"{C.RED}Error: {e}{C.RESET}")
            return False, "", str(e)
    
    def run_tool(self, tool, args):
        """run any tool with its custom arguments"""
        if not self.is_installed(tool):
            msg = f"Error: {tool} not installed or not found in PATH"
            print(f"{C.RED}{msg}{C.RESET}")
            return False, msg
        
        print(f"\n{C.CYAN}[*] Running {tool}...{C.RESET}")
        cmd = [tool] + args
        success, stdout, stderr = self.run_cmd(cmd)
        
        self.execution_log.append({
            "tool": tool,
            "args": args,
            "success": success,
            "output": stdout or stderr
        })
        
        self.results[tool] = {
            "tool": tool,
            "args": args,
            "success": success
        }
        
        return success, stdout or stderr
    
    def check_all(self):
        """peek at all the tools and see which ones are actually working"""
        status = {}
        for tool in self.AVAILABLE_TOOLS.keys():
            status[tool] = self.is_installed(tool)
        return status
