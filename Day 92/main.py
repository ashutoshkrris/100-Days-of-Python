import csv
import requests
from bs4 import BeautifulSoup


# Scrape data
def scrape_website(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    names = [name.get_text().strip()
             for name in soup.find_all(class_='game-name')]
    numbers = [num.get_text() for num in soup.find_all(class_='num')]
    current_players = numbers[::3]
    peak_players = numbers[1::3]
    hours_played = numbers[2::3]

    scraped_data = {
        "names": names,
        "current_players": current_players,
        "peak_players": peak_players,
        "hours_played": hours_played
    }
    return to_csv(scraped_data)

# Convert to CSV
def to_csv(data: dict):
    with open("data.csv", "w", newline='') as f:
        writer = csv.writer(f)
        columns = ['Rank', 'Name', 'Current Players',
                   'Peak Players', 'Hours Played']
        writer.writerow(columns)
        for i in range(25):
            writer.writerow([i+1, data["names"][i], data["current_players"][i],
                             data["peak_players"][i], data["hours_played"][i]])
    print("Done!")


if __name__ == "__main__":
    url = 'https://steamcharts.com/top'
    scrape_website(url)