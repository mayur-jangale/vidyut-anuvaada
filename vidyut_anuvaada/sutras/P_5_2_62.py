# Sutra प.5.2.62: गोषदादिभ्यो वुन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — gozadAdiByo vun

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.62"
SUTRA_TEXT = "गोषदादिभ्यो वुन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — gozadAdiByo vun"


class Sutra5262:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.62: अग्निः'),
		('रामः', '', 'प.5.2.62: रामः'),
		('सीता', '', 'प.5.2.62: सीता'),
	]

