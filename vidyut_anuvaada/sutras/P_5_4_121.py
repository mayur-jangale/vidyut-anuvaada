# Sutra प.5.4.121: नञ्दुःसुभ्यो हलिसक्थ्योरन्यतरस्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — naYduHsuByo halisakTyoranyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.121"
SUTRA_TEXT = "नञ्दुःसुभ्यो हलिसक्थ्योरन्यतरस्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — naYduHsuByo halisakTyoranyatarasyAm"


class Sutra54121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.121: अग्निः'),
		('रामः', '', 'प.5.4.121: रामः'),
		('सीता', '', 'प.5.4.121: सीता'),
	]

