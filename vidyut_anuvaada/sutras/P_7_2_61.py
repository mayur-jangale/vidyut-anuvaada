# Sutra प.7.2.61: अचस्तास्वत् थल्यनिटो नित्यम्
# (Taddhita (secondary derivations)) — acastAsvat Talyaniwo nityam

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.61"
SUTRA_TEXT = "अचस्तास्वत् थल्यनिटो नित्यम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — acastAsvat Talyaniwo nityam"


class Sutra7261:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.61: अग्निः'),
		('रामः', '', 'प.7.2.61: रामः'),
		('सीता', '', 'प.7.2.61: सीता'),
	]

