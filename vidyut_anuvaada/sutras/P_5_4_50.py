# Sutra प.5.4.50: अभूततद्भावे कृभ्वस्तियोगे सम्पद्यकर्तरि च्विः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aBUtatadBAve kfBvastiyoge sampadyakartari cviH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.50"
SUTRA_TEXT = "अभूततद्भावे कृभ्वस्तियोगे सम्पद्यकर्तरि च्विः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aBUtatadBAve kfBvastiyoge sampadyakartari cviH"


class Sutra5450:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.50: अग्निः'),
		('रामः', '', 'प.5.4.50: रामः'),
		('सीता', '', 'प.5.4.50: सीता'),
	]

