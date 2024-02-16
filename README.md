docker compose up -d flask_db

docker compose build

docker compose up flask_app

cd frontend

npm run serve

Port backend: 4000

Port frontend: 8080

localhost:4000/populate pour remplir la DB

localhost:8080 pour lancer le front
