# Sutra प.5.3.35: एनबन्यतरस्यामदूरेऽपञ्चम्याः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — enabanyatarasyAmadUre'paYcamyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.35"
SUTRA_TEXT = "एनबन्यतरस्यामदूरेऽपञ्चम्याः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — enabanyatarasyAmadUre'paYcamyAH"


class Sutra5335:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.35: अग्निः'),
		('रामः', '', 'प.5.3.35: रामः'),
		('सीता', '', 'प.5.3.35: सीता'),
	]

