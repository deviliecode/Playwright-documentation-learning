from playwright.sync_api import Page, expect

def test_ukraine_uefa_rating(page: Page):

    page.goto("https://sport.ua/uk/football")
    # page.wait_for_timeout(2000)

    page.get_by_role("button", name="Show").click()
    # page.wait_for_timeout(2000)

    page.get_by_role("link", name="Рейтинг УЄФА").click()
    # page.wait_for_timeout(2000)

    ukraine_row = page.get_by_role("row").filter(has_text="Україна")
    expect(ukraine_row).to_be_visible()

    all_cells = ukraine_row.get_by_role("cell")
    row_data = all_cells.all_inner_texts()
    print(f"\n[DEBUG] Дані рядка: {row_data}")
