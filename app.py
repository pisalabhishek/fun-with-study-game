import streamlit as st
import random

# Page configuration
st.set_page_config(
    page_title="Engineering Interview Vocabulary Master",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    .word-display {
        font-size: 45px;
        font-weight: bold;
        text-align: center;
        color: #667eea;
        letter-spacing: 8px;
        margin: 30px 0;
        padding: 20px;
        background: #f8f9fa;
        border-radius: 10px;
    }
    .hint-box {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #ffc107;
        margin: 15px 0;
    }
    .definition-box {
        background-color: #d1ecf1;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #17a2b8;
        margin: 15px 0;
    }
    .stats-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Comprehensive Engineering word database
WORD_DATABASE = {
    'Computer Science': [
        {'word': 'ALGORITHM', 'hint': 'Problem-solving steps', 'definition': 'Step-by-step procedure for solving computational problems', 'difficulty': 'easy'},
        {'word': 'POLYMORPHISM', 'hint': 'OOP concept - many forms', 'definition': 'Ability of objects to take multiple forms in programming', 'difficulty': 'medium'},
        {'word': 'ENCAPSULATION', 'hint': 'Data hiding technique', 'definition': 'Bundling data and methods that operate on data within one unit', 'difficulty': 'medium'},
        {'word': 'RECURSION', 'hint': 'Function calls itself', 'definition': 'Programming technique where function calls itself', 'difficulty': 'easy'},
        {'word': 'DATABASE', 'hint': 'Organized data collection', 'definition': 'Structured collection of data stored electronically', 'difficulty': 'easy'},
        {'word': 'BLOCKCHAIN', 'hint': 'Distributed ledger technology', 'definition': 'Decentralized digital ledger recording transactions', 'difficulty': 'medium'},
        {'word': 'COMPILER', 'hint': 'Code translator', 'definition': 'Program that translates high-level code to machine code', 'difficulty': 'medium'},
        {'word': 'DEBUGGING', 'hint': 'Finding and fixing errors', 'definition': 'Process of identifying and removing errors from code', 'difficulty': 'easy'},
        {'word': 'FRAMEWORK', 'hint': 'Development platform', 'definition': 'Software platform for developing applications', 'difficulty': 'easy'},
        {'word': 'CRYPTOGRAPHY', 'hint': 'Secure communication', 'definition': 'Practice of secure communication in presence of adversaries', 'difficulty': 'hard'},
    ],
    'Artificial Intelligence': [
        {'word': 'NEURALNETWORK', 'hint': 'Brain-inspired computing', 'definition': 'Computing system inspired by biological neural networks', 'difficulty': 'medium'},
        {'word': 'DEEPLEARNING', 'hint': 'Advanced ML technique', 'definition': 'Machine learning using multiple layers of neural networks', 'difficulty': 'medium'},
        {'word': 'SUPERVISED', 'hint': 'Learning with labels', 'definition': 'Learning from labeled training data', 'difficulty': 'easy'},
        {'word': 'REGRESSION', 'hint': 'Predicting continuous values', 'definition': 'Statistical method for predicting numerical outcomes', 'difficulty': 'medium'},
        {'word': 'CLUSTERING', 'hint': 'Grouping similar data', 'definition': 'Technique of grouping similar data points together', 'difficulty': 'easy'},
        {'word': 'CONVOLUTION', 'hint': 'CNN operation', 'definition': 'Mathematical operation combining two functions', 'difficulty': 'hard'},
        {'word': 'GRADIENT', 'hint': 'Rate of change', 'definition': 'Vector of partial derivatives used in optimization', 'difficulty': 'medium'},
        {'word': 'OVERFITTING', 'hint': 'Model memorizes data', 'definition': 'Model learns training data too well, poor generalization', 'difficulty': 'medium'},
        {'word': 'ACTIVATION', 'hint': 'Neural network function', 'definition': 'Function determining neuron output', 'difficulty': 'easy'},
        {'word': 'BACKPROPAGATION', 'hint': 'Training algorithm', 'definition': 'Algorithm for training neural networks using gradient descent', 'difficulty': 'hard'},
    ],
    'Mechanical Engineering': [
        {'word': 'THERMODYNAMICS', 'hint': 'Heat and energy laws', 'definition': 'Study of energy transfer and conversion', 'difficulty': 'medium'},
        {'word': 'HYDRAULICS', 'hint': 'Fluid power systems', 'definition': 'Technology using liquid fluid power', 'difficulty': 'easy'},
        {'word': 'PNEUMATICS', 'hint': 'Air pressure systems', 'definition': 'Technology using gas or pressurized air', 'difficulty': 'easy'},
        {'word': 'KINEMATICS', 'hint': 'Motion study', 'definition': 'Study of motion without considering forces', 'difficulty': 'medium'},
        {'word': 'COMBUSTION', 'hint': 'Burning process', 'definition': 'Chemical process of burning fuel with oxygen', 'difficulty': 'easy'},
        {'word': 'METALLURGY', 'hint': 'Metal properties study', 'definition': 'Science of metals and their properties', 'difficulty': 'medium'},
        {'word': 'TURBINE', 'hint': 'Rotary engine', 'definition': 'Rotary mechanical device extracting energy from fluid flow', 'difficulty': 'easy'},
        {'word': 'REFRIGERATION', 'hint': 'Cooling system', 'definition': 'Process of removing heat from enclosed space', 'difficulty': 'easy'},
        {'word': 'DYNAMICS', 'hint': 'Forces and motion', 'definition': 'Study of forces and their effect on motion', 'difficulty': 'medium'},
        {'word': 'MACHINING', 'hint': 'Material removal process', 'definition': 'Process of removing material from workpiece', 'difficulty': 'easy'},
    ],
    'Electrical Engineering': [
        {'word': 'TRANSFORMER', 'hint': 'Voltage converter', 'definition': 'Device transferring electrical energy between circuits', 'difficulty': 'easy'},
        {'word': 'SEMICONDUCTOR', 'hint': 'Partial conductor material', 'definition': 'Material with conductivity between conductor and insulator', 'difficulty': 'medium'},
        {'word': 'CAPACITOR', 'hint': 'Energy storage device', 'definition': 'Component storing electrical energy in electric field', 'difficulty': 'easy'},
        {'word': 'AMPLIFIER', 'hint': 'Signal booster', 'definition': 'Electronic device increasing power of signal', 'difficulty': 'easy'},
        {'word': 'OSCILLATOR', 'hint': 'Wave generator', 'definition': 'Electronic circuit producing repetitive electronic signal', 'difficulty': 'medium'},
        {'word': 'IMPEDANCE', 'hint': 'AC circuit resistance', 'definition': 'Effective resistance of AC circuit to current flow', 'difficulty': 'medium'},
        {'word': 'RESONANCE', 'hint': 'Frequency matching', 'definition': 'Condition when system vibrates at maximum amplitude', 'difficulty': 'medium'},
        {'word': 'RECTIFIER', 'hint': 'AC to DC converter', 'definition': 'Device converting alternating current to direct current', 'difficulty': 'easy'},
        {'word': 'THYRISTOR', 'hint': 'Power control device', 'definition': 'Semiconductor device for controlling electric power', 'difficulty': 'hard'},
        {'word': 'INVERTER', 'hint': 'DC to AC converter', 'definition': 'Device converting direct current to alternating current', 'difficulty': 'easy'},
    ],
    'Electronics & Telecom': [
        {'word': 'MODULATION', 'hint': 'Signal encoding', 'definition': 'Process of varying carrier signal properties', 'difficulty': 'medium'},
        {'word': 'BANDWIDTH', 'hint': 'Frequency range', 'definition': 'Range of frequencies signal occupies', 'difficulty': 'easy'},
        {'word': 'MULTIPLEXER', 'hint': 'Signal combiner', 'definition': 'Device combining multiple signals into one', 'difficulty': 'medium'},
        {'word': 'ANTENNA', 'hint': 'Wireless transmitter/receiver', 'definition': 'Device for transmitting or receiving radio waves', 'difficulty': 'easy'},
        {'word': 'MICROPROCESSOR', 'hint': 'Computer brain chip', 'definition': 'Integrated circuit containing CPU functions', 'difficulty': 'easy'},
        {'word': 'TRANSDUCER', 'hint': 'Energy converter', 'definition': 'Device converting one form of energy to another', 'difficulty': 'medium'},
        {'word': 'DEMODULATION', 'hint': 'Signal extraction', 'definition': 'Process of extracting information from carrier signal', 'difficulty': 'medium'},
        {'word': 'ATTENUATION', 'hint': 'Signal reduction', 'definition': 'Reduction in signal strength during transmission', 'difficulty': 'medium'},
        {'word': 'TOPOLOGY', 'hint': 'Network arrangement', 'definition': 'Physical or logical arrangement of network', 'difficulty': 'easy'},
        {'word': 'PROTOCOL', 'hint': 'Communication rules', 'definition': 'Set of rules governing data communication', 'difficulty': 'easy'},
    ],
    'Civil Engineering': [
        {'word': 'FOUNDATION', 'hint': 'Building base', 'definition': 'Lower part of structure transferring loads to ground', 'difficulty': 'easy'},
        {'word': 'SURVEYING', 'hint': 'Land measurement', 'definition': 'Technique of determining positions on Earth surface', 'difficulty': 'easy'},
        {'word': 'REINFORCEMENT', 'hint': 'Concrete strengthening', 'definition': 'Steel bars embedded in concrete for strength', 'difficulty': 'easy'},
        {'word': 'HYDRAULICS', 'hint': 'Water engineering', 'definition': 'Study of mechanical properties of liquids', 'difficulty': 'easy'},
        {'word': 'GEOTECHNICAL', 'hint': 'Soil engineering', 'definition': 'Engineering behavior of earth materials', 'difficulty': 'medium'},
        {'word': 'CANTILEVER', 'hint': 'Projecting beam', 'definition': 'Rigid structural element anchored at one end', 'difficulty': 'medium'},
        {'word': 'PRESTRESSED', 'hint': 'Pre-compressed concrete', 'definition': 'Concrete with internal stresses to improve performance', 'difficulty': 'hard'},
        {'word': 'EXCAVATION', 'hint': 'Earth removal', 'definition': 'Process of removing earth for construction', 'difficulty': 'easy'},
        {'word': 'COMPACTION', 'hint': 'Soil densification', 'definition': 'Process of increasing soil density', 'difficulty': 'easy'},
        {'word': 'ALIGNMENT', 'hint': 'Layout positioning', 'definition': 'Route or position of linear construction', 'difficulty': 'easy'},
    ],
    'Information Technology': [
        {'word': 'VIRTUALIZATION', 'hint': 'Creating virtual resources', 'definition': 'Creating virtual version of computing resources', 'difficulty': 'medium'},
        {'word': 'CLOUD', 'hint': 'Internet-based computing', 'definition': 'Delivery of computing services over internet', 'difficulty': 'easy'},
        {'word': 'FIREWALL', 'hint': 'Network security', 'definition': 'Network security system monitoring traffic', 'difficulty': 'easy'},
        {'word': 'ENCRYPTION', 'hint': 'Data protection', 'definition': 'Converting information into secure code', 'difficulty': 'medium'},
        {'word': 'SERVER', 'hint': 'Service provider computer', 'definition': 'Computer providing services to other computers', 'difficulty': 'easy'},
        {'word': 'MIDDLEWARE', 'hint': 'Software bridge', 'definition': 'Software connecting different applications', 'difficulty': 'medium'},
        {'word': 'REPOSITORY', 'hint': 'Code storage location', 'definition': 'Central location storing and managing code', 'difficulty': 'easy'},
        {'word': 'DEPLOYMENT', 'hint': 'Application release', 'definition': 'Process of making software available for use', 'difficulty': 'easy'},
        {'word': 'SCALABILITY', 'hint': 'Growth capability', 'definition': 'Capability to handle growing amount of work', 'difficulty': 'medium'},
        {'word': 'PROTOCOL', 'hint': 'Communication standards', 'definition': 'Set of rules governing data transmission', 'difficulty': 'easy'},
    ],
    'Medical': [
        {'word': 'DIAGNOSIS', 'hint': 'Disease identification', 'definition': 'Process of determining disease from symptoms', 'difficulty': 'easy'},
        {'word': 'PATHOLOGY', 'hint': 'Disease study', 'definition': 'Study of causes and effects of diseases', 'difficulty': 'medium'},
        {'word': 'ANESTHESIA', 'hint': 'Pain blocker', 'definition': 'Loss of sensation for medical procedures', 'difficulty': 'easy'},
        {'word': 'IMMUNOLOGY', 'hint': 'Immune system study', 'definition': 'Study of immune system and responses', 'difficulty': 'medium'},
        {'word': 'CARDIOLOGY', 'hint': 'Heart medicine', 'definition': 'Medical specialty dealing with heart disorders', 'difficulty': 'easy'},
        {'word': 'NEPHROLOGY', 'hint': 'Kidney medicine', 'definition': 'Medical specialty dealing with kidneys', 'difficulty': 'medium'},
        {'word': 'ONCOLOGY', 'hint': 'Cancer treatment', 'definition': 'Study and treatment of tumors', 'difficulty': 'medium'},
        {'word': 'PEDIATRICS', 'hint': 'Children medicine', 'definition': 'Medical care of infants and children', 'difficulty': 'easy'},
        {'word': 'RADIOLOGY', 'hint': 'Medical imaging', 'definition': 'Medical specialty using imaging for diagnosis', 'difficulty': 'easy'},
        {'word': 'PHARMACOLOGY', 'hint': 'Drug science', 'definition': 'Study of drugs and their effects', 'difficulty': 'medium'},
    ],
    'Legal/UPSC': [
        {'word': 'JURISDICTION', 'hint': 'Legal authority', 'definition': 'Official power to make legal decisions', 'difficulty': 'easy'},
        {'word': 'CONSTITUTION', 'hint': 'Supreme law', 'definition': 'Fundamental principles governing nation', 'difficulty': 'easy'},
        {'word': 'AMENDMENT', 'hint': 'Law modification', 'definition': 'Change or addition to constitution', 'difficulty': 'easy'},
        {'word': 'FEDERALISM', 'hint': 'Power division system', 'definition': 'System dividing powers between governments', 'difficulty': 'medium'},
        {'word': 'SOVEREIGNTY', 'hint': 'Supreme authority', 'definition': 'Supreme power of state to govern itself', 'difficulty': 'medium'},
        {'word': 'BUREAUCRACY', 'hint': 'Administrative system', 'definition': 'System of government through departments', 'difficulty': 'medium'},
        {'word': 'PARLIAMENT', 'hint': 'Legislative body', 'definition': 'Supreme legislative body of country', 'difficulty': 'easy'},
        {'word': 'JUDICIARY', 'hint': 'Court system', 'definition': 'System of courts administering justice', 'difficulty': 'easy'},
        {'word': 'IMPEACHMENT', 'hint': 'Official removal', 'definition': 'Process of charging official with misconduct', 'difficulty': 'medium'},
        {'word': 'ORDINANCE', 'hint': 'Executive order', 'definition': 'Law made by executive without legislature', 'difficulty': 'medium'},
    ]
}

# Initialize session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = 'menu'
    st.session_state.category = None
    st.session_state.current_word = None
    st.session_state.guessed_letters = []
    st.session_state.lives = 6
    st.session_state.score = 0
    st.session_state.words_completed = 0
    st.session_state.show_hint = False
    st.session_state.show_definition = False
    st.session_state.high_scores = {cat: 0 for cat in WORD_DATABASE.keys()}

def start_game(category):
    st.session_state.game_state = 'playing'
    st.session_state.category = category
    st.session_state.score = 0
    st.session_state.words_completed = 0
    st.session_state.lives = 6
    next_word()

def next_word():
    words = WORD_DATABASE[st.session_state.category]
    st.session_state.current_word = random.choice(words)
    st.session_state.guessed_letters = []
    st.session_state.show_hint = False
    st.session_state.show_definition = False
    st.session_state.game_state = 'playing'

def check_letter(letter):
    if letter not in st.session_state.guessed_letters:
        st.session_state.guessed_letters.append(letter)
        if letter not in st.session_state.current_word['word']:
            st.session_state.lives -= 1
            if st.session_state.lives == 0:
                st.session_state.game_state = 'lost'
                if st.session_state.score > st.session_state.high_scores[st.session_state.category]:
                    st.session_state.high_scores[st.session_state.category] = st.session_state.score
        else:
            # Check if word is complete
            word = st.session_state.current_word['word']
            if all(l in st.session_state.guessed_letters for l in word):
                points = 10 + (st.session_state.lives * 2)
                if not st.session_state.show_hint:
                    points += 5
                st.session_state.score += points
                st.session_state.words_completed += 1
                st.session_state.game_state = 'won'
                if st.session_state.score > st.session_state.high_scores[st.session_state.category]:
                    st.session_state.high_scores[st.session_state.category] = st.session_state.score

def display_word():
    word = st.session_state.current_word['word']
    return ' '.join([letter if letter in st.session_state.guessed_letters else '_' for letter in word])

# Game UI
if st.session_state.game_state == 'menu':
    st.markdown("""
    <div class='main-title'>
        <h1>🎓 Engineering Interview Vocabulary Master</h1>
        <p style='font-size: 18px;'>Master technical terms for your dream job!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📚 Select Your Category:")
    
    col1, col2 = st.columns(2)
    
    categories = list(WORD_DATABASE.keys())
    
    for idx, category in enumerate(categories):
        if idx % 2 == 0:
            with col1:
                if st.button(f"🔧 {category}", key=category, use_container_width=True, type="primary"):
                    start_game(category)
                    st.rerun()
                if st.session_state.high_scores[category] > 0:
                    st.caption(f"🏆 High Score: {st.session_state.high_scores[category]}")
        else:
            with col2:
                if st.button(f"🔧 {category}", key=category, use_container_width=True, type="primary"):
                    start_game(category)
                    st.rerun()
                if st.session_state.high_scores[category] > 0:
                    st.caption(f"🏆 High Score: {st.session_state.high_scores[category]}")
    
    st.markdown("---")
    st.markdown("""
    ### 📖 How to Play:
    - Choose your field/category
    - Guess letters to reveal technical terms
    - Learn definitions of important concepts
    - Prepare for technical interviews!
    - Each correct word earns points
    - Use hints wisely (costs points!)
    """)

elif st.session_state.game_state == 'playing':
    # Header stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("❤️ Lives", st.session_state.lives)
    with col2:
        st.metric("🏆 Score", st.session_state.score)
    with col3:
        st.metric("✅ Words", st.session_state.words_completed)
    with col4:
        st.metric("🎯 Category", st.session_state.category.split()[0])
    
    st.markdown("---")
    
    # Word display
    st.markdown(f"<div class='word-display'>{display_word()}</div>", unsafe_allow_html=True)
    
    # Difficulty badge
    difficulty = st.session_state.current_word['difficulty']
    color = {'easy': '🟢', 'medium': '🟡', 'hard': '🔴'}
    st.markdown(f"<p style='text-align: center;'>{color[difficulty]} Difficulty: {difficulty.upper()}</p>", unsafe_allow_html=True)
    
    # Hint and Definition buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("💡 Show Hint", use_container_width=True):
            st.session_state.show_hint = True
            st.rerun()
    with col2:
        if st.button("📖 Show Definition", use_container_width=True):
            st.session_state.show_definition = True
            st.rerun()
    with col3:
        if st.button("⏭️ Skip Word", use_container_width=True):
            st.session_state.lives -= 1
            if st.session_state.lives <= 0:
                st.session_state.game_state = 'lost'
            else:
                next_word()
            st.rerun()
    
    if st.session_state.show_hint:
        st.markdown(f"""
        <div class='hint-box'>
            <strong>💡 Hint:</strong> {st.session_state.current_word['hint']}
        </div>
        """, unsafe_allow_html=True)
    
    if st.session_state.show_definition:
        st.markdown(f"""
        <div class='definition-box'>
            <strong>📖 Definition:</strong> {st.session_state.current_word['definition']}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔤 Choose a Letter:")
    
    # Keyboard
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cols_per_row = 7
    for i in range(0, len(alphabet), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, col in enumerate(cols):
            if i + j < len(alphabet):
                letter = alphabet[i + j]
                with col:
                    if letter in st.session_state.guessed_letters:
                        if letter in st.session_state.current_word['word']:
                            st.button(letter, key=f"btn_{letter}", disabled=True, use_container_width=True, type="primary")
                        else:
                            st.button(letter, key=f"btn_{letter}", disabled=True, use_container_width=True)
                    else:
                        if st.button(letter, key=f"btn_{letter}", use_container_width=True):
                            check_letter(letter)
                            st.rerun()
    
    st.markdown("---")
    if st.button("🏠 Back to Menu", use_container_width=True):
        st.session_state.game_state = 'menu'
        st.rerun()

elif st.session_state.game_state == 'won':
    st.balloons()
    
    st.markdown("""
    <div class='stats-box'>
        <h2>✅ Correct! Well Done! 🎉</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"### The word was: **{st.session_state.current_word['word']}**")
    
    st.markdown(f"""
    <div class='definition-box'>
        <strong>📖 Definition:</strong> {st.session_state.current_word['definition']}
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏆 Score", st.session_state.score)
    with col2:
        st.metric("❤️ Lives Left", st.session_state.lives)
    with col3:
        st.metric("✅ Words Completed", st.session_state.words_completed)
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➡️ Next Word", use_container_width=True, type="primary"):
            next_word()
            st.rerun()
    with col2:
        if st.button("🏠 Main Menu", use_container_width=True):
            st.session_state.game_state = 'menu'
            st.rerun()

elif st.session_state.game_state == 'lost':
    st.markdown("""
    <div class='stats-box'>
        <h2>❌ Game Over!</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"### The correct word was: **{st.session_state.current_word['word']}**")
    
    st.markdown(f"""
    <div class='definition-box'>
        <strong>📖 Definition:</strong> {st.session_state.current_word['definition']}
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🏆 Final Score", st.session_state.score)
    with col2:
        st.metric("✅ Words Completed", st.session_state.words_completed)
    
    if st.session_state.score == st.session_state.high_scores[st.session_state.category]:
        st.success("🎊 New High Score!")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Play Again", use_container_width=True, type="primary"):
            start_game(st.session_state.category)
            st.rerun()
    with col2:
        if st.button("🏠 Main Menu", use_container_width=True):
            st.session_state.game_state = 'menu'
            st.rerun()
