# m7

1. Clone this repository.
```bash
git clone https://github.com/Moses-93/m7.git
```

2. Create the .env file in the root directory of the project.
```bash
sudo touch .env
```

3. Add your PostgreSQL URL to the .env file: 
```bash
DB_URL="postgresql+psycopg2://postgres:yourpassword@127.0.0.1:5432/postgres"
```

4. Install the required dependencies:
```bash
poetry install
```

5. Create and apply migrations
```bash
alembic revision --autogenerate -m 'Init'
```
```bash
alembic upgrade head
```

6. Run the command to fill the database.
```bash
python seed.py
```

7. Run command:
```bash
python main.py
```