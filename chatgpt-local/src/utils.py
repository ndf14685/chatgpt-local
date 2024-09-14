import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def connect_db():
    conn = sqlite3.connect('chat_history.db')
    return conn

def buscar_respuesta_local(user_input):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT user_input, bot_response FROM conversations")
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        return None, 0  # No hay respuestas en el historial
    
    user_inputs = [row[0] for row in rows]
    bot_responses = [row[1] for row in rows]
    
    vectorizer = TfidfVectorizer().fit_transform([user_input] + user_inputs)
    vectors = vectorizer.toarray()
    
    cosine_similarities = cosine_similarity([vectors[0]], vectors[1:]).flatten()
    max_similarity_index = cosine_similarities.argmax()
    max_similarity_score = cosine_similarities[max_similarity_index]
    
    if max_similarity_score >= 0.7:
        return bot_responses[max_similarity_index], max_similarity_score
    else:
        return None, max_similarity_score
