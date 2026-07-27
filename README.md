# QA Automation Engineering Case Study - Bynry

**Candidate:** Rohan Patil
**Role:** Automation Engineering Intern

## Overview
This repository contains the solution for the B2B SaaS Platform Testing multi-platform automation case study. It includes fixes for flaky tests, a proposed framework design, and API/UI integration tests.

## Repository Structure
* `/tests/test_login_fixes.py`: Refactored code addressing flaky login tests with proper explicit waits and auto-retrying assertions.
* `/tests/test_integration.py`: Combined API and UI test flow verifying project creation and tenant isolation.
* `QA_Automation_Case_Study_Rohan_Patil.pdf`: Complete documentation including the Test Plan, Framework Design (POM + Data-Driven), and detailed testing approach.

## Setup Instructions & Execution
To run these automated test scripts locally:

1. **Clone the repository:**
   `git clone <your-repo-url>`
2. **Install dependencies:**
   `pip install pytest playwright requests`
3. **Install Playwright Browsers:**
   `playwright install`
4. **Execution:**
   `pytest tests/`

## Testing Approach & Framework Design
* **Strategy:** API-first approach for test data setup to reduce UI flakiness. 
* **Framework:** Designed using Pytest and Playwright supporting cross-browser execution and multi-tenant environment configurations via `.env`.
* **Tenant Isolation:** Enforced negative testing to ensure secure boundaries between clients (e.g., Company 1 cannot access Company 2 data).

*Please refer to the attached PDF for the full framework architecture diagram and missing requirements analysis.*
