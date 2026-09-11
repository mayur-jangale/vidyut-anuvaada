# Sutra प.8.1.5: परेर्वर्जने
# ṅamo halaḥ — ङम् before consonants

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.5"
SUTRA_TEXT = "परेर्वर्जने"
SUTRA_DESC = "ṅamo halaḥ — ङम् before consonants"


class Sutra815:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.5: अग्निः'),
		('रामः', '', 'प.8.1.5: रामः'),
		('सीता', '', 'प.8.1.5: सीता'),
	]

