import re

def get_matching_words(regex):
	print "working..."
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

 	return [word for word in words if re.search(regex, word)]

matchCriteria = [r"v",r's+',r"e$",r"b.b",r"b[^b]b",r"b.b",r"aeiou",r"[regulaxpsion]",r"(.)\1"]


for x in range(len(matchCriteria)):
	# print matchCriteria(x)

	matches = get_matching_words(matchCriteria[x])

	if matches:
		print matches
	else:
		print "no matches"

