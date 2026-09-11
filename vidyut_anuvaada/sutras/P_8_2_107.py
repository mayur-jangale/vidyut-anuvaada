# Sutra प.8.2.107: एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ
# (Final transformations (tripāḍī)) — eco'pragfhyasyAdUrAdDUte pUrvasyArDasyAduttarasyedutO

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.107"
SUTRA_TEXT = "एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ"
SUTRA_DESC = "(Final transformations (tripāḍī)) — eco'pragfhyasyAdUrAdDUte pUrvasyArDasyAduttarasyedutO"


class Sutra82107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.107: अग्निः'),
		('रामः', '', 'प.8.2.107: रामः'),
		('सीता', '', 'प.8.2.107: सीता'),
	]

