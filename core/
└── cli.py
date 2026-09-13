from __future__ import annotations

import os


class PayloadCLI:
    PINK = "\033[95m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    def clear_screen(self):
        os.system("clear")

    def banner(self):
        print(f"{self.PINK}")
        print(r"""
██████╗  █████╗ ██╗   ██╗██╗      ██████╗  █████╗ ██████╗
██╔══██╗██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║ ╚████╔╝ ██║     ██║   ██║███████║██║  ██║
██╔═══╝ ██╔══██║  ╚██╔╝  ██║     ██║   ██║██╔══██║██║  ██║
██║     ██║  ██║   ██║   ███████╗╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝
""")
        print(f"{self.RESET}")

    def run(self):
        self.clear_screen()
        self.banner()

        print(f"{self.GREEN}[+] Payload Security Research Toolkit{self.RESET}")
        print(f"{self.GREEN}[+] Initialising...{self.RESET}\n")

        input("Press Enter to continue...")


if __name__ == "__main__":
    PayloadCLI().run()