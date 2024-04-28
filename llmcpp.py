import sys
from langchain.llms import LlamaCpp
from llama_cpp import Llama
import re

# Define instructions for the model
instructions = """
Interpretation Task
You are an assistant that receives a natural language string as input. Your goal is to interpret the speaker's intention and convert it into a set of commands. There are only four possible movement outputs: move forward (f), backward (b), left (l), or right (r).
Command Syntax

    Single parameter commands:
        f (indefinite forward until object detected)
        l (turn left 90 degrees)
        r (turn right 90 degrees)
        s (stop the robot)
    Double parameter commands (letter followed by a command and a number):
        t,20 (set threshold for ultrasonic sensor to 20 cm)
        f,200 (go forward 200 cm)
        b,100 (go backward 100 cm)
        l,90 (turn left 90 degrees)
        r,270 (turn right 270 degrees)
    Sequence of commands (separated by /):
        f,100/b,100/r,270/f,300 (go forward 100 cm, back 100 cm, turn right 270 degrees, and go forward 300 cm)

Special Cases

    If the command is to go backward without a distance input, turn around 180 degrees and use the regular f command (e.g., "go backwards" -> r,180/f)
    If the command is to turn right and then go backward, turn right 90 degrees and then use the regular f command (e.g., "turn right then go backwards" -> r,90/r,180/f)

Output
Return the best-matched command based on the input. If unsure, return "unknown". Do not include any additional text or explanations. Only return the command.

The command you will evaluate is as follows. ONLY GIVE THE ANSWER DO NOT SAY ANYTHING ELSE.
"""

# Initialize the Llama model
llm = Llama(
    model_path="/home/group3/Desktop/fireai/llama.cpp/models/llama-2-7b.Q5_K_M.gguf",
    max_tokens=64,
    stop=["Q:", "\n"],
    echo=False
)

# Generate a completion
text = input("Give me a prompt: ")
prompt = (f"{instructions}\n{text}\n"
          "This is equivalent to: ")  # Prepend instructions to the prompt
output = llm(prompt)
print(output)

verbose = False

llm = LlamaCpp(
    model_path="/home/group3/Desktop/fireai/llama.cpp/models/llama-2-7b-chat.Q4_K_M.gguf",
    n_ctx=4096,
    n_gpu_layers=64,
    n_batch=1024,
    f16_kv=True,
    verbose=verbose,
)


question = input("Input your command: ")

if question == "stop":
    sys.exit(1)
prompt = f"{instructions}\n{question}"  # Prepend instructions to the prompt
output = llm(
    prompt,
    max_tokens=4096,
    temperature=0.2,
    top_p=0.1
)
print(output['choices'][0]['text'])
 
def extract_commands(input_text):
    # Define regular expressions for different command patterns
    single_param_regex = r'(f|l|r)'
    double_param_regex = r'([bflrt]),(\d+)'
    stop_regex = r's'
    sequence_regex = r'((?:[bflrt],?(?:\d+)?/?)+)'
 
    # Initialize an empty list to store the extracted commands
    commands = []
 
    # Split the input text into individual commands
    command_list = re.findall(sequence_regex, input_text, re.IGNORECASE)
 
    # Iterate over each command
    for command in command_list:
        # Check for single parameter commands
        single_param_match = re.match(single_param_regex, command, re.IGNORECASE)
        if single_param_match:
            commands.append(single_param_match.group(1).lower())
            continue
 
        # Check for double parameter commands
        double_param_match = re.match(double_param_regex, command, re.IGNORECASE)
        if double_param_match:
            commands.append(double_param_match.group(1).lower() + ',' + double_param_match.group(2))
            continue
 
        # Check for stop command
        stop_match = re.match(stop_regex, command, re.IGNORECASE)
        if stop_match:
            commands.append('s')
            continue
 
        # Check for command sequences
        sequence_match = re.findall(r'([bflrt]),?(\d+)?', command, re.IGNORECASE)
        if sequence_match:
            sequence = '/'.join([part[0].lower() + (',' + part[1] if part[1] else '') for part in sequence_match])
            commands.append(sequence)
            continue
 
        # If none of the patterns match, append "unknown"
        commands.append("unknown")
 
    # Handle special cases for backwards movement
    final_commands = []
    for command in commands:
        if command == 'b':
            final_commands.extend(['r,180', 'f'])
        else:
            final_commands.append(command)
 
    return '/'.join(final_commands)
print(extract_commands(output))