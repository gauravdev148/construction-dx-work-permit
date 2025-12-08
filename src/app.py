from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# --- Database Setup ---
# This creates a simple file to store data (no complex installation needed)
def init_db():
    conn = sqlite3.connect('safety_permits.db')
    c = conn.cursor()
    # Create a table to hold permit details
    c.execute('''CREATE TABLE IF NOT EXISTS permits 
                 (id INTEGER PRIMARY KEY, worker_name TEXT, location TEXT, 
                  hazard_type TEXT, status TEXT, date_requested TEXT)''')
    conn.commit()
    conn.close()

# --- Routes (Pages) ---

# 1. The Home Page (Dashboard)
@app.route('/')
def index():
    conn = sqlite3.connect('safety_permits.db')
    c = conn.cursor()
    # Get all permits, newest first
    c.execute("SELECT * FROM permits ORDER BY id DESC")
    permits = c.fetchall()
    conn.close()
    return render_template('index.html', permits=permits)

# 2. Submit a New Permit (Worker Action)
@app.route('/submit', methods=['POST'])
def submit_permit():
    worker_name = request.form['worker_name']
    location = request.form['location']
    hazard_type = request.form['hazard_type']
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    conn = sqlite3.connect('safety_permits.db')
    c = conn.cursor()
    # Default status is always 'Pending Review'
    c.execute("INSERT INTO permits (worker_name, location, hazard_type, status, date_requested) VALUES (?, ?, ?, ?, ?)",
              (worker_name, location, hazard_type, 'Pending Review', date_now))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# 3. Approve a Permit (Safety Manager Action)
@app.route('/approve/<int:id>')
def approve_permit(id):
    conn = sqlite3.connect('safety_permits.db')
    c = conn.cursor()
    c.execute("UPDATE permits SET status = 'APPROVED' WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db() # Run the DB setup once when app starts
    app.run(debug=True)