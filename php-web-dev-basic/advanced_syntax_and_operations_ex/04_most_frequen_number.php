<?php

$input = explode(" ", readline());
$counts = array_count_values($input);
arsort($counts);
$top_with_count = array_slice($counts, 0, 1, true);
$top = array_keys($top_with_count);

echo $top[0];
