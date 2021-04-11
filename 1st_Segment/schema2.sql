  
-- Creating table for final_projectDB
CREATE TABLE reddit (
	title VARCHAR (40) NOT NULL,
	score INT,
	subreddit VARCHAR,
	url VARCHAR,
	num_comments INT,
	body VARCHAR,
	date TIMESTAMP
);

SELECT * FROM reddit;