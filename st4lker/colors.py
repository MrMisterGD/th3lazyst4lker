"""
colors and banner - making output look  ~ P R E T T Y ~
"""

class C:
    RED    = "\033[91m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    WHITE  = "\033[97m"
    DIM    = "\033[2m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"
    CYAN   = "\033[96m"
    BLUE   = "\033[94m"

BANNER = f"""{C.BOLD}{C.CYAN}
*******************************************************************
*                                                                 *
*                   Th3LazySt4lker v0.5                           *
*                      Coded by Mr. Mister GD                     *
*                                                                 *
*                    lazy OSINT for lazy people                   *
*                                                                 *
*******************************************************************
{C.RESET}
"""
