from flask import Flask, render_template, request, redirect, url_for
from transitions import Machine

app = Flask(__name__)

# --- THE FORMAL LOGIC (State Machine) ---
class WorkPermitModel(object):
    pass

# Define the Strict States and Transitions
states = ['idle', 'requested', 'safety_check', 'approved', 'active', 'closed']

transitions = [
    {'trigger': 'request_permit', 'source': 'idle', 'dest': 'requested'},
    {'trigger': 'verify_safety', 'source': 'requested', 'dest': 'safety_check'},
    {'trigger': 'manager_approve', 'source': 'safety_check', 'dest': 'approved'},
    {'trigger': 'start_work', 'source': 'approved', 'dest': 'active'},
    {'trigger': 'finish_work', 'source': 'active', 'dest': 'closed'},
    {'trigger': 'reset', 'source': '*', 'dest': 'idle'}  # Reset for demo
]

# Initialize the Machine
model = WorkPermitModel()
machine = Machine(model=model, states=states, transitions=transitions, initial='idle')

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        # Try to execute the transition (Formal Logic Check)
        try:
            if action == 'request':
                model.request_permit()
            elif action == 'verify':
                model.verify_safety()
            elif action == 'approve':
                model.manager_approve()
            elif action == 'start':
                model.start_work()
            elif action == 'finish':
                model.finish_work()
            elif action == 'reset':
                model.reset()
        except Exception as e:
            # If logic forbids the move (e.g., skipping a step)
            error = f"FORMAL VIOLATION: Cannot perform '{action}' from state '{model.state}'."

    return render_template('permit.html', state=model.state, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5002) # Running on 5002 to avoid conflict with AI app