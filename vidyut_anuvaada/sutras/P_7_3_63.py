# Sutra प.7.3.63: वञ्चेर्गतौ
# (Taddhita (secondary derivations)) — vaYcergatO

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.63"
SUTRA_TEXT = "वञ्चेर्गतौ"
SUTRA_DESC = "(Taddhita (secondary derivations)) — vaYcergatO"


class Sutra7363:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.63: अग्निः'),
		('रामः', '', 'प.7.3.63: रामः'),
		('सीता', '', 'प.7.3.63: सीता'),
	]

