"""
the main CLI where all the magic goes down
chaos mode parses your tools and their arguments, standard mode does the usual stuff
"""

import sys
import argparse
import shlex
from .colors import C, BANNER
from .tools import ToolManager
from .reporter import Reporter

class ST4lker:
    """main app class - where the lazy reconaissance happens"""
    
    def __init__(self):
        self.tool_manager = ToolManager()
        self.generate_report = False
    
    def show_help(self):
        """display the help menu - read this if you're lost"""
        help_text = f"""{BANNER}

{C.BOLD}USAGE:{C.RESET}
  st4lker [OPTIONS]

{C.BOLD}OPTIONS:{C.RESET}
  -u, --username <name>     Search by username
  -e, --email <email>       Search by email address
  -n, --name <name>         Search by full name
  -i, --intensity <1-3>     Search intensity (1=High, 2=Medium, 3=Low) [default: 2]
  
  --check-tools             List what tools you actually have installed
  
  -chaos <tool> "<args>" <tool> "<args>" ...
                            Chaos mode - run multiple tools with custom params
                            Put each tool's arguments inside quotes
  
  -r, --report              Generate text report after chaos runs
  
  -h, --help, -help         Show this help

{C.BOLD}CHAOS MODE - THE FUN PART:{C.RESET}
  
  Single tool:
    st4lker -chaos sherlock "admin"
  
  Multiple tools with separate quoted arguments:
    st4lker -chaos holehe "test@example.com" sherlock "user1 user2 --timeout 10" socialscan "username"
  
  Generate report:
    st4lker -chaos holehe "test@example.com" sherlock "admin" -r

{C.BOLD}STANDARD MODE:{C.RESET}
  
  Basic search:
    st4lker -u admin
  
  High intensity:
    st4lker -u admin -i 1
  
  Email search:
    st4lker -e test@gmail.com
  
  All at once:
    st4lker -u admin -e test@gmail.com -n "John Smith"

{C.BOLD}INTENSITY LEVELS:{C.RESET}
  1 (High)    - thorough but slow, hit everything
  2 (Medium)  - balanced (default)
  3 (Low)     - fast, minimal requests

{C.BOLD}TOOLS AVAILABLE:{C.RESET}
  - Sherlock       : username hunting (the classic move)
  - Socialscan     : email/username checker (quick verification)
  - Holehe         : email breach detector (did you get pwned?)
  - Maigret        : detailed username search (sherlock++ mode)
  - PhoneInfoqa    : phone number OSINT (find who's calling)
  - Whois          : domain and IP lookup (know your target)
  - Hunter         : email finder (find business emails)

{C.BOLD}DISCLAIMER:{C.RESET}
  Use responsibly. This is for authorized recon only.
  Don't be dumb. (/^.^)/

"""
        print(help_text)
    
    def check_tools(self):
        """show what tools you have ready to go"""
        status = self.tool_manager.check_all()
        print(f"\n{C.BOLD}Tool Status:{C.RESET}\n")
        for tool, is_installed in status.items():
            desc = self.tool_manager.AVAILABLE_TOOLS[tool]
            status_text = "OK" if is_installed else "MISSING"
            color = C.GREEN if is_installed else C.RED
            print(f"  {tool:<20} -> {color}{status_text}{C.RESET} ({desc})")
    
    def parse_chaos_args(self, chaos_args):
        """
        parse chaos mode - extract tools and their quoted arguments
        format: tool "args" tool "args" tool "args"
        """
        tool_commands = {}
        available_tools = list(self.tool_manager.AVAILABLE_TOOLS.keys())
        
        i = 0
        while i < len(chaos_args):
            arg = chaos_args[i]
            
            # skip report flags
            if arg in ["-r", "--report"]:
                i += 1
                continue
            
            # check if this is a tool name
            if arg in available_tools:
                tool_name = arg
                tool_args = []
                i += 1
                
                # grab the next argument - it should be a quoted string
                if i < len(chaos_args):
                    next_arg = chaos_args[i]
                    
                    # make sure it's not another tool name or report flag
                    if next_arg not in available_tools and next_arg not in ["-r", "--report"]:
                        # parse the quoted string into arguments using shlex
                        try:
                            tool_args = shlex.split(next_arg)
                        except ValueError:
                            # if shlex fails, just use it as-is
                            tool_args = [next_arg]
                        i += 1
                
                tool_commands[tool_name] = tool_args
            else:
                # unknown argument, skip it
                i += 1
        
        return tool_commands
    
    def run_chaos_mode(self, chaos_args, generate_report=False):
        """run chaos mode - multiple tools with custom arguments"""
        print(f"\n{C.BOLD}{C.CYAN}[*] CHAOS MODE ACTIVATED{C.RESET}\n")
        
        tool_commands = self.parse_chaos_args(chaos_args)
        
        if not tool_commands:
            print(f"{C.RED}Error: No valid tools specified{C.RESET}")
            print(f"{C.YELLOW}Available: {', '.join(self.tool_manager.AVAILABLE_TOOLS.keys())}{C.RESET}")
            print(f"{C.YELLOW}Format: st4lker -chaos tool \"args\" tool \"args\"{C.RESET}")
            return
        
        # execute each tool in order
        for tool, args in tool_commands.items():
            if not args:
                print(f"{C.YELLOW}[!] {tool} has no arguments, skipping{C.RESET}")
                continue
            
            self.tool_manager.run_tool(tool, args)
        
        # generate report if requested
        if generate_report:
            reporter = Reporter(self.tool_manager.execution_log, self.tool_manager.results)
            reporter.print_report()
    
    def run_standard_mode(self, username=None, email=None, name=None, intensity=2):
        """run the standard mode - searches without chaos"""
        search_performed = False
        
        if username:
            print(f"\n{C.BOLD}{C.GREEN}[USERNAME] {username}{C.RESET}\n")
            self.tool_manager.run_tool("sherlock", [username])
            self.tool_manager.run_tool("socialscan", [username])
            search_performed = True
        
        if email:
            print(f"\n{C.BOLD}{C.GREEN}[EMAIL] {email}{C.RESET}\n")
            self.tool_manager.run_tool("holehe", [email])
            self.tool_manager.run_tool("socialscan", [email])
            search_performed = True
        
        if name:
            print(f"\n{C.BOLD}{C.GREEN}[NAME] {name}{C.RESET}\n")
            print(f"{C.YELLOW}[!] For names, try breaking them down and searching as usernames{C.RESET}")
            search_performed = True
        
        return search_performed
    
    def main(self):
        """main entry point - where everything starts"""
        print(BANNER)
        
        parser = argparse.ArgumentParser(
            description="Th3LazySt4lker - OSINT Multi Tool",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            add_help=False
        )
        
        parser.add_argument("-u", "--username", help="Search by username")
        parser.add_argument("-e", "--email", help="Search by email")
        parser.add_argument("-n", "--name", help="Search by full name")
        parser.add_argument("-i", "--intensity", type=int, choices=[1, 2, 3], default=2,
                            help="Intensity level (1=High, 2=Medium, 3=Low)")
        parser.add_argument("--check-tools", action="store_true", help="Check installed tools")
        parser.add_argument("-chaos", nargs=argparse.REMAINDER, help="Chaos mode")
        parser.add_argument("-r", "--report", action="store_true", help="Generate report")
        parser.add_argument("-h", "--help", "-help", action="store_true", dest="show_help",
                            help="Show help")
        
        args, unknown = parser.parse_known_args()
        
        # handle help
        if args.show_help or len(sys.argv) == 1:
            self.show_help()
            return
        
        # handle tool check
        if args.check_tools:
            self.check_tools()
            return
        
        # handle chaos mode
        if args.chaos:
            self.run_chaos_mode(args.chaos, generate_report=args.report)
            return
        
        # handle standard mode
        search_performed = self.run_standard_mode(
            username=args.username,
            email=args.email,
            name=args.name,
            intensity=args.intensity
        )
        
        if not search_performed:
            self.show_help()

def main():
    """entry point for pip install"""
    app = ST4lker()
    app.main()

if __name__ == "__main__":
    main()
