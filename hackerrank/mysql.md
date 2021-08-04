

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

