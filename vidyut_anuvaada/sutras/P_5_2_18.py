# Sutra प.5.2.18: गोष्ठात् खञ् भूतपूर्वे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — gozWAt KaY BUtapUrve

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.18"
SUTRA_TEXT = "गोष्ठात् खञ् भूतपूर्वे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — gozWAt KaY BUtapUrve"


class Sutra5218:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.18: अग्निः'),
		('रामः', '', 'प.5.2.18: रामः'),
		('सीता', '', 'प.5.2.18: सीता'),
	]

