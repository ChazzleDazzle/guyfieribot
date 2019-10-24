clean: 
	rm -rf .build

prep: 
	mkdri -p .build

build_requirements: 
	pip install -r requirements.txt -t .build/
	cp *.py .build/
	chmod -R 755 .build/.

zip: 
	cd .build && zip -r -X ../code.zip . 

code: prep build_requirements zip clean

requirements: 
	pip install -r requirements.txt

initdb: 
	cat db_migrate_flavortown_db.sql | sqlite3 flavortown.db

dev: requirements initdb