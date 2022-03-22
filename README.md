# Jaws-of-the-White-Hound
This is a utility for finding XSS vulnerabilities by analyzing the source code of sites 

<h2>Installing:</h2>

Install few important things:

    pip3 install selenium
    sudo apt install firefox

Then you need geckogriver, so download it right here: https://github.com/mozilla/geckodriver/releases

After that do this:

    tar -xvzf geckodriver_linux64.tar.gz
    sudo mv geckodriver /usr/local/bin/geckodriver
    sudo chown root:root /usr/local/bin/geckodriver
    sudo chmod +x /usr/local/bin/geckodriver

<h2>Using:</h2>

    python3 main_sec.py
    
<h2>Keys and commands:</h2>

    help - show command list
    exit - finish work
    options - show list of options
    change - change options. Syntax: change *option* *new value*
    run - start testing

<h2>Warning:</h2>
Versions of program began from 0 can work unstable and in some cases break up your machine, so be careful by using that.


