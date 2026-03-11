# Sales Insight Automator

A full-stack, AI-powered application that accepts a sales logic dataset (CSV or Excel) and automatically generates a business executive summary of actionable insights sent directly via email.

## 🏗️ Architecture

- **Frontend**: React (Vite) + Tailwind CSS SPA, file uploads and validation.
- **Backend**: FastAPI setup in a modular services layout.
- **AI Core**: Google Gemini Generative AI for reasoning and summarization of pandas dataframes metrics.
- **Delivery**: Standard SMTP implementation for emailing stakeholders.
- **Deployment**: Dockerized backend, GitHub Actions CI/CD pipeline suitable for cloud delivery (Render/Vercel).

---

## 🚀 Quick Setup

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
- [Node.js](https://nodejs.org/) (if running frontend locally outside of Docker)
- A **Google Gemini API Key**
- An App-Specific Password for a Gmail account (for SMTP)

### 1. Environment Configuration

Copy the sample environment file to use your own credentials:

```bash
cp .env.example .env
```

Open `.env` and fill out your keys:
- `GEMINI_API_KEY`: Get this from Google AI Studio.
- `EMAIL_SENDER`: Your sending email address (e.g., you@gmail.com).
- `EMAIL_PASSWORD`: An App-specific password if using Gmail 2FA.

### 2. Running Locally using Docker

You can spin up the backend via Docker Compose:

```bash
docker-compose up --build
```
This will start the FastAPI backend and expose it at `http://localhost:8000`. 
API interactive documentation (Swagger UI) is automatically available at `http://localhost:8000/docs`.

### 3. Running the Frontend

In a separate terminal, navigate to the frontend folder:

```bash
cd frontend
npm install
npm run dev
```
The React frontend will be served at `http://localhost:5173`.

---

## 📖 How it Works End-to-End

1. **Upload**: The user uploads a valid `sample_data.csv` on the frontend.
2. **Analysis**: The backend loads it securely into a Pandas DataFrame and aggregates metrics (Total Revenue, Tops Sellers, Cancelled Counts).
3. **AI Generation**: A structured prompt including the mathematical metrics is sent to Gemini to analyze.
4. **Delivery**: The plain text response from Gemini is emailed immediately to the recipient provided in the UI.

---

## 🔒 Security Considerations

- **API Protection**: Using `slowapi` to enforce strict rate limits (5 requests / min).
- **Validation**: Strict size (5MB max) and file extension checking (`.csv`, `.xlsx`). Pydantic ensures data stability.
- **Data Protection**: Input is securely sanitized and the AI layer does not leak raw PII data if implemented correctly.
- **CORS Restricted**: The API uses strict Cross-Origin Resource Sharing. Adjust `allow_origins=["*"]` in production.

---
