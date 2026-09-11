# Sutra प.5.4.144: विभाषा श्यावारोकाभ्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA SyAvArokAByAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.144"
SUTRA_TEXT = "विभाषा श्यावारोकाभ्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA SyAvArokAByAm"


class Sutra54144:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.144: अग्निः'),
		('रामः', '', 'प.5.4.144: रामः'),
		('सीता', '', 'प.5.4.144: सीता'),
	]

