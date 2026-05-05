from playwright.sync_api import expect

def test_website_logo_name(login_to_secret_sauce):


    expect(login_to_secret_sauce.locator(".app_logo")).to_be_visible()
    expect(login_to_secret_sauce.locator(".app_logo")).to_have_text("Swag Labs")

    app_logo_inner_text = login_to_secret_sauce.locator(".app_logo").inner_text()

    print(f"Text: {app_logo_inner_text}")