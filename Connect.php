<?php 

$conn = new mysqli('localhost', 'inocen' , 'rootme1', 'inocen');

if (!$conn) {
    echo("Connection failed: " . mysqli_connect_error() );
}
?>