# Phys29: Policy and Guidelines on Using AI Tools

As we will discuss in detail in lecture, there is a wealth of information on the internet about python programming in the form of documentation, code examples, and discussions in coding forums. More recently, so-called Large Language Models (LLMs) like ChatGPT have emerged as a powerful means to both generate code and learn programming syntax. We will discuss these types of resources in detail in the first lecture where I will provide a detailed example. Below I will describe the specific guidelines for their usage in this course. 

One might think that consulting the internet or using AI assistants (like ChatGPT) for help with your homework is a form of plagiarism or cheating. However, in reality expert programmers (myself included) are constantly using such tools to look up specific details about syntax, figure out how to do something new, and generally to work more efficiently.  **Bottom line**: you are allowed to look things up on the internet while doing your homework and/or use AI tools but you need to follow the specific guidelines described here for their usage. The underlying motivation for these guidelines is that you need to understand what you are getting from these resources and use them as a pedagogical tools,  rather than just blindly copying their outputs. 

## How to Use AI Tools for your Homework Assignments 

Spend at least 30 minutes on **each problem** trying to code up the answer to the problem yourself. For this "biological intelligence" coding step, you are allowed to use the internet, i.e. you can query Google and/or specifically consult coding forums like StackOverflow for help, but you are not allowed to use AI tools. After the 30 minutes uninterrupted minutes of thinking about the problem are up, if you are making good progress and feel like continuing on your own, you should do so. Programming is a lot like learning to speak a new language, and the more time that you spend coding on your own, the faster you will learn the fundamentals.  If you did not use AI to solve the problem you still may find it beneficial to see how the method you came up with compares to the AI generated code (so see below). You will find that sometimes the AI generated code is took a different approach than you did, and you can learn from this.

After the 30 minutes are up, you can use AI tools to assist you. If you are using AI: 

- Copy the problem into the prompt provided by the AI chatbot. Include the following line at the end of your prompt:  **Please do not put any comments of any kind in the code or provide any explanations. I want to understand, comment, and document this code myself.**  This will instruct the AI chatbot not to provide any inline comments in the code or provide any explanations (which typically they default to doing)
- Use the copy and paste feature to copy the AI generated code into your Jupyter notebook. 
- These chatbots are not perfect, and often the code that they produce can be incorrect in subtle or not so subtle ways. You will likely need to make some modifications to the code to get it to work.
- Once you have a code that runs, think about how you can test the results to see if they make sense. 
-  Now it is your task to add comments explaning what the code is doing. These inline comments can be added to Python code via the '#' symbol. Note that no number of comments is too many. While simple lines of code like ```x = 1``` don't need comments, more complicated lines of code like:   

    ```python
    # Generate an array of 100 evenly spaced points between 0 and 1
    x = np.linspace(0,1,100)
    ```   

-  You can ask the AI chatbot specific questions about lines of code, control constructs, functions, etc. This can help you with the inline comment generation. It is probably useful to use Google in tandem in case you need to pull up the python documentation for specific python functions or constructs. You can also use the ```help()``` function in python, i.e. ```help(np.linspace)``` or type ```np.linspace?``` to get help on a specific function.

- I am fully aware that you can also ask the AI chatbot to write the code with the inline comments. If you do so, you are actively making a choice not to learn and **this is considered cheating**.  Things are going to get significantly more challenging later in the course, for which you will need to master the fundamentals of coding. In the future, the AI won't be smart enough to help you, at least not with the current generation of models!

- If you use AI, please cite the source in your notebook, i.e. "Problem solved with the assistance of chatGPT". 

