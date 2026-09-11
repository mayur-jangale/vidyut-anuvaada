# Sutra प.7.2.53: अञ्चेः पूजायाम्
# (Taddhita (secondary derivations)) — aYceH pUjAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.53"
SUTRA_TEXT = "अञ्चेः पूजायाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — aYceH pUjAyAm"


class Sutra7253:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.53: अग्निः'),
		('रामः', '', 'प.7.2.53: रामः'),
		('सीता', '', 'प.7.2.53: सीता'),
	]

