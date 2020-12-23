clean:		## delete pycache, build files
	@rm -rf deploy  
	@rm -rf layer 
	@rm -rf __pycache__

## create Docker image with requirements
docker-build:
	make lambda-layer-build	
	docker-compose build

## prepares layer.zip archive for AWS Lambda Layer deploy 
lambda-layer-build: clean 
	rm -rf layer-dir	
	mkdir layer-dir layer-dir/python layer-dir/bin
	cd layer-dir/bin; unzip -u ../../bin.zip; unzip -u ../../chromium.zip 
	pip3 install -r requirements.txt -t layer-dir/python

	# rm -rf layer-dir
	# mkdir layer-dir
	# mkdir layer layer/python
	# cp -r bin layer/.
	# cd layer/bin; unzip -u ../../chromium.zip 
	# pip3 install -r requirements.txt -t layer/python
	# cd layer; zip -9qr layer.zip .
	# cp layer/layer.zip layer-dir/layer.zip
	# rm -rf layer


