from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Mahasiswa(BaseModel):
    nama: str
    alamat: str
    ipk: float
    semester: int
    hobi: str


# Menyimpan data mahasiswa sementara
data_mahasiswa = []


@app.get("/")
def home():
    return {
        "message": "API Tugas 1 Integrasi Sistem berhasil"
    }


@app.get("/mahasiswa")
def lihat_mahasiswa():
    return {
        "message": "Data mahasiswa berhasil diambil",
        "data": data_mahasiswa
    }


@app.post("/mahasiswa")
def tambah_mahasiswa(mahasiswa: Mahasiswa):
    data_mahasiswa.append(mahasiswa)

    return {
        "message": "Data mahasiswa berhasil ditambahkan",
        "data": mahasiswa
    }


@app.put("/mahasiswa/{nama}")
def ubah_mahasiswa(nama: str, mahasiswa: Mahasiswa):

    for i, data in enumerate(data_mahasiswa):
        if data.nama == nama:
            data_mahasiswa[i] = mahasiswa

            return {
                "message": f"Data mahasiswa {nama} berhasil diubah",
                "data": mahasiswa
            }

    return {
        "message": f"Data mahasiswa {nama} tidak ditemukan"
    }


@app.delete("/mahasiswa/{nama}")
def hapus_mahasiswa(nama: str):

    for i, data in enumerate(data_mahasiswa):
        if data.nama.strip().lower() == nama.strip().lower():
            data_dihapus = data_mahasiswa.pop(i)

            return {
                "message": f"Data mahasiswa {data_dihapus.nama} berhasil dihapus",
                "data": data_dihapus
            }

    return {
        "message": f"Data mahasiswa {nama} tidak ditemukan"
    }