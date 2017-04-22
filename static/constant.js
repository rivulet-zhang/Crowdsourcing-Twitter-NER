'use strict';

const ENTITY_COLOR = {'ORGANIZATION':'#e41a1c', 'PERSON':'#377eb8', 'LOCATION':'#4daf4a', 'OTHERS':'#984ea3'};

function get_entity_color(type){
	return ENTITY_COLOR[type] || undefined;
}