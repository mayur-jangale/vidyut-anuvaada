# Sutra प.7.3.48: अभाषितपुंस्काच्च
# (Taddhita (secondary derivations)) — aBAzitapuMskAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.48"
SUTRA_TEXT = "अभाषितपुंस्काच्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — aBAzitapuMskAcca"


class Sutra7348:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.48: अग्निः'),
		('रामः', '', 'प.7.3.48: रामः'),
		('सीता', '', 'प.7.3.48: सीता'),
	]

