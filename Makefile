.PHONEY: run
run:
	SPOTIPY_REDIRECT_URI=<your_redirect_url> SPOTIPY_CLIENT_ID=<your_client_id> SPOTIPY_CLIENT_SECRET=<your_client_secret> poetry run python main.py 
