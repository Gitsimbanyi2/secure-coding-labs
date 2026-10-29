<?php
/**
 * Secure lookup — mysqli prepared statement.
 * Insecure (never): $mysqli->query("SELECT * FROM users WHERE username = '{$username}'");
 */
function findUser(mysqli $db, string $username): ?array
{
    $stmt = $db->prepare('SELECT id, username FROM users WHERE username = ?');
    $stmt->bind_param('s', $username);
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_assoc();
    $stmt->close();
    return $row ?: null;
}
