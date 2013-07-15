<!doctype html>
<?php

include 'STATS.php';

$GH   = 	number_format(round($MHSAV/1000,2),2);
$UPTIME	=	time()-$WHEN;

function secs_to_h($secs)
{

// Copied from : http://csl.name/php-secs-to-human-text/
// Thanks Christian :D

        $units = array(
                "WEEK"   => 7*24*3600,
                "DAY"    =>   24*3600,
                "HOUR"   =>      3600,
                "MINUTE" =>        60,
                "SECOND" =>         1,
        );

		// specifically handle zero
        if ( $secs == 0 ) return "0 SECONDS";

        $s = "";

        foreach ( $units as $name => $divisor ) {
                if ( $quot = intval($secs / $divisor) ) {
                        $s .= "$quot $name";
                        $s .= (abs($quot) > 1 ? "S" : "") . ", ";
                        $secs -= $quot * $divisor;
                }
        }
        return substr($s, 0, -2);
}

?>

<html>
<head>
<title><?php echo $GH ?> GH</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>

<div id="contain">

	<div class="big <?php echo ($UPTIME < 300 ? 'green' : 'red') ?>">
	<b><?php echo $GH; ?> GH</b>
	</div>

	<div class="little">
	<em><?php echo secs_to_h($ELAPSED); ?></em>
	</div>

</div>

</body>
</html>
