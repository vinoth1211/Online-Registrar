<?php
// database connection code
// $con = mysqli_connect('localhost', 'database_user', 'database_password','database');

$con = mysqli_connect('localhost', 'root', '','online_registrar');

// get the post records
$txtName = $_POST['txtName'];
$txtEmail = $_POST['txtEmail'];
$txtPhone = $_POST['txtPhone'];
$txtNIC = $_POST['txtNIC'];

// database insert SQL code
$sql = "INSERT INTO user (fldNIC, fldName, fldEmail, fldPhone) VALUES ('$txtNIC', '$txtName', '$txtEmail', '$txtPhone')";

// insert in database 
$rs = mysqli_query($con, $sql);

if($rs)
{
 echo "Contact Records Inserted";
}

?>