-- Query to list shows by ranking
SELECT title, SUM(rate) AS rate
  FROM tv_shows AS shows
       INNER JOIN tv_show_ratings AS rating
	   ON shows.id = rating.show_id
 GROUP BY title ORDER BY rate DESC;
