from playwright.sync_api import Page, expect

def test_first_place_team_point(page: Page):

    page.goto("https://sport.ua/uk")
    page.locator(".navbar").get_by_role(role="link", name="Футбол", exact=True).click()
    page.locator(".nav-down-division").get_by_role(role="link", name="Прем'єр ліга", exact=True).click()

    first_place_cell = page.locator("td.place").get_by_text("1", exact=True)
    first_place_row = page.get_by_role("row").filter(has=first_place_cell)

    expect(first_place_row).to_be_visible()

    #Variable just for printing
    place_name = first_place_cell.inner_text()
    first_place_name = first_place_row.locator("td.name").inner_text()
    points = first_place_row.locator("td.points").inner_text()

    print(f"{place_name} місце: {first_place_name} — {points} очків")

def test_second_place_team_point(page:Page):

    page.goto("https://sport.ua/uk")
    page.locator(".navbar").get_by_role(role="link", name="Футбол", exact=True).click()
    page.locator(".nav-down-division").get_by_role(role="link", name="Прем'єр ліга", exact=True).click()

    second_place_cell = page.locator("td.place").get_by_text("2", exact=True)
    second_place_row = page.get_by_role("row").filter(has=second_place_cell)

    expect(second_place_row).to_be_visible()

    place_name = second_place_cell.inner_text()
    second_place_name = second_place_row.locator("td.name").inner_text()
    points = second_place_row.locator("td.points").inner_text()

    print(f"{place_name} місце: {second_place_name} — {points} очків")