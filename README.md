docker compose up -d flask_db
docker compose build
docker compose up flask_app
cd frontend
npm run serve
