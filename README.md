# Web Scraping dengan Menggunakan BeautifulSoup <br>
Project ini merupakan implementasi web scraping dengan menggunakan `Python` dengan memanfaatkan library `BeautifulShop`. Case yang akan dibahas pada project ini adalah bagaimana mengambil data dari situs IMDb (Internet Movie Database).<br>
IMDb (Internet Movie Database) adalah sebuah basis data daring informasi yang berkaitan dengan film, acara televisi, video rumahan, dan permainan video, dan acara internet, termasuk daftar pemeran, biografi kru produksi dan personil, ringkasan alur cerita, trivia, dan ulasan serta penilaian oleh penggemar.<br>
Pada project Capstone antara lain berisi: 
1. pengumpulan data dan informasi pada situs IMDb dengan mengimplementasikan teknik web scrapping menggunakan `BeatufilSoup`
2. Creating Dataframe dan Data Wrangling
2. Data Visualization dengan menganalisa informasi yang didapat yaitu film terpopuler versi IMDB dengan menggunakan `matplotlib` dan `Flask` dashboard.

## Dependency ##
- beautifulSoup4
- pandas
- flask
- matplotlib

atau dapat dengan cara langsung menginstall requirement.txt yang ada pada project ini
> `pip install -r requirements.txt`

## Hasil Scraping ##
Berikut adalah hasil scraping yang telah diubah ke dalam bentuk DataFrames <br><br>


HTML                     |  Scraping               | Data Frames
:-------------------------:|:-------------------------:|:-------------------------:
![](images/halaman_html.png)    |  <img src="images/arrow.png" width="80" height="60" />   |  ![](images/hasil_scraping.png)



## Hasil Plot ##
Berikut adalah plot perbandingan 7 film terpopuler berdasarkan rating, meta score dan votes <br>
Rating                     |  Meta Score               | Votes
:-------------------------:|:-------------------------:|:-------------------------:
![](images/rating.png)     |  ![](images/meta_score.png)   |  ![](images/votes.png)

## Flask ##
Berikut merupakan hasil tampilan dashboard dengan menggunakan `Flask` <br><br>
<img src="images/flask.png" />
