from openai import OpenAI
from markdown_pdf import MarkdownPdf, Section
import pypandoc

from prompt import tailor_prompt

import json

def get_file_name():
    '''Prompt the user to enter a file name. Will add more validation later.'''
    file_name = input("Enter a name for your resume:")
    if len(file_name) == 0:
        print("File name cannot be empty.")
        get_file_name()

    return file_name

def run_tailor():
    try:
        # Load the config file.
        with open('./config.json', 'r') as f:
            data = json.load(f)

        # Grab the user's info from the config file.
        user_info = data['user_info']

        print("Tailor - easily tailor your resume to fit any job posting.")
        print("Enter a link to the target job posting below.")
        job_posting_link = input("Link:")

        print("Generating...")

        client = OpenAI(
            api_key=data['api_key']
        )

        response = client.responses.create(
            model="gpt-4.1",
            tools=[{"type": "web_search_preview"}],
            input=f"{tailor_prompt}. Generate a markdown formatted resume for the following job posting: {job_posting_link} using my information: {user_info}."
        )

        file_name = get_file_name()

        pdf = MarkdownPdf()
        pdf.add_section(Section(response.output_text))
        pdf.save(f"{file_name}.pdf")

        print("Your resume has been generated!")

    except FileNotFoundError:
        print(
            "Error: 'config.json' not found. Please ensure the file exists in the same directory as your main.py file.")

    except json.JSONDecodeError:
        print("Error: Could not decode JSON from 'config.json'. Check file content for valid JSON format.")


if __name__ == "__main__":
    run_tailor()