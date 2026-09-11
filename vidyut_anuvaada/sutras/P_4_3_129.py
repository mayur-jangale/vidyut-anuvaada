# Sutra प.4.3.129: छन्दोगौक्थिकयाज्ञिकबह्वृचनटाञ्ञ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — CandogOkTikayAjYikabahvfcanawAYYyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.129"
SUTRA_TEXT = "छन्दोगौक्थिकयाज्ञिकबह्वृचनटाञ्ञ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — CandogOkTikayAjYikabahvfcanawAYYyaH"


class Sutra43129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.129: अग्निः'),
		('रामः', '', 'प.4.3.129: रामः'),
		('सीता', '', 'प.4.3.129: सीता'),
	]

