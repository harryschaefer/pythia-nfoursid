
# select the model to fit
from .models import provided
from .models import ibr


class SimSettings():

    ORDER_OF_MODEL_TO_FIT = 4

    NUM_TRAINING_DATAPOINTS = 5000
    NUM_BLOCK_ROWS = 30
    NOISE_AMPLITUDE = .1

    NUM_TEST_DATAPOINTS = 20

    FIGSIZE = 3
    figsize = (FIGSIZE*1.5, FIGSIZE)

    TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjJhZjkwZTg3YmUxNDBjMjAwMzg4OThhNmVmYTExMjgzZGFiNjAzMWQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIzMjU1NTk0MDU1OS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6IjMyNTU1OTQwNTU5LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTA5ODQwNzExNjMyMzQ0NzI4NTc5IiwiaGQiOiJnZW5lcmFsLWRldi5jbyIsImVtYWlsIjoiaGFycnkuc2NoYWVmZXJAZ2VuZXJhbC1kZXYuY28iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6IktJMXctOURnOWY1Nmd1eWpxYXNHYWciLCJpYXQiOjE3MTk0ODE0NTYsImV4cCI6MTcxOTQ4NTA1Nn0.dLIW5m5wE0RX3b7z5uWzAk4vqS8aZj5VrDed3Ega3thU27UVEiA9bN2cizcacy4pXiaHrY5xP9RmdOBHPH6kzDwrAsYfU5bCWOTGigpRU4i0FyhgR5-C33yorKT2at_qFlX3NeOU6Pb3mZwvzpkPGQhSfsUsjEYeTLL4_NwGToOflTpFI1jyjyH964sipBxlzc2-BAd7iI3iGVwoZKKNOAYmPlOnaaxm54raxNzJiMp784UJUJewNwK37ABr3crODhzwz4PHf0kyYxhQd2-dKVCSitL0A5CUHIWJxzg01botkNx0jrZEyIbhoXm2Lyd7r7LLUV1xGkbfKHIy06bE4w"

    INPUT_DIM = provided.INPUT_DIM
    OUTPUT_DIM = provided.OUTPUT_DIM
    INTERNAL_STATE_DIM = provided.INTERNAL_STATE_DIM
    A = provided.A
    B = provided.B
    C = provided.C
    D = provided.D
    sp_A = provided.sp_A
    sp_B = provided.sp_B
    sp_C = provided.sp_C
    sp_D = provided.sp_D

    IBR_INPUT_DIM = ibr.INPUT_DIM
    IBR_OUTPUT_DIM = ibr.OUTPUT_DIM
    IBR_INTERNAL_STATE_DIM = ibr.INTERNAL_STATE_DIM
    IBR_A = ibr.A
    IBR_B = ibr.B
    IBR_C = ibr.C
    IBR_D = ibr.D
    
