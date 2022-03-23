deploy:
	@gcloud app deploy --project=nimble-arcana-774 || true

run:
	@dev_appserver.py --enable_console=true .
