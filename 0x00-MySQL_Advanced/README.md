<!DOCTYPE html>
<html lang="en">
  <head>
       
  </head>

  <body>
    <div class="col-xs-12 col-md-10 col-lg-8 contains-images">
      <h1 class="gap">
    0x00. MySQL advanced
    
  </h1>
     <div class="panel panel-default">
    <div class="panel-heading">
      <h3 class="panel-title">Concepts</h3>
    </div>
    <div class="panel-body">
      <p>
        <em>For this project, we expect you to look at this concept:</em>
      </p>
      <ul>
          <li>
            <a href="/concepts/555">Advanced SQL</a>
          </li>
      </ul>
    </div>
  </div>
      <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/8w9di_hk19DIMSBEV3EayQ" title="MySQL cheatsheet" target="_blank">MySQL cheatsheet</a></li>
<li><a href="/rltoken/2GJbZ48zRPA70o2YhTdH7g" title="MySQL Performance: How To Leverage MySQL Database Indexing" target="_blank">MySQL Performance: How To Leverage MySQL Database Indexing</a></li>
<li><a href="/rltoken/K180X2OCzb6gzPngjn-EIg" title="Stored Procedure" target="_blank">Stored Procedure</a></li>
<li><a href="/rltoken/cJ1qA4o-rRm4rWIsqYKSZg" title="Triggers" target="_blank">Triggers</a></li>
<li><a href="/rltoken/vHg1z3UAOcWMvOt8xZHeiA" title="Views" target="_blank">Views</a></li>
<li><a href="/rltoken/g-c1m6iljScpi4LeqxBRqQ" title="Functions and Operators" target="_blank">Functions and Operators</a></li>
<li><a href="/rltoken/gLVwKjQfRL0Jr_nWqAS7VQ" title="Trigger Syntax and Examples" target="_blank">Trigger Syntax and Examples</a></li>
<li><a href="/rltoken/X789nJ22H6HVh1uCQPl0lg" title="CREATE TABLE Statement" target="_blank">CREATE TABLE Statement</a></li>
<li><a href="/rltoken/mfrWMt1KL3NHXblJykMgZg" title="CREATE PROCEDURE and CREATE FUNCTION Statements" target="_blank">CREATE PROCEDURE and CREATE FUNCTION Statements</a></li>
<li><a href="/rltoken/oCu8Rg9WfKyF4BhTt8dZGQ" title="CREATE INDEX Statement" target="_blank">CREATE INDEX Statement</a></li>
<li><a href="/rltoken/FEZNlZFKZmD1ISnLINkCwQ" title="CREATE VIEW Statement" target="_blank">CREATE VIEW Statement</a></li>
</ul>

<h2>KNOWLEDGE CHECK</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/NEA0Fr7muHfukl5lziVAhg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create tables with constraints</li>
<li>How to optimize queries by adding indexes</li>
<li>What is and how to implement stored procedures and functions in MySQL</li>
<li>What is and how to implement views in MySQL</li>
<li>What is and how to implement triggers in MySQL</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>All your files will be executed on Ubuntu 18.04 LTS using <code>MySQL 5.7</code> (version 5.7.30)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>&hellip;)</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Comments for your SQL file:</h3>

<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>

<h3>Use &ldquo;container-on-demand&rdquo; to run MySQL</h3>

<ul>
<li>Ask for container <code>Ubuntu 18.04 - Python 3.7</code></li>
<li>Connect via SSH</li>
<li>Or via the WebTerminal</li>
<li>In the container, you should start MySQL before playing with it:</li>
</ul>

<pre><code>$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
</code></pre>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>

<h3>How to import a SQL dump</h3>

<pre><code>$ echo &quot;CREATE DATABASE hbtn_0d_tvshows;&quot; | mysql -uroot -p
Enter password: 
$ curl &quot;https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql&quot; -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo &quot;SELECT * FROM tv_genres&quot; | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
</code></pre>

  </div>
</div>       
          <h2 class="gap">TASKS mandatory</h2>
    <div data-role="task11633" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-11633">
  <span id="user_id" data-id="251885"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. We are all unique!
    </h3>
    
  </div>

   <!-- Task Body -->
   <p>Write a SQL script that creates a table <code>users</code> following these requirements:</p>

<ul>
<li>With these attributes:

<ul>
<li><code>id</code>, integer, never null, auto increment and primary key</li>
<li><code>email</code>, string (255 characters), never null and unique</li>
<li><code>name</code>, string (255 characters)</li>
</ul></li>
<li>If the table already exists, your script should not fail</li>
<li>Your script can be executed on any database</li>
</ul>

<p><strong>Context:</strong>
<em>Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application</em></p>

</div>
<div>
    <h3>1. In and not out</h3>
    <!-- Task Body -->
    <p>Write a SQL script that creates a table <code>users</code> following these requirements:</p>

<ul>
<li>With these attributes:

<ul>
<li><code>id</code>, integer, never null, auto increment and primary key</li>
<li><code>email</code>, string (255 characters), never null and unique</li>
<li><code>name</code>, string (255 characters)</li>
<li><code>country</code>, enumeration of countries: <code>US</code>, <code>CO</code> and <code>TN</code>, never null (= default will be the first element of the enumeration, here <code>US</code>)</li>
</ul></li>
<li>If the table already exists, your script should not fail</li>
<li>Your script can be executed on any database</li>
</ul>
<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Best band ever!
    </h3>
    <!-- Task Body -->
    <p>Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Import this table dump: <a href="/rltoken/uPn947gnZLaa0FJrrAFTGQ" title="metal_bands.sql.zip" target="_blank">metal_bands.sql.zip</a></li>
<li>Column names must be: <code>origin</code> and <code>nb_fans</code></li>
<li>Your script can be executed on any database</li>
</ul>

<p><strong>Context:</strong>
<em>Calculate/compute something is always power intensive&hellip; better to distribute the load!</em></p>
   
<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Old school band
    </h3>
        <!-- Task Body -->
    <p>Write a SQL script that lists all bands with <code>Glam rock</code> as their main style, ranked by their longevity</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Import this table dump: <a href="/rltoken/uPn947gnZLaa0FJrrAFTGQ" title="metal_bands.sql.zip" target="_blank">metal_bands.sql.zip</a></li>
<li>Column names must be: <code>band_name</code> and <code>lifespan</code> (in years <strong>until 2022</strong> - please use <code>2022</code> instead of <code>YEAR(CURDATE())</code>)</li>
<li>You should use attributes <code>formed</code> and <code>split</code> for computing the <code>lifespan</code></li>
<li>Your script can be executed on any database</li>
</ul>
<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Buy buy buy
    </h3>
    <!-- Task Body -->
    <p>Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.</p>

<p>Quantity in the table <code>items</code> can be negative.</p>

<p><strong>Context:</strong>
<em>Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc&hellip; to keep your data in a good shape, let MySQL do it 
<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Email validation to sent
    </h3>
  </div>

  <!-- Task Body -->
   <p>Write a SQL script that creates a trigger that resets the attribute <code>valid_email</code> only when the <code>email</code> has been changed.</p>

<p><strong>Context:</strong>
<em>Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!</em></p>
 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Add bonus
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="251885"></span>

<!-- Task Body -->
   <p>Write a SQL script that creates a stored procedure <code>AddBonus</code> that adds a new correction for a student.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Procedure <code>AddBonus</code> is taking 3 inputs (in this order):

<ul>
<li><code>user_id</code>, a <code>users.id</code> value (you can assume <code>user_id</code> is linked to an existing <code>users</code>)</li>
<li><code>project_name</code>, a new or already exists <code>projects</code> - if no <code>projects.name</code> found in the table, you should create it</li>
<li><code>score</code>, the score value for the correction</li>
</ul></li>
</ul>

<p><strong>Context:</strong>
<em>Write code in SQL is a nice level up!</em></p>
</div>
  </div>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Average score
    </h3>

    
  </div>

   <!-- Task Body -->
   <p>Write a SQL script that creates a stored procedure <code>ComputeAverageScoreForUser</code> that computes and store the average score for a student.
Note: An average score can be a decimal</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Procedure <code>ComputeAverageScoreForUser</code> is taking 1 input:

<ul>
<li><code>user_id</code>, a <code>users.id</code> value (you can assume <code>user_id</code> is linked to an existing <code>users</code>)</li>
</ul></li>
</ul>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. Optimize simple search
    </h3>

    

  <div class="panel-body">
    <span id="user_id" data-id="251885"></span>

<!-- Task Body -->
   <p>Write a SQL script that creates an index <code>idx_name_first</code> on the table <code>names</code> and the first letter of <code>name</code>.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Import this table dump: <a href="/rltoken/BluyCCIIfw0NqcjqUiUdEw" title="names.sql.zip" target="_blank">names.sql.zip</a></li>
<li>Only the first letter of <code>name</code> must be indexed</li>
</ul>

<p><strong>Context:</strong>
<em>Index is not the solution for any performance issue, but well used, it&rsquo;s really powerful!</em></p>


  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      10. Safe divide
    </h3>
  </div>
    <!-- Task Body -->
    <p>Write a SQL script that creates a function <code>SafeDiv</code> that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>You must create a function</li>
<li>The function <code>SafeDiv</code> takes 2 arguments:

<ul>
<li><code>a</code>, INT</li>
<li><code>b</code>, INT</li>
</ul></li>
<li>And returns <code>a / b</code> or 0 if <code>b == 0</code></li>
</ul>
</div>  
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      11. No table for a meeting
    </h3>
  </div>
<ul>
<li>The view <code>need_meeting</code> should return all students name when:

<ul>
<li>They score are under (strict) to 80</li>
<li><strong>AND</strong> no <code>last_meeting</code> date <strong>OR</strong> more than a month</li>
</ul></li>
</ul>
</div>
</div>
</div>
</div>

<h2>NOTES</h2>
<h3>MSQL CHEETSHEET</h3>
browing your database
<pre>
SHOW DATABASES;
SHOW TABLES # for viewing tables in a database
SHOW FIELDS FROM table_name / DESCRIBE table; # for viewing columns in a table
SHOW CREATE TABLE table_name; # for viewing the CREATE TABLE statement
SHOW INDEX FROM table_name; # for viewing indexes in a table
SHOW PROCESSLIST; # for viewing active connections
SHOW STATUS; # for viewing global status
KILL process_number; # for killing a connection
</pre>

Selecting
<pre>
SELECT * FROM table; # for selecting all rows from a table
SELECT * FROM table1, table2; # for selecting rows from multiple tables

SELECT field1, field2 FROM table1, table2; # for selecting specific columns from multiple tables
SELECT field1, field2 FROM table1, table2 WHERE condition; # for selecting specific columns from multiple tables

SELECT ... FROM ... WHERE condition # for selecting rows from a table that meet a certain condition

SELECT ... FROM ... WHERE condition AND condition2; # for selecting rows from a table that meet multiple conditions
SELECT ... FROM ... WHERE condition OR condition2; # for selecting rows from a table that meet at least one of the conditions
SELECT ... FROM ... WHERE condition GROUP BY field; # for grouping rows from a table
SELECT ... FROM ... WHERE condition GROUP BY field HAVING condition2; # for grouping rows from a table and then selecting only the rows that meet a certain condition
SELECT ... FROM ... WHERE condition ORDER BY field1, field2; # for ordering rows from a table
SELECT ... FROM ... WHERE condition ORDER BY field1, field2 DESC; # for ordering rows from a table in descending order
SELECT ... FROM ... WHERE condition LIMIT 10; # for limiting the number of rows returned
SELECT DISTINCT field1 FROM ...; # for selecting only distinct values from a table
SELECT DISTINCT field1, field2 FROM ...; # for selecting only distinct values from a table
</pre>
<b> SELECT JOIN </b>
<pre>
SELECT * FROM table1 JOIN table2 ON condition; # for selecting rows from multiple tables
SELECT * FROM table1 LEFT JOIN table2 ON condition; # for selecting rows from multiple tables and including rows from table2 that don&rsquo;t have a match in table1
SELECT ... FROM t1 JOIN t2 ON t1.id1 = t2.id2 WHERE condition; # for selecting rows from multiple tables and including rows from table2 that don&rsquo;t have a match in table1
SELECT ... FROM t1 LEFT JOIN t2 ON t1.id1 = t2.id2 WHERE condition; # for selecting rows from multiple tables and including rows from table2 that don&rsquo;t have a match in table1
SELECT ... FROM t1 JOIN (t2 JOIN t3 ON ...) ON ... # for selecting rows from multiple tables and including rows from table2 that don&rsquo;t have a match in table1
</pre>
<b> CONDITONS </b>
<pre>
field1 = value1 # for selecting rows where field1 is equal to value1
field1 <> value1 # for selecting rows where field1 is not equal to value1
field1 LIKE 'value _ %' # for selecting rows where field1 matches a certain pattern
field1 IS NULL # for selecting rows where field1 is null
field1 IS NOT NULL # for selecting rows where field1 is not null

field1 IS IN (value1, value2) # for selecting rows where field1 is equal to value1 or value2
field1 IS NOT IN (value1, value2) # for selecting rows where field1 is not equal to value1 or value2
condition1 AND condition2 # for selecting rows where condition1 AND condition2
condition1 OR condition2 # for selecting rows where condition1 OR condition2
</pre>

<b> CREATE / OPEN DELETE DATABASE </b>
<pre>
CREATE DATABASE DatabaseName; # for creating a database
CREATE DATABASE DatabaseName CHARACTER SET utf8; # for creating a database with a specific character set
USE DatabaseName; # for opening a database
DROP DATABASE DatabaseName; # for deleting a database
ALTER DATABASE DatabaseName CHARACTER SET utf8; # for changing the character set of a database
</pre>
DELETE
<pre> 
DELETE FROM table1 / TRUNCATE table1;
# for deleting all rows from a table
DELETE FROM table1 WHERE condition; # for deleting rows from a table that meet a certain condition
DELETE FROM table1, table2 WHERE table1.id1 = table2.id2 AND condition; # for deleting rows from multiple tables that meet a certain condition
</pre>
UPDATES
<pre>
UPDATE table1 SET field1=new_value1 WHERE condition;
UPDATE table1, table2 SET field1=new_value1, field2=new_value2, ... WHERE
  table1.id1 = table2.id2 AND condition;
  </pre>
  <pre>
CREATE DELETE MODIFY TABLE
CREATE TABLE table (field1 type1, field2 type2);
CREATE TABLE table (field1 type1, field2 type2, INDEX (field));
CREATE TABLE table (field1 type1, field2 type2, PRIMARY KEY (field1));
CREATE TABLE table (field1 type1, field2 type2, PRIMARY KEY (field1,field2));
<br>
<hr>
EATE TABLE table1 (fk_field1 type1, field2 type2, ...,
  FOREIGN KEY (fk_field1) REFERENCES table2 (t2_fieldA))
    [ON UPDATE|ON DELETE] [CASCADE|SET NULL]
<hr>
CREATE TABLE table1 (fk_field1 type1, fk_field2 type2, ...,
 FOREIGN KEY (fk_field1, fk_field2) REFERENCES table2 (t2_fieldA,t2_fieldB))
 <hr>
 CREATE TABLE table IF NOT EXISTS;
 <hr>
CREATE TEMPORARY TABLE table;
<hr>
<b> DROP </b>
<hr>
DROP TABLE table;
DROP TABLE IF EXISTS table;<br>
DROP TABLE table1, table2, ...
<br><b>ALTER</b>
ALTER TABLE table MODIFY field1 type1
ALTER TABLE table MODIFY field1 type1 NOT NULL ...
ALTER TABLE table CHANGE old_name_field1 new_name_field1 type1
ALTER TABLE table CHANGE old_name_field1 new_name_field1 type1 NOT NULL ...
ALTER TABLE table ALTER field1 SET DEFAULT ...
ALTER TABLE table ALTER field1 DROP DEFAULT
ALTER TABLE table ADD new_name_field1 type1
ALTER TABLE table ADD new_name_field1 type1 FIRST
ALTER TABLE table ADD new_name_field1 type1 AFTER another_field
ALTER TABLE table DROP field1
ALTER TABLE table ADD INDEX (field);
<br>CHANGE FIELD ORDR
<br>
ALTER TABLE table MODIFY field1 type1 FIRST
ALTER TABLE table MODIFY field1 type1 AFTER another_field
ALTER TABLE table CHANGE old_name_field1 new_name_field1 type1 FIRST
ALTER TABLE table CHANGE old_name_field1 new_name_field1 type1 AFTER
  another_field
</pre>
KEY
<br>
<pre>
CREATE TABLE table (..., PRIMARY KEY (field1, field2))
CREATE TABLE table (..., FOREIGN KEY (field1, field2) REFERENCES table2
(t2_field1, t2_field2))
</pre>
USERS AND PRIVILEDGE
<pre>
CREATE USER 'user'@'localhost';
GRANT ALL PRIVILEGES ON base.* TO 'user'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, INSERT, DELETE ON base.* TO 'user'@'localhost' IDENTIFIED BY 'password';
REVOKE ALL PRIVILEGES ON base.* FROM 'user'@'host'; -- one permission only
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user'@'host'; -- all permissions
FLUSH PRIVILEGES;
<hr>
PASSWORD
SET PASSWORD = PASSWORD('new_pass');
SET PASSWORD FOR 'user'@'host' = PASSWORD('new_pass');
SET PASSWORD = OLD_PASSWORD('new_pass');
<hr>
DROP USER 'user'@'host';
</pre>
host '%' means any host
<br>
MAIN DATA TYPES
<pre>
TINYINT (1o: -128 to +127)
SMALLINT (2o: +-65 000)
MEDIUMINT (3o: +-16 000 000)
INT (4o: +- 2 000 000 000)
BIGINT (8o: +-9.10^18)
<hr>
Precise interval: -(2^(8*N-1)) -> (2^8*N)-1
⚠ INT(2) = “2 digits displayed” – NOT “number with 2 digits max”
<hr>
FLOAT(M,D)
DOUBLE(M,D)
FLOAT(D=0->53)
⚠ 8,3 -> 12345,678 – NOT 12345678,123!
<hr>
TIME (HH:MM)
YEAR (AAAA)
DATE (AAAA-MM-JJ)
DATETIME (AAAA-MM-JJ HH:MM; années 1000->9999)
TIMESTAMP (like DATETIME, but 1970->2038, compatible with Unix)
<hr>
VARCHAR (single-line; explicit size)
TEXT (multi-lines; max size=65535)
BLOB (binary; max size=65535)
Variants for TEXT&BLOB: TINY (max=255), MEDIUM (max=~16000), and LONG (max=4Go). Ex: VARCHAR(32), TINYTEXT, LONGBLOB, MEDIUMTEXT
<hr>
ENUM ('value1', 'value2', ...) -- (default NULL, or '' if NOT NULL)
</pre>
RESET ROOT PASSWORD
<pre>
$ /etc/init.d/mysql stop
 <hr>
$ mysqld_safe --skip-grant-tables
<hr>
$ mysql # on another terminal
mysql> UPDATE mysql.user SET password=PASSWORD('new_pass') WHERE user='root';
<hr>
## Switch back to the mysqld_safe terminal and kill the process using Control + \
$ /etc/init.d/mysql start
</pre>
<h2> MySQL Performance: How To Leverage MySQL Database Indexing </h2>
<h3>WHAT IS INDEXING</h3>
<li>Is a structure that can be used to get fastest response from common queries
<li>smaller tablesare generated faster by generating small tables called <code>index</code> from a specified columnor set of columns.
<li>a colum is called a <code>key</code> and can be used to enforce uniqueness.
</li>
<code>+------+----------+----------+<br/>
|  ROW | COLUMN_1 | COLUMN_2 |<br/>
+------+----------+----------+<br/>
|    1 |    data1 |    data2 |<br/>
+------+----------+----------+<br/>
|    2 |    data1 |    data1 |<br/>
+------+----------+----------+<br/>
|    3 |    data1 |    data1 |<br/>
+------+----------+----------+<br/>
|    4 |    data1 |    data1 |<br/>
+------+----------+----------+<br/>
|    5 |    data1 |    data1 |<br/>
+------+----------+----------+</code></p></div>
<li> Queries utilizeindexes to identify and retrieve the target data even if they are a combination of keys
<li>without index, the query will result in inspecting  every row to find the target data.
<li>Indexing produce a fastest response for queries that use the indexed columns.
</li>
<h2> WHEN TO ENABLE INDEXING </h2>
<li>Indexingif good when working with huge tables that has regular accessed data
</li>
<h2>WHAT TO INDEX</h2>
<li>Columns that are used in WHERE clause
<li>Columns that are used in ORDER BY clause
</li>
<h2>WHAT IS A UNIQUE INDEX</h2>
<li>A unique index is an index that can be used to enforce uniqueness of a column or set of columns.
<li> this is based on the configured index key
<li>constraint will ensure that there are no duplicates entrys in the table based on configured key
</li>
<h2>WHAT IS A PRIMARY KEY INDEX</h2>
<li>A primary key index is an index that can be used to enforce uniqueness of a column or set of columns.
<li> pimary key is used yo optimize indexes and speed up queries.
<li> primary key is used to uniquely identify a row in a table.
<li>It helps to make sure that the desgnated PRIMARY KEY cannot be null
</li>
<h2>MANAGING INDEXES</h2>
this include 
  <li> <code>CREATING</code>
  <li><code> DELETION</code>
  <li> <code>LISTING</code>
  </li>
<h3>1 Listing/ Showing Indexes </h3>
Tables can have more than one index<br>
<b><em>SYNTAX USED:</em></b>
<pre> SHOW INDEX FROM table_name</pre>
<h3> 2 CREATING INDEXES </h3>
<li>you determine the index where to enforce uniqueness when necessary
<li>Indexes can be created when creating a table or after a table is created
<li>Indexes can be created on a single column or multiple columns
<li>Indexes can be created on a single column with a unique constraint or multiple columns with a unique constraint
<li>
EXAMPLE
<b><em>SYNTAX: <br><strong> 1creating table with standard INDEX</strong></em></b>
<pre>
CREATE TABLE tableName (
ID int,
LName varchar(255),
FName varchar(255),
DOB varchar(255),
LOC varchar(255),
INDEX ( ID )
);
</pre>
<hr>
 <strong> 2 Create a Table with Unique Index & Primary Key</strong>
 <pre>
 CREATE TABLE tableName (
ID int,
LName varchar(255),
FName varchar(255),
DOB varchar(255),
LOC varchar(255),
PRIMARY KEY (ID),
UNIQUE INDEX ( ID )
);
</pre>
<hr>
 <strong> Add an Index to Existing Table</strong>
 <pre>
 CREATE INDEX indexName ON tableName (ID, LName, FName, LOC);
 </pre>
 <hr>
 <strong>Add an Index to Existing Table with Primary Key</strong>
<pre>
CREATE UNIQUE INDEX indexName ON tableName (ID, LName, FName, LOC);
</pre>
<hr>
<h3>  DELETING INDEXES </h3>
<li>Indexes can be deleted when a table is dropped or after a table is created
<pre>
DROP INDEX indexName ON tableName;
</pre>
</body>
</html>