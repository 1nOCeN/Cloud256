<?php
                   //host       name     password   data base name
$conn = new mysqli('localhost', 'inocen' , 'rootme1', 'inocen');

// conn check.
if (!$conn) {
    echo("Connection failed: " . mysqli_connect_error() );
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['submit'])) {

    // Collect DATA.
    $email = htmlspecialchars($_POST['Email']);
    $username = htmlspecialchars($_POST['Username']);
    $password = htmlspecialchars($_POST['Password']);

    // Hashing
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    //crate the sql table.
    $add = "INSERT INTO users(username, email, password) VALUES ( '$username', '$email', '$hashedPassword')";

    // check
    if (mysqli_query($conn, $add)){
        echo "<p>Registration successful! Your data has been saved.</p>";
    } else {
        echo "Erorr!" . mysqli_error($conn);
    }

    //Back for signup
    header("Location: Login.html");

    // Close the Conn
    $conn->close();
    exit();
}
?>
