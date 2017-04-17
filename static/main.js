'use strict';

// tweet['entity'] = []
// tweet['entity'].append({'type':'org', 'term':'Purdue Univeristy', 'isAuto':True})
function styling_tweet_entity(tweet){

	var text_html = tweet['text'];

	tweet['entity'].forEach(function(entity){
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

function get_tweet_entity(tweet){

  return tweet['entity'].map(function(entity){
                              return {term:entity.term, 'type':entity.type};
                            });
}

function add_entity_in_tweets(tweets, term, type, comment){

  tweets.forEach(function(tweet){

    if(tweet['text'].toLowerCase().indexOf(term.toLowerCase()) !== -1){
      tweet.entity.push({'type':type, 'term':term, 'isAuto':false, 'comment':comment});
    }

  });

  return tweets;

}

function check_term_exist_in_tweets(tweets, term){

    var flag = false;
    tweets.forEach(function(tweet){
      if(tweet['text'].toLowerCase().indexOf(term.toLowerCase()) !== -1){
        flag = true;
      }
    });
    return flag;
}