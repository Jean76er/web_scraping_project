<?php
	//connect to mongdb
	$m = new MongoClient();
	
	echo "Connection to database successfully";
	//Select a database
	$db = $m->jean_database;

	echo "Database jean_database selected"
?>
