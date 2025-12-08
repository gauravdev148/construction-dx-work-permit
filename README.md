# 🛡️ Digital Work Permit System (Formal State Machine)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Logic](https://img.shields.io/badge/Logic-Finite_State_Machine-red)
![Status](https://img.shields.io/badge/Status-Research_Prototype-green)

**A deterministic state-machine system for enforcing safety protocol compliance.**

This project models the "Permit-to-Work" (PTW) process as a **Finite State Machine (FSM)**. Unlike standard databases, this system uses formal transition rules to ensure that a permit cannot reach an `ACTIVE` state without passing through mandatory `SAFETY_CHECK` and `APPROVAL` states. This prevents "process skipping," a common cause of industrial accidents.

---

## 📸 State Transition Visualization
![State Machine UI](permit_preview.png)
*(Figure 1: Visual tracking of the permit lifecycle. Transitions are strictly enforced by the backend logic.)*

---

## 🚀 Key Features

* **Deterministic Logic:**
    * Implements a strict FSM using the `transitions` library.
    * Invalid transitions (e.g., jumping from `Idle` to `Active`) raise immediate `FormalViolation` errors.
* **Process Enforcement:**
    * **Safety Check Constraint:** Work cannot begin until the safety verification state is successfully resolved.
    * **Auditability:** Every state change is tracked and validated against the logic model.
* **Visual Status Tracking:**
    * Provides a clear, linear view of the safety workflow for site managers.

---

## 🛠️ Technical Implementation

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Logic Engine** | Python `transitions` | Formal State Machine implementation |
| **Backend** | Flask | Web Interface & API |
| **Frontend** | Bootstrap 5 | Visual State Diagram |

```python
# Logic Sample: Strict Transition Rules
transitions = [
    {'trigger': 'verify_safety', 'source': 'requested', 'dest': 'safety_check'},
    {'trigger': 'manager_approve', 'source': 'safety_check', 'dest': 'approved'},
    # If a user tries to skip 'safety_check', the system rejects the action.
]
```

---

## ⚡ How to Run

### 1. Setup Environment
```bash
# Create Virtual Environment (Sandbox)
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Install Dependencies (Flask + Transitions)
pip install -r requirements.txt
```

### 2. Launch Application
```bash
# Navigate to the Source Folder
cd src

# Start the Logic Engine
python app.py
```
*Access the system at:* `http://127.0.0.1:5002`

---

## 🔧 Troubleshooting (Windows Users)

If you see a **"running scripts is disabled"** error when trying to activate the environment, run this command in PowerShell to allow script execution:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
*Then try running `.\venv\Scripts\activate` again.*

---

## 👤 Author
**Gaurav Dev**
* *Focus:* Safety-Critical Systems, Process Automation, Formal Methods.