# AI Inventory Management Web Application

A full-stack web application to manage inventory and generate intelligent restock recommendations.

## Features
- Add, update, and delete inventory items
- Track product details (name, category, quantity, price, supplier)
- Low-stock detection system
- AI-based restock recommendation engine
- RESTful API with FastAPI
- Interactive frontend using React

## Tech Stack
- Frontend: React (Vite)
- Backend: FastAPI (Python)
- Database: SQLite
- API: REST

## Project Structure
backend/ - FastAPI backend and database logic  
frontend/ - React UI and API integration  

## How to Run

### Backend
cd backend  
python -m venv venv  
venv\Scripts\activate  
pip install fastapi uvicorn sqlalchemy  
uvicorn main:app --reload  

### Frontend
cd frontend  
npm install  
npm run dev  

## API Documentation
http://127.0.0.1:8000/docs

## Screenshots
<img width="1885" height="871" alt="image" src="https://github.com/user-attachments/assets/c40d8f30-7cdb-474c-9d76-545219ed3935" />
<img width="1881" height="1022" alt="image" src="https://github.com/user-attachments/assets/aad5d626-41f8-4c16-96f7-da48de00a77d" />

