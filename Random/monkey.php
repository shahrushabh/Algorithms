<?php

// you can write to stdout for debugging purposes, e.g.
// print "this is a debug message\n";

function solution($A, $D) {
    // write your code in PHP7.0
    
    $total_distance = count($A);
    $coverable_distance = 0;
    $positions = array();
    
    // Check if he can complete it in one jump.
    if($D >= $total_distance){
        return 0;
    }

    // Sort the array $A by value so that we can reveal stone in the order.
    asort($A);

    // Go through the array $A as the stones come out of the water.
    foreach($A as $position=>$time){
        // Count this position if time is >= 0
        if($time >= 0){
            $coverable_distance += $position;
            $positions[$time] = $position;
        }

        if($coverable_distance >= $total_distance && valid_positions($positions, $D)){
            return $time;
        }
    }
    
    // If we get here monkey is never able to go over to the other side. Return -1.
    return -1;
}

function valid_positions($P,$max_distance){
    
    // return false if less than 2 positions are provided.
    if(count($P) < 2){
        return false;
    }
    
    // check pairs of positions that can be coverable limited by the maximum distance.
    $first_position = 0;
    $second_position = 0;
    $first = true;
    foreach($P as $pos){
        
        if($first){
            $first = false;
            $first_position = $pos;
        }else{
            if($pos != null){
                $second_position = $pos;
                if(abs($second_position - $first_position) <= $max_distance){
                    $first_position = $second_position;
                }else{
                    return false;
                }    
            }
        }
    }
    
    // If we get here, all positions are valid and coverable.
    return true;
}

// Computes sum of all 2 digit numbers in an array.
function solution($A) {
    // write your code in PHP7.0
    $sum = 0;
    foreach($A as $num){
        if(($num > 9 && $num < 100) || ($num < -9 && $num > -100)){
            $sum += $num;
        }
    }
    return $sum;
}
