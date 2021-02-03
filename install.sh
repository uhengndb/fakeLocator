#! /usr/bin/bash
pkg install php
pkg install unzip
pkg install python
pip install requests
printf "\e[1;92m[*] Downloading Ngrok ....\e[0m\n"
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip -o ngrok.zip
printf "\e[1;92m[*] Unziping ngrok.zip\e[0m\n"
unzip ngrok.zip
clear
printf "\e[1;93m[*] Enter Ngrok Authentication Token : \e[1;94m"
read token
./ngrok authtoken $token
printf "\e[1;93m[*] Installation Completed.\e[0m\n"
