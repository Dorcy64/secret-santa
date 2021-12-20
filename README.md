Intro
=====

**secret-santa** can help you manage a list of secret santa participants by
randomly assigning pairings and sending whatsapp texts. It can avoid pairing 
couples to their significant other, and allows custom email messages to be 
specified.

Dependencies
------------

selenium

Usage
-----

Copy data.py.example to data.py and enter in the participants details. 

Modify the participants and couples lists and change the generated_text in main.py if you wish.

    cd secret-santa/
    cp data.py.example data.py
    
Go to whatsapp_selenium and change the executable path to your executable path (where the chromium file is on your computer).
If you don't have chromium, you can dowload it here https://chromedriver.chromium.org/downloads/version-selection

Go to main.py change the host name to your host name.

run main.py

Wait for the program to start, scan the whatsapp code, and turn away.

Once done, close the browser.
