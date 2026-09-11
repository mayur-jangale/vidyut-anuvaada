# Sutra प.5.3.93: वा बहूनां जातिपरिप्रश्ने डतमच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vA bahUnAM jAtiparipraSne qatamac

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.93"
SUTRA_TEXT = "वा बहूनां जातिपरिप्रश्ने डतमच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vA bahUnAM jAtiparipraSne qatamac"


class Sutra5393:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.93: अग्निः'),
		('रामः', '', 'प.5.3.93: रामः'),
		('सीता', '', 'प.5.3.93: सीता'),
	]

