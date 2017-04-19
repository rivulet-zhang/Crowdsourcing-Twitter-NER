create table
ETY
(
	id 			integer primary key,
	name    	text      not null,
	source    	text      not null,
	user    	text      not null,
	tweet_time 	text      not null,
	context    	text      not null,
	convers_id 	text      not null,
	isAuto    	text      not null,
	comment    	text      
);

create table
NPO
(
	id 			integer primary key,
	name    	text      not null,
	class    	text      not null,
	description text      not null,
	dest    	text      not null
);

create table
TWEETS
(
	id 			integer primary key,
	user    	text      not null,
	tweet_time 	text      not null,
	content    	text      not null,
	convers_id 	text      not null
);