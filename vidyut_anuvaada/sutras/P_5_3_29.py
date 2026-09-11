# Sutra प.5.3.29: विभाषा परावराभ्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA parAvarAByAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.29"
SUTRA_TEXT = "विभाषा परावराभ्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA parAvarAByAm"


class Sutra5329:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.29: अग्निः'),
		('रामः', '', 'प.5.3.29: रामः'),
		('सीता', '', 'प.5.3.29: सीता'),
	]

