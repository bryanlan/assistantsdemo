from openaiint import create_assistant, create_thread, submit_message, wait_on_run, get_response, run_message

ASSISTANT_INSTRUCTIONS = (
    "Create interactive 'Choose Your Own Adventure' stories. "
    "Start by asking the user's preferences for the protagonist's age and gender. "
    "Provide options for the story's setting and the protagonist's role. "
    "Generate a story based on these choices, offering decision points to the user. "
    "Ensure the story reaches a natural conclusion and invite the user to play again."
)


# Main Function
def main():
    # Create an assistant
    assistant = create_assistant(ASSISTANT_INSTRUCTIONS, "AdventureCreator")

# Create a new thread for the conversation
    thread = create_thread()
    user_input = "Start an adventure"
    print("AI Please create an adventure for me!")
    # Main interaction loop
    playing = True
    while playing:
        

        # Send the message to the thread and create a run
        submit_message(thread, user_input)
        run = run_message(assistant.id, thread)

        # Wait for the run to complete and get the response
        run = wait_on_run(run, thread)
        messages = get_response(thread)
        last_message = messages.data.pop()


        # Display the latest message from the assistant
        print(last_message.content[0].text.value)  
        # Get user's choice or input
        user_input = input("Your choice (or type 'exit' to end): ")
        if user_input.lower() == 'exit':
            playing = False
            continue

    # End of the game
    print("Thank you for playing!")

if __name__ == "__main__":
    main()