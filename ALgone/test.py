import os
import openai

os.environ['OPENAI_API_KEY'] = "API_KEY"
openai.api_key = os.getenv("OPENAI_API_KEY")
text = """fakulti mana yang mempunyai pelajar paling ramai?"""
SQL_PREFIX = """You are an agent designed to give SQL Query.
You are given a table and a question.
You must answer the question using SQL.
You must answer ONLY SQL Query.
If the answer is unavailable or unreliable, answer 'Not sure'
The table is as follows:
`-- Table: um_mart.FACT_STUDENT

CREATE TABLE IF NOT EXISTS um_mart."FACT_STUDENT"
(
    "NO_MATRIK" character varying(10) COLLATE pg_catalog."default" NOT NULL,
    "NO_DAFTAR" character varying(20) COLLATE pg_catalog."default",
    "NO_MATRIK_LAMA" character varying(20) COLLATE pg_catalog."default",
    "SESI_AKADEMIK" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "NO_SEM_AKADEMIK" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "NAMA" character varying(200) COLLATE pg_catalog."default",
    "STATUS_FAST_TRACK" character varying(3) COLLATE pg_catalog."default",
    "KTRGN_SALURAN_MASUK" character varying(200) COLLATE pg_catalog."default",
    "STATUS_PASUM" character varying(200) COLLATE pg_catalog."default",
    "KOHORT_PASUM" character varying(200) COLLATE pg_catalog."default",
    "KTRGN_IJAZAH_BM" character varying(200) COLLATE pg_catalog."default",
    "KTRGN_IJAZAH_BI" character varying(200) COLLATE pg_catalog."default",
    "KTRGN_PROGRAM" character varying(200) COLLATE pg_catalog."default",
    "KTRGN_MOD_PENGAJIAN" character varying(200) COLLATE pg_catalog."default",
    "KTRGN_JENIS_PENGAJIAN" character varying(200) COLLATE pg_catalog."default",
    "MIXED_MODE_RATIO" character varying(200) COLLATE pg_catalog."default",
    "ST_NONST" character varying(100) COLLATE pg_catalog."default",
    "UNJURAN_PROGRAM" character varying(100) COLLATE pg_catalog."default",
    "SESI_MULA_PROGRAM" character varying(100) COLLATE pg_catalog."default",
    "SEM_MULA_PROGRAM" character varying(100) COLLATE pg_catalog."default",
    "KTRGN_FAKULTI" character varying(100) COLLATE pg_catalog."default",
    "KTRGN_JABATAN" character varying(100) COLLATE pg_catalog."default",
    "KOD_NEC2" character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT "FACT_STUDENT_PK" PRIMARY KEY ("NO_MATRIK", "SESI_AKADEMIK", "NO_SEM_AKADEMIK")
)`
The question is as follows:
"""
complete = SQL_PREFIX + text
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=complete,
    temperature=0,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)
output = response.choices[0].text.strip()
print(output)