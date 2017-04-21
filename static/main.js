'use strict';

//change color of text if it is a entity;
function styling_tweet_entity(tweet){

	var text_html = tweet['content'];

	tweet['entity'].forEach(function(entity){

    if(!entity.hasOwnProperty('term'))
      return;

		var s = text_html.toLowerCase().search(entity.term.toLowerCase());
		if(s < 0 || s >= text_html.length)
			console.error("error parsing entity");
		else{
			var token = "<b><font color='" + get_entity_color(entity.type) + "'>" + entity.term + "</font></b>";
			text_html = text_html.slice(0, s) + token + text_html.slice(s+entity.term.length);
		}
	});

  tweet['text_tagged'] = text_html;
	return tweet;
}

// add the entity from user input to the tweet list;
function add_entity_in_tweets(tweets, npo, ety, type, comment){

  tweets.forEach(function(tweet){

    if(tweet['content'].toLowerCase().indexOf(npo.toLowerCase()) !== -1){
      tweet.entity.push({'type':type, 'npo':npo, 'ety':ety, 'isAuto':false, 'comment':comment});
    }

  });

  return tweets;

}

// check if a term exists in the tweet;
function check_term_exist_in_tweets(tweets, term){

    var flag = false;
    tweets.forEach(function(tweet){
      if(tweet['content'].toLowerCase().indexOf(term.toLowerCase()) !== -1){
        flag = true;
      }
    });
    return flag;
}