# Tailor - A simple CLI resume tailor.

Tailor was born mainly to prevent me from going insane by tailoring my resume for every single job posting I was applying for.

With this tool, you can easily list all of your skills, education, past jobs, etc. and it will generate a tailored resume using whatever information you provide it that closest matches the job posting.

## How to use

1. Clone the repo
2. `python -m venv venv`
3. `venv\scripts\activate` or `source venv/bin/activate`
2. Install packages - `pip install -r requirements.txt`
3. Rename the config_example.json file to config.json
4. Fill out the config file information with your own info and OpenAI API key.
5. Run Tailor, and paste a job posting link when it asks for one.
6. ...
7. Profit with a new tailored resume.

## Notes

Is it perfect? No, not really. But I feel it can give you a good starting point or direction to go when applying to different positions.

## Future features

1. Reading info from an existing resume instead of having to manually fill out the config.
2. Error checking, things like invalid urls, etc.
3. More prompt tweaking to generate better results consistently.
