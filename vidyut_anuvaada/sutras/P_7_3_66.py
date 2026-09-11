# Sutra प.7.3.66: यजयाचरुचप्रवचर्चश्च
# (Taddhita (secondary derivations)) — yajayAcarucapravacarcaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.66"
SUTRA_TEXT = "यजयाचरुचप्रवचर्चश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yajayAcarucapravacarcaSca"


class Sutra7366:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.66: अग्निः'),
		('रामः', '', 'प.7.3.66: रामः'),
		('सीता', '', 'प.7.3.66: सीता'),
	]

