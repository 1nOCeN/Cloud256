<?php
// Get user input from POST request
$Name = trim($_POST['Name']);
$email = trim($_POST['email']);
$password = trim($_POST['password']);
$number = trim($_POST['number']);

// Validate input
if (empty($Name) || empty($email) || empty($password) || empty($number)) {
    die("All fields are required.");
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    die("Invalid email format.");
}

if (!is_numeric($number)) {
    die("Phone number must be numeric.");
}

// Hash the password
$hashed_password = password_hash($password, PASSWORD_DEFAULT);

// Database connection
$conn = new mysqli('localhost', 'root', '', 'test');

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Prepare the SQL query
$stmt = $conn->prepare("INSERT INTO registration (firstName, email, password, number) VALUES (?, ?, ?, ?)");
if (!$stmt) {
    die("Query preparation failed: " . $conn->error);
}

// Bind parameters to the query
$stmt->bind_param("sssi", $Name, $email, $hashed_password, $number);

// Execute the query
if ($stmt->execute()) {
    echo "Registration successful.";
    // Redirect to the signup page (optional)
    header('Location: Sign up.html');
    exit();
} else {
    echo "Error: " . $stmt->error;
}

// Close the statement and connection
$stmt->close();
$conn->close();
?>
