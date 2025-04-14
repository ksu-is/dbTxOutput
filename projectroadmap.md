# 📍 Project Roadmap: dbTxOutput

This roadmap tracks the progress of a Python-based log export utility that reads transaction data from an Oracle database, formats it into structured JSON, and writes it to the local filesystem for ingestion by NewRelic infrastructure agent (`logging.d`)

---

## ✅ Sprint 1: Planning, Setup, and Codebase Research (In progress)

**Goal**: Establish the repository, define project structure, explore similar codebases, and outline initial responsibilities using Markdown.

### ✅ Task List

#### 📁 GitHub Setup & Repo Configuration
- [x] Accepted invite and joined `ksu-is` GitHub organization  
- [x] Created team within the organization and verified team membership  
- [x] Created public repository for project with open source license (e.g., MIT)  
- [x] Created and edited `README.md` using Markdown  
- [x] Created `projectroadmap.md` with task list and sprint breakdown  

#### 🔍 Codebase Exploration
- [x] Searched GitHub for a related Python + OracleDB repository  
- [x] Cloned and reviewed a related codebase for potential use or inspiration
      - Cloned and ran tutorials against local db:  https://github.com/oracle/python-oracledb.git
- [x] Attempted to run the cloned code and documented issues/notes
      - Working as expected, connected to local oracle XE and created and dropped pythondemo user using tutorial python code:
      PS E:\github\python-oracledb\samples\tutorial> python create_user.py
Enter password for SYSTEM: 
Creating user...
Enter the User to be created [pythondemo]:
Enter the Password for pythondemo:
SQL File Name:  E:\github\python-oracledb\samples\tutorial\sql\create_user.sql
Done.
PS E:\github\python-oracledb\samples\tutorial> python drop_user.py
Enter password for SYSTEM:
Enter password for pythondemo:
Dropping the tutorial user...
SQL File Name:  E:\github\python-oracledb\samples\tutorial\sql\drop_user.sql
Done.
PS E:\github\python-oracledb\samples\tutorial>
- [x] Recorded findings in this roadmap  

#### 🧠 Project Planning
- [x] Define required JSON structure for output
- [x] Document database query and relevant fields
- [x] Outline initial folder and file structure
- [x] Draft Sprint 2 tasks and assigned responsibilities (to myself)

---

## 🧩 Sprint 2: Initial Coding & File Output (In Progress)

**Goal**: Build the MVP (minimum viable product) to extract Oracle data, convert it to JSON, and write it to a local file using Python.
**Updated**:  Worked through checkpoint logic and implementing code skeleton.  Final Sprint will complete the MVP.

### ✅ Task List

#### 🔌 Database Connectivity
- [x] Install `oracledb` module and connect to Oracle XE using Python  
  _Assigned to: Trenton McNeil_

- [x] Finalize `checkpoint_id` logic  
  _Assigned to: Trenton McNeil_

---


#### 💬 Git & Communication
- [x] Make at least **6 meaningful commits per hour while working** in GitHub with clear, specific messages  
  _Assigned to: Trenton McNeil_

- [x] Document any blockers, fixes, or important notes below each task  
  _Assigned to: Trenton McNeil_

---



## 📊 Sprint 3: MVP Demo & Presentation (Upcoming)

**Goal**: Complete and demonstrate a working MVP that ingests Oracle data and writes formatted logs visible in NewRelic. Deliver the presentation slide and finish roadmap tracking.

### ✅ Task List


#### 📤 JSON Output & Checkpoint Handling
- [ ] Write JSON objects to `outputfile.json` in the `/nr_import/` path  
  _Assigned to: Trenton McNeil_

- [ ] Read/write `checkpoint_id.txt` to track progress across runs by extracting from most recent output file
  _Assigned to: Trenton McNeil_

---

#### 🧪 Manual Testing
- [ ] Manually run the script and confirm that JSON output is correctly formatted  
  _Assigned to: Trenton McNeil_

- [ ] Validate that checkpoint ID logic prevents reprocessing of old records  
  _Assigned to: Trenton McNeil_

---

#### 🚀 PoC Functionality

- [ ] Confirm that all required JSON fields are present and properly formatted  
  _Assigned to: Trenton McNeil_

- [ ] Verify EPOCH ms timestamp conversion  
  _Assigned to: Trenton McNeil_

- [ ] Manually verify that logs are picked up by `logging.d` and appear in NewRelic (may want to use a free NR account)
  _Assigned to: Trenton McNeil_

---

#### 📈 Presentation Slide
- [ ] Create PowerPoint slide with:
  - Project title and team member(s)  
  - Project tagline (“Export Oracle logs to JSON for NewRelic observability”)  
  - 1–2 visuals (screenshot, code, NewRelic example)
  _Assigned to: Trenton McNeil_

- [ ] Upload slide to D2L  
  _Assigned to: Trenton McNeil_

- [ ] Commit slide to GitHub repository  
  _Assigned to: Trenton McNeil_

---

#### 📓 Reflection
- [ ] Final `projectroadmap.md` update with notes on progress  
- [ ] Add short summary of what worked well, any issues faced, and future plans  

---

## 🔜 Future Sprints (Outside Project Timeline)

### 📌 Notes & Emerging Tasks
_Track new tasks or ideas here:_
- [ ] Refactor output file name with timestamp for future rotation support  
- [ ] Consider YAML or `.env` file for config paths and DB creds  
- [ ] Add retry wrapper around Oracle query in case of intermittent disconnect  

---

_These sprints are not required for the course but represent intended future enhancements:_

### Sprint 4: Automation and Resilience
- Add cron job  
- Implement hourly file rotation  
- Improve error handling and retry logic

### Sprint 5: Packaging and Configuration
- Add config file (`.env` or YAML) or Hashicorp vault for credentials and/or paths  

---
