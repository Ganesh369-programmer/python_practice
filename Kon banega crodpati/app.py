from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

questions = [
    {"question": "Which language was used to create Facebook?", "options": ["Python", "French", "JavaScript", "PHP"], "answer": 4},
    {"question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"], "answer": 2},
    {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": 2},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], "answer": 1},
    {"question": "In which year did India gain independence?", "options": ["1945", "1947", "1950", "1962"], "answer": 2},
    {"question": "Which gas is most abundant in the Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "answer": 3},
    {"question": "Who is known as the 'Father of the Nation' in India?", "options": ["Jawaharlal Nehru", "Sardar Patel", "Mahatma Gandhi", "Subhas Bose"], "answer": 3},
    {"question": "Which sport is associated with the term 'googly'?", "options": ["Football", "Cricket", "Tennis", "Hockey"], "answer": 2},
    {"question": "Which Indian city is famous for its IT industry and is called the 'Silicon Valley of India'?", "options": ["Hyderabad", "Bengaluru", "Pune", "Gurgaon"], "answer": 2},
    {"question": "What is the chemical symbol for gold?", "options": ["Ag", "Au", "Fe", "Cu"], "answer": 2},
    {"question": "Which Indian festival is known as the Festival of Lights?", "options": ["Holi", "Dussehra", "Diwali", "Eid"], "answer": 3},
    {"question": "Who was the first woman Prime Minister of India?", "options": ["Sonia Gandhi", "Indira Gandhi", "Pratibha Patil", "Sushma Swaraj"], "answer": 2},
    {"question": "Which animal is known as the 'Ship of the Desert'?", "options": ["Camel", "Horse", "Elephant", "Donkey"], "answer": 1},
    {"question": "In which ocean is the island nation of Maldives located?", "options": ["Pacific", "Atlantic", "Indian", "Arctic"], "answer": 3},
    {"question": "Which Indian scientist won the Nobel Prize for Physics in 1930?", "options": ["Homi Bhabha", "C.V. Raman", "Satyendra Bose", "A.P.J. Abdul Kalam"], "answer": 2},
    {"question": "What is the name of the longest river in India?", "options": ["Yamuna", "Godavari", "Brahmaputra", "Ganga"], "answer": 4},
    {"question": "Which Bollywood actor is known as 'King Khan'?", "options": ["Salman Khan", "Aamir Khan", "Shah Rukh Khan", "Saif Ali Khan"], "answer": 3},
    {"question": "Which monument in India was built by Emperor Shah Jahan in memory of his wife?", "options": ["Qutub Minar", "Red Fort", "Taj Mahal", "India Gate"], "answer": 3},
    {"question": "What is the smallest unit of digital information?", "options": ["Byte", "Bit", "Kilobyte", "Megabyte"], "answer": 2}
]

levels = ["1,000", "2,000", "3,000", "5,000", "10,000", "20,000", "40,000", "80,000", "1,60,000", "3,20,000","6,40,000" , "1,25,0000" , "2,50,0000" , "5,00,0000" , "7,50,0000" , "1 Crore" , "7 Crore"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_question/<int:q_index>')
def get_question(q_index):
    if q_index < len(questions):
        return jsonify({"question": questions[q_index], "level": levels[q_index]})
    return jsonify({"message": "Game Over"})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    q_index = data.get("q_index")
    user_answer = data.get("answer")
    if questions[q_index]["answer"] == user_answer:
        return jsonify({"correct": True, "next_level": levels[q_index]})
    return jsonify({"correct": False})

if __name__ == '__main__':
    app.run(debug=True)

# Project Structure:
# KBC-WebApp/
# ├── static/
# │   ├── styles.css
# │   ├── script.js
# ├── templates/
# │   ├── index.html
# ├── app.py
# ├── requirements.txt
