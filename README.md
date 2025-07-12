# Cowsay_greetings
## 🐮 Terminal Joke Greeter
Displays a random joke and random animal when starting kitty
```
 _________________________________________
/ I asked my German friend if he knew the \
\ square root of 81. He said no           /
 -----------------------------------------
\                             .       .
 \                           / `.   .' " 
  \                  .---.  <    > <    >  .---.
   \                 |    \  \ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \~~~\.'                    `./~~~/
       ---------   \__/                        \__/
      .'  O    \     /               /       \  " 
     (_____,    `._.'               |         }  \/~~~/
      `----.          /       }     |        /    \__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'   
                     |     /        |     /     ~-.     `-. _  _  _
                     |_____|        |_____|         ~ - . _ _ _ _ _>
```
## Setup
Download cowsay and other ascii art animals
```
pip install cowsay
```

Create a jokes.txt file at 
```
touch ~/.config/kitty/jokes.txt
```
Write the jokes you want to display into it. Every joke has to be on a new line respectively.

If you want to use the script only in the kitty terminal paste this into your shell config (~/.bshrc or ~/.zshrc):
```
if [ "$TERM" = "xterm-kitty" ]; then
    ~/.config/kitty/greetings.py
fi
```

Make the script executable in your terminal
```
chmod +x ~/path/to/git/repo/greetings.py
```
Edit your jokes.txt as you please.

Have fun being suprised on what awaits you next time you open a terminal :)
