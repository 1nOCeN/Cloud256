<?php

$conn = new mysqli('localhost', 'inocen', 'rootme1', 'inocen');

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Example: Fetching the email dynamically (e.g., from a GET parameter)
$email = isset($_GET['email']) ? $_GET['email'] : ''; // Replace with dynamic data or form submission

if (!$email) {
    die("Email parameter is missing!");
}

// SQL query to fetch user details by email
$sql = "SELECT name, email, subscription_plan FROM users WHERE email = ?";
$stmt = $conn->prepare($sql); // Use prepared statements to prevent SQL injection
$stmt->bind_param("s", $email); // "s" indicates the parameter is a string
$stmt->execute();
$result = $stmt->get_result();

// Check if the user exists
if ($result->num_rows > 0) {
    $user = $result->fetch_assoc(); // Fetch user data as an associative array
} else {
    die("No user found with the given email.");
}

// Close the database connection
$stmt->close();
$conn->close();
?>
