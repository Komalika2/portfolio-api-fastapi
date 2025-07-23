from fastapi import APIRouter

router = APIRouter()

@router.get("/internships")
def get_internships():
    return [
        {
            "company": "Quantsapp Pvt Ltd",
            "role": "Python Developer",
            "duration": "Jun 2024 - Oct 2024",
            "description": " • Designed a real-time data streaming POC using Apache Kafka for low-latency trade signal processing across brokers
                             • Automated & validated daily financial holdings by integrating BSE SOAP APIs, AWS S3, DynamoDB & RTA
                            reports, enabling accurate discrepancy reporting across internal & external data sources for an options trading platform
                             • Automated retrieval and formatting of live market data—including option chain, charts, corporate actions & deal flows
                            into dynamic Excel reports using Python and Xlwings, enhancing analysis, visualization & decision-making efficiency"
        },
        {
            "company": "TimeMarks Pvt Ltd",
            "role": "ML Developer Intern",
            "duration": "May 2023 - July 2023",
            "description": " • Leveraged AWS to construct a muzzle recognition model, significantly contributing to the cattle identification system
                             • Labelled a dataset of 50+ cattle images targeting the muzzle in the Amazon Custom Rekognition Label for training
                             • Achieved an F1-score of 0.714 by evaluating the model’s performance using a test dataset to get performance metrics"
        },
         {
            "company": "Anandpragyai",
            "role": "Data Science Intern",
            "duration": "July 2023 - Feb 2024",
            "description": " • Proficiently handling the project, including data preparation, model creation, training, testing & AI-experimentation
                             • Initiated extensive Technological Research in Encryption, NLP, & multi-modal input delivering cutting-edge solutions
                             • Working on diverse Data Modalities and Models, actively striving to achieve solutions & addressing futuristic usecases"
        }
    ]

@router.get("/projects")
def get_projects():
    return [
        {
            "title": "Trading Strategy Prediction",
            "tools": ["BitMEX", "XGBoost", "RNN", "LSTM"],
            "summary": "Predicted bullish/bearish signals and future prices using 8 years of trading data."
        },
        {
            "title": "AI Chatbot for PDF",
            "tools": ["LangChain", "FAISS", "HuggingFace", "Streamlit"],
            "summary": "Built a chatbot to answer questions from uploaded PDF files."
        },
        {
            "title": "Recommendation System",
            "tools": ["KNN", "Scikit-learn", "Amazon Reviews"],
            "summary": "Built item-item collaborative filtering system using KNNWithMeans algorithm."
        }
    ]




# # # app/routes.py
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from uuid import uuid4

# from app import models, schemas
# from app.database import SessionLocal

# router = APIRouter()

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/portfolio/", response_model=schemas.Portfolio)
# def create_portfolio(portfolio: schemas.PortfolioCreate, db: Session = Depends(get_db)):
#     db_portfolio = models.Portfolio(id=str(uuid4()), **portfolio.dict())
#     db.add(db_portfolio)
#     db.commit()
#     db.refresh(db_portfolio)
#     return db_portfolio

# @router.get("/portfolio/", response_model=list[schemas.Portfolio])
# def read_portfolios(db: Session = Depends(get_db)):
#     return db.query(models.Portfolio).all()

# @router.get("/portfolio/{portfolio_id}", response_model=schemas.Portfolio)
# def read_portfolio(portfolio_id: str, db: Session = Depends(get_db)):
#     item = db.query(models.Portfolio).filter(models.Portfolio.id == portfolio_id).first()
#     if item is None:
#         raise HTTPException(status_code=404, detail="Portfolio not found")
#     return item

# @router.delete("/portfolio/{portfolio_id}")
# def delete_portfolio(portfolio_id: str, db: Session = Depends(get_db)):
#     item = db.query(models.Portfolio).filter(models.Portfolio.id == portfolio_id).first()
#     if item is None:
#         raise HTTPException(status_code=404, detail="Portfolio not found")
#     db.delete(item)
#     db.commit()
#     return {"message": "Deleted successfully"}
