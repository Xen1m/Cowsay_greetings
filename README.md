# Cowsay_greetings
## 🐮 Terminal Joke Greeter
Displays a random joke and random animal when starting kitty
## Setup
Download cowsay and other ascii art animals via pip or pipx
```
pip install cowsay
```

Make a jokes.txt file at 
```
touch ~.config/kitty/jokes.txt
```
Write the jokes you want to display into it. Every joke has to be on a new line respectively.

If you want to use the script only in the kitty terminal paste this into your shell config:
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
