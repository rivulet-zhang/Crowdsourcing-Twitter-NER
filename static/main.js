'use strict';

// tweet['entity'] = []
// tweet['entity'].append({'type':'org', 'term':'Purdue Univeristy', 'isAuto':True})
function styling_tweet(tweet){

	var text_html = tweet['text'];

	tweet['entity'].forEach(function(entity){
		var s = text_html.search(entity.term);
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