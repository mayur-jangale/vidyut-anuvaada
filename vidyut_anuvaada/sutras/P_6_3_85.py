# Sutra प.6.3.85: ज्योतिर्जनपदरात्रिनाभिनामगोत्ररूपस्थानवर्णवयोवचनबन्धुषु
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.85"
SUTRA_TEXT = "ज्योतिर्जनपदरात्रिनाभिनामगोत्ररूपस्थानवर्णवयोवचनबन्धुषु"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6385:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.85: अग्निः'),
		('रामः', '', 'प.6.3.85: रामः'),
		('सीता', '', 'प.6.3.85: सीता'),
	]

