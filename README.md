# TestSSR

This project was inspired by SSAccount.py

SSAccount.py provided some codes which can verify the availability of shadowsocks account. 

At the beginning, I just revised some codes, use thoese codes to find out optimum accounts by sorting latencies.

I wrote some python scripts to collect free accounts from http://doub.bid/sszhfx , https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7 and other websites. Those scripts generate some json files. I can execute another tiny python scripts to combine those json files into one json file. Everyday I can collect about 95-110 free accounts.

Soon I found that latency was not good measurement for figuring out optimum accounts. I found a bandwidth speed test ultility, speedtest-cli. One day after I integrated speedtest-cli into my test program, I thought test youtube video download speed is better, instead of bandwidth speed test. I found youtube-dl in no time.

At last, I tinkered with youtube-dl, subprocess, urllib2, requests and other python modules, created a test program for sorting out optimum accounts from dozens free accounts.

Pre-req:

pip install youtube-dl

pip install requests

