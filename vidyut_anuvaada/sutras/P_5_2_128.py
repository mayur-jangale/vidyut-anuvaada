# Sutra प.5.2.128: द्वन्द्वोपतापगर्ह्यात् प्राणिस्थादिनिः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvandvopatApagarhyAt prARisTAdiniH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.128"
SUTRA_TEXT = "द्वन्द्वोपतापगर्ह्यात् प्राणिस्थादिनिः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvandvopatApagarhyAt prARisTAdiniH"


class Sutra52128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.128: अग्निः'),
		('रामः', '', 'प.5.2.128: रामः'),
		('सीता', '', 'प.5.2.128: सीता'),
	]

