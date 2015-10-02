walk(document.body);

function walk(node) {
	var child;

	switch (node.nodeType) {
		// Element
		case 1: 
			for (child = node.firstChild; child; child = child.nextSibling) {
				walk(child);
			}
			break;
		// Text
		case 3:
			node.nodeValue = handleText(node.nodeValue);
			break;
	}
}

function getRandomSub(uppercase) {
	r = Math.floor((Math.random() * 3) + 1); 
	if( uppercase == true ) {
		switch (r) {
			case 1:
				return "There";
			case 2:
				return "Their";
			case 3:
				return "They're";
		}
	}
	else {
		switch (r) {
			case 1:
				return "there";
			case 2:
				return "their";
			case 3:
				return "they're";
		}
	}
}

function handleText(str){
	w = str.split(/\b/); // Split on word boundaries
	for( var i = 0; i < w.length; i++ ) {
		if( w[i] == "Their" || w[i] == "There" || w[i] == "They're" ) {
			w[i] = getRandomSub(true);
		} else if( w[i] == "their" || w[i] == "there" || w[i] == "they're" ) {
			w[i] = getRandomSub(false);
		}
	}
	return w.join("");
}

