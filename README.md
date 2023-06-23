# coingecko_btc
A small ETL that uses python3, sqlite, and mage for orchestration

The Notebooks contain the code were the extraction, transformation, and loading occurs, those notebooks are only meant for showing how the ETL was constructed, and what logic was used.

The orchestrations is done with mage, we need to decompress the btc_mage_tar.gz and run:

$ docker run -it -p 6789:6789 -v $(pwd):/home/src mageai/mageai /app/run_app.sh mage start coingecko_btc

in the working folder in order to start the orchestrator, after that we can go to:

http://localhost:6789/pipelines/coingecko_btc/edit?sideview=tree

in our browser to see the tree of the pipeline, anyways a live demonstration will be done.
