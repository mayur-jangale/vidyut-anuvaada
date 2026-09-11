# Sutra प.1.1.1: वृद्धिरादैच्
# Defines vṛddhi as the set of vowels {ā, ai, au}

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.1"
SUTRA_TEXT = "वृद्धिरादैच्"
SUTRA_DESC = "Defines vṛddhi as the set of vowels {ā, ai, au}"


class Sutra111:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_1
		return apply_1_1_1(word, pos)

	EXAMPLES = [
		('देवाः', '', 'vṛddhi={आ,ऐ,औ};input=देवाः;matches='),
		('अग्निः', '', 'vṛddhi={आ,ऐ,औ};input=अग्निः;matches='),
	]

