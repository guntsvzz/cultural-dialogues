import argparse
import pandas as pd
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from tqdm import tqdm  # Import tqdm for the progress bar

from models import model
from utils import compare_dimensions, save_dialogues_to_jsonl, categorize
from templates import normbank_template, verify_hofstede_template
from parsers import HofstedeDimension

# Set random seed for reproducibility
random_seed = 1234

# Create NormBank prompt template
normbank_prompt = PromptTemplate(
    template=normbank_template,
    input_variables=["situation", "constraints", "country"]
)

output_parser = StrOutputParser()
chain = normbank_prompt | model | output_parser

parser = JsonOutputParser(pydantic_object=HofstedeDimension)
verify_hofstede_prompt = PromptTemplate(
    template=verify_hofstede_template,
    input_variables=["dialogues"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
verify_hofstede_chain = verify_hofstede_prompt | model | parser

def main(args):
    # Step 1: Load Hofstede Dimensions Data
    file_path = 'datasets/6-dimensions-for-website-2015-08-16.csv'
    df_hofstede_dimension = pd.read_csv(file_path, sep=';')
    df_hofstede_dimension = df_hofstede_dimension.replace('#NULL!', None)
    df_hofstede_dimension.dropna(subset=["pdi", "idv", "mas", "uai", "ltowvs", "ivr"], inplace=True)
    df_hofstede_dimension.rename(columns={"ltowvs":"lto"}, inplace=True)

    # Apply the categorization function to each column
    for column in ['pdi', 'idv', 'mas', 'uai', 'lto', 'ivr']:
        df_hofstede_dimension[f'{column}_value'] = df_hofstede_dimension[column].apply(categorize)

    # Step 2: Retrieve the selected country dimension
    country_dimension = df_hofstede_dimension[df_hofstede_dimension['country'] == args.country].to_dict(orient='records')[0]

    # Step 3: Load NormBank CSV and prepare sample
    file_path = 'datasets/NormBank.csv'
    df = pd.read_csv(file_path)
    if args.norm == 'all':
        df_expected = df
    else:
        df_expected = df[df.norm == args.norm]
    df_expected = df_expected.sample(n=args.num_sample, random_state=random_seed)
    
    # Step 4: Loop through the number of samples specified by the user, with progress bar
    for i in tqdm(range(args.num_sample), desc="Generating dialogues", unit="sample"):
        sample = df_expected.iloc[i].to_dict()

        # Step 4.1: Define input values and invoke the chain to generate the dialogue
        input_values = {
            "situation": sample["setting"],
            "constraints": sample["constraints"],
            "country": args.country
        }
        dialogues = chain.invoke(input_values)

        # Step 4.2: Hofstede verification and save the result
        verify_hofstede_answer = verify_hofstede_chain.invoke({"dialogues": dialogues})
        
        match_count = compare_dimensions(country_dimension, verify_hofstede_answer)
        print(f'MATCH COUNT : {match_count}')
        # Step 4.4 : save file to jsonl
        save_dialogues_to_jsonl(
            sample["setting"], sample["constraints"], args.country, verify_hofstede_answer, dialogues, match_count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate a conversation between two agents.")
    parser.add_argument('--country', type=str, required=True, help="Country for the conversation")
    parser.add_argument('--num_sample', type=int, required=True, help="Number of samples for dialogue generation")
    parser.add_argument('--norm', type=str, choices=['taboo', 'normal', 'expected', 'all'], default='all', help='Specify the norm category')
    args = parser.parse_args()
    main(args)
