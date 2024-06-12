# Film Liste

Dieses Projekt wurde erstellt, um die 100 am besten bewerteten Filme von IMDb abzurufen und einige Informationen über diese Filme in einer CSV-Datei zu speichern. Das Projekt verwendet die Bibliotheken BeautifulSoup und pandas, um Daten von IMDb zu extrahieren und in eine CSV-Datei zu verarbeiten. Scrapy wurde in diesem Projekt nicht verwendet.

Im Rahmen des Projekts wurden 25 Filme abgerufen. Der Grund dafür ist, dass auf der IMDb-Seite jeweils 25 Filme angezeigt werden. Diese Einschränkung wird angewendet, um die Ladezeit der Seite und die Effizienz des Datenextraktionsprozesses zu verbessern.

## Verwendete Technologien

- BeautifulSoup
- pandas

## Verwendung

Um das Projekt auszuführen, befolgen Sie diese Schritte:

1. Installieren Sie die notwendigen Bibliotheken:
   ```
   pip install pandas
   pip install beautifulsoup4
   pip install requests
   ```
2. Führen Sie die Datei `main.py` aus:
   ```
   python main.py
   ```

## Ausgabe

Wenn Sie das Projekt ausführen, wird eine Datei mit dem Namen `movies.csv` erstellt, die Informationen über die 25 am besten bewerteten Filme enthält.

---

# Film List

This project was created to fetch the top 100 highest-rated movies from IMDb and save some information about these movies in a CSV file. The project uses BeautifulSoup and pandas libraries to scrape data from IMDb and process it into a CSV file. Scrapy was not used in this project.

As part of the project, 25 movies were fetched. The reason for this is that the IMDb page displays 25 movies at a time. This limitation is applied to improve the page load time and the efficiency of the data scraping process.

## Technologies Used

- BeautifulSoup
- pandas

## Usage

To run the project, follow these steps:

1. Install the necessary libraries:
   ```
   pip install pandas
   pip install beautifulsoup4
   pip install requests
   ```
2. Run the `main.py` file:
   ```
   python main.py
   ```

## Output

When you run the project, a file named `movies.csv` will be created, containing information about the top 25 highest-rated movies.

---

# Film Listesi

Bu proje, IMDb'nin en yüksek puanlı 100 filmini çekmek ve bu filmlerle ilgili bazı bilgileri bir CSV dosyasına kaydetmek amacıyla oluşturulmuştur. Bu proje, BeautifulSoup ve pandas kütüphanelerini kullanarak IMDb'den veri çekmekte ve bu verileri işleyerek bir CSV dosyasına kaydetmektedir. Bu projede Scrapy kullanılmamıştır.

Proje kapsamında, 25 film çekilmiştir. Bunun sebebi, IMDb sayfasında aynı anda görüntülenebilen film sayısının 25 olmasıdır. Bu sınırlama, sayfanın yüklenme süresini ve veri çekme işleminin verimliliğini artırmak amacıyla uygulanmıştır.

## Kullanılan Teknolojiler

- BeautifulSoup
- pandas

## Kullanım

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. Gerekli kütüphaneleri yükleyin:
   ```
   pip install pandas
   pip install beautifulsoup4
   pip install requests
   ```
2. `main.py` dosyasını çalıştırın:
   ```
   python main.py
   ```

## Çıktı

Projeyi çalıştırdığınızda, `movies.csv` adlı bir dosya oluşturulacak ve bu dosya en yüksek puanlı 25 film hakkında bilgileri içerecektir.
