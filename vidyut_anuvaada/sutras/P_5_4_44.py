# Sutra प.5.4.44: प्रतियोगे पञ्चम्यास्तसिः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pratiyoge paYcamyAstasiH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.44"
SUTRA_TEXT = "प्रतियोगे पञ्चम्यास्तसिः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pratiyoge paYcamyAstasiH"


class Sutra5444:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.44: अग्निः'),
		('रामः', '', 'प.5.4.44: रामः'),
		('सीता', '', 'प.5.4.44: सीता'),
	]

