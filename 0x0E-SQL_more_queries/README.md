# 0x0D SQL - Introduction :snake:

> SQL is a domain-specific language used in programming and designed for managing data held in a relational database management system, or for stream processing in a relational data stream management system. This project covers the part 2 of SQL. The purpose of these SQL projects is to gain skills to manipulate SQL along Python to enhance the data engineering

At the end of this project, I was able to solve these questions:
  
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

## Tasks :heavy_check_mark:

0. Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
1. Script that creates the MySQL server user user_0d_1.
2. Script that creates the database hbtn_0d_2 and the user user_0d_2.
3. Script that creates the table force_name on your MySQL server.
4. Script that creates the table id_not_null on your MySQL server.
5. Script that creates the table unique_id on your MySQL server.
6. Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
7. Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
8. Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
9. Script that lists all cities contained in the database hbtn_0d_usa.
10. Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
11. Script that lists all shows contained in the database hbtn_0d_tvshows.
12. Script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
13. Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
14. Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
15. Script that lists all Comedy shows in the database hbtn_0d_tvshows.
16. Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
17. Script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
18. Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
19. Script that lists all shows from hbtn_0d_tvshows_rate by their rating.
20. Script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
 

## Results :chart_with_upwards_trend:

| Filename |||||
| ------ |---|---|---|---|
| [0-privileges.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/0-privileges.sql)| [1-create_user.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/1-create_user.sql)|[2-create_read_user.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/2-create_read_user.sql)|[3-force_name.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/3-force_name.sql)|[4-never_empty.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/4-never_empty.sql)|
| [5-unique_id.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/5-unique_id.sql)| [6-states.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/6-states.sql)|[7-cities.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/7-cities.sql)|[8-cities_of_california_subquery.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/8-cities_of_california_subquery.sql)|[9-cities_by_state_join.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/9-cities_by_state_join.sql)|
| [10-genre_id_by_show.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/10-genre_id_by_show.sql)| [11-genre_id_all_shows.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/11-genre_id_all_shows.sql)|[12-no_genre.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/12-no_genre.sql)|[13-count_shows_by_genre.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/13-count_shows_by_genre.sql)|[14-my_genres.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/14-my_genres.sql)|
| [15-comedy_only.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/15-comedy_only.sql)| [16-shows_by_genre.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/16-shows_by_genre.sql)|[100-not_my_genres.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/100-not_my_genres.sql)|[101-not_a_comedy.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/101-not_a_comedy.sql)|[102-rating_shows.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/102-rating_shows.sql)|
|[103-rating_genres.sql](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/103-rating_genres.sql)|


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
