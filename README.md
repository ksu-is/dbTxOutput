This project is structured to meet course requirements over three sprints, with additional development planned outside the class timeline for professional use.

## Sprint 1: Planning & Research (Complete) ✅
- Project topic approved and listed in team spreadsheet
- GitHub repo created under KSU-IS organization
- README.md edited and committed to GitHub
- Researched Python + OracleDB solutions
- Created projectroadmap.md and added notes on codebase evaluation
- Created initial project folder structure and file placeholders

## Sprint 2: Initial Coding & File Output 🔧
- Connect to Oracle XE database using oracledb module
- Run SQL query with hardcoded checkpoint ID
- Output results to outputfile.json in working directory
- Read/write checkpoint_id.txt to track latest ID
- At least 6 commits with specific messages in GitHub
- Update projectroadmap.md to reflect progress

## Sprint 3: Demo-Ready PoC & Presentation 📊
- Implement filtering logic (records > last checkpoint only) instead of hardcoded checkpoint ID
- Test end-to-end flow and verify NewRelic log ingestion
- Create one PowerPoint slide with:
  - Team members: Trenton McNeil
  - Project title and tagline
  - Optional screenshot of output or NewRelic dashboard
- Upload PowerPoint to GitHub repo and D2L
- Update projectroadmap.md to reflect progress

## Future Sprints (Outside Project Timeline) 🔜

### Sprint 4: Automation and Resilience
- Add cron job or looped daemon script
- Implement hourly file rotation
- Enhance logging and retry logic for query failures

### Sprint 5: Packaging and Configuration
- Externalize DB creds and paths in config.yaml

### Sprint 6: Testing and CI/CD
- Integrate with GitHub Actions for basic CI pipeline
- Add healthcheck endpoint or logs for alerting
