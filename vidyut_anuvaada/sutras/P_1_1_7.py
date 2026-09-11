# Sutra प.1.1.7: हलोऽनन्तराः संयोगः
# A consonant immediately following another consonant forms a consonant cluster (saṃyoga)

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.7"
SUTRA_TEXT = "हलोऽनन्तराः संयोगः"
SUTRA_DESC = "A consonant immediately following another consonant forms a consonant cluster (saṃyoga)"


class Sutra117:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_7
		return apply_1_1_7(word, pos)

	EXAMPLES = [
		('अग्निः', '', 'saṃyoga-pairs=none;count=0'),
		('अस्मिन्', '', 'saṃyoga-pairs=none;count=0'),
		('पान्त', '', 'saṃyoga-pairs=none;count=0'),
		('सूक्त', '', 'saṃyoga-pairs=none;count=0'),
		('पर्वत', '', 'saṃyoga-pairs=पर वत;count=2'),
	]

