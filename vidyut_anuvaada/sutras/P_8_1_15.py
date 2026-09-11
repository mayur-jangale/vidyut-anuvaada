# Sutra प.8.1.15: द्वन्द्वं रहस्यमर्यादावचनव्युत्क्रमणयज्ञपात्रप्रयोगाभिव्यक्तिषु
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.15"
SUTRA_TEXT = "द्वन्द्वं रहस्यमर्यादावचनव्युत्क्रमणयज्ञपात्रप्रयोगाभिव्यक्तिषु"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.15: अग्निः'),
		('रामः', '', 'प.8.1.15: रामः'),
		('सीता', '', 'प.8.1.15: सीता'),
	]

