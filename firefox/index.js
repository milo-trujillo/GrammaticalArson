var self = require('sdk/self');

// Every time a page loads, run firePayload(the_new_tab)
require("sdk/tabs").on("ready", firePayload);

// Inject our javascript payload into the new page
function firePayload(tab) {
	tab.attach({
		contentScriptFile: self.data.url("payload.js")
	});
}

// a dummy function, to show how tests work.
// to see how to test this function, look at test/test-index.js
function dummy(text, callback) {
  callback(text);
}

exports.dummy = dummy;
