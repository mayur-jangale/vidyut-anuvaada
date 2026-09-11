# Sutra प.8.2.104: क्षियाऽऽशीःप्रैषेषु तिङ् आकाङ्क्षम्
# (Final transformations (tripāḍī)) — kziyA''SIHprEzezu tiN AkANkzam

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.104"
SUTRA_TEXT = "क्षियाऽऽशीःप्रैषेषु तिङ् आकाङ्क्षम्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — kziyA''SIHprEzezu tiN AkANkzam"


class Sutra82104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.104: अग्निः'),
		('रामः', '', 'प.8.2.104: रामः'),
		('सीता', '', 'प.8.2.104: सीता'),
	]

