from datetime import datetime

from fastapi import HTTPException, UploadFile
import os
import uuid


def save_file_db(Model, model_id, file: UploadFile, db):
    MAX_FILE_SIZE = 2 * 1024 * 1024
    ext = os.path.splitext(file.filename)[-1].lower()

    ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(400, "Fayl formati mos kelmadi !!!")

    content = file.file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(400, "Rasm hajmi katta!")

    file.file.seek(0)
    _, file_extension = os.path.splitext(file.filename)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_filename = f"{timestamp}_{uuid.uuid4().hex[:8]}{file_extension}"

    image_path = os.path.join("images", unique_filename)

    try:
        with open(image_path, "wb") as buffer:
            buffer.write(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Faylni yozishda xatolik yuz berdi: {e}")

    db.query(Model).filter(Model.id == model_id).update({
        Model.image_path: unique_filename
    })
    db.commit()
    return {"detail": f"rasm qo'shildi, file: {unique_filename}"}


def delete_file_f(Model, model_id, db):
    file_info = db.query(Model).filter(Model.id == model_id).first()
    path = f"./images/{file_info.image_path}"
    try:
        os.remove(path)
    except Exception as e:
        raise HTTPException(400, f'fayl mavjud emas {e}')
