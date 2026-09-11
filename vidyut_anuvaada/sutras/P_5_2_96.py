# Sutra प.5.2.96: प्राणिस्थादातो लजन्यतरस्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prARisTAdAto lajanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.96"
SUTRA_TEXT = "प्राणिस्थादातो लजन्यतरस्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prARisTAdAto lajanyatarasyAm"


class Sutra5296:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.96: अग्निः'),
		('रामः', '', 'प.5.2.96: रामः'),
		('सीता', '', 'प.5.2.96: सीता'),
	]

