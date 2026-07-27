import pytest
from playwright.sync_api import sync_playwright, expect

def test_user_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto("https://app.workflowpro.com/login")
        page.fill("#email", "admin@company1.com")
        page.fill("#password", "password123")
        page.click("#login-btn")
        
        # FIX: Wait for navigation to complete to handle CI/CD delays
        page.wait_for_url("**/dashboard", timeout=10000) 
        
        # FIX: Use auto-retrying expect to handle dynamic DOM rendering
        welcome_message = page.locator(".welcome-message")
        expect(welcome_message).to_be_visible(timeout=10000)
        browser.close()

def test_multi_tenant_access():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto("https://app.workflowpro.com/login")
        page.fill("#email", "user@company2.com")
        page.fill("#password", "password123")
        page.click("#login-btn")
        
        page.wait_for_url("**/dashboard")
        
        # FIX: Ensure the element is actually attached to the DOM before fetching all
        page.wait_for_selector(".project-card", state="visible", timeout=15000)
        
        projects = page.locator(".project-card").all()
        assert len(projects) > 0, "No projects loaded on the dashboard"
        
        for project in projects:
            assert "Company2" in project.text_content()
            
        browser.close()
      
