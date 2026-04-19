"""
report generation - make your findings look professional (or at least readable)
"""

from datetime import datetime
from .colors import C

class Reporter:
    """generates findings reports because sometimes you need to prove what you found"""
    
    def __init__(self, execution_log, tool_results):
        self.execution_log = execution_log
        self.tool_results = tool_results
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def generate_text_report(self):
        """create a text report of all your mess"""
        report = []
        report.append("\n" + "=" * 70)
        report.append("OSINT FINDINGS REPORT")
        report.append("=" * 70)
        report.append(f"Generated: {self.timestamp}")
        report.append("=" * 70 + "\n")
        
        # summary section
        total_runs = len(self.execution_log)
        successful = sum(1 for r in self.execution_log if r["success"])
        
        report.append("SUMMARY")
        report.append("-" * 70)
        report.append(f"Total Tools Run: {total_runs}")
        report.append(f"Successful: {successful}")
        report.append(f"Failed: {total_runs - successful}\n")
        
        # detailed results
        report.append("DETAILED RESULTS")
        report.append("-" * 70)
        
        for i, execution in enumerate(self.execution_log, 1):
            tool = execution["tool"]
            args = " ".join(execution["args"])
            status = "SUCCESS" if execution["success"] else "FAILED"
            
            report.append(f"\n[{i}] {tool.upper()}")
            report.append(f"    Arguments: {args}")
            report.append(f"    Status: {status}")
        
        report.append("\n" + "=" * 70)
        report.append("END OF REPORT")
        report.append("=" * 70 + "\n")
        
        return "\n".join(report)
    
    def print_report(self):
        """print report to console"""
        report = self.generate_text_report()
        print(f"\n{C.BOLD}{C.BLUE}{report}{C.RESET}")
        return report
    
    def save_report(self, filename=None):
        """save report to file"""
        if filename is None:
            filename = f"osint_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        report = self.generate_text_report()
        
        try:
            with open(filename, "w") as f:
                f.write(report)
            print(f"{C.GREEN}>>> Report saved to: {filename}{C.RESET}")
            return filename
        except Exception as e:
            print(f"{C.RED}Error saving report: {e}{C.RESET}")
            return None
