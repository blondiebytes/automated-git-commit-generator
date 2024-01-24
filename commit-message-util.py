import os
import subprocess
import google.generativeai as genai

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def generate_commit_message():
	git_changes = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
	return model.generate_content('''You are an expert at creating a github commit message 
		for a set of changes. Here is a diff of changes we need a commit message for: ''' 
		+ str(git_changes))

if __name__ == '__main__':
	print(generate_commit_message().text)