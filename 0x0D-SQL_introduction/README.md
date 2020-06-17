# 0x0D SQL - Introduction :snake:

> SQL is a domain-specific language used in programming and designed for managing data held in a relational database management system, or for stream processing in a relational data stream management system. This project covers the part 1 of SQL. The purpose of these SQL projects is to gain skills to manipulate SQL along Python to enhance the data engineering

At the end of this project, I was able to solve these questions:
  
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

## Tasks :heavy_check_mark:

0. Script that lists all databases of your MySQL server
1. Script that creates the database hbtn_0c_0 in your MySQL server.
2. Script that deletes the database hbtn_0c_0 in your MySQL server.
3. Script that lists all the tables of a database in your MySQL server.
4. Script that creates a table called first_table in the current database in your MySQL server.
5. Script that creates a table called first_table in the current database in your MySQL server.
6. Script that creates a table called first_table in the current database in your MySQL server.
7. Script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
8. Script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
9. Script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
10. Script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
11. Script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
12. Script that updates the score of Bob to 10 in the table second_table.
13. Script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
14. Script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server. 
15. Script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server. 
16. Script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
17. Script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
18. Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
19. Script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
20. Script that displays the max temperature of each state (ordered by State name).
 

## Results :chart_with_upwards_trend:

| Filename |||||
| ------ |---|---|---|---|
| [0-list_databases.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/0-list_databases.sql)| [1-create_database_if_missing.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/1-create_database_if_missing.sql)|[2-remove_database.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/2-remove_database.sql)|[3-list_tables.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/3-list_tables.sql)|[4-first_table.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/4-first_table.sql)|
| [5-full_table.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/5-full_table.sql)| [6-list_values.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/6-list_values.sql)|[7-insert_value.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/7-insert_value.sql)|[8-count_89.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/8-count_89.sql)|[9-full_creation.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/9-full_creation.sql)|
| [10-top_score.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/10-top_score.sql)| [11-best_score.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/11-best_score.sql)|[12-no_cheating.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/12-no_cheating.sql)|[13-change_class.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/13-change_class.sql)|[14-average.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/14-average.sql)|
| [15-groups.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/15-groups.sql)| [16-no_link.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/16-no_link.sql)|[100-move_to_utf8.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/100-move_to_utf8.sql)|[101-avg_temperatures.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/101-avg_temperatures.sql)|[102-top_city.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/102-top_city.sql)|
|[103-max_state.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/103-max_state.sql)|


## Additional info :construction:
### Resources

- MySQL 5.7

### Try It On Your Machine :computer:	
```bash
git clone https://github.com/edward0rtiz/holbertonschool-higher_level_programming.git
cd 0x0D-SQL_introduction
CONNECT TO A SQL SERVER (ONCE INSTALLED)
mysql -hlocalhost -uroot -p
TEST SCRIPT
cat FILENAME.sql | mysql -hlocalhost -uroot -p
```
