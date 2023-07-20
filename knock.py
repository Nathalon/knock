# Copyright 2023 Elijah Gordon (SLcK) <braindisassemblue@gmail.com>

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from argparse import Namespace, ArgumentParser
from asyncio import sleep, run
from os import name
from subprocess import call
from random import uniform
from colorama import Fore, Style, init

init(autoreset=True)

COLOR_CHOICES = {
    'black': Fore.BLACK,
    'red': Fore.RED,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE
}

lines = """Wake up, Neo...
The Matrix has you...
Follow the white rabbit.
Knock, knock, Neo."""

ascii_art = """
          (`.         ,-,
           `\ `.    ,;' /
            \`. \ ,'/ .'
      __     `.\ Y /.'
   .-'  ''--.._` ` (
 .'            /   `
,           ` '   Q '
,         ,   `._    \\
|         '     `-.;_'
`  ;    `  ` --,.._;
`    ,   )   .'
 `._ ,  '   /_
    ; ,''-,;' ``-
     ``-..__\``--`       Follow the white rabbit.
"""


def clear_screen():
    call("cls" if name == "nt" else "clear", shell=True)


async def typing_effect(text, delay_range=(0.03, 0.12), lowercase=False, uppercase=False, color=None, bold=False):
    try:
        if lowercase:
            text = text.lower()
        elif uppercase:
            text = text.upper()

        color_code = COLOR_CHOICES.get(color, Fore.GREEN)
        style_code = Style.BRIGHT if bold else Style.NORMAL

        for line in text.splitlines():
            for char in line:
                print(style_code + color_code + char, end='', flush=True)
                await sleep(uniform(*delay_range))
            print()
            await sleep(1)
            clear_screen()

        while args.repeat:
            for line in text.splitlines():
                for char in line:
                    print(style_code + color_code + char, end='', flush=True)
                    await sleep(uniform(*delay_range))
                print()
                await sleep(1)
                clear_screen()

    except KeyboardInterrupt:
        clear_screen()


def display_ascii_art():
    print(ascii_art)


if __name__ == "__main__":
    default_args = Namespace()
    default_args.delay = 0.05
    default_args.lowercase = False
    default_args.uppercase = False
    default_args.color = None
    default_args.bold = False
    default_args.hop = False
    default_args.repeat = False

    clear_screen()
    parser = ArgumentParser(description="Matrix Typing Effect Script")
    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show the version information."
    )
    parser.add_argument(
        "-l", "--lowercase",
        action="store_true",
        help="Convert the text to all lowercase before typing."
    )
    parser.add_argument(
        "-u", "--uppercase",
        action="store_true",
        help="Convert the text to all uppercase before typing."
    )
    parser.add_argument(
        "-c", "--color",
        help="Choose the color for the typing effect."
    )
    parser.add_argument(
        "-lc", "--list-colors",
        action="store_true",
        help="List the available color choices."
    )
    parser.add_argument(
        "-b", "--bold",
        action="store_true",
        help="Make the text bold during typing effect."
    )
    parser.add_argument(
        "-H", "--hop",
        action="store_true",
        help="Display the ASCII art."
    )
    parser.add_argument(
        "-r", "--repeat",
        action="store_true",
        help="Repeat the typing effect in a loop until interrupted."
    )
    args = parser.parse_args(namespace=default_args)

    if args.version:
        print("Matrix Typing Effect Script - Version 1.0")
    elif args.list_colors:
        print("Available colors:")
        for color in COLOR_CHOICES.keys():
            print(color)
    elif args.hop:
        display_ascii_art()
    else:
        try:
            run(typing_effect(
                lines,
                delay_range=(0.03, 0.12),
                lowercase=args.lowercase,
                uppercase=args.uppercase,
                color=args.color,
                bold=args.bold
            ))
        except KeyboardInterrupt:
            clear_screen()
