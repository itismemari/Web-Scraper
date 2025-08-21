from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting specific information from the following text content: {chunks}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama3.1")


def parse_with_ollama(chunks , parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model # Create a chain with the prompt and the model it first checks the prompt and then the model

    parsed_result = []

    for i , chunk in enumerate(chunks , start= 1): # Loop through each chunk and the start means it starts from 1 (i) and enumerate is used to get both index and value
        rseponse = chain.invoke({"chunks" : chunk , "parse_description" : parse_description})

        print(f"Parsed batch {i} of {len(chunks)}")
        parsed_result.append(rseponse)

    return "\n".join(parsed_result)    