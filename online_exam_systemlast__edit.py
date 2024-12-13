# This code is made by :(>>Youssef Amr<<>>Youssef Hisham<<>>Omar Wael<<)

# Online Exam System // Python Project 
import json

# at the register page
# the main things is divided into classes to be easily attached.
class User:
    # init: for initializing the following inputs
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id  # also id is added here for more personal protection
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.name}, Email: {self.email}"

class UserModel:
    def __init__(self):
        self.users = []
        self.current_user = None

    def add_user(self, user_id, name, email, password):
        if not self.validate_input(user_id, name, email, password):
            return
        user = User(user_id, name, email, password)
        self.users.append(user)
        print(f"User added: {user}")

    # to make user as valid or invalid
    def view_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            print(user)

    # to update any of the user authentication
    def edit_user(self, user_id, new_name=None, new_email=None, new_password=None):
        for user in self.users:
            if user.user_id == user_id:
                if new_name:
                    user.name = new_name
                if new_email:
                    user.email = new_email
                if new_password:
                    user.password = new_password
                print(f"User updated: {user}")
                return
        print("User not found.")

    # this is extra usage in the code, as deleted user will be immediately deleted in the system
    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print(f"User deleted: {user}")
                return
        print("User not found.")

    # json save data file
    def load_users(self, filename):
        try:
            with open(filename, 'r') as file:  # read file
                data = json.load(file)
                for item in data:
                    self.users.append(User(**item))
                print("Users loaded successfully.")
                #except is an exception like else
        except FileNotFoundError:
            print("File not found.")

    def save_users(self, filename):
        with open(filename, 'w') as file:  # allow writing in the file
            json.dump([user.__dict__ for user in self.users], file)  # json dump: from python to json
            print("Users saved successfully.")

    def validate_input(self, user_id, name, email, password):
        if not user_id or not name or not email or not password:
            print("All fields are required.")
            return False
        return True
    # return is used in the functions as break.

    def authenticate_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                self.current_user = user
                print(f"Welcome, {user.name}!")  # as Welcome youssef
                return True
        print("Invalid email or password!!")
        return False

    # for searching for the users 
    def search_users(self, keyword):
        results = [user for user in self.users if keyword.lower() in user.name.lower() or keyword.lower() in user.email.lower()]
        if not results:
            print("No users found.")
        for user in results:
            print(user)

    # this is an extra information for the user 
    def print_summary(self):
        print("User Summary:")
        for user in self.users:
            print(f"User {user.user_id}: {user.name}, {user.email}")


class AdminModel(UserModel):
    def __init__(self):
        # to allow the admin to access all user methods, content 
        super().__init__()

class OnlineExamSystem:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.user_answers = []
        # to start from the initial score
        self.score = 0

    def add_question(self, question, options, answer):
        self.questions.append({"question": question, "options": options, "answer": answer})

    def take_exam(self):
        question_number = 1
        for q in self.questions:
            print(f"Q{question_number}: {q['question']}")
            option_letter = 'A'
            for option in q['options']:
                print(f"  {option_letter}. {option}")
                option_letter = chr(ord(option_letter) + 1)
            # only upper answers is validated 
            user_answer = input("Your answer: ").upper()
            # append = add user question
            self.user_answers.append(user_answer)
            if user_answer == q['answer']:
                # to add question and score when finish the current question and click enter
                self.score += 1
            question_number += 1

    # len: return number of questions 
    def display_score(self):
        print(f"\nYou scored: {self.score} out of {len(self.questions)}")
    # used with json
    def save_score(self, filename):
        with open(filename, "w") as file:
            file.write(f"Score: {self.score}/{len(self.questions)}\n")
            question_number = 1
            for q in self.questions:
                file.write(f"Q{question_number}: {q['question']}\n")
                file.write(f"Your answer: {self.user_answers[question_number - 1]}, Correct answer: {q['answer']}\n")
                # means that the question after being answered it will be automatically turned to the following question
                question_number += 1

# Create cases
user_model = UserModel()
admin_model = AdminModel()
exam_system = OnlineExamSystem()

# Adding exam questions  # after answers in the [list] will be the options in upper characters
exam_system.add_question("What is the keyword used to define a function in Python?", ["def", "function", "define", "func"], "A")
exam_system.add_question("Which of these data types is not immutable?", ["Tuple", "List", "String", "Integer"], "B")
# not in our programming content this term but it is an easy question so we put it
exam_system.add_question("Which statement is used to handle exceptions?", ["catch", "try", "except", "finally"], "C")
exam_system.add_question("What is the output of print(2**3)?", ["6", "8", "9", "12"], "B")
exam_system.add_question("How do you insert COMMENTS in Python code?", ["#", "//", "/*", "<!--"], "A")
exam_system.add_question("Which method can be used to remove whitespace from both ends of a string?", ["strip()", "trim()", "cut()", "rstrip()"], "A")
exam_system.add_question("What is the correct file extension for Python files?", [".pt", ".pyt", ".pyth", ".py"], "D")

# Example usage of user model
admin_model.add_user(1, "khaled", "khaled@example.com", "password1")
admin_model.add_user(2, "ali", "ali@example.com", "password2")
admin_model.view_users()
admin_model.edit_user(1, new_name="mia")
admin_model.delete_user(2)
admin_model.load_users("users.json")
admin_model.save_users("users.json")
admin_model.authenticate_user("mahmoud@example.com", "password1")
admin_model.search_users("al")
admin_model.print_summary()

# Taking the exam: allow user to answer exam questions
exam_system.take_exam()
exam_system.display_score()
exam_system.save_score("exam_score.txt")

# At the end we hope from this project to be a great start for us 
# and also we hope that the project make all of you interested in this python code, thanks for this opportunity.



