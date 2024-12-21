<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    echo "Form submitted!";
    print_r($_POST);
} else {
    echo "No POST data received.";
}
?>
