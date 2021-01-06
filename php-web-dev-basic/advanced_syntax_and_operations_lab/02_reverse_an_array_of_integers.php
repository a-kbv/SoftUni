<?php
$n = readline();
$numbers = [];
for($i = 0; $i < $n; $i++) {
    $numbers[] = readline();
}
$numbers = array_reverse($numbers);
foreach ($numbers as $number){
    echo $number." ";
}
