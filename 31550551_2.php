
<!DOCTYPE html>
<!--Name: Jean Torres-Rosario-->
<script>
    function isNumber(num) {
        return typeof num === 'number';
    }

    function pressed(index) {
        var table;
        var rows;
        var switching;
        var shouldSwitch;
        var i, x, y;
        table = document.getElementById("stocks");
        switching = true;

        while (switching) {
            switching = false;
            rows = table.rows;

            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;

                x = rows[i].getElementsByTagName("td")[index];
                y = rows[i + 1].getElementsByTagName("td")[index];
                value1 = x.innerHTML;
                value2 = y.innerHTML;
                if(isNaN(value1) == false) {
                    if(parseFloat(value1) > parseFloat(value2)) {
                        shouldSwitch = true;
                        break
                    }
                } 
                else {
                    if (value1.toLowerCase() > value2.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                    }
                }
            }
            

            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
            }
        }
    }
</script>
<html>

    <body>
        <?php
            require('vendor/autoload.php');


            $client = new \MongoDB\Client("mongodb://localhost:27017");
	
            echo "Connection to database successfully\n";

            $db = $client->jean_database;
  
            echo "Database jean_database selected\n";

            $collection = $db->jean_collection;

            echo "Succesfully connected to collection jean_collection\n";

            $information = $collection->find([], ['sort' => ['Name'=>1]]);

            echo "<table id=\"stocks\" border=\"1\">\n";
            #table header
            echo "<thead>\n";
            echo "<tr>\n";
            echo "<th onclick=\"pressed(0)\" >Index</th>";
            echo "<th onclick=\"pressed(1)\">Name</th>";
            echo "<th onclick=\"pressed(2)\">Symbol</th>";
            echo "<th onclick=\"pressed(3)\">Price (Introday)</th>";
            echo "<th onclick=\"pressed(4)\">Change</th>";
            echo "<th onclick=\"pressed(5)\">Volume</th>";

            echo "</tr>\n";
            echo "</thead>\n";

            echo "<tbody>";

            echo "<tr>\n";
            


            foreach ($information as $document) {
                foreach($document as $key => $value) {
                    if($key != '_id') {
                        echo "<td>";
                        echo "{$value}";
                        echo "</td>";
                    }
                        
                }
                echo "\n</tr>\n";
            }
            echo "</tbody>\n";
            echo "</table>\n"
        ?>
    </body>
</html>
