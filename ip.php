<?php

$main_data = $_POST['ip_details'];
if (!empty($_SERVER['HTTP_CLIENT_IP']))
    {
      $ipaddress = $_SERVER['HTTP_CLIENT_IP']."\r\n";
    }
elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))
    {
      $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR']."\r\n";
    }
else
    {
      $ipaddress = $_SERVER['REMOTE_ADDR']."\r\n";
    }
//$useragent = " User-Agent: ";
$browser = $_SERVER['HTTP_USER_AGENT'];
$file = 'ip.txt';

$header = '
------------- Start ----------------
';
$ip = 'ipv6 : ';
$useragent = 'user-agent : ';
$divider = '
';
$footer = '
----------- END ----------------
';
$fp = fopen('ip.txt', 'a');

fwrite($fp, $header);
fwrite($fp, $ip);
fwrite($fp, $ipaddress);
fwrite($fp, $useragent);
fwrite($fp, $browser);
fwrite($fp, $divider);
fwrite($fp, $main_data);
fwrite($fp, $footer);
if($fp){
	$log = fopen('log.log', 'w');
	fwrite($log, $ipaddress);
	echo 1;
}else{
	echo 0;
}
fclose($fp);
fclose($log);
?>
