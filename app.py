# sudo apt-get install libsndfile1

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    # HF_AUTH_TOKEN = os.getenv("HF_AUTH_TOKEN")   
    # model = StableDiffusionPipeline.from_pretrained("dreambooth_weights/",use_auth_token=HF_AUTH_TOKEN).to("cuda")
    print("_no initial model")

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:

    print(f"model inputs are: {model_inputs}")

    return {'success': True }