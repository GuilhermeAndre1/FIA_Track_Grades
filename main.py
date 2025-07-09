from scrapping import scrape_sections_with_tables

url = "https://en.wikipedia.org/wiki/List_of_motor_racing_circuits_by_FIA_grade"
sections = scrape_sections_with_tables(url)

for section in sections:
    print(f"Título: {section['title']}")
    print(f"Descrição: {section['description']}")
    for linha in section['table']:
        print(linha)
    print("-" * 40)