# Sutra प.7.2.13: कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि
# (Taddhita (secondary derivations)) — kfsfBfvfstudrusruSruvo liwi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.13"
SUTRA_TEXT = "कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — kfsfBfvfstudrusruSruvo liwi"


class Sutra7213:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.13: अग्निः'),
		('रामः', '', 'प.7.2.13: रामः'),
		('सीता', '', 'प.7.2.13: सीता'),
	]

