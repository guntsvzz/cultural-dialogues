import json
# Function to compare Hofstede dimensions
def compare_dimensions(country_dimension, verify_hofstede_answer):
    match_count = 0
    for key in verify_hofstede_answer:
        if country_dimension.get(f"{key}_value") == verify_hofstede_answer[key]:
            match_count += 1
    return match_count

# Save the dialogues if match_count >= 4
def save_dialogues_to_jsonl(situation, constraints, country, verify_hofstede_answer, dialogues, match_count, file_path='dialogues.jsonl'):
    if match_count >= 4:
        data = {
            'situation':situation,
            'constraints':constraints,
            'country': country,
            'hofstede_dimension': verify_hofstede_answer,
            'dialogues': dialogues
        }
        with open(file_path, 'a') as file:
            json.dump(data, file)
            file.write('\n')
            
# Create a function to convert numeric values into categories: low, medium, high
def categorize(value):
    if int(value) <= 35:
        return 'low'
    elif 36 <= int(value) <= 75:
        return 'medium'
    else:
        return 'high'