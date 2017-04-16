create table
suggested_vehicle
(
	id 			integer primary key,
	recv_time	timestamp not null,
	maker    	text      not null,
	model    	text      not null,
	year     	integer   not null,
	category 	text      not null,
	link     	text      not null,
	explain  	text      not null,
	feedback  	text      not null,
	picked_date	text      not null,
	track		text	  not null
);