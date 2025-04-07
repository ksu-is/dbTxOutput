# 📍 Project Roadmap: dbTxOutput

## 🧩 Sprint 2: Initial Coding & File Output (Due before next review)

**Goal**: Build the minimum viable flow to extract Oracle data, convert it to JSON, and write it to a local file using Python. Begin tracking progress via commits and roadmap updates.

---

### ✅ Task List

#### 🔌 Database Connectivity
- [ ] Install `oracledb` module and connect to Oracle XE using Python  
  _Assigned to: Trenton McNeil_
- [ ] Create and populate mock audit table for local testing  
  _Assigned to: Trenton McNeil_
- [ ] Run SQL query using a hardcoded `LAST_ID` (checkpoint) value of 1
  _Assigned to: Trenton McNeil_

---

#### 📤 JSON Output & Checkpoint Handling
- [ ] Transform query result rows into JSON objects  
  _Assigned to: Trenton McNeil_

- [ ] Write JSON objects to `outputfile.json` in the `/nr_import/` path  
  _Assigned to: Trenton McNeil_

- [ ] Read/write `checkpoint_id.txt` to track progress across runs  
  _Assigned to: Trenton McNeil_

---

#### 🧪 Manual Testing
- [ ] Manually run the script and confirm that JSON output is correctly formatted  
  _Assigned to: Trenton McNeil_

- [ ] Validate that checkpoint ID logic prevents reprocessing of old records  
  _Assigned to: Trenton McNeil_

---

#### 💬 Git & Communication
- [ ] Make at least **6 meaningful commits** in GitHub with clear, specific messages  
  _Assigned to: Trenton McNeil_

- [ ] Document any blockers, fixes, or important notes below each task  
  _Assigned to: Trenton McNeil_

---

### 📌 Notes & Emerging Tasks

_Use this section to track new tasks or ideas as they arise:_

- [ ] Refactor output file name with timestamp for future rotation support
- [ ] Consider YAML or `.env` file for config paths and DB creds
- [ ] Add retry wrapper around Oracle query in case of intermittent disconnect

---

