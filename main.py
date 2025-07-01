from openai import OpenAI
from markdown_pdf import MarkdownPdf, Section

import json

try:
    #Load the config file.
    with open('./config.json', 'r') as f:
        data = json.load(f)

    #Grab the user's info from the config file.
    user_info = data['user_info']

    print("Tailor - easily tailor your resume to fit any job posting.")
    print("Enter a link to the target job posting below.")
    link = input("Link:")


    print("Generating...")

    client = OpenAI(
      api_key=data['api_key']
    )

    response = client.responses.create(
      model="gpt-4.1",
      tools=[{"type": "web_search_preview"}],
      input=f"Do not do anything except for what is explained below."
            f"You are an expert resume writer that has written resumes for top talent."
            f"You use correct grammar, and all of your resumes generated pass an ATS screener."
            f"Generate a rich text formatted resume for the following job posting: {link} using my information: {user_info}."
            f"Do not add anything about references."
            f"Do not add a summary at the beginning or end of the resume."
            f"Do not add any skills that the user has not listed. Only use the top 5 relevant skills from the skills pool."
            f"Do not lie, but you can adjust things to sound better if needed."
            f"Use Arial as the font."
            f"Do not add any unnecessary sections that do not exist in the user info section.",
    )

    file_name = input("Enter a name for your resume:")

    pdf = MarkdownPdf()
    pdf.add_section(Section(response.output_text))
    pdf.save(f"{file_name}.pdf")

    print("Your resume has been generated!")

except FileNotFoundError:
    print("Error: 'config.json' not found. Please ensure the file exists in the same directory as your main.py file.")

except json.JSONDecodeError:
    print("Error: Could not decode JSON from 'config.json'. Check file content for valid JSON format.")
