def edu_friend_chatbot():
    print("EduBot : Hey! I'm your study buddy. Ask me about exams, stress, study tips, career, and more!")
    print("Type 'bye' whenever you want to exit.\n")

    while True:
        user_input = input("You: ").lower()

        # Greetings
        if 'hello' in user_input or 'hi' in user_input:
            print("EduBot : Hi there! How can I support you today?")
        
        # How are you
        elif 'how are you' in user_input:
            print("EduBot : I'm feeling smart and helpful! 😊 How about you?")

        # Study tips
        elif 'study tips' in user_input or 'how to study' in user_input:
            print("EduBot : Use Pomodoro (25 min focus, 5 min break), make flashcards, and teach others to remember better!")

        # Career advice
        elif 'career' in user_input:
            print("EduBot : Let’s explore! Are you more into tech, medicine, art, business, or something else?")

        # Exams
        elif 'exam' in user_input:
            print("EduBot : Start revision early, practice past papers, and keep a checklist of topics done.")

        # Motivation
        elif 'motivation' in user_input:
            print("EduBot : You’re stronger than you think. Keep going. Every effort you make is building your future!")

        # Time table
        elif 'time table' in user_input or 'schedule' in user_input:
            print("EduBot : Here’s a simple study timetable:\n"
                  "🕘 9–11 AM: Deep study (hard subjects)\n"
                  "☕ 11–11:30 AM: Break\n"
                  "🕚 11:30–1 PM: Practice problems\n"
                  "🍴 1–2 PM: Lunch & rest\n"
                  "📘 2–4 PM: Reading / Notes\n"
                  "🎮 4–5 PM: Short break or hobby\n"
                  "📚 5–7 PM: Revise & recap\n"
                  "🛌 10 PM: Sleep early for a fresh mind!")



        # Stress relief
        elif 'stress' in user_input or 'relax' in user_input:
            print("EduBot : Stress is normal. Try deep breathing or listen to calming music.\n")
                 
                  

        # Feeling low
        elif 'sad' in user_input or 'depressed' in user_input or 'anxious' in user_input:
            print("EduBot : I’m here for you. Try talking to someone you trust.\n"
                  "Remember, taking breaks and being kind to yourself is important.")

        # Thank you
        elif 'thank' in user_input:
            print("EduBot : Always happy to help! 😊")

        # Exit
        elif 'bye' in user_input:
            print("EduBot : Take care! Keep going—you’re doing amazing. See you soon!")
            break

        # Fallback
        else:
            print("EduBot : Hmm... I didn't catch that. Ask me about studying, motivation, career!")

# Run the chatbot
edu_friend_chatbot()
