# Sutra प.7.2.49: सनीवन्तर्धभ्रस्जदम्भुश्रिस्वृयूर्णुभरज्ञपिसनाम्
# (Taddhita (secondary derivations)) — sanIvantarDaBrasjadamBuSrisvfyUrRuBarajYapisanAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.49"
SUTRA_TEXT = "सनीवन्तर्धभ्रस्जदम्भुश्रिस्वृयूर्णुभरज्ञपिसनाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — sanIvantarDaBrasjadamBuSrisvfyUrRuBarajYapisanAm"


class Sutra7249:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.49: अग्निः'),
		('रामः', '', 'प.7.2.49: रामः'),
		('सीता', '', 'प.7.2.49: सीता'),
	]

