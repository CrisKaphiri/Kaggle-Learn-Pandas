import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files("datasnaek/youtube-new", path="./data", unzip=True)
