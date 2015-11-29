<?php
define("MAX_DATA_SIZE", 100);

if(isset($_POST['data']) && strlen($_POST['data']) <= MAX_DATA_SIZE) {
    if(file_put_contents('data.txt', $_POST['data'])) {
        echo "success";
    } else {
        echo "fail";
    }
} else {
    echo file_get_contents('data.txt');
}
?>
