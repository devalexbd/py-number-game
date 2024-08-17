# py-number-game
 A number guessing game created using Python and the numpy library.

## Set-up
In order to create a Python program that could create pseudo-random numbers, I needed to use the 'numpy' library.

To use numpy I first had to create a virtual environment inside my VS Code project. The reason for this is so that whichever dependencies I download for this Python project, they are local to this singular project and don't influence others; should they encounter conflicts or should I want to use another version of the same dependency.

To create this virtual environment, I made sure I was in the root folder for my project in the VS Code terminal and used the command: `py -m venv env`. This would then create a new folder in my project called "env".

After this, I had to activate the environment so I could install numpy into it. However, upon using `./env/Scripts/activate` I encountered an error related to Execution Policy settings on Windows. This was preventing me from executing certain scripts on my machine. To temporarily bypass this and run the commands I needed, I used `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`. This allowed me to bypass this restriction during my current PowerShell session.

Once this was resolved, I activated my virtual environment and typed `pip install numpy` and this downloaded the dependency into my Python project.

Lastly, in VS Code, I had to make sure I had the virtual environment selected as my current Python interpreter. Once this was done I was able to easily run my code using the numpy library.
