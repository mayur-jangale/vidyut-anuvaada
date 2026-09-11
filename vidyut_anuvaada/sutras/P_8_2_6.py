# Sutra प.8.2.6: स्वरितो वाऽनुदात्ते पदादौ
# uttaratrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.6"
SUTRA_TEXT = "स्वरितो वाऽनुदात्ते पदादौ"
SUTRA_DESC = "uttaratrāsiddham — repeated"


class Sutra826:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.6: अग्निः'),
		('रामः', '', 'प.8.2.6: रामः'),
		('सीता', '', 'प.8.2.6: सीता'),
	]

