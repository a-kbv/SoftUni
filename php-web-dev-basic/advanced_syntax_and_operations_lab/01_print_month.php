<?php
$months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
];

$index = readline();
if (1 < $index && $index <= 12){
    echo $months[$index-1];
}
else{
    echo "Invalid Month!";
}