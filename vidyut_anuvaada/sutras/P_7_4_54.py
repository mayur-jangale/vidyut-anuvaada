# Sutra प.7.4.54: सनि मीमाघुरभलभशकपतपदामच इस्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.54"
SUTRA_TEXT = "सनि मीमाघुरभलभशकपतपदामच इस्"
SUTRA_DESC = "taddhita — continued"


class Sutra7454:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.54: अग्निः'),
		('रामः', '', 'प.7.4.54: रामः'),
		('सीता', '', 'प.7.4.54: सीता'),
	]

