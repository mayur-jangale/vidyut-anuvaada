# Sutra प.5.4.141: वयसि दन्तस्य दतृ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vayasi dantasya datf

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.141"
SUTRA_TEXT = "वयसि दन्तस्य दतृ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vayasi dantasya datf"


class Sutra54141:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.141: अग्निः'),
		('रामः', '', 'प.5.4.141: रामः'),
		('सीता', '', 'प.5.4.141: सीता'),
	]

