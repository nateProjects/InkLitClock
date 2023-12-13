<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quote Viewer</title>
</head>
<body>
    <?php
        $fileName = 'quote.txt'; // Replace with the actual file name
        $fileContents = file_get_contents($fileName);

        echo nl2br($fileContents); // Add line breaks for better readability
    ?>
</body>
</html>
