from openai import OpenAI
import time
import os
from fileops import write_text_file, read_json_file

# Initialize the OpenAI client with your API key
pwFiles = "apikeys.json"
pwData = read_json_file(pwFiles)
os.environ["OPENAI_API_KEY"] = pwData['OPENAI_API_KEY']
client = OpenAI()

# Function to create a new thread
def create_thread():
    return client.beta.threads.create()

# Function to create an assistant
def create_assistant(instruct, assistantName, modelType = "gpt-4-1106-preview"):
    return client.beta.assistants.create(
        model=modelType,
        instructions=instruct,
        name=assistantName
    )

# Function to send a message and create a run
def submit_message( thread, user_message, roletype = "user"):
    if roletype != "user":
        user_message = roletype + ":"+ user_message
    return client.beta.threads.messages.create(thread_id=thread.id, role="user", content=user_message)


def run_message(assistant_id, thread):
    return client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant_id)

# Function to wait for a run to complete
def wait_on_run(run, thread):
    while run.status in ["queued", "in_progress"]:
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        time.sleep(0.5)
    return run

# Function to retrieve messages from a thread
def get_response(thread):
    return client.beta.threads.messages.list(thread_id=thread.id, order="asc", limit = 100)


