# Sutra प.5.1.29: विभाषा कार्षापणसहस्राभ्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA kArzApaRasahasrAByAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.29"
SUTRA_TEXT = "विभाषा कार्षापणसहस्राभ्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA kArzApaRasahasrAByAm"


class Sutra5129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.29: अग्निः'),
		('रामः', '', 'प.5.1.29: रामः'),
		('सीता', '', 'प.5.1.29: सीता'),
	]

