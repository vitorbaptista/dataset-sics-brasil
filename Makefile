.PHONY: check_updated_data test
LATEST_DATA_FILE := data/lista-sics-maio-de-2018.xlsx

data/sics-brasil.csv: $(LATEST_DATA_FILE)
	libreoffice --convert-to csv --outdir data $(LATEST_DATA_FILE)
	$(eval CONVERTED_CSV_PATH := $(addsuffix .csv, $(basename $(LATEST_DATA_FILE))))
	python scripts/clean_csv.py $(CONVERTED_CSV_PATH) > $@

$(LATEST_DATA_FILE):
	wget http://www.acessoainformacao.gov.br/lai-para-sic/$(notdir $(LATEST_DATA_FILE)) -O $@

test:
	goodtables data/datapackage.json

check_updated_data:
	python scripts/check_new_data_available.py
