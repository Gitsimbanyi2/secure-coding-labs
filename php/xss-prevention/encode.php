<?php
/**
 * Encode for HTML body context.
 * Insecure (never): echo $_GET['q'];
 */
function h(?string $value): string
{
    return htmlspecialchars($value ?? '', ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}
