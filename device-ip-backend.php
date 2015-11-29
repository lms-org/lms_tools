<?php
define("MAX_DATA_SIZE", 100);

$data = $_POST['data'];

if(isset($data) && strlen($data) <= MAX_DATA_SIZE) {
    $data = date('Y-m-d H:i:s') . ' ' . $data;
    if(file_put_contents('data.txt', $data)) {
        echo "success";
    } else {
        echo "fail";
    }
} else {
    echo htmlspecialchars(file_get_contents('data.txt'));
}
?>
