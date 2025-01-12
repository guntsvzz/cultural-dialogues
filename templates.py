normbank_template = """
Generate a dialogue based on the following instructions:

Situation: {situation}
Constraints: {constraints}
Country: {country}

Please ensure the dialogue reflects the context described above.
Speaker's name should reflect the country provided.
"""

verify_hofstede_template = """
Dialogues:
{dialogues}

Analyze the provided dialogues using Hofstede’s Cultural Dimensions Theory and predict how the score reflects the six dimensions. 

Return a JSON object.
{format_instructions}
"""