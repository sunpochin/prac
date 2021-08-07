

### Weather Observation Station 5: ( https://www.hackerrank.com/challenges/weather-observation-station-5/problem?h_r=next-challenge&h_v=zen )
  
  * Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
The STATION table is described as follows:
  ~~~~sql
    * SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) ASC, CITY ASC LIMIT 1;
    SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) DESC, CITY ASC LIMIT 1;
  ~~~~


### Weather Observation Station 6
  * Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
  
~~~~sql
SELECT city FROM station WHERE REGEXP_LIKE(city,'^[aeiou].*');
~~~~


### Weather Observation Station 7
  * Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
  
~~~~sql
SELECT DISTINCT city FROM station WHERE REGEXP_LIKE(city,'^.*[aeiou]$');
~~~~


### Weather Observation Station 8 (https://www.hackerrank.com/challenges/weather-observation-station-8/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_r=next-challenge&h_v=zen)

  * Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

~~~~sql
SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(CITY,'^[aeiou].*[aeiou]$');
~~~~
  



~~~~sql
SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(CITY,'^(?!aeiou).*');
~~~~

~~~~sql
SELECT DISTINCT city FROM station WHERE substr(city, 1, 1) NOT IN ('a','e','i','o','u');
~~~~

  * Putting a ^ inside the closed bracket means something completely different than putting it outside the brackets. Putting it inside the brackets makes it match all characters EXCEPT the ones inside the bracket. So instead of writing [bcdfghjklmnpqrstvwxyz], we can write [^aeiou]


### Weather Observation Station 8 ( www.hackerrank.com/challenges/weather-observation-station-11/ )

~~~~sql
SELECT DISTINCT CITY FROM STATION WHERE SUBSTR(CITY, LENGTH(CITY), 1) NOT IN ('a','e','i','o','u') OR SUBSTR(CITY, 1, 1) NOT IN ('a','e','i','o','u');
~~~~


### Weather Observation Station 12 ( https://www.hackerrank.com/challenges/weather-observation-station-12/problem )

~~~~sql
SELECT DISTINCT CITY FROM STATION WHERE SUBSTR(CITY, LENGTH(CITY), 1) NOT IN ('a','e','i','o','u') AND SUBSTR(CITY, 1, 1) NOT IN ('a','e','i','o','u');
~~~~


### Higher Than 75 Marks ( https://www.hackerrank.com/challenges/more-than-75-marks/problem )

~~~~sql
SELECT * FROM STUDENTS WHERE MARKS > 75 ORDER BY SUBSTR(NAME, LENGTH(NAME) - 3, 3);
~~~~


### Higher Than 75 Marks ( https://www.hackerrank.com/challenges/more-than-75-marks/problem )

~~~~sql
SELECT NAME FROM STUDENTS WHERE MARKS > 75 ORDER BY SUBSTR(NAME, LENGTH(NAME) - 2, 3), ID ASC;
~~~~


### The PADS ( https://www.hackerrank.com/challenges/the-pads/problem )

~~~~sql
select concat(occupation, '(', substr(occupation, 1, 1), ')') as name from occupations;
~~~~
