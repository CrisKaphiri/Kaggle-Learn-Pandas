import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files("zynicide/wine-reviews", path="./data", unzip=True)
