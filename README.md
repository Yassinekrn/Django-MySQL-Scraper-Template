# Django MySQL Scraper 🐍

![Django Logo](https://www.djangoproject.com/m/img/logos/django-logo-negative.png)  
![MySQL Logo](https://www.mysql.com/common/logos/logo-mysql-170x115.png)

## Overview 🌟

**Django MySQL Scraper** is a simple yet powerful web scraping application built with Django and MySQL. This project provides a RESTful API that allows authenticated users to perform web scraping and retrieve scholarship structured data in JSON format.

### Key Features 🚀

- **Web Scraping**: Efficiently scrape data from specified web pages.
- **RESTful API**: Interact with the scraper through a secure API, allowing for easy integration with frontend applications.
- **User Authentication**: Secure your API with a simple authentication mechanism, ensuring that only authorized users can access the scraping functionality.
- **Data Storage**: Store scraped data seamlessly in a MySQL database while managing user data in the same environment.

## Technologies Used 🛠️

- **Backend**: Django
- **Database**: MySQL
- **Frontend**: React
- **Libraries**: `django-rest-framework`, `beautifulsoup4`, `requests`

## Getting Started ⚙️

### Prerequisites 📋

- Python 3.8 or higher
- Django 4.1 or higher
- MySQL

### Installation 🏗️

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YassineKrn/django-mysql-scraper.git
   cd django-mysql-scraper
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your database settings** in `settings.py`.

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the API:**
   Visit `http://127.0.0.1:8000/api/scrape/` to use the scraping endpoint.

## Usage 📦

### API Endpoints 🌐

- **POST /api/scrape/**: Start the scraping process and receive data in JSON format.  
  **Authentication required**: Yes 🔑

### Example Request 📨

```bash
curl -X POST http://127.0.0.1:8000/api/scrape/ \
-H "Authorization: Bearer <your_token>" \
-H "Content-Type: application/json"
```

## Contributing 🤝

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project. (work in progress)

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements 🙏

- [Django](https://www.djangoproject.com/)
- [MySQL](https://www.mysql.com/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

---

Feel free to reach out or submit issues if you encounter any problems! 😊
