# Sutra प.3.4.76: क्तोऽधिकरणे च ध्रौव्यगतिप्रत्यवसानार्थेभ्यः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kto'DikaraRe ca DrOvyagatipratyavasAnArTeByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.76"
SUTRA_TEXT = "क्तोऽधिकरणे च ध्रौव्यगतिप्रत्यवसानार्थेभ्यः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kto'DikaraRe ca DrOvyagatipratyavasAnArTeByaH"


class Sutra3476:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

