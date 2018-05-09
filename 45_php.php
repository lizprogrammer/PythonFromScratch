<?php

$python = exec('python 45_php.py');


$data = file_get_contents('name.json');
$display_data = json_decode($data);
for each($display_data as $dd){
	echo "$dd";
}

//echo $python;


?>