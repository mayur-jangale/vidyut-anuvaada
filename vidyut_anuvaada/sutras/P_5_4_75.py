# Sutra प.5.4.75: अच् प्रत्यन्ववपूर्वात् सामलोम्नः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ac pratyanvavapUrvAt sAmalomnaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.75"
SUTRA_TEXT = "अच् प्रत्यन्ववपूर्वात् सामलोम्नः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ac pratyanvavapUrvAt sAmalomnaH"


class Sutra5475:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.75: अग्निः'),
		('रामः', '', 'प.5.4.75: रामः'),
		('सीता', '', 'प.5.4.75: सीता'),
	]

