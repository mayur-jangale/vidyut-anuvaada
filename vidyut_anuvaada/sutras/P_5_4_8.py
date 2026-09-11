# Sutra प.5.4.8: विभाषा अञ्चेरदिक्स्त्रियाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA aYceradikstriyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.8"
SUTRA_TEXT = "विभाषा अञ्चेरदिक्स्त्रियाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA aYceradikstriyAm"


class Sutra548:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.8: अग्निः'),
		('रामः', '', 'प.5.4.8: रामः'),
		('सीता', '', 'प.5.4.8: सीता'),
	]

