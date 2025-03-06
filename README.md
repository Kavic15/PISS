# PISS
## Prevency Interaction Special Software

PISS is simple python code for interacting with social media simulator Prevency which includes: facebook, twitter and linkedin

(PISS only works with facebook and twitter)

### BEWARE: ###
### This code is written with philosophy: ###
"If it's stupid and it works, it's not stupid.", don't expect any well-arranged code as I am in a hurry.

##
### How to make it work:
1. clone this repository
2. open in vscode
3. press ctrl+shift+P
4. search for "Python: create Environment..."
5. pick "venv"
6. pick your preffered python version (I use 3.10.11)
7. check "requirements.txt" for installing needed libraries

### Usage
You will need to see how http requests look like (either by looking into network section after inspecting a prevency website or via software like Burp Suite) and getting needed authorization token and excersise id, as well as user ids. \
You will need to update "auth.py" accordingly, as this file is crucial for program to function. \
You will need to generate pool of possible posts and comments into "post_pool" directory \
For using AI to generate posts and comments automatically you download and install ollama. \ 

I strongly advise to edit code as much as possible for your needs.