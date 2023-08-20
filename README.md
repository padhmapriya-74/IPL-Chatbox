# IPL-Chatbox
This interactive platform allows users to input queries in plain language and receive responses in
plain language without relying on artificial intelligence. With a focus on human
moderators, the chatroom aims to provide accurate and engaging answers to IPL
2022-related questions, ensuring an immersive user experience.
The Indian Premier League, known for its thrilling matches, star-studded teams,
and passionate fanbase, has become a global phenomenon in the world of cricket.
With numerous teams, players, statistics, and match dynamics to keep track of, IPL
enthusiasts often seek an accessible and reliable source of IPL-related information.
ChatGPT for IPL offers a solution by combining the capabilities of ChatGPT with
the vast knowledge base of IPL-related data. It enables cricket enthusiasts to ask
questions, explore team and player statistics, discuss match details, and delve into
the rich history of the IPL.


● Data Structure: Tree (Binary Tree)
It is a Team-Hierarchical Tree data structure where each team is going to
serve as a node with “matches” as root node and the sub-teams represent
child nodes.

Data Storage:JSON files

Algorithm Used:
Breadth-First Search:
BFS visits nodes in a level-by-level
manner, which often results in a more intuitive and straight-forward traversal order.
Queue data structure has to be used to implement this algorithm.

Backend:
Programming language Used: Python
Framework which works on Python: Flask, as it helps us to integrate the
frontend and backend and fulfill our need for successful handling of user input
queries and responses.

Preprocessing the user query:
Preprocessing the user input query becomes inevitable as we’re not using AI, ML
models here. Ultimately, We need to preprocess the queries for this project.

Parsing: Soon after the input query is split into a list of words using split()
method, the relevant JSON file has to be spotted out and it has to be parsed
into a Python object. Only then, from that Python object, correct responses
can be shown to user.

Others:
● Testing user login credentials using RegEx and raising appropriate
errors when the credentials are wrong
All the user credentials are stored in a text file after hashing using sha
algorithm when they sign up. When a user tries to login only if the
credentials match with those in the text file it moves to the chatroom
page.
● Testing the website with sample queries after development. The
same questions can be formed in different ways in English. So to
handle all such cases conditions have been given and tested in order
that the correct response is delivered to the user.
● Raising errors when an user query cannot be responded. Say for
an example, if a query related to COVID is asked, the website should
through an error as COVID is not our domain. Also, when the relevant
JSON file fails to load.
