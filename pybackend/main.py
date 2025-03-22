import multiprocessing
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from data.models import NoteInDB, init_db, SessionLocal

# Initialize the database tables (if not already created)
init_db()

app = FastAPI()

# Pydantic models for input and response
class Note(BaseModel):
    title: str
    content: str

class NoteInResponse(Note):
    id: int

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new note (POST)
@app.post("/notes/", response_model=NoteInResponse)
def create_note(note: Note, db: Session = Depends(get_db)):
    db_note = NoteInDB(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# Get all notes (GET)
@app.get("/notes/", response_model=List[NoteInResponse])
def get_notes(db: Session = Depends(get_db)):
    return db.query(NoteInDB).all()

# Get note by ID (GET)
@app.get("/notes/{note_id}", response_model=NoteInResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(NoteInDB).filter(NoteInDB.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

# Update a note (PUT)
@app.put("/notes/{note_id}", response_model=NoteInResponse)
def update_note(note_id: int, note: Note, db: Session = Depends(get_db)):
    db_note = db.query(NoteInDB).filter(NoteInDB.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    
    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    return db_note

# Delete a note (DELETE)
@app.delete("/notes/{note_id}", response_model=NoteInResponse)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = db.query(NoteInDB).filter(NoteInDB.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    
    db.delete(db_note)
    db.commit()
    return db_note


if __name__ == '__main__':
    multiprocessing.freeze_support()  # For Windows support
    # CONSIDER SOMETHING WITH PORT
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False, workers=1)