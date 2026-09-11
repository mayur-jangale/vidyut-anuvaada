# Sutra प.5.4.47: हीयमानपापयोगाच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — hIyamAnapApayogAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.47"
SUTRA_TEXT = "हीयमानपापयोगाच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — hIyamAnapApayogAcca"


class Sutra5447:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.47: अग्निः'),
		('रामः', '', 'प.5.4.47: रामः'),
		('सीता', '', 'प.5.4.47: सीता'),
	]

