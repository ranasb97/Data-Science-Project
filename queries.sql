CREATE TABLE automobiles (
    name VARCHAR(100),
    mpg FLOAT,
    cylinders INT,
    displacement FLOAT,
    horsepower FLOAT,
    weight INT,
    acceleration FLOAT,
    model_year INT,
    origin VARCHAR(20)
);

-- Average MPG
SELECT AVG(mpg) FROM automobiles;

-- Highest horsepower cars
SELECT name, horsepower
FROM automobiles
ORDER BY horsepower DESC
LIMIT 5;

-- Average MPG by origin
SELECT origin, AVG(mpg)
FROM automobiles
GROUP BY origin;

-- Heaviest cars
SELECT name, weight
FROM automobiles
ORDER BY weight DESC
LIMIT 10;