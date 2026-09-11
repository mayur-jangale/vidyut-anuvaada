# Sutra प.7.1.81: शप्श्यनोर्नित्यम्
# (Taddhita (secondary derivations)) — SapSyanornityam

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.81"
SUTRA_TEXT = "शप्श्यनोर्नित्यम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — SapSyanornityam"


class Sutra7181:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.81: अग्निः'),
		('रामः', '', 'प.7.1.81: रामः'),
		('सीता', '', 'प.7.1.81: सीता'),
	]

