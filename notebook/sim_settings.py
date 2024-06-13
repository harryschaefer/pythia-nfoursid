
# select the model to fit
import models.provided as model

class SimSettings():

    ORDER_OF_MODEL_TO_FIT = 4

    NUM_TRAINING_DATAPOINTS = 5000
    NUM_BLOCK_ROWS = 30
    NOISE_AMPLITUDE = .1

    NUM_TEST_DATAPOINTS = 20

    FIGSIZE = 3
    figsize = (FIGSIZE*1.5, FIGSIZE)

    TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjNkNTgwZjBhZjdhY2U2OThhMGNlZTdmMjMwYmNhNTk0ZGM2ZGJiNTUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIzMjU1NTk0MDU1OS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6IjMyNTU1OTQwNTU5LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTA5ODQwNzExNjMyMzQ0NzI4NTc5IiwiaGQiOiJnZW5lcmFsLWRldi5jbyIsImVtYWlsIjoiaGFycnkuc2NoYWVmZXJAZ2VuZXJhbC1kZXYuY28iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6Ind2WTRBQWtKNkNaOEt4UzdhSDd0a0EiLCJpYXQiOjE3MTk0MDk0NDMsImV4cCI6MTcxOTQxMzA0M30.mQVhkBpOCtGPixUQ0W5eu6Ym5kN5YuBAdqXi2D8yYVPfiJvr_uvdKeJ6xXlCRwPj53i5HA_b_e7eO_zCaog9GlZbBkI4ZCAuLG3m17pGWsiSGU3C3ZjWqiaVwwTcUY3YZV6yo1vOEy-shx9Gk3OU8PolpfLvALn5nmymGxDAhm-QB5iwvNE1rX9ZloKk4iBb0gpudAwfMPq6jqAHJtg_Hbm6hicw9_C06mhnQbGK0uPSRhjirIhrwagqTycT_4OjK0qMYnjoh_jko7mYk2GscrhaOKaGgalfRtLFSSSsM_vsCJLo9pRmoXZbZWhXp-gzcd5UmvxeZ9UTCE8zWHnA_A"

    INPUT_DIM = model.INPUT_DIM
    OUTPUT_DIM = model.OUTPUT_DIM
    INTERNAL_STATE_DIM = model.INTERNAL_STATE_DIM
    A = model.A
    B = model.B
    C = model.C
    D = model.D

    sp_A = model.sp_A
    sp_B = model.sp_B
    sp_C = model.sp_C
    sp_D = model.sp_D
