# Sutra प.7.3.62: प्रयाजानुयाजौ यज्ञाङ्गे
# (Taddhita (secondary derivations)) — prayAjAnuyAjO yajYANge

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.62"
SUTRA_TEXT = "प्रयाजानुयाजौ यज्ञाङ्गे"
SUTRA_DESC = "(Taddhita (secondary derivations)) — prayAjAnuyAjO yajYANge"


class Sutra7362:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.62: अग्निः'),
		('रामः', '', 'प.7.3.62: रामः'),
		('सीता', '', 'प.7.3.62: सीता'),
	]

