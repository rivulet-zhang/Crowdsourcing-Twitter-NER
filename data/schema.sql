create table
ETY
(
	id 			integer primary key,
	name    	text      not null,
	source    	text      not null,
	user    	text      not null,
	tweet_time 	text      not null,
	context    	text      not null,
	isAuto    	text      not null
);

create table
NPO
(
	id 			integer primary key,
	name    	text      not null,
	dest    	text      not null
);

create table
TWEETS
(
	id 			integer primary key,
	user    	text      not null,
	tweet_time 	text      not null,
	content    	text      not null,
	entities 	text      not null
);